import socket, threading, time

HOST, PORT, NUM_CLIENTS = '127.0.0.1', 65432, 3
client_times, lock = {}, threading.Lock()

def handle_client(conn, addr):
    client_times[addr] = (float(conn.recv(1024).decode()), conn)
    print(f"Received time from {addr}")

def main():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen(NUM_CLIENTS)
    print("Coordinator started. Waiting for clients...")
    threads = [threading.Thread(target=handle_client, args=server.accept()) for _ in range(NUM_CLIENTS)]
    for t in threads: t.start()
    for t in threads: t.join()

    all_times = [t for t, _ in client_times.values()] + [time.time()]
    avg_time = sum(all_times) / len(all_times)
    print(f"Average time: {avg_time:.2f}")

    for addr, (client_time, conn) in client_times.items():
        adjustment = avg_time - client_time
        conn.send(str(adjustment).encode())
        conn.close()
        print(f"Sent adjustment {adjustment:.2f} to {addr}")

    server.close()

if __name__ == '__main__':
    main()

# python clckSyncClient.py 
# python clckSync.py  