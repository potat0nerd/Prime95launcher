import time
import subprocess
import os

results_file_name = 'results.txt'
with open(results_file_name, 'w') as f:
    f.write("")
with open(results_file_name) as f:
    text = f.readlines()

subprocess.Popen('taskkill /f /im prime95.exe',stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)
time.sleep(5)
subprocess.Popen('prime95.exe -T')
starttime = time.time()
refresh_delay = 0
time.sleep(5)
no_errors = 1
completed_tests = []

while no_errors:
    old_text = text
    with open(results_file_name) as f:
        text = f.readlines()
    if len(old_text) != len(text):
        fft_list = []
        for x in range(len(text)):
            if text[x][0] != "[":
                if text[x][:5] == "FATAL":
                    subprocess.Popen('taskkill /f /im prime95.exe', stdout=subprocess.DEVNULL,
                                     stderr=subprocess.STDOUT)
                    print(text[x+1])
                    no_errors = 0
                    break
                else:
                    fft = int(text[x].split()[1][:-1])
                    if fft not in completed_tests:
                        completed_tests.append(fft)
                        completed_tests.sort()
                    fft_list.append(fft)
        os.system("cls")
        for x in completed_tests:
            print(f"{x}k {fft_list.count(x)}")






    else:
        #print("increase delay",refresh_delay+1)
        refresh_delay += 1
    if no_errors:
        time.sleep(refresh_delay)


print(f"Error found, Prime95 has been terminated after {int(time.time()-starttime)}")
a = input()