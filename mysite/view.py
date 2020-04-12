from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'welcome to test !'
    return render(request,'hello.html',context)
