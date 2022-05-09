from django.http import HttpResponse
import datetime
from django.shortcuts import render
from app.models import Addon, Coat, Frame, Glass, Ilpatti, Length, Mnet, Product, Quotation, QuotationItem, Shutter, Uchannel, Location, Clip


# Create your views here.

def home(request):

    prod = Product.objects.all()
    frame = Frame.objects.all()
    shutter = Shutter.objects.all()
    ilpatti = Ilpatti.objects.all()
    clip = Clip.objects.all()
    uch = Uchannel.objects.all()
    glass = Glass.objects.all()
    coat = Coat.objects.all()
    length = Length.objects.all()
    location = Location.objects.all()
    net = Mnet.objects.all()

    return render(request,'index.html',{'products':prod, 'frame':frame,'shutter':shutter,'ilpatti':ilpatti,'clip':clip,'uch':uch,'glass':glass,'net':net ,'coat':coat, 'length':length, 'location':location})

def delpartial(request):

    return HttpResponse("")

def partial(request, id):
    id = int(id) + 1 
    prod = Product.objects.all()
    frame = Frame.objects.all()
    shutter = Shutter.objects.all()
    ilpatti = Ilpatti.objects.all()
    clip = Clip.objects.all()
    uch = Uchannel.objects.all()
    glass = Glass.objects.all()
    coat = Coat.objects.all()
    length = Length.objects.all()
    location = Location.objects.all()
    net = Mnet.objects.all()

    return render(request, 'part-form.html', {'no':id,'products':prod, 'frame':frame,'shutter':shutter,'ilpatti':ilpatti,'clip':clip,'uch':uch,'glass':glass,'net':net ,'coat':coat, 'length':length, 'location':location })

