import Image
import matplotlib.image

def img(array, add):
    img = array[0]
    mfc = array[1]
    add = add.split(".")
    if array[1]!="MFC":
        matplotlib.image.imsave(add[0], image_dn, cmap="gray", format=add[1])
    else:
        img = Image.fromarray(rgbArray)
        img.save(add[0]+"."+add[1])
