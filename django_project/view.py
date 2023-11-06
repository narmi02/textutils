from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyzer(request):
    djtext = request.GET.get('text', 'default')

    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    spacerem = request.GET.get('spaceremove', 'off')
    newlinerem = request.GET.get('newlineremov', 'off')
    count = request.GET.get('count', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    analyzed = ""
    if removepunc == "on":
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

            params = {
                'purpose': "Remove punctuations",
                'analyze_text': analyzed
            }
            djtext=analyzed
    if (fullcaps == "on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': "Capitalize", 'analyze_text': analyzed}
            djtext=analyzed
    if (spacerem == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
            params = {'purpose': 'Space Removes', "analyze_text": analyzed}
            djtext=analyzed

    if (newlinerem == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n":
                    analyzed = analyzed + char
            params = {'purpose': 'Removes New Lines', 'analyze_text': analyzed}
            djtext=analyzed

    # if (count == "on"):
    #         count = len(djtext)
    #         params = {'purpose': 'Number of characters', 'analyze_text': count}

    if(removepunc!="on" and count!="on" and newlinerem!="on" and spacerem!="on" and fullcaps!="on" ):
        return HttpResponse("Your not selected anything")
    return render(request, 'analyzer.html', params)