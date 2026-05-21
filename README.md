# Light_Sync
Light_Sync is an object-oriented, Python-based LED controller designed for Raspberry Pi hardware. Built to interface with WS281x LED strips, the project abstracts hardware complexities to allow for programmatic, time-synchronized ambient lighting and dynamic physical animations.
**Architecture**
driver.py: The main execution script that instantiates a strip of 15 LEDs, runs a 10-second fireplace animation, and ensures lights are safely cleared upon a KeyboardInterrupt.
light_strip.py: The core controller that inherits from RPConnector to manage the array of LED objects. It handles broad operations like brightness adjustment across all LEDs, position-specific targeting, and reading the system time for dynamic color updates.
rp_connector.py: The low-level class that configures the DMA channel and initializes the Adafruit_NeoPixel library to push color state arrays directly to the physical hardware.
light.py: Represents an individual node on the LED strip, storing its exact zero-indexed position and current assigned color.
color.py: A utility class standardizing input representations and facilitating clean RGB-to-Hex conversions.
**Requirements**
Raspberry Pi with GPIO capabilities.
WS281x (or equivalent) LED strip.
Python 3.x.
rpi_ws281x Python library.
