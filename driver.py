from light_strip import LightStrip 
import time
import random

# Create Strip Object of size 15
strip = LightStrip(15)

def fireplace(timer):
    start_time = time.time()

    # Define colors we want to use for fireplace
    fire_colors = ((0,0,0), (255,50,0), (100,0,0), (255,50,0), (255, 100, 0), (255, 0, 0), (100,0,0))
    fire_colors_size = len(fire_colors)

    # Delay Start (2 Seconds)
    time.sleep(2) 

    # Set brightness low for the initial colors 
    strip.set_brightness_all_positions(0.1) 
    strip.show_lights()   # Note: We need to do show_lights() every time we want the lights to display on the physical strip.
  
    # Run until timer is complete
    while time.time() - start_time < timer:
        # Note: _ is an unused variable for the following reason
        # We want to set the color of RANDOM indices for 1/8th of the side of the led strip. 
        for _ in range(strip.size // 8):
            # Select random position from 0 to length of the strip - 1
            pos = random.randint(0, strip.size-1)

            # Select random color from fire_colors
            color_pos = random.randint(0, fire_colors_size - 1)

            # Set color at index "pos" to "color_pos" (our previous two variables)
            strip.set_color_at_position(pos, fire_colors[color_pos])

        strip.show_lights()
        time.sleep(500/1000.0)

try:
    # Run fireplace effect for 10 seconds
    fireplace(10)

    # Turn off all lights after effect is done
    strip.set_color_all_positions((0,0,0))
    strip.show_lights()
except KeyboardInterrupt:
    # If user clicks control C, then kill the program, and clear the lights
    strip.set_color_all_positions((0,0,0))
    strip.show_lights()
