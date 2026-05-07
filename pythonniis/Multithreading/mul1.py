import threading

def print_numbers():
	for i in range(1,6):
		print("Number:",i)

def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print("letters:", ch)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Done")         		