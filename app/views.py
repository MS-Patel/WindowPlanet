from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')


def qoute(request):

    if request.method == 'POST':
        height= float(request.POST['height'])
        width = float(request.POST['width'])
        frame_type = request.POST['frametype']
        frame_rate = float(request.POST['framerate'])
        glass_type = request.POST['glasstype']
        glass_rate = float(request.POST['glassrate'])
        net_type = request.POST['nettype']
        net_rate = float(request.POST['netrate'])
        addon = request.POST['addon']
        addon_rate = float(request.POST['addonrate'])
        size= height*width
        glass_prize = size* glass_rate
    return render(request,'qoutation.html',{'size':size,'glass_type':glass_type,'glass_prize':glass_prize})