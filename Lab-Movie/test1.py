from jes4py import*


def makeRectMovieA(directory):
    for num in range(1,150):
        canvas = makeEmptyPicture(300,200)
        if num == 1:
            addRectFilled(canvas,0,0,50,50,red)
        else:
            addRectFilled(canvas,num+8,num+4,50,50,red)
        if num+8 >= 250 or num +4 >= 150:
            return
        numStr = str(num)
        if num <10:
            writePictureTo(canvas ,directory+"/ frame0"+numStr+".jpg")
        if num >= 10:
            writePictureTo(canvas,directory+"/ frame"+numStr+".jpg")

    movie = makeMovieFromInitialFile(directory+"/ frame00.jpg")
    return movie

def makeRectMovieB(directory):
    print(1)
    for num in range(1,150):
        canvas = makeEmptyPicture(300,200)

rectM = makeRectMovieA("./Lab-Movie/Part2/")
playMovie(rectM)

# a:  from top left to buttom right
# B:  from top right to buttom left
# C:  from buttom left to top right
# D:  from buttom right to top left
# Do this at home
