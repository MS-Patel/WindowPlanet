from math import prod
from django.shortcuts import render


from app.models import Coat, Frame, Glass, Ilpatti, Length, Mnet, Product, Shutter, Uchannel, Location
from qoute.models import Products, Quotation

# Create your views here.

def home(request):

    prod = Product.objects.all()
    frame = Frame.objects.all()
    shutter = Shutter.objects.all()
    ilpatti = Ilpatti.objects.all()
    uch = Uchannel.objects.all()
    glass = Glass.objects.all()
    coat = Coat.objects.all()
    length = Length.objects.all()
    location = Location.objects.all()
    net = Mnet.objects.all()


    return render(request,'index.html',{'products':prod, 'frame':frame,'shutter':shutter,'ilpatti':ilpatti,'uch':uch,'glass':glass,'net':net ,'coat':coat, 'length':length, 'location':location})

def partial(request, id):
    
    return render(request, 'part-form.html', {'no':id})

def qoute(request):

    if request.method == 'POST':
        
        print(request.POST)
        product         = request.POST.get('product')
        pd = product.split('-')
        product = pd[0]
        product_name = pd[1]
        location        =request.POST.get('location')
        frame_type      = request.POST.get('frametype')
        frame_size      = float(request.POST.get('framesize'))
        frame_weight    = float(request.POST.get('frameweight'))
        frame_rate      = float(request.POST.get('framerate'))
        # coat.rate      = float(request.POST.get('framecoat'))

        shutter_type    = request.POST.get('shuttertype')
        shutter_size    = float(request.POST.get('shuttersize'))
        shutter_rate    = float(request.POST.get('shutterrate'))
        shutter_weight  = float(request.POST.get('shutterweight'))
        # coat.rate    = float(request.POST.get('shuttercoat'))

        lpatti_type     = request.POST.get('lpattitype')
        lpatti_size     = float(request.POST.get('lpattisize'))
        lpatti_rate     = float(request.POST.get('lpattirate'))
        lpatti_weight   = float(request.POST.get('lpattiweight'))
        # coat.rate     = float(request.POST.get('lpatticoat'))
        
        uchannel_type   = request.POST.get('uchannel_type')
        uchannel_size   = float(request.POST.get('uchannel_size'))
        uchannel_rate   = float(request.POST.get('uchannel_rate'))
        uchannel_weight = float(request.POST.get('uchannel_weight'))
        # coat.rate   = float(request.POST.get('coat.rate'))

        glass_type      = request.POST.get('glasstype')
        glass_rate      = float(request.POST.get('glassrate'))

        net_type        = request.POST.get('nettype')
        net_rate        = float(request.POST.get('netrate'))

        addon           = request.POST.get('addon')
        addon_rate      = float(request.POST.get('addonrate'))

        if request.POST.get('labourrate'):
            labour_rate = float(request.POST.get('labourrate'))
        else:
            labour_rate = 0

        coating = request.POST.get('coating')
        coat=Coat.objects.get(name=coating)

        fh                  = float(request.POST.get('height'))
        fw                  = float(request.POST.get('width'))

        fm_size             = 0
        fm_weight           = 0  
        fm_coat             = 0
        frame_prize         = 0
        sh                  = 0 
        sw                  = 0 
        shtt_size           = 0  
        sh_coat             = 0
        sh_weight           = 0  
        shutter_prize       = 0  
        il_size             = 0
        il_weight           = 0  
        il_coat             = 0
        lpatti_prize        = 0   
        uh                  = 0 
        uw                  = 0 
        uc_size             = 0
        uc_coat             = 0
        uc_weight           = 0  
        uchannel_prize      = 0 
        glass_size          = 0 
        glass_prize         = 0
        net_size            = 0   
        net_prize           = 0  
        coat_total          = 0 
        total               = 0  
        grand_total         = 0

#############################################################################################################       2 Track Window

        
        if product == "1":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw-0.375)/2
            shtt_size           = (sh*4)+(sw*4) 
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            il_size             = (sh*3)
            il_weight           = round(((il_size * lpatti_weight) / lpatti_size),2)
            il_coat             = round(((il_size*coat.rate)/12),2)
            lpatti_prize        = round((il_weight * lpatti_rate),2)

            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


