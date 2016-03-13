import numpy as np

def forMFC(array):
    row = len(array)
    col = len(array[0])

    red=np.empty([row/2,col/2])
    blue=np.empty([row/2,col/2])
    green=np.empty([row/2,col/2])

    count_red_row =0
    count_red_col = 0
    count_green_row =0
    count_green_col = 0
    count_blue_row =0
    count_blue_col = 0

    for i in range(row):
        for j in range(col):
            if (i%2==0):
                if(j%2==0):
                    red[count_red_row][count_red_col] = (data[i][j])
                    count_red_col+=1
                if(j%2>0):
                    green[count_green_row][count_green_col] = (data[i][j])
                    count_green_col+=1
            if (i%2>0):
                if(j%2>0):
                    blue[count_blue_row][count_blue_col] = (data[i][j])
                    count_blue_col+=1

        count_red_col=0
        count_green_col=0
        count_blue_col=0
        
        if (i%2>0):
            count_blue_row+=1
        if (i%2==0):
            count_red_row+=1
            count_green_row+=1

    rgbArray = np.zeros((252,346,3), 'uint8')
    rgbArray[..., 0] = red
    rgbArray[..., 1] = green
    rgbArray[..., 2] = blue

    return rgbArray
