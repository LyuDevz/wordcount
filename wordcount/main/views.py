from django.shortcuts import render
import re
import string

def main(request):
    return render(request, 'main.html')

def result(request):
    text=request.GET["text"]
    text_list=text.split()
    
    # 각 단어의 개수를 담아주기 위한 딕셔너리
    text_dict={}
    
    for word in text_list :
        if word in text_dict :
            text_dict[word] +=1
        else:
            text_dict[word] = 1
    return render(request, 'result.html', {'words':text_dict.items()})