class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        return print(self.real , "i +" , self.img , "j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return ComplexNumber(newReal ,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return ComplexNumber(newReal ,newImg)
    
c1 = ComplexNumber(1,3)
c2 = ComplexNumber(2,5)
c1.show()
c2.show()
c3 = c1 + c2
c4 = c1 - c2
c3.show()
c4.show()

