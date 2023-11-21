import os
from django.shortcuts import render, redirect
from django.views import View
from poetic_assitant.forms import Prompts_Form

from openai import OpenAI



class index(View):
    openai_api_key = ENTER_YOUR_API_KEY
    client = OpenAI(api_key=openai_api_key)

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {
            'form': Prompts_Form(),
        })

    def post(self, request, *args, **kwargs):
        openai_api_key = ENTER_YOUR_API_KEY
        client = OpenAI(api_key=openai_api_key)

        num_visits = request.session.get('num_visits', 3)
        request.session['num_visits'] = num_visits + 1
        
        if num_visits > 5:
                response = 'Your number of questions time up' 
                
        else:
            form = Prompts_Form(data=request.POST)
            if form.is_valid():
                prompt = form.cleaned_data['user_entery']
                
                try:
                    completion = client.chat.completions.create(model="gpt-3.5-turbo",messages=[
                            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                            {"role": "user", "content": 'Crie um poema com o seguinte tópico em programação e sua logíca' + prompt}
                        ],
                    temperature=0,
                    max_tokens=1024)
                    response = completion.choices[0].message.content

                except Exception as e:
                    response = "Erro durante a solicitação da API"

                
        return render(request, 'index.html', {
                'response': response, 
                'form' : Prompts_Form(),
                'num_visits': num_visits})
