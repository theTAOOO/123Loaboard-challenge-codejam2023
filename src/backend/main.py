import sys
sys.path.append('src')

from backend.io import mqtt_connect

def main():
    my_connection = mqtt_connect.MQTTConnect()

if __name__ == "__main__":
    main()