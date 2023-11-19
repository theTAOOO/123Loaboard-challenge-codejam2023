import sys
sys.path.append('src')

from backend.structures import GlobalController

def main():
    my_controller = GlobalController.GlobalController()
    my_controller.MQTTController.Connect()
    # while(True):
    #     continue
    time.sleep(5)
    print(my_controller.TruckBank.truck_list)

if __name__ == "__main__":
    main()