import requests as req
import time

#calculate request per second

count = 0
start = time.time()

for i in range(1000):
    text = 'qwerty'
    req.get("http://127.0.0.1:5000/api/bottomize", data={'text': text})
    count += 1

end = time.time()

print()
print(f"1000 requests took {end - start} seconds")
print(f"Average of {count / (end - start)} requests per second")