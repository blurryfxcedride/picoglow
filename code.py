import board
import neopixel
import time
from effects import *

# Initialize the NeoPixel strip
NUM_PIXELS = 8
pixels = neopixel.NeoPixel(
    board.GP16, 
    NUM_PIXELS, 
    brightness=1.0, 
    auto_write=False,
    pixel_order=neopixel.GRB
)

def parse_color(color_str):
    """Convert color string to RGB tuple"""
    return tuple(int(x) for x in color_str.split(','))

def read_cues():
    """Read cues from CSV file without using csv module"""
    cues = []
    with open('cues.csv', 'r') as file:
        # Skip header line
        header = file.readline()
        print(f"Header: {header.strip()}")
        
        # Read each line
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            print(f"Processing line {line_num}: {line}")
            try:
                # Split the line by comma, but handle quoted values
                parts = []
                current = []
                in_quotes = False
                
                for char in line:
                    if char == '"':
                        in_quotes = not in_quotes
                    elif char == ',' and not in_quotes:
                        parts.append(''.join(current))
                        current = []
                    else:
                        current.append(char)
                parts.append(''.join(current))
                
                # Make sure we have exactly 5 parts
                if len(parts) != 5:
                    print(f"Wrong number of values in line {line_num}: got {len(parts)}, expected 5")
                    continue
                    
                effect, colors, duration, speed, brightness = parts
                
                # Parse colors if provided
                color_list = []
                if colors:
                    # Remove quotes if present
                    colors = colors.strip('"')
                    color_list = [parse_color(c) for c in colors.split('|')]
                
                cue = {
                    'effect': effect,
                    'colors': color_list,
                    'duration': float(duration),
                    'speed': float(speed),
                    'brightness': float(brightness)
                }
                cues.append(cue)
                print(f"Successfully parsed cue: {cue}")
                
            except Exception as e:
                print(f"Error parsing line {line_num}: {str(e)}")
                continue
                
    print(f"Total cues loaded: {len(cues)}")
    return cues

def run_cue(cue):
    """Run a single cue"""
    effect = cue['effect']
    start_time = time.monotonic()
    
    # Get the effect function
    effect_func = globals().get(effect)
    if not effect_func:
        print(f"Unknown effect: {effect}")
        return

    # Run the effect for the specified duration
    while time.monotonic() - start_time < cue['duration']:
        effect_func(pixels, cue['colors'], cue['speed'], cue['brightness'])

def clear_pixels():
    """Turn off all pixels"""
    pixels.fill((0, 0, 0))
    pixels.show()

def main():
    print("Starting light show...")
    while True:
        try:
            # Read cues from file
            print("Reading cues from file...")
            cues = read_cues()
            print(f"Found {len(cues)} cues")
            
            # Run each cue
            for i, cue in enumerate(cues):
                print(f"Running cue {i+1}: {cue['effect']}")
                run_cue(cue)
                clear_pixels()
                
        except KeyboardInterrupt:
            clear_pixels()
            break
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            clear_pixels()
            time.sleep(1)

if __name__ == "__main__":
    try:
        print("Initializing...")
        main()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
