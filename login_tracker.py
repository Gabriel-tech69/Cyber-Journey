login = ['success', 'fail', 'success', 'success', 'fail', 'success']
count = 0
for attempts in login:
    if attempts == 'success':
        count = count + 1
print(f"{count} login attempts successful")
