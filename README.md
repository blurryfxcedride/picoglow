# PicoGlow - A Simple NeoPixel Light Show Controller

This project allows you to create custom light shows for a NeoPixel LED strip using a Raspberry Pi Pico and CircuitPython.

If you find any bugs or have any suggestions... please make an issue!

## Setup
1. Install CircuitPython on your Raspberry Pi Pico
2. Install Required Libraries:
   - Download the latest CircuitPython Library Bundle from [CircuitPython's website](https://circuitpython.org/libraries)
   - From the bundle, copy these files to the `lib` folder on your CIRCUITPY drive:
     - `neopixel.mpy`
     - `adafruit_pixelbuf.mpy`
3. Copy all the project files to your CIRCUITPY drive
4. Connect your NeoPixel strip to:
   - Data: GPIO Pin 16
   - Power: VBUS (5V)
   - Ground: GND

## How to Use
1. Edit the `cues.csv` file to design your light show
2. Each row in the CSV represents a lighting cue with the following columns:
   - effect: The lighting effect to use (see Available Effects below)
   - colors: Comma-separated RGB values (e.g., "255,0,0|0,255,0" for red and green)
   - duration: How long to run the effect (in seconds)
   - speed: Speed of the effect (1-10, where 10 is fastest)
   - brightness: LED brightness (0-1.0)

## Available Effects
- solid: Display solid color(s)
- rainbow: Cycle through rainbow colors
- chase: Chase effect with given colors
- sparkle: Random twinkling effect with given colors
- fade: Fade between given colors
- pulse: Creates random pulses of color that fade in and out with subtle spreading to neighboring pixels
- lightning: Creates lightning-like strikes with branching and double-strike effects

## Effect Details

### Solid
Displays one or more solid colors. If multiple colors are provided, it will distribute them across the strip.
```csv
solid,"255,0,0|0,255,0",3,1,1.0  # Alternates between red and green
```

### Rainbow
Creates a smooth rainbow effect cycling through all colors.
```csv
rainbow,,5,5,0.5  # Note: doesn't need color values
```

### Chase
Creates a chasing effect with the provided colors.
```csv
chase,"255,0,0|0,255,0",4,7,0.8  # Red and green chase
```

### Sparkle
Creates random twinkling effects using the provided colors.
```csv
sparkle,"0,0,255|255,255,255",3,8,0.6  # Blue and white sparkles
```

### Fade
Smoothly transitions between the provided colors.
```csv
fade,"255,0,0|0,255,0|0,0,255",6,3,0.7  # Fades between red, green, and blue
```

### Pulse
Creates random pulses that fade in and out, with a subtle spread to neighboring pixels.
```csv
pulse,"255,0,0",10,3,1.0  # Random red pulses
```

### Lightning
Creates dramatic lightning-like effects with:
- Random length strikes
- Branching patterns
- 90% chance of double strikes
- Variable timing between strikes
```csv
lightning,"255,0,0",10,2,1.0  # Red lightning strikes
```

## Example Cue
```csv
effect,colors,duration,speed,brightness
rainbow,,5,5,0.5
solid,"255,0,0",3,1,1.0
lightning,"255,0,0",10,2,1.0
pulse,"255,0,0",8,3,0.8
```
