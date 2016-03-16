from numpy import zeros
from numpy import flipud

def readBin(address):
    image_dn = zeros([504,692], dtype = float)
    filename = address
    flip = 0

    def binToInt(astring):
        temp = ' '.join(format(ord(i),'b').zfill(8) for i in astring)
        temp = temp[0:8]+temp[9:17]
        temp = int(temp,2)
        return temp

    def binToInt2(astring)
        temp = ' '.join(format(ord(i),'b').zfill(8) for i in astring)
        temp = temp[0:8]
        temp = int(temp,2)
        return temp

    with open(filename, "rb") as f:
        f.seek(1)
        payload = f.read(2)
        if payload == 1:
            payload="SMI-VIS"
            f.seek(103)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(104)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(105)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(106)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(107)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(108)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl 

            f.seek(141)
            w_h = f.read(1)
            w_h = binToInt2(1)

            f.seek(142)
            w_l = f.read(1)
            w_l = binToInt2(1)

            wavelength = 400+((w_h)*256)+w_l
            
        elif payload == 2:
            payload="SMI-NIR"
            f.seek(103)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(104)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(105)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(106)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(109)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(110)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl 

            f.seek(145)
            w_h = f.read(1)
            w_h = binToInt2(1)

            f.seek(146)
            w_l = f.read(1)
            w_l = binToInt2(1)

            wavelength = 700+((w_h)*256)+w_l
            
        elif payload == 2:
            payload="HPT-R"
            f.seek(113)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(114)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(115)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(116)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(117)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(118)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl 

            wavelength = payload
            
        elif payload == 2:
            payload="HPT-G"
            f.seek(113)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(114)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(115)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(116)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(119)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(120)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl
            wavelength = payload
            
        elif payload == 2:
            payload="HPT-B"
            flip = 1
            f.seek(113)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(114)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(115)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(116)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(121)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(122)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl
            wavelength = payload
            
        elif payload == 2:
            payload="HPT-N"
            flip = 1
            f.seek(113)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(114)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(115)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(116)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(123)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(124)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl
            wavelength = payload
            
        elif payload == 2:
            payload="WFC"
            f.seek(127)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(128)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(129)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(130)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(131)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(132)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl
            wavelength = "PANCHROMATIC"
            
        else:
            payload="MFC"
            f.seek(135)
            vh = f.read(1)
            vh = binToInt2(vh)

            f.seek(136)
            vl = f.read(1)
            vl = binToInt2(vl)

            v = (vh*256)+vl

            f.seek(137)
            hh = f.read(1)
            hh = binToInt2(hh)


            f.seek(138)
            hl = f.read(1)
            hl = binToInt2(hl)
            
            h = (hh*256)+hl

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(139)
            gh = f.read(1)
            gh = binToInt2(gh)

            f.seek(140)
            gl = f.read(1)
            gl = binToInt2(gl)

            gain = (gh*256)+gl
            wavelength = "COLOURED"
            
        f.seek(85)
        year = f.read(1)
        year = 2000+binToInt2(year)
        
        f.seek(86)
        month = f.read(1)
        month = binToInt2(month)

        f.seek(87)
        day = f.read(1)
        day = binToInt2(day)

        f.seek(88)
        hour = f.read(1)
        hour = binToInt2(hour)

        f.seek(89)
        minute = f.read(1)
        minute = binToInt2(minute)

        f.seek(90)
        sec = f.read(1)
        sec = binToInt2(sec)

        f.seek(91)
        msec = f.read(1)
        msec = float(binToInt2(msec))/100

        f.seek(92)
        misec = f.read(1)
        misec = float(binToInt2(misec)/10000

        captime = str(year)+"/"+str(month)+"/"+str(day)+"/"+str(hour)+":"+str(minute)+":"+(str(sec+msec+misec))
        
        f.seek(199) #start ng image data after header
        for i in range(0,504):
            for j in range(0,692):
                data = f.read(2)
                data = binToInt(data)
                image_dn[i,j]=data
                
    print "Bin file from: "+payload
    if flip == 1:
        image_dn = flipud(image_dn)
    else:
        pass

    if payload=="MFC":
        image_dn = forMFC(image_dn)
        
    return image_dn, payload, captime, gain, expT, wavelenght
