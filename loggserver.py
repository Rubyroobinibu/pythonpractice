import socket
import logging

def main():

    LOG_FORMAT ="%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
        filename="D:\logg.log", 
        level=logging.DEBUG, #includes all other levels like infor warning and error critical
        # level=logging.INFO, includes all levels below it like warning error and critical  
        format=LOG_FORMAT,
        # filemode='w' #default is append mode. if 'w' given whenever file is run its old log is overwriten
        )
    
    logger=logging.getLogger()
    
    host='127.0.0.10'
    port=5000

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("created a socket")
    logger.info("logger: created socket")
    
    s.bind((host,port))
    print("binded host and port to socket")
    logger.info("binded host and port to socket")

    s.listen(1)
    logger.debug("server enter in listening mode")

    print("waiting for connection ........")
    logger.info("waiting for connection from client")
    conn,addr=s.accept()
    print("connection from "+str(addr))
    logger.info("connection from: "+str(addr))

    while True:
        #receives 1024 bytes of data from client at a time
        data=conn.recv(1024).decode('utf-8')
        if not data:
            logger.debug("data not received from client")
            break
        print(data)
        data=data.upper()
        print("sending "+data)
        logger.info("sending "+data)
        conn.send(data.encode("utf-8"))
    
    conn.close()
    logger.info("conn closed")

if __name__=='__main__':
    main()
