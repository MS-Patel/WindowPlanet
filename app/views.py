import math
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')


def qoute(request):

    if request.method == 'POST':
        
        frame_type = request.POST['frametype']
        frame_size = float(request.POST['framesize'])
        frame_weight = float(request.POST['frameweight'])
        frame_rate = float(request.POST['framerate'])
        frame_coat = float(request.POST['framecoat'])

        shutter_type = request.POST['shuttertype']
        shutter_size = float(request.POST['shuttersize'])
        shutter_rate = float(request.POST['shutterrate'])
        shutter_weight = float(request.POST['shutterweight'])
        shutter_coat = float(request.POST['shuttercoat'])

        lpatti_type = request.POST['lpattitype']
        lpatti_size = float(request.POST['lpattisize'])
        lpatti_rate = float(request.POST['lpattirate'])
        lpatti_weight = float(request.POST['lpattiweight'])
        lpatti_coat = float(request.POST['lpatticoat'])

        uchannel_type = request.POST['uchannel_type']
        uchannel_size = float(request.POST['uchannel_size'])
        uchannel_rate = float(request.POST['uchannel_rate'])
        uchannel_weight = float(request.POST['uchannel_weight'])
        uchannel_coat = float(request.POST['uchannel_coat'])

        glass_type = request.POST['glasstype']
        glass_rate = float(request.POST['glassrate'])

        net_type = request.POST['nettype']
        net_rate = float(request.POST['netrate'])

        addon = request.POST['addon']
        addon_rate = float(request.POST['addonrate'])


####################################################################################################################################

        fh= float(request.POST['height'])
        fw = float(request.POST['width'])

        fm_size = ((fh*2)+(fw*2))
        fm_weight = round(((fm_size * frame_weight)/ frame_size),2)
        fm_coat = round(((fm_size*frame_coat)/12),2)
        frame_prize= round((fm_weight*frame_rate),2)
        
        sh = fh-2.75
        sw = (fw-0.5)/2
        shtt_size = (sh*6)+(sw*6)
        sh_coat = round(((shtt_size*shutter_coat)/12),2)
        sh_weight = round(((shtt_size * shutter_weight)/ shutter_size),2)
        shutter_prize = round((sh_weight * shutter_rate),2)
    
        il_size = (sh*3)
        il_weight = round(((il_size * lpatti_weight) / lpatti_size),2)
        il_coat = round(((il_size*lpatti_coat)/12),2)
        lpatti_prize = round((il_weight * lpatti_rate),2)

        uh = sh-5
        uw = sw-5
        uc_size = (uh+uw)*2
        uc_coat = round(((uc_size * uchannel_coat)/12),2)
        uc_weight = round(((uc_size* uchannel_weight) / uchannel_size),2)
        uchannel_prize = round((uc_weight * uchannel_rate),2)

        glass_size= round(((((sh-4.125) * (sw-4.125))*2)/144),2)
        glass_prize = round((glass_size * glass_rate),2)

        net_size = round(((sh*sw)/144),2)
        net_prize = net_size * net_rate

        coat_total = round((fm_coat + sh_coat + il_coat +uc_coat),2)
        total = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate),2)
        grand_total = round((coat_total +total),2)

        data = {
            "Frame":
                {
                'type':frame_type,
                'size':str(fm_size)+' inch',
                'weight':fm_weight,
                'rate':frame_rate,
                'coat':fm_coat,
                'prize':frame_prize,
                },
            
            "Shutter":
                {
                'type':shutter_type,
                'size':str(shtt_size)+ ' inch',
                'weight':sh_weight,
                'rate':shutter_rate,
                'coat':sh_coat,
                'prize':shutter_prize,
                },
                        
            "I/L Patti":
                {
                'type':lpatti_type,
                'size':str(lpatti_size)+ ' inch',
                'weight':il_weight,
                'rate':lpatti_rate,
                'coat':il_coat,
                'prize':lpatti_prize,
                },

            "U Channel":
                {
                'type':uchannel_type,
                'size':str(uchannel_size)+ ' inch',
                'weight':uc_weight,
                'rate':uchannel_rate,
                'coat':uc_coat,
                'prize':uchannel_prize,
                },

            "Net":
                {
                'type':net_type,
                'size':str(net_size)+ ' sq.foot',
                'rate':net_rate,
                'prize':net_prize,
                },
            "Glass":
                {
                'type':glass_type,
                'size':str(glass_size)+ ' sq.foot',
                'rate':glass_rate,
                'prize':glass_prize,
                },
            "Addon":
                {
                'type':addon,
                'prize':addon_rate,
                }
        }

    return render(request,'qoutation.html',{"data":data ,'total':total ,'coat_total':coat_total,'grand_total':grand_total})