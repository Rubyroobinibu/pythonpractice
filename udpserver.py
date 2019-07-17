import socket
def main():
    host='127.0.0.3'
    port=5000

    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("created udp socket")

    s.bind((host,port))
    print("binded host and port")

    while True:
        data, addr = s.recvfrom(1024)
        data=data.decode('utf-8')
        print("message from:"+str(addr))
        print(data)
        data=data.upper()
        print("sending : "+data)
        s.sendto(data.encode("utf-8"),addr)
    
    s.close()
if __name__=='__main__':
    main()



    

if __name__=='__main__':
    main()