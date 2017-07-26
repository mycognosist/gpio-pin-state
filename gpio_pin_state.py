# Print state of GPIO pins on Raspberry Pi

import os.path

pins = ["20", "21", "05", "06", "13", "19", "14", "15"]

for pin in pins:
    try:
        if not os.path.exists("/sys/class/gpio/gpio" + pin + "/value"):
            s = str(pin)
            f.write(s)
            f.close()
        with open("/sys/class/gpio/gpio" + pin + "/value") as currentPin:
            status = currentPin.read()
            print("Pin %s: %s" % (pin, status)),
    except:
        print ("Pin %s: Error reading pin state." % pin)
