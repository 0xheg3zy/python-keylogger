import socket
HOST = "0.0.0.0" # change this
PORT = 8888 #change this

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode())
            except Exception as Ex:
                print(f"[-] Error : {Ex}")
