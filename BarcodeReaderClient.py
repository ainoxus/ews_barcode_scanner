# The way BarcodeReaderClient works is by "listening" for scans done by the user at all times. After that, whenever the user scans a barcode, BarcodeReaderClient creates a server class, which requires a single string input - the barcode.
import socket
import time
class BarcodeReaderClient:
    def __init__(self):
        connect_addr = socket.gethostname()  # TODO: use the actual address of the barcode scanner chip
        connect_port = 1234  # TODO: adjust the port accordingly (recommended on pc: use a port above 1024)
        retry_delay = 5  # number of seconds to wait before retrying to connect in case of a refused connection error (adjust according to need)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                s.connect((connect_addr, connect_port))  # Connecting the client to the server using the pre-specified connect_addr and connect_port
                break  # Terminating the infinite loop if the connection between client and server was successful
            except ConnectionRefusedError:
                print("The hosting server refused to connect\nRetrying in 5 seconds...")  # TODO: (optional) add a live timer on screen
                time.sleep(retry_delay)  # Pausing execution thread for 5 seconds
            except:  # TODO: for debugging purposes, accustom code to work on the client chip
                raise "An unknown error has occurred...:("

        self.send_barcodes(s)


    def send_barcodes(self, client_server):
        while True:
            barcode = input()
            client_server.send(bytes(barcode, "utf-8"))

if __name__ == '__main__':
    BarcodeReaderClient()  # TODO: for testing purposes, remember to delete!