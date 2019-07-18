import socket
def main():
    host='127.0.0.10'
    port=5000

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("created a socket")

    s.connect((host,port))
    print("connected to server successfully")

    msg=input("enter the msg to be sent to the server: \n")

    print("enter q to quit")
    while msg !='q':
        s.send(str.encode(msg, 'utf-8'))
        data=s.recv(1024).decode('utf-8')
        print("the received data from server is : \n" +data)
        msg=input("enter the msg to be sent to the server: \n")
        print(msg)

    s.close()

if __name__=='__main__':
    main()