def qoute(request):

    if request.method == 'POST':
        

        qt = Quotation.objects.last()
        if qt:
            qouteid = int(qt.id) + 1
        else:
            qouteid = 1000

        productlist         = request.POST.getlist('product')
        locationlist        =request.POST.getlist('location')
        coatinglist         =request.POST.getlist('coating')
        frame_typelist      = request.POST.getlist('frametype')
        frame_sizelist      = request.POST.getlist('framesize')
        frame_weightlist    = request.POST.getlist('frameweight')
        frame_ratelist      = request.POST.getlist('framerate')
        # coat.rate      = float(request.POST.getlist('framecoat'))

        shutter_typelist    = request.POST.getlist('shuttertype')
        shutter_sizelist    = request.POST.getlist('shuttersize')
        shutter_ratelist    = request.POST.getlist('shutterrate')
        shutter_weightlist  = request.POST.getlist('shutterweight')
        # coat.rate    = float(request.POST.getlist('shuttercoat'))

        lpatti_typelist     = request.POST.getlist('lpattitype')
        lpatti_sizelist     = request.POST.getlist('lpattisize')
        lpatti_ratelist     = request.POST.getlist('lpattirate')
        lpatti_weightlist   = request.POST.getlist('lpattiweight')
        # coat.rate     = float(request.POST.getlist('lpatticoat'))
        
        uchannel_typelist   = request.POST.getlist('uchannel_type')
        uchannel_sizelist   = request.POST.getlist('uchannel_size')
        uchannel_ratelist   = request.POST.getlist('uchannel_rate')
        uchannel_weightlist = request.POST.getlist('uchannel_weight')
        # coat.rate   = float(request.POST.getlist('coat.rate'))

        clip_typelist     = request.POST.getlist('cliptype')
        clip_sizelist     = request.POST.getlist('clipsize')
        clip_ratelist     = request.POST.getlist('cliprate')
        clip_weightlist   = request.POST.getlist('clipweight')
        # coat.rate     = float(request.POST.getlist('clipcoat'))


        glass_typelist      = request.POST.getlist('glasstype')
        glass_ratelist      = request.POST.getlist('glassrate')

        net_typelist        = request.POST.getlist('nettype')
        net_ratelist        = request.POST.getlist('netrate')

        
        # extra_ratelist      = request.POST.getlist('extrarate')

        labour_ratelist     = request.POST.getlist('labourrate')

        transport_ratelist  = request.POST.getlist('transportrate')



        fhlist              = request.POST.getlist('height')
        fwlist              = request.POST.getlist('width')
        fmlist              = request.POST.getlist('margin')
        qtylist             = request.POST.getlist('qty')
        hl_list             = request.POST.getlist('handlelock')
        pl_list             = request.POST.getlist('pushlock')

    


        qoute = []
        for i,j in enumerate(productlist):
            product = j
            pd = product.split('-')
            product = pd[0]
            product_name = pd[1]
            coating         = coatinglist[i]
            location        =locationlist[i]
            frame_type      = frame_typelist[i]
            frame_size      = float(frame_sizelist[i])
            frame_weight    = float(frame_weightlist[i])
            frame_rate      = float(frame_ratelist[i])
            # coat.rate      = float(request.POST.getlist('framecoat'))

            shutter_type    = shutter_typelist[i]
            shutter_size    = float(shutter_sizelist[i])
            shutter_rate    = float(shutter_ratelist[i])
            shutter_weight  = float(shutter_weightlist[i])
            # coat.rate    = float(request.POST.getlist('shuttercoat'))

            lpatti_type     = lpatti_typelist[i]
            lpatti_size     = float(lpatti_sizelist[i])

            if lpatti_ratelist[i]:
                lpatti_rate = float(lpatti_ratelist[i])
            else:
                lpatti_rate = 0

            if lpatti_weightlist[i]:    
                lpatti_weight   = float(lpatti_weightlist[i])
            else:
                lpatti_weight = 0
            # coat.rate     = float(request.POST.getlist('lpatticoat'))
            
            uchannel_type   = uchannel_typelist[i]
            uchannel_size   = float(uchannel_sizelist[i])

            if uchannel_ratelist[i]:
                uchannel_rate   = float(uchannel_ratelist[i])
            else:
                uchannel_rate = 0

            if uchannel_weightlist[i]:
                uchannel_weight = float(uchannel_weightlist[i])
            else:
                uchannel_weight=0
            # coat.rate   = float(request.POST.getlist('coat.rate'))

            clip_type     = clip_typelist[i]
            clip_size     = float(clip_sizelist[i])

            if clip_ratelist[i]:
                clip_rate     = float(clip_ratelist[i])
            else:
                clip_rate = 0
            
            if clip_weightlist[i]:
                clip_weight   = float(clip_weightlist[i])
            else:
                clip_weight = 0
            # coat.rate     = float(request.POST.getlist('lpatticoat'))

            glass_type      = glass_typelist[i]
            glass_rate      = float(glass_ratelist[i])

            net_type        = net_typelist[i]
            net_rate        = float(net_ratelist[i])

            # if extra_ratelist[i]:
            #     extra_rate   = float(extra_ratelist[i])
            # else:
            #     extra_rate = 0    

            
            if labour_ratelist[i]:
                labour_rate = float(labour_ratelist[i])
            else:
                labour_rate = 0

            if transport_ratelist[i]:
                transport_rate= float(transport_ratelist[i])
            else:
                transport_rate = 0
                
            if hl_list[i]:
                hl = float(hl_list[i])
            else:
                hl = 0

            if pl_list[i]:
                pl = float(pl_list[i])
            else:
                pl = 0

            
            
            coat=Coat.objects.get(name=coating)

            fh                  = float(fhlist[i])
            fw                  = float(fwlist[i])
            qty                 = float(qtylist[i])
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
            ch                  = 0
            cw                  = 0 
            cl_size             = 0
            cl_weight           = 0  
            cl_coat             = 0
            clip_prize          = 0  
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
            addon_total         = 0  
            lab_rate            = float(labour_ratelist[i])
            
            

    #############################################################################################################       2 Track Window
            
            if product == "1":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size) #frame_size=freame_length
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-2.75)
                sw                  = ((fw-0.375)/2)
                shtt_size           = (((sh*4)+(sw*4))/12)
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)
            
                il_size             = ((sh*3) / 12)
                il_weight           = ((il_size * lpatti_weight) / lpatti_size)
                il_coat             = (il_size*coat.rate)
                lpatti_prize        = (il_weight * lpatti_rate)

                

                uh                  = (sh-5)
                uw                  = (sw-5)
                uc_size             = (((uh+uw)*2) / 12)
                uc_coat             = (uc_size * coat.rate)
                uc_weight           = ((uc_size* uchannel_weight) / uchannel_size)
                uchannel_prize      = (uc_weight * uchannel_rate)

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = (((sh-3.375) + (sw-3.375)) * 2) 

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)

                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat + il_coat +uc_coat+cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + clip_prize + labour_rate + transport_rate)
                
               
                

                
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today() 


    #####################################################################*########################################       3 Track Window(2+1)
            
            if product == "2":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-2.75)
                sw                  = ((fw-0.375)/2)
                shtt_size           = (((sh*6)+(sw*6))/12) 
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)
            
                il_size             = ((sh*4) / 12)
                il_weight           = ((il_size * lpatti_weight) / lpatti_size)
                il_coat             = (il_size*coat.rate)
                lpatti_prize        = (il_weight * lpatti_rate)

                uh                  =(sh-5)
                uw                  = (sw-5)
                uc_size             = (((uh+uw)*2) / 12)                      
                uc_coat             = (uc_size * coat.rate)
                uc_weight           = ((uc_size* uchannel_weight) / uchannel_size)
                uchannel_prize      = (uc_weight * uchannel_rate)

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = (((sh-3.375) + (sw-3.375)) * 2)

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)
                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat + il_coat +uc_coat+cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize + clip_prize + labour_rate+ transport_rate)
                

                
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today()
    #############################################################################################################       3 Track Window
            
            if product == "3":

                fm_size             = (((fh*2)+(fw*2))/12)
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-2.75)
                sw                  = ((fw+2.25)/3)
                shtt_size           = (((sh*6)+(sw*6))/12) 
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)
            
                il_size             = ((sh*4) / 12)
                il_weight           = ((il_size * lpatti_weight) / lpatti_size)
                il_coat             = (il_size*coat.rate)
                lpatti_prize        = (il_weight * lpatti_rate)

                uh                  = (sh-5)
                uw                  = (sw-5)
                uc_size             = (((uh+uw)*2) / 12)
                uc_coat             = (uc_size * coat.rate)
                uc_weight           = ((uc_size* uchannel_weight) / uchannel_size)
                uchannel_prize      = (uc_weight * uchannel_rate)

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = ((sh-3.375) + (sw-3.375)) * 2

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)
                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat + il_coat +uc_coat+cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + uchannel_prize  + clip_prize + labour_rate+ transport_rate)
                

                addon_total = 0
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today()
    #############################################################################################################       3 Track Window(4+2)
            
            if product == "4":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-2.75)
                sw                  = ((fw+2)/4)
                shtt_size           = (((sh*6)+(sw*6))/12)
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)
            
                il_size             = ((sh*4) / 12)
                il_weight           = ((il_size * lpatti_weight) / lpatti_size)
                il_coat             = (il_size*coat.rate)
                lpatti_prize        = (il_weight * lpatti_rate)

                uh                  = (sh-5)
                uw                  = (sw-5)
                uc_size             = (((uh+uw)*2) / 12)
                uc_coat             = (uc_size * coat.rate)
                uc_weight           = ((uc_size* uchannel_weight) / uchannel_size)
                uchannel_prize      = (uc_weight * uchannel_rate)

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = ((((sh-3.375) + (sw-3.375))) * 2)

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)
                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat + il_coat +uc_coat+cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + clip_prize + uchannel_prize  + labour_rate+ transport_rate)
                

                addon_total = 0
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today()

    #############################################################################################################       4 Track Window

            
            if product == "5":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-2.75)
                sw                  = ((fw+4.75)/4)
                shtt_size           = (((sh*8)+(sw*8))/12)
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)
            
                il_size             = ((sh*5) / 12)
                il_weight           = ((il_size * lpatti_weight) / lpatti_size)
                il_coat             = (il_size*coat.rate)
                lpatti_prize        = (il_weight * lpatti_rate)

                uh                  = (sh-5)
                uw                  = (sw-5)
                uc_size             = (((uh+uw)*2) / 12)
                uc_coat             = (uc_size * coat.rate)
                uc_weight           = ((uc_size* uchannel_weight) / uchannel_size)
                uchannel_prize      = (uc_weight * uchannel_rate)

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = (((sh-3.375) + (sw-3.375)) * 2)

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)
                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat + il_coat +uc_coat+cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + clip_prize + uchannel_prize  + labour_rate+ transport_rate)
                

                addon_total = 0
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today()
    #############################################################################################################       4 Track Window(3+1)

            if product == "6":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-2.75)
                sw                  = ((fw+2.25)/3)
                shtt_size           = (((sh*8)+(sw*8))/12)
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)
            
                il_size             = ((sh*5) / 12)
                il_weight           = ((il_size * lpatti_weight) / lpatti_size)
                il_coat             = ((il_size*coat.rate)/12)
                lpatti_prize        = (il_weight * lpatti_rate)

                uh                  = (sh-5)
                uw                  = (sw-5)
                uc_size             = (((uh+uw)*2) / 12)
                uc_coat             = (uc_size * coat.rate)
                uc_weight           = ((uc_size* uchannel_weight) / uchannel_size)
                uchannel_prize      = (uc_weight * uchannel_rate)

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = (((sh-3.375) + (sw-3.375)) * 2)

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)
                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat + il_coat +uc_coat+cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + glass_prize + net_prize + clip_prize + uchannel_prize + labour_rate+ transport_rate)
                
                addon_total = 0
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today()
    #############################################################################################################       R-40 Signle shutter
            
            if product == "7":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = (fh-1.5)
                sw                  = (fw-1.5)
                shtt_size           = (((sh*2)+(sw*2))/12)
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)


                ch                  = (sh-3.125)
                cw                  = (sw-4.25)
                cl_size             = (((ch*2)+(cw*2))/12)
                cl_coat             = (cl_size*coat.rate)
                cl_weight           = ((cl_size * clip_weight)/ clip_size)
                clip_prize          = (cl_weight * clip_rate)
            

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = (((sh-3.375) + (sw-3.375)) * 2)

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)
                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat +cl_coat)
                total               = (frame_prize + shutter_prize  + glass_prize + net_prize + clip_prize + + labour_rate+ transport_rate)
                

                addon_total = 0
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         +=(gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                today               = datetime.date.today()       
    #############################################################################################################       R-40 Double Shutter

            
            if product == "8":

                fm_size             = (((fh*2)+(fw*2))/12) 
                fm_weight           = ((fm_size * frame_weight)/ frame_size)
                fm_coat             = (fm_size*coat.rate)
                frame_prize         = (fm_weight*frame_rate)
                
                sh                  = fh-2.75
                sw                  = fw-1.875
                shtt_size           = (((sh*4)+(sw*4))/12)
                sh_coat             = (shtt_size*coat.rate)
                sh_weight           = ((shtt_size * shutter_weight)/ shutter_size)
                shutter_prize       = (sh_weight * shutter_rate)


                ch                  = sh-3.125
                cw                  = sw-4.25
                cl_size             = (((ch*4)+(cw*4))/12)
                cl_coat             = (cl_size*coat.rate)
                cl_weight           = ((cl_size * clip_weight)/ clip_size)
                clip_prize          = (cl_weight * clip_rate)
               

                glass_size          = ((((sh-3.375) * (sw-3.375))*2)/144)
                glass_prize         = (glass_size * glass_rate)
                gr_ft               = (((sh-3.375) + (sw-3.375)) * 2)

                net_size            = ((sh*sw)/144)
                net_prize           = (net_size * net_rate)

                labour_rate         = (fm_size*lab_rate) 

                coat_total          = (fm_coat + sh_coat +cl_coat)
                total               = (frame_prize + shutter_prize + lpatti_prize + clip_prize + glass_prize + net_prize + uchannel_prize  + labour_rate+ transport_rate)
                

                addon_total = 0
                addon_total         += (pl * Addon.objects.get(item="PushLock").rate)
                addon_total         += (hl * Addon.objects.get(item="HandleLock").rate)
                addon_total         += (Addon.objects.get(item="silicone").rate)
                addon_total         += (Addon.objects.get(item="screw").rate)
                addon_total         += (16 * Addon.objects.get(item="lcorner").rate)
                addon_total         += (4 * Addon.objects.get(item="malefemale").rate)
                addon_total         += (2 * Addon.objects.get(item="longpatti").rate)
                addon_total         += (4 * Addon.objects.get(item="log").rate)
                addon_total         += (8 * Addon.objects.get(item="cleat").rate)
                addon_total         += (gr_ft * Addon.objects.get(item="pvc").rate)
                addon_total         += (shtt_size * 2 * Addon.objects.get(item="woolen").rate)
                addon_total         += (4 * Addon.objects.get(item="bearing").rate)
                grand_total          = round(coat_total +total+addon_total,2)
                addon_total         = round(addon_total,2)
                """Shows todays current time and date."""
                today               = datetime.date.today()
                 
               
            data = {
                "Frame":
                    {
                    'type'           :frame_type,
                    'size'           :str(round(fm_size,2))+' ft',
                    'weight'         :round(fm_weight,2),
                    'rate'           :frame_rate,
                    'coat'           :round(fm_coat,2),
                    'prize'           :round(frame_prize,2),
                    },
                
                "Shutter":
                    {
                    'type'           :shutter_type,
                    'size'           :str(round(shtt_size,2))+ ' ft',
                    'weight'           :round(sh_weight,2),
                    'rate'           :shutter_rate,
                    'coat'           :round(sh_coat,2),
                    'prize'           :round(shutter_prize,2),
                    },
                            
                "I/L Patti":
                    {
                    'type'           :lpatti_type,
                    'size'           :str(round(il_size,2))+ ' ft',
                    'weight'           :round(il_weight,2),
                    'rate'           :lpatti_rate,
                    'coat'           :round(il_coat,2),
                    'prize'           :round(lpatti_prize,2),
                    },
                "U Channel":
                    {
                    'type'           :uchannel_type,
                    'size'           :str(round(uc_size,2))+ ' ft',
                    'weight'           :round(uc_weight,2),
                    'rate'           :uchannel_rate,
                    'coat'           :round(uc_coat,2),
                    'prize'           :round(uchannel_prize,2),
                    },

                "Clip":
                    {
                    'type'           :clip_type ,
                    'size'           :str(round(cl_size,2))+ ' ft',
                    'weight'           :round(cl_weight,2),
                    'rate'           :clip_rate,
                    'coat'           :round(cl_coat,2),
                    'prize'           :round(clip_prize,2),
                    },

                "Net":
                    {
                    'type'           :net_type,
                    'size'           :str(round(net_size,2))+ ' sq.ft',
                    'rate'           :net_rate,
                    'prize'           :round(net_prize,2),
                    },
                "Glass":
                    {
                    'type'           :glass_type,
                    'size'           :str(round(glass_size,2))+ ' sq.ft',
                    'rate'           :glass_rate,
                    'prize'           :round(glass_prize,2),
                    },
                
                "Labour":
                    {
                    'type'           :"Labour Charge",
                    'prize'           :round(labour_rate,2),
                    },
                "Trans":
                    {
                    'type'           :"Transport Charge",
                    'prize'           :round(transport_rate,2),
                    },
                
                
            } 
            total = {'qouteid':qouteid,'qty':qty,'w': fw,'h': fh,'product':product_name, 'pd_code':product,'location':location,'pl':pl,'hl':hl,'coating':coating,'total':round(total,2) ,'coat_total': round(coat_total,2),'grand_total':grand_total,'addon_total':addon_total}
            item = [data,total]
            qoute.append(item)
        context = { 'qoutes':qoute,'today':today}
        
        return render(request,'qoutation.html',context)


def tab_content(request):
  
    if request.method == 'POST':
        
        quotation_date=datetime.date.today()
        qoute = request.POST.get('qouteid')
        to  =request.POST.get('to')
        to_address_line_1  =request.POST.get('to_address_line_1')
        to_address_line_2  =request.POST.get('to_address_line_2')
        to_address_line_3  =request.POST.get('to_address_line_3')
        to_contact_no  =request.POST.get('to_contact_no')
        deliver_to  =request.POST.get('deliver_to')
        deliver_to_address_line_1  =request.POST.get('deliver_to_address_line_1')
        deliver_to_address_line_2  =request.POST.get('deliver_to_address_line_2')
        deliver_to_address_line_3  =request.POST.get('deliver_to_address_line_3')
        deliver_to_contact_no  =request.POST.get('deliver_to_contact_no')
        customer_reference  =request.POST.get('customer_reference')
        responsible  =request.POST.get('responsible')
        
        total_qty = 0
        totalvalue = 0
        totalsize=0
        totallabour=0
        total_transport_charge=0
        finalvalue=0
        gst=0
        summery = 0
        if qoute:
            qt = Quotation.objects.create(id=qoute,quotation_date=quotation_date,total_transport_charge=total_transport_charge,finalvalue=finalvalue,gst=gst,summery=summery,totalsize=totalsize,totallabour=totallabour,total_qty = total_qty, totalvalue=totalvalue,to=to,deliver_to=deliver_to,customer_reference=customer_reference,responsible=responsible,to_address_line_1=to_address_line_1,to_address_line_2=to_address_line_2,to_address_line_3=to_address_line_3,to_contact_no=to_contact_no,deliver_to_address_line_1=deliver_to_address_line_1,deliver_to_address_line_2=deliver_to_address_line_2,deliver_to_address_line_3=deliver_to_address_line_3,deliver_to_contact_no=deliver_to_contact_no)
            productlist = request.POST.getlist('product')
        # qlist = request.POST.getlist('q')
        wlist = request.POST.getlist('w') #width
        hlist = request.POST.getlist('h') #height
        mlist = request.POST.getlist('m')
        locationlist = request.POST.getlist('location') #location
        qtylist = request.POST.getlist('qty') #quantity
        totallist= request.POST.getlist('total')
        lablist = request.POST.getlist('labourrate')
        translist = request.POST.getlist('tranportrate')
        framelist = request.POST.getlist('framerate') #section details
        glasslist = request.POST.getlist('glassrate')
        coatinglist = request.POST.getlist('coating')
        pllist = request.POST.getlist('pl')
        hllist = request.POST.getlist('hl') 

        


        for i,j in enumerate(productlist):

            product = Product.objects.get(code=j)
            # q = float(qlist[i])
            w = float(wlist[i])#width
            h = float(hlist[i]) #height
            m = float(mlist[i]) 
            size = round(((w*h)/144),2)  #Sq.Ft. per Window
            location = locationlist[i]   #location
            pl = pllist[i]
            hl = hllist[i]
            total =float(totallist[i])
            ma= round(( total+((total * m ) /100)),2)
            qty = float(qtylist[i]) #quantity
            labt = float(lablist[i])
            frame = framelist[i]  #section details
            coating = coatinglist[i]
            glass = glasslist[i]
            value = round(( ma * qty),2)
            # total_qid = q 
            total_qty += (qty) # end quantity
            totalvalue += (ma)
            totalsize +=(size) # end total area  Sq.Ft. per Window
            
            totallabour += (labt)
           
            
            transt = float(translist[i])
            total_transport_charge += ( transt)
            finalvalue += value
            average_value = (finalvalue / totalsize)
            gst=((finalvalue * 18 ) /100)
            summery = (finalvalue+gst)
           
            QuotationItem.objects.create(qoutation=qt,
                                            product=product,
                                            h=h, #height
                                            w=w, #width
                                            size=size, #size sq.per window 
                                            location=location,
                                            pl=pl,
                                            hl=hl,
                                            qty=qty, #quantity
                                            unitprice=ma,
                                            value=value,
                                            labour=labt,
                                            section=frame,  #section details
                                            shutter=coating,
                                            glass=glass,
                                            transport_charge=transt,
                                            )
        qt.quotation_date=quotation_date                                    
        qt.qoute = qoute
        qt.total_qty = total_qty, # total qty
        qt.totalvalue = round(totalvalue,2)
        qt.to =to
        qt.to_address_line_1 =to_address_line_1
        qt.to_address_line_2 =to_address_line_2
        qt.to_address_line_3 =to_address_line_3
        qt.to_contact_no =to_contact_no
        qt.deliver_to =deliver_to
        qt.deliver_to_address_line_1 =deliver_to_address_line_1
        qt.deliver_to_address_line_2 =deliver_to_address_line_2
        qt.deliver_to_address_line_3 =deliver_to_address_line_3
        qt.deliver_to_contact_no =deliver_to_contact_no
        qt.customer_reference =customer_reference
        qt.responsible =responsible
        qt.totalsize                = round(totalsize,2) # total size sq.ft per window
        qt.totallabour              = round(totallabour,2)
        qt.total_transport_charge   = round(total_transport_charge,2)
        qt.finalvalue               = round(finalvalue,2)
        qt.gst                      = round(gst,2)    
        qt.summery = round(summery,2)
        qt.save()

        # qt=Quotation.objects.last()
    
        items= QuotationItem.objects.filter(qoutation=qt)
        for i in items:
            print(i.pl)
        today= datetime.date.today()
        context = { 'data': items,'to':to,'to_address_line_1':to_address_line_1,'to_address_line_2':to_address_line_2,'to_address_line_3':to_address_line_3,'to_contact_no':to_contact_no,'deliver_to_address_line_1':deliver_to_address_line_1,'deliver_to_address_line_2':deliver_to_address_line_2,'deliver_to_address_line_3':deliver_to_address_line_3,'deliver_to_contact_no':deliver_to_contact_no,'deliver_to':deliver_to,'customer_reference':customer_reference,'responsible':responsible,'today':today,'quotation_date':quotation_date, 'qoute':qoute , 'total': totalvalue, 'qty' : total_qty ,'sqft' : totalsize, 'avgvalue':average_value ,'totallabour':totallabour,'finalvalue':finalvalue ,'total_transport_charge':total_transport_charge,'gst':gst,'summery':summery } 

        return render(request,'tab_content.html',context)