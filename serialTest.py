import serial
import time
import sys
import getopt

def main(argv):
    device = ''
    text = ''
    try:
        opts, args = getopt.getopt(argv,"hd:t:",["device=","text="])
    except getopt.GetoptError:
        print 'advancedSerial.py -d <device> -t <text>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'advancedSerial.py -d <device> -t <text>'
            sys.exit()
        elif opt in ("-d", "--device"):
            device = arg
        elif opt in ("-t", "--text"):
            text = arg
    print 'Device is "', device
    print 'Text is "', text

    s = serial.Serial(device, 9600) # Namen ggf. anpassen
    #s.open()
    time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden

    s.write(text)
    try:
        while True:
            response = s.readline()
            print(response)
    except KeyboardInterrupt:
        s.close()


if __name__ == "__main__":
   main(sys.argv[1:])