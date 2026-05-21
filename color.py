class Color:
    def __init__(self, r, g, b):
        color_hex = self.rgb2hex(r, g, b)   # Convert input rgb to hex
        self.rgb = (r, g, b)
        self.hexadecimal = color_hex

    def rgb2hex(self, r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)