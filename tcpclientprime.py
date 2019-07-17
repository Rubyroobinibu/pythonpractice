import socket

def main():
    host='127.0.0.6'
    #host='localhost'
    port=8002

    #create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("SOCKET CREATED")

    #bind host and port to the socket
    s.connect((host,port))
    print("binding successful to the socket")

    message = input("enter limit: \n")
    print("enter q to quit")
    while message!= 'q' :
        s.send(str.encode(message,'utf-8'))
        data=s.recv(1024).decode('utf-8')
        print("data received from the server: {}".format(data))
        message=input('enter the limit again: \n')
        print(message)
    s.close()

if __name__=="__main__":
    main()