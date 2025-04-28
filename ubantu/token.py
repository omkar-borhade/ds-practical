import threading, time, random

class TokenRing:
    def __init__(self, n):
        self.n, self.token, self.holder, self.running = n, True, 0, True
        self.lock = threading.Lock()

    def critical_section(self, pid):
        print(f"Process {pid} ENTERING critical section.")
        time.sleep(random.uniform(1, 2))
        print(f"Process {pid} EXITING critical section.")

    def request_token(self, pid):
        while self.running:
            with self.lock:
                if self.holder == pid and self.token:
                    self.critical_section(pid)
                    self.token = False
                    self.holder = (pid + 1) % self.n
                    self.token = True
            time.sleep(1)

    def start(self):
        threads = [threading.Thread(target=self.request_token, args=(i,)) for i in range(self.n)]
        for t in threads: t.start()
        try: 
            while True: time.sleep(0.1)
        except KeyboardInterrupt:
            self.running = False
            print("\nStopping simulation...")
            for t in threads: t.join()

if __name__ == "__main__":
    TokenRing(5).start()

    # python token.py