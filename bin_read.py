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

    with open(filename, "rb") as f:
        f.seek(1)
        payload = f.read(2)
        if payload == 1:
            payload="SMI-VIS"
        elif payload == 2:
            payload="SMI-NIR"
        elif payload == 2:
            payload="HPT-R"
        elif payload == 2:
            payload="HPT-G"
        elif payload == 2:
            payload="HPT-B"
            flip = 1
        elif payload == 2:
            payload="HPT-N"
            flip = 1
        elif payload == 2:
            payload="WFC"
        else:
            payload="MFC"
            
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
        
    return image_dn, payload
