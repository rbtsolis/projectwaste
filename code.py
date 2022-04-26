import time

start_time = time.time()
time.sleep(3)
end_time = time.time()


print('Time Taken:', time.strftime("%H hours, %M Minutes and %S seconds", time.gmtime(end_time - start_time)))
