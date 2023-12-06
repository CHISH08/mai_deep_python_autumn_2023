import signal
import subprocess
import time

server_process = subprocess.Popen(["./venv/bin/python3", "server.py", "-w", "10", "-k", "7"])

time.sleep(2)

subprocess.run(["./venv/bin/coverage", "run", "-m", "unittest", "discover", "-s", ".", "-p", "*_test.py"])

time.sleep(10)
server_process.send_signal(signal.SIGINT)
