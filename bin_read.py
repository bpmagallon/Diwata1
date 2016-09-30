from numpy import zeros
from numpy import flipud, array
import mfc_reader
from struct import unpack

def readBin(address):

    #variables
    image_dn = zeros([504,692], dtype = float)
    filename = address
    flip = 0

    #converts binary to dec
    def binDateToInt(astring):
        temp = ' '.join(format(ord(i),'b').zfill(8) for i in astring)
        temp1 = temp[0:4]
        temp1 = int(temp1,2)
        temp2 = temp[4:8]
        temp2 = int(temp2,2)
        temp = (temp1*10)+temp2
        
        return temp

    #computes exposure time depending on the shutter mode (smd)
    def expTime(smd, v, h):

        if smd==0 or smd==2:
            exposureTime = (v*525+h)*0.00006356
        else:
            exposureTime = (0.03337*v)+(524-h)*(0.00006356)+(float(487)/float(780))*(0.00006356)

        return exposureTime

    """
    check file extension
    .bin=from xtx/shu

    .rg3=from scu
        -> has additional header 151 bytes
    """
    #gets bin extension
    extension = address[-3:]
    if extension == "rg3":
        shift=152
    else:
        shift=0
    
    with open(filename, "rb") as f:
        
        """
        check what payload was used, compute
        exposure time, get wavelength, gain
        1 = SMI-VIS
        2 = SMI-NIR
        3 = HPT-R
        4 = HPT-G
        5 = HPT-B
        6 = HPT-N
        7 = WFC
        8 = MFC
        """
        f.seek(shift+2)
        payload = f.read(2)
        payload = unpack(">H",payload)[0]

        #for SMI
        if (payload == 1) or (payload == 2):
            if payload==1:
                payload="SMI-VIS"
                #wavelength used
                f.seek(shift+152)
                w = f.read(2)
                w = unpack(">H",w)[0] 
                wavelength = 400+ (w-16384)

                #smi gain
                f.seek(shift+116)
                gain = f.read(2)
                gain = unpack(">H",gain)[0]
            
            else:
                payload="SMI-NIR"
                #wavelength used
                f.seek(shift+156)
                w = f.read(2)
                w = unpack(">H",w)[0]
                wavelength = 730+ (w-16384)

                #smi gain
                f.seek(shift+118)
                gain = f.read(2)
                gain = unpack(">H",gain)[0]
                
            #reads shutter mode 0-disable 1-enable 
            f.seek(shift+111)
            smd = f.read(1)
            smd = unpack(">B",smd)[0]

            #reads shutter speed MSV
            f.seek(shift+112)
            v = f.read(2)
            v = unpack(">H",v)[0]

            #reads shutter speed LSV
            f.seek(shift+114)
            h = f.read(2)
            h = unpack(">H",h)[0]

            #computes exposure time
            expT = expTime(smd, v, h)

        #for HPT   
        elif (payload == 3) or (payload == 4) or (payload == 5) or (payload == 6):
            if payload == 3:
                payload="HPT-R"
                f.seek(shift+126)
                gain = f.read(2)
                gain = unpack(">H",gain)[0]
                wavelength = payload

            elif payload == 4:
                payload="HPT-G"
                f.seek(shift+128)
                gain = f.read(2)
                gain = unpack(">H",gain)[0]
                wavelength = payload

            elif payload == 5:
                payload="HPT-B"
                f.seek(shift+130)
                gain = f.read(2)
                gain = unpack(">H",gain)[0]
                wavelength = payload
                
            else:
                payload="HPT-N"
                f.seek(shift+132)
                gain = f.read(2)
                gain = unpack(">H",gain)[0]
                wavelength = payload
     
            f.seek(shift+121)
            smd = f.read(1)
            smd = unpack(">B",smd)[0]
            
            f.seek(shift+122)
            v = f.read(2)
            v = unpack(">H",v)[0]

            f.seek(shift+124)
            h = f.read(2)
            h = unpack(">H",h)[0]

            expT = expTime(smd, v, h)

        elif payload == 7:
            payload="WFC"
            f.seek(shift+135)
            smd = f.read(1)
            smd = unpack(">B",smd)[0]

            f.seek(shift+136)
            v = f.read(2)
            v = unpack(">H",v)[0]

            f.seek(shift+138)
            h = f.read(2)
            h= unpack(">H",h)[0]

            expT = expTime(smd, v, h)

            f.seek(shift+140)
            gain = f.read(2)
            gain = unpack(">H",gain)[0]
            wavelength = "PANCHROMATIC"
            
        else:
            payload="MFC"
            f.seek(shift+143)
            smd = f.read(1)
            smd = unpack(">B",smd)[0]
            
            f.seek(shift+144)
            v = f.read(2)
            v = unpack(">H",v)[0]

            f.seek(shift+146)
            h = f.read(2)
            h = unpack(">H",h)[0]

            expT = expTime(smd, v, h)

            f.seek(shift+148)
            gain = f.read(2)
            gain = unpack(">H",gain)[0]
            wavelength = "COLOURED"

        print payload
        #image capture time
        f.seek(shift+94)
        year = f.read(1)
        year = binDateToInt(year)+2000
        
        f.seek(shift+95)
        month = f.read(1)
        month = binDateToInt(month)

        f.seek(shift+96)
        day = f.read(1)
        day = binDateToInt(day)

        f.seek(shift+97)
        hour = f.read(1)
        hour = binDateToInt(hour)

        f.seek(shift+98)
        minute = f.read(1)
        minute = binDateToInt(minute)

        f.seek(shift+99)
        sec = f.read(1)
        sec = binDateToInt(sec)

        f.seek(shift+100)
        msec = f.read(1)
        msec = float(binDateToInt(msec))/100

        f.seek(shift+101)
        misec = f.read(1)
        misec = float(binDateToInt(misec))/10000

        captime = str(year)+"/"+str(month)+"/"+str(day)+" "+str(hour)+":"+str(minute)+":"+(str(((float(sec))+msec+misec)))
        
        f.seek(shift+200) #start ng image data after header
        data = f.read(504*692*2)
        data = array(unpack(">"+"H"*(504*692),data)).reshape(504,692)
        image_dn = data
        
    print "Bin file from: "+payload

    """
    flip the image if it is HPT-B
    -> ccd positioning
    """
    if flip == 1:
        image_dn = flipud(image_dn)
    else:
        pass

    """
    MFC camera uses Bayer filter,
    output makes the image 1/4 the original size
    """
    if payload=="MFC":
        image_dn = mfc_reader.forMFC(image_dn)
        
    print "Payload: "+payload
    print "Capture Time:"+str(captime)
    print "Gain:"+str(gain)
    print "Exposure Time:"+str(expT)+" s"
    print "Wavelength:" + str(wavelength) 
    return image_dn, payload, captime, gain, expT, wavelength, shift
