# модуль для записи данных и истории проведения операций 
# (последние 10 операций с указанием даты и времени проведения операций)

from datetime import datetime

def get_logbook(x, y, str_, result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ('log.txt', 'a') as log:
        log.write(f'{now} \n{x} {str_} {y} = {result} \n\n')


