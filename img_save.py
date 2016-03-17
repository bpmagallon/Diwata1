import Image
import matplotlib.image

def img(array, add):
    img = array[0]
    mfc = array[1]
    if array[1]!="MFC":

        matplotlib.image.imsave(add, img, cmap="gray", format="png")
    else:
        img_mfc = Image.fromarray(img.astype('uint8'))
        img_mfc.save(add)
