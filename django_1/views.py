from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def show_hello(request):
    hello = """
            <html>
                <body>
                    <p>Hello World</p>
                </body>
            </html>
                 """
    return HttpResponse(hello)

def show_random(request):
    numb = randint(0, 100)
    rand = """
        <html>
            <body>
                <p>The random number is {}!</p>
            </body>
        </html>
             """.format(numb)
    return HttpResponse(rand)

def pick_number(request, max_number):
    wylosowana_liczba = randint(0, int(max_number))
    result = f"Użytkownik podal wartość {max_number}. Wylosowana liczba to {wylosowana_liczba}."
    return HttpResponse(result)