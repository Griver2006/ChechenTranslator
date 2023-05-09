from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import *


def main(request):
    if request.method == 'POST':
        print(request.POST.get('input_word', ''))
    return render(request, 'translator_app/main.html', {'title': 'Главная страница'})


def translate(request):
    if request.method == 'POST':
        input_text = request.POST.get("text", "")
        try:
            word_translate = Word.objects.filter(word__iexact=input_text)[0].word_translate
        except IndexError:
            try:
                word_translate = Word.objects.filter(word_translate__iexact=input_text)[0].word_translate
            except IndexError:
                word_translate = ''
        return JsonResponse({"translated_text": word_translate})
    else:
        return HttpResponse("Request method is not a GET")