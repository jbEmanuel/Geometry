import math 

class Rectangle():
    """ Rectangle class for calculating the geometric measures of a rectangle.
    
    Attributes:
        comp (float) representing the lenght (comprimento) value of the rectangle
        lag (float) representing the lenght (largura) of the rectangle
            
    """
    def __init__(self, comp, larg):
        self.comp = comp 
        self.larg = larg 
    
    def area(self):
        """Function to calculate the area of the rectangle.
        
        Args: 
            None
        
        Returns: 
            float: area of the rectangle 
    
        """
        _area = self.comp *self.larg 

        return _area 

    def perimeter(self):
        """Function to calculate the perimeter of the rectangle.
        
        Args: 
            None
        
        Returns: 
            float: perimeter of the rectangle 
    
        """
        if self.comp == self.larg:
            _perimeter = 4 * self.comp
        else: 
            _perimeter = 2 * (self.comp + self.larg)
        
        return _perimeter