#############################################################################################################       3 Track Window(2+1)

        
        if product == "2":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw-0.375)/2
            shtt_size           = (sh*6)+(sw*6) 
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            il_size             = (sh*4)
            il_weight           = round(((il_size * lpatti_weight) / lpatti_size),2)
            il_coat             = round(((il_size*coat.rate)/12),2)
            lpatti_prize        = round((il_weight * lpatti_rate),2)

            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2                        
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)

#############################################################################################################       3 Track Window

        
        if product == "3":

            fh                  = float(request.POST.get('height'))
            fw                  = float(request.POST.get('width'))

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw+2.25)/3
            shtt_size           = (sh*6)+(sw*6) 
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            il_size             = (sh*4)
            il_weight           = round(((il_size * lpatti_weight) / lpatti_size),2)
            il_coat             = round(((il_size*coat.rate)/12),2)
            lpatti_prize        = round((il_weight * lpatti_rate),2)

            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


#############################################################################################################       3 Track Window(4+2)

        
        if product == "4":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw+2)/4
            shtt_size           = (sh*6)+(sw*6)
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            il_size             = (sh*4)
            il_weight           = round(((il_size * lpatti_weight) / lpatti_size),2)
            il_coat             = round(((il_size*coat.rate)/12),2)
            lpatti_prize        = round((il_weight * lpatti_rate),2)

            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


#############################################################################################################       4 Track Window

        
        if product == "5":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw+4.75)/4
            shtt_size           = (sh*8)+(sw*8)
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            il_size             = (sh*5)
            il_weight           = round(((il_size * lpatti_weight) / lpatti_size),2)
            il_coat             = round(((il_size*coat.rate)/12),2)
            lpatti_prize        = round((il_weight * lpatti_rate),2)

            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


#############################################################################################################       4 Track Window(3+1)

        
        if product == "6":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw+2.25)/3
            shtt_size           = (sh*8)+(sw*8)
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            il_size             = (sh*5)
            il_weight           = round(((il_size * lpatti_weight) / lpatti_size),2)
            il_coat             = round(((il_size*coat.rate)/12),2)
            lpatti_prize        = round((il_weight * lpatti_rate),2)

            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


#############################################################################################################       R-40 Signle shutter

        
        if product == "7":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-1.5
            sw                   = fw-1.5
            shtt_size           = (sh*2)+(sw*2)
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            #uh use here as clip here
            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


#############################################################################################################       R-40 Double Shutter

        
        if product == "8":

            fm_size             = ((fh*2)+(fw*2))
            fm_weight           = round(((fm_size * frame_weight)/ frame_size),2)
            fm_coat             = round(((fm_size*coat.rate)/12),2)
            frame_prize         = round((fm_weight*frame_rate),2)
            
            sh                  = fh-2.75
            sw                  = (fw-1.875)/2
            shtt_size           = (sh*4)+(sw*4)
            sh_coat             = round(((shtt_size*coat.rate)/12),2)
            sh_weight           = round(((shtt_size * shutter_weight)/ shutter_size),2)
            shutter_prize       = round((sh_weight * shutter_rate),2)
        
            #uh use here as clip here
            uh                  = sh-5
            uw                  = sw-5
            uc_size             = (uh+uw)*2
            uc_coat             = round(((uc_size * coat.rate)/12),2)
            uc_weight           = round(((uc_size* uchannel_weight) / uchannel_size),2)
            uchannel_prize      = round((uc_weight * uchannel_rate),2)

            glass_size          = round(((((sh-3.375) * (sw-3.375))*2)/144),2)
            glass_prize         = round((glass_size * glass_rate),2)

            net_size            = round(((sh*sw)/144),2)
            net_prize           = net_size * net_rate

            coat_total          = round((fm_coat + sh_coat + il_coat +uc_coat),2)
            total               = round((frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + addon_rate + labour_rate),2)
            grand_total         = round((coat_total +total),2)


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
                },
            "Labour":
                {
                'type':"Labour Charge",
                'prize':labour_rate,
                },
        }
        # print(data, coat.rate,frame_prize, total,coat_total,grand_total)
        return render(request,'qoutation.html',{"data":data ,'w': fw,'h': fh,'product':product_name, 'pd_code':product,'location':location,'total':total ,'coat_total':coat_total,'grand_total':grand_total})


def tab_content(request):
  
    print(request.POST)
    return render(request,'tab_content.html')