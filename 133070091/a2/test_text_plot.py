import text_plot
import unittest

class TestPlot(unittest.TestCase):

      def test_text_plot(self):
         self.assertEqual(text_plot.plot([1,3,7], [1,2,3]),None)
         self.assertEqual(text_plot.plot([1,3,4,6], [6,7,2,3]),None)
                  

      def test_Unequal_Length_Error(self):
         self.assertRaises(IndexError, text_plot.plot, [1,3,4,6], [1,2,3])
         self.assertRaises(IndexError, text_plot.plot, [1,2,3], [1,20,3,6])
                  

      def test_TypeError(self):
         self.assertRaises(TypeError, text_plot.plot , [1,3,4,6], [1,1,2,'3'])
         self.assertRaises(TypeError, text_plot.plot, [1,3,4,'l'], [1,2,2,3])
         self.assertRaises(TypeError, text_plot.plot, [-40], ['-12.2k'])

if __name__ == '__main__':
         unittest.main()


