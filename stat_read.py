from struct import unpack

def readStat(address, binOut):
    filename = address
    """
    checks the Satellite System Status
    Values to be checked:
        DPU +3.3V, 5V, 1.8V, 15V, -15V Voltage and Current
        DPU +5VD VoltageCurrent
        DPU +5VA Current
        LCTF1+2 +3.3V Current
        LCTF1+2 +15V Current
        LCTF1+2 -15V Current

        HPT VIS Current
        HPT NIR Current
        SMI VIS+NIR Current
        OOC2 Current
        OOC3 Current
        TAMU Current

        HPT TEMP
        SMI TEMP
        WFC TEMP
        MFC TEMP
        FPGA TEMP
        DPU TEMP

        LCTF VIS TEMP
        LCTF NIR TEMP
    """

    #input from binOut
    #image_dn, payload, captime, gain, expT, wavelength, shift
    shift = binOut[6]
    with open(filename, "rb") as f:

        #DPU
        f.seek(shift+25)
        dpu = f.read(1)
        dpu = unpack(">B",dpu)[0]*5/float(255)
        dpu = (((dpu+4.17)/float(19500))-0.000273)*1000000

        f.seek(shift+41)
        dpu3p3VV = f.read(1)
        dpu3p3VV = unpack(">B", dpu3p3VV)[0]*5/float(255)

        f.seek(shift+40)
        dpu5VV = f.read(1)
        dpu5VV = (unpack(">B", dpu5VV)[0]*5/float(255))*5/float(3.76)

        f.seek(shift+42)
        dpu15VV = f.read(1)
        dpu15VV = (unpack(">B", dpu15VV)[0]*5/float(255))*15/float(3.75)

        f.seek(shift+43)
        dpum15VV = f.read(1)
        dpum15VV = -1*(unpack(">B", dpum15VV)[0]*5/float(255))*15/float(3.75)

        f.seek(shift+44)
        dpu18VV = f.read(1)
        dpu18VV = (unpack(">B", dpu18VV)[0]*5/float(255))*1.8/float(3.6)

        f.seek(shift+31)
        dpu3p3VC = f.read(1)
        dpu3p3VC = (unpack(">B", dpu3p3VC)[0]*5/float(255))/float(11.32)

        f.seek(shift+32)
        dpu5VD = f.read(1)
        dpu5VD = (unpack(">B", dpu5VD)[0]*5/float(255))/float(2.27)

        f.seek(shift+33)
        dpu5VA = f.read(1)
        dpu5VA = (unpack(">B", dpu5VA)[0]*5/float(255))/float(41.32)

        #LCTF
        f.seek(shift+28)
        lctf33VC = f.read(1)
        lctf33VC = (unpack(">B", lctf33VC)[0]*5/float(255))/float(11.32)

        f.seek(shift+29)
        lctf15VC = f.read(1)
        lctf15VC = (unpack(">B", lctf15VC)[0]*5/float(255))/float(5.45)

        f.seek(shift+30)
        lctfm15VC = f.read(1)
        lctfm15VC = (unpack(">B", lctfm15VC)[0]*5/float(255))/float(17.73)

        f.seek(shift+26)
        lctfVIS = f.read(1)
        lctfVIS = (float(64)/float(3))*(unpack(">B", lctfVIS)[0]*5/float(255))-17

        f.seek(shift+27)
        lctfNIR = f.read(1)
        lctfNIR = (float(64)/float(3))*(unpack(">B", lctfNIR)[0]*5/float(255))-17
        
        #HPT
        f.seek(shift+20)
        hpt = f.read(1)
        hpt = unpack(">B",hpt)[0]*5/float(255)
        hpt = (((hpt+4.17)/float(19500))-0.000273)*1000000

        f.seek(shift+35)
        hptvisC = f.read(1)
        hptvisC = (unpack(">B", hptvisC)[0]*5/float(255))/float(2.27)

        f.seek(shift+34)
        hptnirC = f.read(1)
        hptnirC = (unpack(">B", hptnirC)[0]*5/float(255))/float(6.82)

        #SMI
        f.seek(shift+21)
        smi = f.read(1)
        smi = unpack(">B",smi)[0]*5/float(255)
        smi = (((smi+4.17)/float(19500))-0.000273)*1000000

        f.seek(shift+36)
        smiC = f.read(1)
        smiC = (unpack(">B", smiC)[0]*5/float(255))/float(3.41)

        #MFC
        f.seek(shift+23)
        mfc = f.read(1)
        mfc = unpack(">B",mfc)[0]*5/float(255)
        mfc = (((mfc+4.17)/float(19500))-0.000273)*1000000

        f.seek(shift+38)
        mfcC = f.read(1)
        mfcC = (unpack(">B", mfcC)[0]*5/float(255))/float(6.82)

        #WFC
        f.seek(shift+22)
        wfc = f.read(1)
        wfc = unpack(">B",wfc)[0]*5/float(255)
        wfc = (((wfc+4.17)/float(19500))-0.000273)*1000000

        f.seek(shift+37)
        wfcC = f.read(1)
        wfcC = (unpack(">B", wfcC)[0]*5/float(255))/float(6.82)
        
        #FPGA
        f.seek(shift+24)
        FPGA = f.read(1)
        FPGA = unpack(">B",FPGA)[0]*5/float(255)
        FPGA = (((FPGA+4.17)/float(19500))-0.000273)*1000000

        #TAMU
        f.seek(shift+39)
        tamuC = f.read(1)
        tamuC = (unpack(">B", tamuC)[0]*5/float(255))/float(1.71)

        print "DPU +3.3V Voltage: "+str(dpu3p3VV)
        print "DPU +5V Voltage: "+str(dpu5VV)
        print "DPU +15V Voltage: "+str(dpu15VV)
        print "DPU -15V Voltage: "+str(dpum15VV)
        print "DPU +1.8V Voltage: "+str(dpu18VV)    

        print "DPU +3.3V Current: "+str(dpu3p3VC)
        print "DPU +5VD Current: "+str(dpu5VD)
        print "DPU +5VA Current: "+str(dpu5VA)
    
        print "LCTF1+2 +3.3V Current: "+str(lctf33VC)
        print "LCTF1+2 +15V Current: "+str(lctf15VC)
        print "LCTF1+2 -15V Current: "+str(lctfm15VC)

        print "HPT VIS Current: "+str(hptvisC)
        print "HPT NIR Current: "+str(hptnirC)
        print "SMI VIS+NIR Current: "+str(smiC)
        print "WFC Current: "+str(wfcC)
        print "MFC Current: "+str(mfcC)
        print "TAMU Current: "+str(tamuC)

        print "HPT TEMP: "+str(hpt)
        print "SMI TEMP: "+str(smi)
        print "WFC TEMP: "+str(wfc)
        print "MFC TEMP: "+str(mfc)
        print "FPGA TEMP: "+str(FPGA)
        print "DPU TEMP: "+str(dpu)

        print "LCTF VIS TEMP: "+str(lctfVIS)
        print "LCTF NIR TEMP: "+str(lctfNIR)
