from django.shortcuts import render
import pyautogui as pg
import time
# Create your views here.
def index(request):
    return render(request,'msg/index.html')

def msg(request):
    time.sleep(10)

    for i in range(10):
        pg.write('?')
        pg.press('Enter')

    return render(request, 'msg/thanks.html')
