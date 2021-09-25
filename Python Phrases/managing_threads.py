import threading
import _thread
import time

###########################################################
# OLD FORM OF THREAD
###########################################################
do_exit = 0
def print_time(thread_name, delay, counter):
	while counter:
		if do_exit:
			_thread.exit()
		time.sleep(delay)
		print(f"{thread_name}: {time.ctime(time.time())}")
		counter -= 1


# _thread.start_new_thread(print_time, ("Thread_1", 2, ))
# _thread.start_new_thread(print_time, ("Thread_2", 4, ))

# while 1:
# 	pass


###########################################################
# NEW FORM OF THREAD
###########################################################

class newThread(threading.Thread):
	def __init__(self, thread_id, name, counter):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.name = name
		self.counter = counter

	def run(self):
		print(f"Start {self.name}")

		# GET LOCK TO SYNCHRONIZE THE THREAD
		threading_lock.acquire()
		print_time(self.name, self.counter, 5)

		# FREE LOCK TO NEXT THREAD
		threading_lock.release()


# CREATE THREAD LOCK
threading_lock = threading.Lock()
threads = list()

# CREATE NEW THREAD
thread_1 = newThread(1, 'Thread_01', 1)
thread_2 = newThread(2, 'Thread_02', 2)

# START THE THREAD
thread_1.start()
thread_2.start()

threads.append(thread_1)
threads.append(thread_2)

for t in threads:
	t.join()

print("Exit main thread")


###########################################################
# SYNCHRONIZING THREADS
###########################################################
