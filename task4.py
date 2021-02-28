from datetime import datetime
from geolite2 import geolite2

geo = geolite2.reader()


def calculate_Timestamp(time):
    time2 = time1
    element = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S,%f")
    Timestamp = datetime.timestamp(element)
    return Timestamp


def ipInfo(ip=""):
    try:
        x = geo.get(ip)
    except ValueError:
        # Faulty IP value
        return "NULL"
    try:
        return x["country"]["names"]["en"]
    except:
        # fault in geting country name
        return "NULL"

file1 = open("task4.log", "r")
Lines = file1.readlines()
#f2mhf,f2mh,f2mf,f2m use to store modbus's rest,IP,etc in a CSV file.

#f2mhf,f2mh,f2hf,f2h use to store HTTP's rest,IP,etc in a CSV file.

#f2mhf,f2hf,f2mf,f2f use to store FTP's rest,IP,etc in a CSV file.
try:
    f = open("modbus http ftp.csv")
    f2 = open("modbus http ftp.csv", "a")

    fm = open("modbus.csv")
    f2m = open("modbus.csv", "a")

    fh = open("http.csv")
    f2h = open("http.csv", "a")

    ff = open("ftp.csv")
    f2f = open("ftp.csv", "a")

    fmf = open("modbus ftp.csv")
    f2mf = open("modbus ftp.csv", "a")

    fmh = open("modbus http.csv")
    f2mh = open("modbus http.csv", "a")

    fhf = open("http ftp.csv")
    f2hf = open("http ftp.csv", "a")

except IOError:
    f = open("modbus http ftp.csv", "w")
    f.write('"Timestamp","IP","IP Country","Request"\n')
    f.close()
    f2 = open("modbus http ftp.csv", "a")

    fh = open("http.csv", "w")
    fh.write('"Timestamp","IP","IP Country","Request"\n')
    fh.close()
    f2h = open("http.csv", "a")

    fm = open("modbus.csv", "w")
    fm.write('"Timestamp","IP","IP Country","Request"\n')
    fm.close()
    f2m = open("modbus.csv", "a")

    ff = open("ftp.csv", "w")
    ff.write('"Timestamp","IP","IP Country","Request"\n')
    ff.close()
    f2f = open("ftp.csv", "a")

    fmh = open("modbus http.csv", "w")
    fmh.write('"Timestamp","IP","IP Country","Request"\n')
    fmh.close()
    f2mh = open("modbus http.csv", "a")

    fmf = open("modbus ftp.csv", "w")
    fmf.write('"Timestamp","IP","IP Country","Request"\n')
    fmf.close()
    f2mf = open("modbus ftp.csv", "a")

    fhf = open("http ftp.csv", "w")
    fhf.write('"Timestamp","IP","IP Country","Request"\n')
    fhf.close()
    f2hf = open("http ftp.csv", "a")
#countt sore line number of file is reading can use to analyze specific portion of file
countt = 0
for line in Lines:
    time1 = line[0:23]
    Request = ""
    IP = ""
    IPCounty = ""
#space seperate every line with space and store it to find IP
    space = line.split(" ")
    

    d = line[24:43]
    if d == "Modbus traffic from":
        
        IP += space[5]
        IP = IP[:-1]
        
        IPCounty += ipInfo(IP)
        
        updated_line = " ".join(line.split(" ")[:-1])
        Request += updated_line
        Request = Request[24:]
        
        f2.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2m.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2mh.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2mf.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )


    dd = line[24:49]
    if dd == "HTTP/1.1 GET request from":
        
        updated_line = " ".join(line.split(" ")[:-1])
        Request += updated_line
        Request = Request[24:]
        
        IP += space[6]
        IP = IP[:-2]
        IP = IP[2:]
        
        IPCounty += ipInfo(IP)
        
        f2.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2h.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2mh.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2hf.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )


    ddd = line[24:38]
    if ddd == "FTP traffic to":
        
        updated_line = " ".join(line.split(" ")[:-1])
        Request += updated_line
        Request = Request[24:]
        
        IP += space[5]
        IP = IP[:-2]
        IP = IP[2:]
        
        IPCounty += ipInfo(IP)
        
        f2.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2f.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2mf.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
        f2hf.write(
            '"{}","{}","{}","{}"\n'.format(calculate_Timestamp(time1), IP, IPCounty, Request)
        )
    countt += 1
