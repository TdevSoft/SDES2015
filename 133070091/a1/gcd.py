def gcd(a, b):
         if b>a:
             a,b=b,a
         if not ( (type(a)==int or type(a)==long) and (type (b)==int or type (b)==long) ) :
            raise TypeError
         elif b<0:
            raise ValueError
         while b:
             a, b = b, a%b
         return a
