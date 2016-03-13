def attitude(attAdd):
    
    split = i.split("\n")
    split = split[0].split(",")

    #img loc
    place = split[0]

    #satpos
    plat = float(split[1])
    plon = float(split[2])
    palt = float(split[3])

    #sat att
    r = float(split[4])
    p = float(split[5])

    #before sat pos
    lat2 = float(split[6])
    lon2 = float(split[7])

    #img pos
    ilat = float(split[8])
    ilon = float(split[9])

    b = 6356.752
    a = 6378.137

    #rollwithrespecttoearth
    rTrue = degrees(tan(radians(r))*palt/a)
    pTrue = degrees(tan(radians(p))*palt/a)

    #change in pos
    dellat = lat2 - plat
    dellon = lon2 - plon

    #sinA=cotBeta
    sinA = sin(radians(dellon))
    tanB = tan(radians(dellat))
    beta = atan(1/(sinA/tanB))

    alpha = 90-degrees(beta)
    #change of lat and lon due to roll

    corlat1 = degrees(asin(sin(radians(rTrue))*sin(radians(alpha))))
    corlon1 = degrees(atan(cos(radians(alpha))*tan(radians(rTrue))))

    corlat2 = degrees(asin(sin((beta))*sin(radians(pTrue))))
    corlon2 = degrees(acos(cos(radians(pTrue))/cos(radians(corlat2))))

    sumlat = corlat1 + corlat2
    sumlon = corlon1 + corlon2

    estlat = (plat - sumlat)/((b/a)**2)
    estlon = plon - sumlon

    errlat = abs(estlat - ilat)*a*pi/180
    errlon = abs(estlon - ilon)*a*pi/180 

    return estlat, estlon
    
