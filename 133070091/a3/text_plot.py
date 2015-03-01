import sys

class DataLengthMismatch(Exception):
    pass

class InvalidSize(Exception):
    pass    
    
class Canvas:
    """Canvas is a 2d list of characters"""
    
    def __init__ (self, size = None):    #if size==0, get terminal size    #assumed no error in user input size
        """initiate a canvas with size = user given size / default size / current terminal size"""
        
        if size==None:
            self.rows, self.cols= 30, 80
        elif size==0:
            self.rows, self.cols = getTerminalSize()
        else:
            self.rows, self.cols = size
        
        self.body=[]
        for i in range (0,self.rows):
            self.body.append(list(' '*self.cols))
            
    def show (self, output_file = None):
        """Show the Canvas body on output_file"""
        
        if (output_file==None):
            output_file=sys.stdout
        else:
            output_file=open(output_file,'w')
        for line in self.body[::-1]:
            output_file.write(''.join(line)+'\n')
        
    def _scale_to_canvas_body_ (self,x,y):
        
        minX=min(x)
        maxX=max(x)
        if minX==maxX:
           x=[1 for i in x]            #tackes problem with horizontal line
        else:   
           x=[float(i) for i in x]
           x=[  int(       ((i-minX)/(maxX-minX))*(self.cols-1) + 0.5        ) for i in x]
        minY=min(y)
        maxY=max(y)
        if minY==maxY:
          y=[1 for i in y]             #tackles problem with vertical line
        else:
          y=[float(i) for i in y]
          y=[  int(      ((i-minY)/(maxY-minY))*(self.rows-1) + 0.5         ) for i in y]
        return x,y
        
        
            
        
    def _plot_ (self, x, y):
        """        """
        x,y=self._scale_to_canvas_body_(x,y)
        for i in range(len(x)):
           self.body[y[i]][x[i]]='*'

def getTerminalSize():   #this function definition is taken from http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
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
    return int(cr[0]), int(cr[1])

def verify_data(x,y,size):
    if (len(x)!=len(y)):
       raise DataLengthMismatch ("Length of x and y did not match.")
       
    for i in range(len(x)):
       try:
         2+x[i]
       except:
         raise TypeError(str(type(x[i]))+" is not supported. Check type of x["+str(i)+"].")
    for i in range(len(x)):
       try:
         2+y[i]
       except:
         raise TypeError(str(type(y[i]))+" is not supported. Check type of y["+str(i)+"].")
    if not (size==None or size==0 or ( len(size)==2 and type(size[0])==int and type(size[1])==int)  ):
       raise InvalidSize("Check the size parameter.")
         
    
              
def plot(x,y,size=None,output_filename=None):
    "Plot y vs. x.\n keep size=0 to fit the current terminal size"
    verify_data(x,y,size)
    c = Canvas(size)
    c._plot_(x,y)
    c.show(output_filename)
       
def main():
    import numpy as np
    x = np.linspace(0, 2*np.pi, 60)
    plot(x, np.sin(x), size=(30, 80))
       
if __name__=="__main__":
    main()
