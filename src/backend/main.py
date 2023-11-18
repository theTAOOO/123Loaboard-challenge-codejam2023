import sys
sys.path.append('src')

from backend.io import mqtt_connect
from backend.structures import global_controller
import time

def main():
    my_controller = global_controller.GlobalController()
    my_controller.MQTTController.Connect()
    # while(True):
    #     continue
    time.sleep(5)
    print(my_controller.TruckBank.truck_list)

if __name__ == "__main__":
    main()