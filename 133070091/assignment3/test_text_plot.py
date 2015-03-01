import text_plot
import unittest
import numpy
import os

class TestPlot(unittest.TestCase):        

      def test_text_plot(self):                #the sample test_case_output files should be in the current directory
         text_plot.plot([1,3,7], [1,2.0,3.0],None,"output_file.txt")
         a=open("test_case_output_1.txt",'r').read()
         b=open("output_file.txt",'r').read()
         self.assertEqual(a,b)   #check if working
         
         x=[1]*20
         y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
         text_plot.plot(x,y,(10,10),"output_file.txt")
         a=open("test_case_output_2.txt",'r').read()
         b=open("output_file.txt",'r').read()
         self.assertEqual(a,b)         
         
         x=[1]*20
         y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
         text_plot.plot(x,y,(20,10),"output_file.txt")
         a=open("test_case_output_3.txt",'r').read()
         b=open("output_file.txt",'r').read()
         self.assertEqual(a,b) 
         
         x=[1]*20
         y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
         text_plot.plot(y,x,(20,20),"output_file.txt")
         a=open("test_case_output_4.txt",'r').read()
         b=open("output_file.txt",'r').read()
         self.assertEqual(a,b) 
         os.remove("output_file.txt")
                  

      def test_Unequal_Length_Error(self):
         self.assertRaises(text_plot.DataLengthMismatch, text_plot.plot, [1,3,4,6], [1,2,3])
         self.assertRaises(text_plot.DataLengthMismatch, text_plot.plot, [1,2,3], [1,20,3,6])
      
                 
      def test_TypeError(self):
         self.assertRaises(TypeError, text_plot.plot, [1,3,4,6], [1,1,2,'3'])
         self.assertRaises(TypeError, text_plot.plot, [1,3,4,'l'], [1,2,2,3])
         self.assertRaises(TypeError, text_plot.plot, [-40], ['-12.2k'])
         
      def test_SizeError(self):
        self.assertRaises(text_plot.InvalidSize, text_plot.plot, [1,3,7], [1,2.0,3.0], (3.0,1.0), "output_file.txt")

if __name__ == '__main__':
         unittest.main()


