from django.shortcuts import render
from app.models import Coat, Frame, Glass, Ilpatti, Length, Mnet, Product, Quotation, QuotationItem, Shutter, Uchannel, Location


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

    return render(request, 'part-form.html', {'no':id,'products':prod, 'frame':frame,'shutter':shutter,'ilpatti':ilpatti,'uch':uch,'glass':glass,'net':net ,'coat':coat, 'length':length, 'location':location })

def qoute(request):

    if request.method == 'POST':

        qt = Quotation.objects.last()
        if qt:
            qouteid = int(qt.id) + 1
        else:
            qouteid = 1000

        productlist         = request.POST.getlist('product')
        locationlist        =request.POST.getlist('location')
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

        glass_typelist      = request.POST.getlist('glasstype')
        glass_ratelist      = request.POST.getlist('glassrate')

        net_typelist        = request.POST.getlist('nettype')
        net_ratelist        = request.POST.getlist('netrate')

        addonlist           = request.POST.getlist('addon')
        addon_ratelist      = request.POST.getlist('addonrate')

        labour_ratelist = request.POST.getlist('labourrate')

        coatinglist = request.POST.getlist('coating')

        fhlist              = request.POST.getlist('height')
        fwlist              = request.POST.getlist('width')
        qtylist             = request.POST.getlist('qty')

        qoute = []
        for i,j in enumerate(productlist):
            product = j
            pd = product.split('-')
            product = pd[0]
            product_name = pd[1]
            
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
            lpatti_rate     = float(lpatti_ratelist[i])
            lpatti_weight   = float(lpatti_weightlist[i])
            # coat.rate     = float(request.POST.getlist('lpatticoat'))
            
            uchannel_type   = uchannel_typelist[i]
            uchannel_size   = float(uchannel_sizelist[i])
            uchannel_rate   = float(uchannel_ratelist[i])
            uchannel_weight = float(uchannel_weightlist[i])
            # coat.rate   = float(request.POST.getlist('coat.rate'))

            glass_type      = glass_typelist[i]
            glass_rate      = float(glass_ratelist[i])

            net_type        = net_typelist[i]
            net_rate        = float(net_ratelist[i])

            addon           = addonlist[i]
            addon_rate      = float(addon_ratelist[i])

            if labour_ratelist[i]:
                labour_rate = float(addon_ratelist[i])
            else:
                labour_rate = 0

            coating = coatinglist[i]
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw-0.375)/2
                shtt_size           = (sh*4)+(sw*4) 
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                il_size             = (sh*3)
                il_weight           = round(((il_size/12 * lpatti_weight) / lpatti_size),2)
                il_coat             = round(((il_size/12 *coat.rate)/12),2)
                lpatti_prize        = round((il_weight * lpatti_rate),2)

                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw-0.375)/2
                shtt_size           = (sh*6)+(sw*6) 
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                il_size             = (sh*4)
                il_weight           = round(((il_size/12 * lpatti_weight) / lpatti_size),2)
                il_coat             = round(((il_size/12 *coat.rate)/12),2)
                lpatti_prize        = round((il_weight * lpatti_rate),2)

                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2                        
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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

                fm_size             = ((fh*2)+(fw*2))
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw+2.25)/3
                shtt_size           = (sh*6)+(sw*6) 
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                il_size             = (sh*4)
                il_weight           = round(((il_size/12 * lpatti_weight) / lpatti_size),2)
                il_coat             = round(((il_size/12 *coat.rate)/12),2)
                lpatti_prize        = round((il_weight * lpatti_rate),2)

                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw+2)/4
                shtt_size           = (sh*6)+(sw*6)
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                il_size             = (sh*4)
                il_weight           = round(((il_size/12 * lpatti_weight) / lpatti_size),2)
                il_coat             = round(((il_size/12 *coat.rate)/12),2)
                lpatti_prize        = round((il_weight * lpatti_rate),2)

                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw+4.75)/4
                shtt_size           = (sh*8)+(sw*8)
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                il_size             = (sh*5)
                il_weight           = round(((il_size/12 * lpatti_weight) / lpatti_size),2)
                il_coat             = round(((il_size/12 *coat.rate)/12),2)
                lpatti_prize        = round((il_weight * lpatti_rate),2)

                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw+2.25)/3
                shtt_size           = (sh*8)+(sw*8)
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                il_size             = (sh*5)
                il_weight           = round(((il_size/12 * lpatti_weight) / lpatti_size),2)
                il_coat             = round(((il_size/12 *coat.rate)/12),2)
                lpatti_prize        = round((il_weight * lpatti_rate),2)

                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-1.5
                sw                   = fw-1.5
                shtt_size           = (sh*2)+(sw*2)
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                #uh use here as clip here
                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
                fm_weight           = round(((fm_size/12 * frame_weight)/ frame_size),2)
                fm_coat             = round(((fm_size/12 *coat.rate)/12),2)
                frame_prize         = round((fm_weight*frame_rate),2)
                
                sh                  = fh-2.75
                sw                  = (fw-1.875)/2
                shtt_size           = (sh*4)+(sw*4)
                sh_coat             = round(((shtt_size/12 *coat.rate)/12),2)
                sh_weight           = round(((shtt_size/12 * shutter_weight)/ shutter_size),2)
                shutter_prize       = round((sh_weight * shutter_rate),2)
            
                #uh use here as clip here
                uh                  = sh-5
                uw                  = sw-5
                uc_size             = (uh+uw)*2
                uc_coat             = round(((uc_size/12 * coat.rate)/12),2)
                uc_weight           = round(((uc_size/12 * uchannel_weight) / uchannel_size),2)
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
            total = {'qouteid':qouteid,'qty':qty,'w': fw,'h': fh,'product':product_name, 'pd_code':product,'location':location,'total':total ,'coat_total':coat_total,'grand_total':grand_total}
            item = [data,total]
            qoute.append(item)
        context = { 'qoutes':qoute}

        return render(request,'qoutation.html',context)


def tab_content(request):
  
    if request.method == 'POST':
 
        qoute = request.POST.get('qouteid')
        total_qty = 0
        totalvalue = 0
        if qoute:
            qt = Quotation.objects.create(id=qoute, total_qty = total_qty, totalvalue=totalvalue)
        productlist = request.POST.getlist('product')
        wlist = request.POST.getlist('w')
        hlist = request.POST.getlist('h')
        locationlist = request.POST.getlist('location')
        qtylist = request.POST.getlist('qty')
        totallist= request.POST.getlist('total')

        for i,j in enumerate(productlist):

            product = Product.objects.get(code=j)
            w = float(wlist[i])
            h = float(hlist[i])
            size = w*h
            location = locationlist[i]
            total = float(totallist[i])
            qty = float(qtylist[i])
            value = total * qty
            total_qty +=qty
            totalvalue +=value 
            QuotationItem.objects.create(qoutation=qt,
                                            product=product,
                                            h=h,
                                            w=w,
                                            size=size,
                                            location=location,
                                            qty=qty,
                                            unitprice=total,
                                            value=value)
        qt.total_qty = total_qty
        qt.totalvalue = totalvalue
        qt.save()

        items= QuotationItem.objects.filter(qoutation=qt)

        context = { 'data': items}

        return render(request,'tab_content.html',context)