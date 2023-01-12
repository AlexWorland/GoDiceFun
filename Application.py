import godice as gd
import time

def main():
    print("Scanning for dice...")
    dice_devices = gd.discover_dice()
    while len(dice_devices) < 1:
        print("Found no go dice, retrying...")
        dice_devices = gd.discover_dice()
    print ("Found %d go dice", len(dice_devices))
    for device in dice_devices:
        print("\tFound go dice: %s", device)
    
    die = gd.create_dice(dice_devices[0])

    print("Waiting for die to initiate...")
    while not die.initiated:
        print(".", end="")
        time.sleep(0.5)
    print("")
    
    die.pulse_led(2, 10, 10, [0, 255, 0])

    print("Die initiated")

    while True:
        while not die.result_queue.empty():
            result = die.result_queue.get()
            status = result[0]
            
            # Rolling
            if status == 0:
                print("Rolling...")
                continue

            value = result[1]

            # Not Rolling
            if "MS" in status:
                print("Value: %s -- Move Stable", value)
            elif "S" in status:
                print("Value: %s -- Stable", value)
            elif "TS" in status:
                print("Value: %s -- Tilt Stable", value)
            elif "FS" in status:
                print("Value: %s -- Fake Stable", value)
            elif "B" in status:
                print("Value: %s -- Battery Low", value)
            elif "C" in status:
                print("Color Changed To: %s", value)

if __name__ == "__main__":
    main()
            