#from _typeshed import OpenTextModeUpdating
from django.http import request
from django.shortcuts import render
from subprocess import run,PIPE
import sys
import subprocess
#import torch
#import fairseq

# Create your views/functions/classes here which are mapped to urls.

def index(request):
    return render(request,'speechrecon/ind2.html')

def speech(request):
    a=5
    return render(request,'speechrecon/index.html',{'data':a})

def external(request):
    inp = request.POST.get('param')
    #out = run(sys.executable,['.\ts1.py', inp], shell = False, stdout = PIPE)
    #out = str(inp) + ' is the input.'
    #print(out)

    #out = subprocess.run([sys.executable,'C:\\Users\\rohit\\STT\\speechrecon\\ts1.py',inp], shell = False , stdout = PIPE)
    #print(out)
    return render(request,'speechrecon/ind2.html',{'data1' : inp})