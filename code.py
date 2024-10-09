import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3
max = 255
while True:
    print("""Type 1 to show red
Type 2 to show blue
Type 3 to show green
""")
    Prog = input("Select your color, or quit(type q): ").lower()
    if Prog == 'q':
        #Turn off the leds
        for i in range(10):
            cp.pixels[i]=(0,0,0)
            cp.pixels.show()
        print("All LEDs are OFF.")
        print("Program ended.")
        break
    try:
     
 
        color = int(Prog)
        if color == 1:
            for i in range(10):
                cp.pixels[i] = (max, 0, 0)  
                cp.pixels.show()
                time.sleep(0.3)

        elif color == 2:
            for i in range(10):
                cp.pixels[i] = (0, 0, max) 
                cp.pixels.show()
                time.sleep(0.3)

        elif color == 3:
          
            for i in range(10):
                cp.pixels[i] = (0, max, 0)  
                cp.pixels.show()
                time.sleep(0.3)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
    except ValueError:
        print("Invalid Input. Please type an integer")
        continue
