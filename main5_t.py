import threading
import time

#設定開始時間
start_time = time.time()


def task1():
    print("Task 1 is starting...")
    time.sleep(2)
    print("Task 1 is done.")

def task2():
    print("Task 2 is starting...")
    time.sleep(3)
    print("Task 2 is done.")

def task3():
    print("Task 3 is starting...")
    time.sleep(5)
    print("Task 3 is done.")

#執行 ->測試結果為10秒
# task1()
# task2()
# task3()


#執行 同時執行與結束 目標為TASK123->測試結果為5秒
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)

#執行開始
thread1.start()
thread2.start()
thread3.start()
#執行結束
thread1.join()
thread2.join()
thread3.join()

#結束時間
end_time = time.time()

#印出執行時間
print(f"Execution time : {end_time - start_time}")
print("All tasks have finished.")
