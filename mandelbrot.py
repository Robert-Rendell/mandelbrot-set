# Credits to https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/mandelbrot-set

from PIL import Image, ImageDraw

MAX_ITERATIONS = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITERATIONS:
        z = z*z + c
        n += 1
    return n

def draw_mandelbrot_set():
    # Image size (pixels)
    WIDTH = 600
    HEIGHT = 400

    # Plot window
    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1

    palette = []

    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            m = mandelbrot(c)
            # The color depends on the number of iterations
            color = 255 - int(m * 255 / MAX_ITERATIONS)
            # Plot the point
            draw.point([x, y], (color, color, color))

    im.save('output.png', 'PNG')

if __name__ == "__main__":
    for a in range(-10, 10, 5):
        for b in range(-10, 10, 5):
            c = complex(a / 10, b / 10)
            print(c, mandelbrot(c))

    draw_mandelbrot_set()