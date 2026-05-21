from light import Light
from rp_connector import RPConnector

class LightStrip(RPConnector):
    def __init__(self, size):
        self.size = size    # Size of the light strip
        self.lights = []                # List of Lights which will reflect on the real life strip
        self.create_strip()   # Initialize default strip of size passed in.

        RPConnector.__init__(self, size)
        
    '''
    Override function to update all colors so it's simplified
    '''
    def show_lights(self):
        new_lights = [light.color.rgb for light in self.lights]

        # For now only print the lights, until you have the physical lights set up
        print(self.lights)

        # Uncomment line below once the physical lights are connected
        self.update_all_colors(new_lights)

    '''
    Create initial strip or reset strip to default colors.
    '''
    def create_strip(self):
        for i in range(self.size):
            l = Light(i)
            l.set_color(255, 0, 0) # Set each light to red
            self.lights.append(l)

    '''
    Set all lights to a new color
    '''
    def set_color_all_positions(self, new_color):
        r = new_color[0]
        g = new_color[1]
        b = new_color[2]

        for light in self.lights:
            light.set_color(r,g,b)

    '''
    Set color of light at a given position
    '''
    def set_color_at_position(self, position, new_color):
        r = new_color[0]
        g = new_color[1]
        b = new_color[2]

        self.lights[position].set_color(r,g,b)

    '''
    Set brightness of all lights
    '''
    def set_brightness_all_positions(self, new_brightness):
        if new_brightness < 0 or new_brightness > 1:
            print(f"Cannot set brightness to {new_brightness}. The ")

        for light in self.lights:
            new_color = [int(new_brightness * value) for value in light.color.rgb]

            r = new_color[0]
            g = new_color[1]
            b = new_color[2]

            light.set_color(r,g,b)

    '''
    Create function here to:
    1. Check for time
    2. Call function to set the color of the lights based on the time calculated above
    '''
    def check_time_hr(self):
        import datetime
        time1=datetime.datetime.now()
        str_time_hr=time1.strftime("%H") 
        return str_time_hr #returns the hour as a string
    
    def check_time_min(self):
        import datetime
        time2=datetime.datetime.now()
        str_time_min=time2.strftime("%M")
        return str_time_min #returns the minute as a string
    
    def color_change(self):
        if (self.check_time_hr()=='08'):
            if (self.check_time_min()=='00'):
                self.set_color_all_positions((219, 147, 125))
            if(self.check_time_min()=='05'):
                self.set_color_all_positions((224, 125, 94))
            if(self.check_time_min()=='10'):
                self.set_color_all_positions((230,116,81)) #changes color to orange
            
        if(self.check_time_hr()=='12'):
            self.set_color_all_positions((239,233,80)) #changes color to yellow 
            print('color changed to yellow')
        if(self.check_time_hr()=='17'):
            self.set_color_all_positions((190,169,222)) #changes color to blue
            print('color changed to blue')
        if(self.check_time_hr()=='20'):
            self.set_color_all_positions((19,24,98)) #changes color to dark blue 
            print('color changed to dark blue')

        
