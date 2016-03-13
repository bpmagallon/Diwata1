import bin_read
import error_catch
import toa_convert
import img_save

def commRead(command):
    commands = []
    string = command

    binComm = string.find("-bin")
    if binComm != -1:
        split = string.split("-bin")
        split = split[1].split(" ")
        binAdd = split[1]
        err = error_catch.errCatch(2, binAdd)
        if err != 2:
            binOut = bin_read.readBin(binAdd)
    else:
        error_catch.errCatch(1, binAdd)
    
    toaComm = string.find("-toa")
    if toaComm != -1:
        split = string.split("-toa")
        split = split[1].split(" ")
        gain = split[1]
        expT = split[2]
        err = error_catch.errCatch(3, str(gain)+" "+str(expT))
        if err != 3:
            toaOut = toa_convert.toa(binOut, gain, expT)
        
    imgComm = string.find("-img")
    if imgComm != -1:
        split = string.split("-img")
        split = split[1].split(" ")
        imgAdd = split[1]
        err = error_catch.errCatch(2, imgAdd)
        if err !=2:
            if toaComm != -1:
                img_save.img(toaOut, imgAdd)
            else:
                img_save.img(binOut, imgAdd)
        
    attComm = string.find("-att")
    if attComm != -1:
        split = string.split("-att")
        split = split[1].split(" ")
        attAdd = split[1]
        error_catch.errCatch(2, attAdd)

    footComm = string.find("-footprint")
    if footComm != -1:
        split = string.split("-footprint")
        split = split[1].split(" ")
        footAdd = split[1]
        error_catch.errCatch(2, footAdd)
