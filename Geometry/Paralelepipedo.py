import math 

class Paralelepipedo():
    """ Paralelepipedo class for calculating the geometric measures of a paralelepipedo.
    
    Attributes:
        x (float) representing the lenght (comprimento) value of the paralelepipedo
        y (float) representing the lenght (largura) of the paralelepipedo
        z (float) representing the lenght (altura) of the paralelepipedo
            
    """
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z 
    
    def volume(self):
        """Function to calculate the volume of a paralelepipedo.
        
        Args: 
            None
        
        Returns: 
            float: volume of the paralelepipedo 
    
        """

        result = self.x * self.y * self.z 
        
        return result

    