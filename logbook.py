# модуль для записи данных и истории проведения операций 
# (последние 10 операций с указанием даты и времени проведения операций)

from datetime import datetime

def get_logbook(x, y, sign, result):
    str_ = f'{x} {sign} {y} = {result};'

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ('our_log.csv', 'a+') as log:
        log.write(f'{now} \n{str_} ')
        log.seek(0)
        f1 = log.readlines()
    with open ('our_log.csv', 'w+') as log:
        if len(f1) > 20:
            f2 = f1[-20:]
            log.writelines(f2 + ['\n'])
        else:
            log.writelines(f1 + ['\n'])



