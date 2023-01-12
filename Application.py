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
    
    die = gd.create_dice(dice_devices[0].address)

    print("Waiting for die to initiate...")
    while not die.initiated:
        print("Waiting for die to initiate...")
        time.sleep(1)
    print("")
    
    die.pulse_led(2, 10, 10, [0, 255, 0])

    die.set_die_type(gd.DieType.D20)

    print("Die initiated")

    batteryCountInterval = 10

    batterCounter = batteryCountInterval

    while True:
        while not die.result_queue.empty():
            result = die.result_queue.get()
            status = result[0]
            
            # Rolling
            if status == "R":
                print("Rolling...")
                continue

            value = result[1]

            # Not Rolling
            if "MS" in status:
                print("Value:", value, "-- Move Stable")
            elif "S" in status:
                print("Value:", value, "-- Stable")
            elif "TS" in status:
                print("Value:", value, "-- Tilt Stable")
            elif "FS" in status:
                print("Value:", value, "-- Fake Stable")
            elif "B" in status:
                print("Value:", value, "-- Battery Level")
                if value < 50:
                    die.pulse_led(5, 40, 50, [255, 255, 0])
            elif "C" in status:
                print("Color Changed To:", value)

            if "B" not in status:
                if value == 20:
                    die.pulse_led(6, 5, 10, [0, 255, 0])
                elif value == 1:
                    die.pulse_led(6, 5, 10, [255, 0, 0])
            
            if batterCounter == 0:
                die.send_battery_request()
                batterCounter = batteryCountInterval
            else:
                batterCounter -= 1
if __name__ == "__main__":
    main()
            