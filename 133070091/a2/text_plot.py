defaultmaxY=30
defaultmaxX=80
maxX=defaultmaxX
maxY=defaultmaxY

def fitScreen(y,fitminY,fitmaxY):
     y=[float(i) for i in y]
     y=[i-min(y) for i in y]
     y=[i/(max(y)-min(y)) for i in y]
     y=[i*(fitmaxY-fitminY) for i in y] 
     y=[i+fitminY for i in y]
     y=[int(i+.5) for i in y]
     return y
     
def plotFunction (x,y):  #here x and y range from max to min values of them
     xStartmin=min(x)-1
     for y_i in range(maxY,0,-1):
         indices=[i for i, y_temp in enumerate(y) if y_temp == y_i ]
         x_pos=[]
         for i in indices:
             x_pos.append(x[i])
         print_str=''
         last_indx=xStartmin
         for i in x_pos:
             print_str+=(i-last_indx-1)*' '+'*'
             last_indx=i
         print print_str



def TerminalSize():   #this function definition is taken from http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])



     

def plot(x,y):
     try:
         maxX,maxY=TerminalSize()
     else:
         pass
     y=fitScreen(y,1,maxY)
     x=fitScreen(x,1,maxX)
     plotFunction(x,y)


if __name__ == "__main__":
     import math
     try:
        maxX,maxY=TerminalSize()
     except:
        pass
     x=range(0,maxX)
     y=[]
     for i in x:
        y.append ( math.sin( (i*math.pi*2)/(maxX-1) ))
     plot(x,y)


