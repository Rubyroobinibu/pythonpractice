import socket
def main():
    host='127.0.0.10'
    port=5000

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("created a socket")

    s.bind((host,port))

    s.listen(1)

    print("waiting for connection ........")
    conn,addr=s.accept()
    print("connection from "+str(addr))

    while True:
        #receives 1024 bytes of data from client at a time
        data=conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(data)
        data=data.upper()
        print("sending "+data)
        conn.send(data.encode("utf-8"))
    
    conn.close()

if __name__=='__main__':
    main()
