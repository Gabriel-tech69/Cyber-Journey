data = [512, 2048, 256, 4096, 1024, 128]
count = 0
total = 0
for datum in data:
    total = total + datum
    if datum > 1000:
        count = count + 1
print(f"Total data transferred: {total}")
print(f"Total data greater than 1000: {count}")
