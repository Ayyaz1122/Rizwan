import operator

from django.shortcuts import render
from . import counter

def home(request):
    return render(request, 'index.html', {'key1': 'I am coming from Python code'})

def result(request):
    article = request.GET ['article']
    var_dict, word_count = counter.counter(article)
    return render(request, 'result.html', {'article': article, 'word_count': word_count, 'dict_words': var_dict})
