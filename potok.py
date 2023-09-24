import time
import threading


def sleepTime(wait, name):
    print("Выводим текст: {}".format(name))
    time.sleep(wait)
    print("ВЫводим текст повторно: {}".format(name))


td = threading.Thread(target=sleepTime, name='SleepTime', args=(3, 'SleepTime'))

start = time.time()
t_list = []

for i in range(5):

    name = 'SleepTime: ' + str(i)
    print("{} был запущен".format(name))

    td = threading.Thread(target=sleepTime, name=name, args=(3, name))
    td.start()
    t_list.append(td)

for t in t_list:
    t.join()


end = time.time()

print("Время обработки: ", (end-start))
