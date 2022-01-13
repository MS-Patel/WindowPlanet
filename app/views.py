from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')


def qoute(request):

    if request.method == 'POST':
        
        frame_type = request.POST['frametype']
        frame_size = float(request.POST['framesize'])
        frame_rate = float(request.POST['framerate'])
        glass_type = request.POST['glasstype']
        glass_rate = float(request.POST['glassrate'])
        lpatti_type = request.POST['lpattitype']
        lpatti_rate = float(request.POST['lpattirate'])
        uchannel_type = request.POST['uchannel_type']
        uchannel_rate = float(request.POST['uchannel_rate'])
        net_type = request.POST['nettype']
        net_rate = float(request.POST['netrate'])
        addon = request.POST['addon']
        addon_rate = float(request.POST['addonrate'])

        fh= float(request.POST['height'])
        fw = float(request.POST['width'])

        frame_prize= ((fh*2)+(fw*2)) * (frame_size/frame_rate)
        
        sh = fh-2.75
        sw = (fw-0.5)/2
        shutter_size = (sh*6)+(sw*6)
        shutter_prize = shutter_size * (frame_size/frame_rate)

        lpatti_size = (sh*3)
        lpatti_prize = ilpatti_size * (frame_size/frame_rate)

        net_size = sh*sw
        net_prize = net_size * net_rate

        uh = sh-5
        uw = sw-5
        uchannel_size = (uh+uw)*2
        uchannel_prize = uchannel_size*uchannel_rate

        glass_size= ((sh-4.125) * (sw-4.125))*2
        glass_prize = (glass_size * glass_rate)

        total = frame_prize + glass_prize + net_prize + uchannel_prize + addon_rate

        data = {
            "Frame":
                {
                'type':frame_type,
                'size':frame_size,
                'rate':frame_rate,
                'prize':frame_prize,
                },
            
            "Glass":
                {
                'type':glass_type,
                'size':glass_size,
                'rate':glass_rate,
                'prize':glass_prize,
                },
            
            "I/L Patti":
                {
                'type':lpatti_type,
                'size':lpatti_size,
                'rate':lpatti_rate,
                'prize':lpatti_prize,
                },

            "Net":
                {
                'type':net_type,
                'size':net_size,
                'rate':net_rate,
                'prize':net_prize,
                },
            "U Channel":
                {
                'type':uchannel_type,
                'size':uchannel_size,
                'rate':uchannel_rate,
                'prize':uchannel_prize,
                },
            "Addon":
                {
                'type':addon,
                'prize':addon_rate,
                }
        }

    return render(request,'qoutation.html',{"data":data ,'total':total })