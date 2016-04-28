from numpy import zeros
from numpy import flipud
import mfc_reader

def readBin(address):
    image_dn = zeros([504,692], dtype = float)
    filename = address
    flip = 0

    def binToInt(astring):
        temp = ' '.join(format(ord(i),'b').zfill(8) for i in astring)
        temp = temp[0:8]+temp[9:17]
        temp = int(temp,2)
        return temp

    def binToInt2(astring):
        temp = ' '.join(format(ord(i),'b').zfill(8) for i in astring)
        temp = temp[0:8]
        temp = int(temp,2)
        return temp

    with open(filename, "rb") as f:
        f.seek(2)
        payload = f.read(2)
        payload = binToInt(payload)

        if payload == 1:
            payload="SMI-VIS"
            f.seek(112)
            v = f.read(2)
            v = binToInt(v)

            f.seek(114)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(116)
            g = f.read(2)
            g = binToInt(g)

            gain = g

            f.seek(150)
            w = f.read(2)
            w = binToInt(w)

            wavelength = 400+w
            
        elif payload == 2:
            payload="SMI-NIR"
            f.seek(112)
            v = f.read(2)
            v = binToInt(v)

            f.seek(114)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(118)
            g = f.read(2)
            g = binToInt(g)

            gain = g

            f.seek(154)
            w = f.read(2)
            w = binToInt(w)

            wavelength = 700+w
            
        elif payload == 3:
            payload="HPT-R"
            f.seek(122)
            v = f.read(2)
            v = binToInt(v)

            f.seek(124)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(126)
            g = f.read(2)
            g = binToInt(g)

            gain = g

            wavelength = payload
            
        elif payload == 4:
            payload="HPT-G"
            f.seek(122)
            v = f.read(2)
            v = binToInt(v)
 
            f.seek(124)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(128)
            g = f.read(2)
            g = binToInt(g)

            gain = g
            wavelength = payload
            
        elif payload == 5:
            payload="HPT-B"
            flip = 1
            f.seek(122)
            v = f.read(2)
            v = binToInt(v)

            f.seek(124)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(130)
            g = f.read(1)
            g = binToInt(g)

            gain = g
            wavelength = payload
            
        elif payload == 6:
            payload="HPT-N"
            flip = 1
            f.seek(122)
            v = f.read(2)
            v = binToInt(v)

            f.seek(124)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(132)
            g = f.read(2)
            g = binToInt(g)

            gain = g
            wavelength = payload
            
        elif payload == 7:
            payload="WFC"
            f.seek(136)
            v = f.read(2)
            v = binToInt(v)


            f.seek(138)
            h = f.read(2)
            h= binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(140)
            g = f.read(1)
            g = binToInt(g)

            gain = g
            wavelength = "PANCHROMATIC"
            
        else:
            payload="MFC"
            f.seek(144)
            v = f.read(2)
            v = binToInt(v)

            f.seek(146)
            h = f.read(2)
            h = binToInt(h)

            expT = (0.03337*v)+(524-h)*(0.00006356)+(487/780)*(0.00006356)

            f.seek(148)
            g = f.read(2)
            g = binToInt(g)

            gain = g
            wavelength = "COLOURED"
            
        f.seek(94)
        year = f.read(1)
        year = 2000+binToInt2(year)
        
        f.seek(95)
        month = f.read(1)
        month = binToInt2(month)

        f.seek(96)
        day = f.read(1)
        day = binToInt2(day)

        f.seek(97)
        hour = f.read(1)
        hour = binToInt2(hour)

        f.seek(98)
        minute = f.read(1)
        minute = binToInt2(minute)

        f.seek(99)
        sec = f.read(1)
        sec = binToInt2(sec)

        f.seek(100)
        msec = f.read(1)
        msec = float(binToInt2(msec))/100

        f.seek(101)
        misec = f.read(1)
        misec = float(binToInt2(misec))/10000

        captime = str(year)+"/"+str(month)+"/"+str(day)+"/"+str(hour)+":"+str(minute)+":"+(str(((float(sec))+msec+misec)))
        
        f.seek(200) #start ng image data after header
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
        image_dn = mfc_reader.forMFC(image_dn)
    print "Payload: "+payload
    print "Capture Time:"+str(captime)
    print "Gain:"+str(gain)
    print "Exposure Time:"+str(expT)+" s"
    return image_dn, payload, captime, gain, expT, wavelength
