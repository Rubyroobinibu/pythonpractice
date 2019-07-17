import socket

def main():
    host='127.0.0.6'
    #host='localhost'
    port=8002

    #create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("SOCKET CREATED")

    #bind host and port to the socket
    s.bind((host,port))
    print("binding successful to the socket")

    #listen to one connection at a time
    s.listen(1)

    #accepting connection
    print("waiting for the server")
    conn,addr=s.accept()
    print("connection from:"+str(addr))
    #server runs infinitely for sending and recv msgs
    lst1=[]

    while True:
            #receiver 1024 bytes of data from client at a time
            data =conn.recv(1024).decode("utf-8")
            if not data:
                break
            for i in range(2,int(data)+1):
                flag=0
               
                for j in range(2,i):
                    if i%j==0:
                        flag=1
                        break
                if flag==0:
                    lst1.append(i)
            conn.send(str(lst1).encode("utf-8"))
    conn.close()
 



if __name__=="__main__":
    main()