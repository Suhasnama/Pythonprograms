import socket

def main():

    host = ""
    port = 4000

    s = socket.socket()

    s.connect((host , port))

    while  True:
        data = bytes(input(">>>").encode("utf-8"))

        if data != "q":
            s.send(data)
            data = s.recv(1024)
            print("Data received from server is :"+str((data).decode("utf-8")))
       
if __name__ == "__main__":
    main()
