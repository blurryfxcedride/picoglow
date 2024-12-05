import time
import random

def solid(pixels, colors, speed, brightness):
    """Display solid color(s)"""
    pixels.brightness = brightness
    for i in range(len(pixels)):
        color = colors[i % len(colors)]
        pixels[i] = color
    pixels.show()

def rainbow(pixels, colors, speed, brightness):
    """Create rainbow effect"""
    pixels.brightness = brightness
    for j in range(255):
        for i in range(len(pixels)):
            pixel_index = (i * 256 // len(pixels)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(0.1 / speed)

def chase(pixels, colors, speed, brightness):
    """Create chase effect with given colors"""
    pixels.brightness = brightness
    for i in range(len(pixels) * 2):
        for j in range(len(pixels)):
            if ((j + i) % len(pixels)) < len(colors):
                pixels[j] = colors[(j + i) % len(colors)]
            else:
                pixels[j] = (0, 0, 0)
        pixels.show()
        time.sleep(0.1 / speed)

def sparkle(pixels, colors, speed, brightness):
    """Create sparkle effect with given colors"""
    pixels.brightness = brightness
    for _ in range(20 * speed):
        pixel = random.randint(0, len(pixels) - 1)
        color = random.choice(colors)
        pixels[pixel] = color
        pixels.show()
        time.sleep(0.05 / speed)
        pixels[pixel] = (0, 0, 0)

def fade(pixels, colors, speed, brightness):
    """Fade between given colors"""
    pixels.brightness = brightness
    steps = 100  # Increased steps for smoother transition
    
    # For red to white fade, we'll adjust green and blue channels
    while True:  # Infinite loop
        # Fade from red to white
        for step in range(steps):
            value = int((255 * step) / steps)  # Calculate green/blue value
            for i in range(len(pixels)):
                pixels[i] = (255, value, value)  # Red stays 255, others increase
            pixels.show()
            time.sleep(0.02 / speed)
            
        # Fade from white to red
        for step in range(steps):
            value = int(255 - (255 * step) / steps)  # Calculate decreasing green/blue value
            for i in range(len(pixels)):
                pixels[i] = (255, value, value)  # Red stays 255, others decrease
            pixels.show()
            time.sleep(0.02 / speed)

def pulse(pixels, colors, speed, brightness):
    """Create random pulses of color from black"""
    pixels.brightness = brightness
    steps = 30  # Steps for each pulse
    
    while True:
        # Random wait between pulses
        time.sleep(random.uniform(0.1, 2.0))
        
        # Random starting pixel
        start_pixel = random.randint(0, len(pixels)-1)
        
        # Fade in
        for step in range(steps):
            intensity = int((255 * step) / steps)
            pixels[start_pixel] = (intensity, 0, 0)  # Red pulse
            
            # Optionally affect neighboring pixels with less intensity
            if start_pixel > 0:
                pixels[start_pixel-1] = (intensity//2, 0, 0)
            if start_pixel < len(pixels)-1:
                pixels[start_pixel+1] = (intensity//2, 0, 0)
                
            pixels.show()
            time.sleep(0.01 / speed)
            
        # Hold at full brightness briefly
        time.sleep(random.uniform(0.05, 0.2))
        
        # Fade out
        for step in range(steps):
            intensity = int(255 - (255 * step) / steps)
            pixels[start_pixel] = (intensity, 0, 0)
            
            # Fade out neighbors too
            if start_pixel > 0:
                pixels[start_pixel-1] = (intensity//2, 0, 0)
            if start_pixel < len(pixels)-1:
                pixels[start_pixel+1] = (intensity//2, 0, 0)
                
            pixels.show()
            time.sleep(0.01 / speed)
        
        # Ensure pixels are fully off
        pixels[start_pixel] = (0, 0, 0)
        if start_pixel > 0:
            pixels[start_pixel-1] = (0, 0, 0)
        if start_pixel < len(pixels)-1:
            pixels[start_pixel+1] = (0, 0, 0)
        pixels.show()

def lightning(pixels, colors, speed, brightness):
    """Create lightning-like effect with sudden bright flashes"""
    pixels.brightness = brightness
    
    while True:
        # Wait random time between strikes
        time.sleep(random.uniform(0.5, 3.0))
        
        # Create a strike pattern
        strike_length = random.randint(3, len(pixels))
        start_pos = random.randint(0, len(pixels) - strike_length)
        
        # Initial flash
        for i in range(start_pos, start_pos + strike_length):
            pixels[i] = (255, 0, 0)  # Bright red
        pixels.show()
        time.sleep(0.02)  # Very brief flash
        
        # Quick dim
        for i in range(start_pos, start_pos + strike_length):
            pixels[i] = (64, 0, 0)  # Dimmer red
        pixels.show()
        time.sleep(0.02)
        
        # Secondary flash (branching)
        branch_pos = random.randint(start_pos, start_pos + strike_length - 1)
        branch_length = random.randint(2, 4)
        for i in range(branch_pos, min(branch_pos + branch_length, len(pixels))):
            pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(0.01)
        
        # Final bright flash
        for i in range(start_pos, start_pos + strike_length):
            pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(0.03)
        
        # Quick fade out sequence
        fade_steps = 10
        for step in range(fade_steps):
            intensity = int(255 * (fade_steps - step) / fade_steps)
            for i in range(start_pos, start_pos + strike_length):
                pixels[i] = (intensity, 0, 0)
            pixels.show()
            time.sleep(0.01 / speed)
        
        # Ensure all pixels are off
        for i in range(len(pixels)):
            pixels[i] = (0, 0, 0)
        pixels.show()
        
        # Occasional double strike
        if random.random() < 0.9:  # 90% chance of double strike
            time.sleep(0.1)
            # Repeat a shorter version of the strike
            short_length = random.randint(2, 4)
            short_start = random.randint(0, len(pixels) - short_length)
            for i in range(short_start, short_start + short_length):
                pixels[i] = (255, 0, 0)
            pixels.show()
            time.sleep(0.02)
            # Quick fade out
            for step in range(5):
                intensity = int(255 * (5 - step) / 5)
                for i in range(short_start, short_start + short_length):
                    pixels[i] = (intensity, 0, 0)
                pixels.show()
                time.sleep(0.01 / speed)
            # Clear
            for i in range(len(pixels)):
                pixels[i] = (0, 0, 0)
            pixels.show()

def wheel(pos):
    """Generate rainbow colors across 0-255 positions"""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)
