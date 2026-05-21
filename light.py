from color import Color

class Light:
    def __init__(self, position):
        self.position = position    # Position of the light on the strip starting from 0
        self.color = None           # Default color of the light
    
    '''
    Set the color of this light to Color object
    '''
    def set_color(self, r, g, b):
        self.color = Color(r, g, b)

    '''
    Overrides the print method, and treats the light as the hex representation
    '''
    def __repr__(self) -> str:
        return self.color.hexadecimal if self.color else None
