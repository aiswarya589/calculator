from django.shortcuts import render,redirect
from django.http import HttpResponse
def home(request):
    result=None
    if request.method=='POST':
        '''
        user1=input()
        user2=input()
        if user1=='rock' and user2=='scissor':
            output = "user1"
        elif user1 == 'rock' and user2=='paper':
            output = "user2"
        elif user1 == 'scissor' and user2 == 'paper':
            output ="user1"
        elif user1 == 'scissor' and user2=='rock':
            output="user2"
        elif user1=='paper' and user2=='rock':
            output = "user1"
        elif user1 =='paper' and user2 == 'scissor':
            output= "user2"
        else:
            output = "tie"
        return output
        '''


        
        a=int(request.POST.get('num1'))
        b=int(request.POST.get('num2'))
        op=request.POST.get('op')
        if op=='add':
            result=a+b
        elif op=='sub':
            result=a-b
        elif op=='mul':
            result=a*b
        elif op=='div':
            result=a/b
        else:
            return render(request,'home.html',{'error':error}) 
        #return render(request,'home.html',{'result':result})
        return redirect('hello',result)
        
    return render(request,'home.html') 
def hello(request,result):
    return render(request,'result.html',{'result':result}) 
# Create your views here.