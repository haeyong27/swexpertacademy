counter = 0

def increment():
  global counter
  counter += 1

increment()
print(counter)
increment()
print(counter)