import csv
import datetime

class Logger:
    def __init__(self, id, comp_name, username, proj_name, return_take, required_quantity, remained_quantity):  # TODO: all of those required input arguments are going to be passed in by the DBManager class
        dt_now = datetime.datetime.now()
        path = f"C:\\Users\\abdel\\Downloads\\ews_barcode_scanner\\app\\server_files\\logs\\{dt_now.year}-{dt_now.month}-{dt_now.day}.csv"
        self.writeFile(path, id, comp_name, username, proj_name, return_take, required_quantity, remained_quantity)

    def writeFile(self, path, id, comp_name, username, proj_name, return_take, required_quantity, remained_quantity):
        dt_now = datetime.datetime.now()
        row = [f"{dt_now.hour}:{dt_now.minute}:{dt_now.second}", username, proj_name, id, comp_name, return_take, required_quantity, remained_quantity]
        try:
            f = open(path)
            f.close()
            with open(path, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)
        except FileNotFoundError:
            header = ["time", "user name", "project name", "id", "name", "Return/Take", "required quantity", "remained quantity"]
            with open(path, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(header)
            with open(path, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)

if __name__ == '__main__':  # TODO: for debugging purposes only actual call is going to be made by the MainManager class
    Logger("FRZ008", "Metal Film Resistors - Through Hole 15 OHM 0.25W 1%", "ibrahim_the_great", "great_project", "take_forever_and_ever", 8, 100)
