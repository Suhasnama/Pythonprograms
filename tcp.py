import socket

def main():

    host = ""
    port = 4000

    s = socket.socket()
    
    s.bind((host , port))

    s.listen(1)
    
    conn , addr = s.accept()
    
    print("Connection from "+str(addr))
    
    while True:
        data = str(conn.recv(1024).decode("utf-8"))

        if not data:
            conn.close
            break
            
        if data != "q":            
            print("Data is "+str(data))
            data = str(len(str(data)))
            conn.send(bytes(data.encode("utf-8")))

if __name__ == "__main__":
    main()
