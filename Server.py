import socket
class Server:  # This class should be running all the time as it is a server - the server is just a socket in itself.
    def __init__(self):
        bind_addr = socket.gethostname()  # TODO: use the actual address of the barcode scanner chip
        bind_port = 1234  # TODO: adjust the port accordingly (recommended on pc: use a port above 1024)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((bind_addr, bind_port))  # binding the server to the barcode scanner 
        s.listen(2)  # TODO: adjust the 5 as fit for listening to the received data
        clientSocket, address = s.accept()  # TODO: add a connection error handler if necessary...
        print(f"{address} has established a connection.")  # TODO: only for debugging purposes, delete later!

        while True:  # keeps server running all the time
            barcode = clientSocket.recv(1024)
            if barcode.decode("utf-8") == "":
                break
            else:
                print(barcode.decode("utf-8"))


if __name__ == '__main__':
    Server()  # TODO: for debugging purposes, remember to use the appropriate method for running the server on the raspberry pi.