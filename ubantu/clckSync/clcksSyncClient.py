import socket, time

HOST, PORT = '127.0.0.1', 65432

def client_node(offset):
    local_time = time.time() + offset
    print(f"[Offset {offset}] Time: {local_time:.2f}")

    with socket.socket() as s:
        s.connect((HOST, PORT))
        s.send(str(local_time).encode())
        adjustment = float(s.recv(1024).decode())

    print(f"[Offset {offset}] Adjustment: {adjustment:.2f}, Adjusted time: {local_time + adjustment:.2f}")

if __name__ == '__main__':
    offset = float(input("Enter initial clock offset (e.g., 3.2): "))
    client_node(offset)

# python clckSyncClient.py 
# python clckSync.py  


