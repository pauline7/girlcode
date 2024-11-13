#from unicodedata import category
from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404, HttpResponseRedirect, HttpResponse
#from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import Group  #for group permissions
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .forms import *
# gemini
from girlcode.settings import GENERATIVE_AI_KEY
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
genai.configure(api_key=GENERATIVE_AI_KEY)

def ask_gemini(message):
    # Modify model name according to your specific Gemini model
    model = genai.GenerativeModel('gemini-pro')  # Replace with your model name
    response = model.generate_content( message)
    return response.text.strip()

# @login_required
def index(request):
    """View function for home page of site."""

    # The 'all()' is implied by default.
    post_list = Post.objects.all()
    num_posts = Post.objects.count()
    #num_agencies = Agency.objects.count()

    #Scrapping One
    # response2 = requests.get("https://flo.uri.sh/visualisation/15700151/embed?auto=1")
    # soup = BeautifulSoup(response2.text, 'html.parser')
    # # Gemini-enhanced scraping 2:Graphs
    # graph_summary = soup.find('main', class_='fl-layout-wrapper')
    # prompt = f"Extract key information from this graph in less than 100 words: {graph_summary}"
    # graphs = ask_gemini(prompt)

    #Scrapping Two
    #url = requests.get("https://tourtravelandcamping.com/listings/")
    response = requests.get("https://www.africadatahub.org/femicide-kenya")
    soup = BeautifulSoup(response.text, 'html.parser')
    # Traditional scraping
    headings = soup.find_all('h5')
    headings = headings[0: 10]
    news = ['one',]
    for items in headings:
        news.append(items.text.strip())
    # Gemini-enhanced scraping 1:Paragraph contents
    product_summary = soup.find_all('p')
    prompt = f"Extract key features from this product description in less than 100 words: {product_summary}"
    features = ask_gemini(prompt)
    # Gemini-enhanced scraping 2:Graphs
    graph_summary = soup.find_all('div', class_='left-column')
    prompt = f"Extract key information from this graphs and summarize in 50 words: {graph_summary}"
    graphs = ask_gemini(prompt)
    # features_list = []
    # for fea in features:
    #     features_list.append(fea)
    # # Gemini-enhanced scraping 2
    # product_description = soup.find('p', class_='card-text')
    # prompt = f"Extract key features from this product description: {product_description}"
    # features = ask_gemini(prompt)

    #print(features)

    #Pagination
    p = Paginator(post_list, 50)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {
        'post_list': post_list,
        'num_posts': num_posts,
        #'num_agencies': num_agencies,
        "page_obj": page_obj,
        'news': news,
        'features': features,
        'graphs': graphs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@method_decorator(login_required, name='dispatch')
class PostDetailView(generic.DetailView):
    model = Post
    # agency_name = Agency.agency_name()
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = PostComment.objects.filter(
            post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = PostComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  post_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


# def package_create(request):  
#     if request.method == 'POST':  
#         form = PackageForm(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
  
#             # Getting the current instance object to display in the template  
#             img_object = form.instance
              
#             #return render(request, 'listings/package_form.html', {'form': form, 'img_obj': img_object}) 
#             return redirect('/listings') 
#     else:  
#         form = PackageForm()  
  
#     return render(request, 'listings/package_form.html', {'form': form}) 

def post_create(request):   
    if request.user.is_authenticated:
        # get all the users of the group writer
        #users_in_group = Group.objects.get(name="agencies").user_set.all()
        # only if that user is a part the group  
        if request.method == 'POST':  
            form = PostForm(request.POST, request.FILES)  
            if form.is_valid():  
                form.save()  
    
                # Getting the current instance object to display in the template  
                img_object = form.instance
                
                #return render(request, 'listings/package_form.html', {'form': form, 'img_obj': img_object}) 
                return redirect('/storytime') 
        else:  
            form = PostForm()  
    
        return render(request, 'storytime/post_form.html', {'form': form}) 
    else:
        return HttpResponseRedirect("/")


# def privacy(request):
#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'terms_and_conditions/privacy.html')

# def appads(request):
#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'app-ads.txt')
