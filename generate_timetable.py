import os
import csv
from datetime import datetime, timedelta
from room_capacities import ROOM_CAPACITIES, get_available_room

errors = []

def read_lector_students(lector: str) -> dict:
    students = []
    file_path = f'students/{lector}.csv'
    if os.path.exists(file_path):
        with open(f'students/{lector}.csv', 'r') as f:
            wsp_reader = csv.reader(f, delimiter='\t')
            for row in wsp_reader:
                students.append({
                    'lector': lector, 
                    'id': row[0].strip(),
                    'name': row[1].strip()
                })
    else:
        errors.append(f'File not exists: {file_path}')

    return students

# BB	Байсаков Бейсенбек Миятбекович
# MB	Мухсимбаев Бобур Абдирахимович
# UN	Усюкин Никита Александрович
# ZZ	Жиенбеков Жалғас Жұмағалиұлы
# AA	Ақша Аян Әділетұлы
# SA	Садуақас Алмас Ардақұлы
# TE	Эм Тимур Олегович
# MI	Меңлібай Ислам Ерденұлы
# NT	Нұржігіт Төленді



def read_all_teacher_groups():
    students = []
    for lector in ['TE', 'ZZ', 'AA', 'UN', 'MB', 'BB', 'MI', 'NT', 'SA']:
       students.extend(read_lector_students(lector=lector))
    
    return students


def generate_timetable(students: list) -> list:
    final_data = []
    remaining_places = {**ROOM_CAPACITIES}
    exam_datetime = datetime(2024, 12, 7, 9, 0, 0)
    for student in students:
        available_room, remaining_places, isAvailableSeat = get_available_room(remaining_places)
        if not isAvailableSeat:
            exam_datetime += timedelta(minutes=90)
            available_room, remaining_places, isAvailableSeat = get_available_room({**ROOM_CAPACITIES})

        final_data.append([student['lector'], student['id'], student['name'], 
                        exam_datetime.strftime('%d.%m.%Y / %H:%M'), available_room])
    
    return final_data


def save_file(filename='final_data.csv', data=None):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(data)    



students = read_all_teacher_groups()
timetable = generate_timetable(students=students)
save_file(data=timetable)
