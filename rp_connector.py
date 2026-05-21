from rpi_ws281x import *
import time

class RPConnector:
    def __init__(self, num_pixels):
        # LED strip configuration:
        LED_COUNT      = num_pixels     # Number of LED pixels.
        LED_PIN        = 18             # GPIO pin connected to the pixels (18 uses PWM!).
        LED_FREQ_HZ    = 800000         # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10             # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255              # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False          # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0              # set to '1' for GPIOs 13, 19, 41, 45 or 53
        
        self.size = num_pixels
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()

    def update_all_colors(self, new_lights):
        for i in range(self.size):
            self.strip.setPixelColor(i, Color(*new_lights[i]))
        self.strip.show()
    