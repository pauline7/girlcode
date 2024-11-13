# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
# import genai
from girlcode.settings import GENERATIVE_AI_KEY
import google.generativeai as genai
from .models import Chat, Prompt
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Replace with your Google Cloud API key
genai.configure(api_key=GENERATIVE_AI_KEY)


def ask_gemini(message):
    # Modify model name according to your specific Gemini model
    model = genai.GenerativeModel('gemini-pro')  # Replace with your model name
    response = model.generate_content( message)
    return response.text.strip()

#@method_decorator(login_required, name='dispatch')
def chat(request):
    chats = Chat.objects.filter(user = request.user)
    prompt_list = Prompt.objects.all()
    num_prompts = Prompt.objects.count()

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemini(message)

        chat = Chat(user = request.user,message =message, response= response, created_at= timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    
    context = {
        'chats':chats,
        'num_prompts': num_prompts,
        'prompt_list': prompt_list,
    }

    return render(request, 'girlchat.html', context=context)

