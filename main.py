import multiprocessing
import concurrent.futures
import requests
import threading
import time
"""def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")

start = time.perf_counter()
for i in range(10):
    t1 = threading.Thread(target=task, args=[i])
    t1.start()
    t1.join()
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")"""



'''img_urls = ['https://i.pinimg.com/474x/a6/69/73/a66973901b4fe11ea5365481ce4a0c04.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")'''

def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")