import sys
sys.path.append('src')

from backend.structures import GlobalController
import threading

def main():
    my_controller = GlobalController.GlobalController()

    main_thread = threading.Thread(target = my_controller.MQTTController.Connect)
    flask_thread = threading.Thread(target=my_controller.ReactController.start_thread)

    main_thread.start()
    flask_thread.start()

if __name__ == "__main__":
    main()