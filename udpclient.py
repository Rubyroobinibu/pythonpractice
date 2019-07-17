import socket
def main():
    host='127.0.0.3'
    port=5001

    server=('127.0.0.3',5000)
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))

    msg=input("enter the msg to be sent to the server: \n")

    print("enter q to quit")
    while msg !='q':
        s.sendto(msg.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data=data.decode('utf-8')
        print("received data from server: "+data)
        msg=input("enter msg")

    s.close()

if __name__=='__main__':
    main()