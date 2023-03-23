from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def result(request):
    text=request.GET["text"]
    text_list=text.split()
    text_dict={}
    for word in text_list :
        if word in text_dict :
            text_dict[word] +=1
        else:
            text_dict[word] = 1
    return render(request, 'result.html', {'words':text_dict.items()})