import os
import csv
from datetime import datetime, timedelta
from room_capacities import ROOM_CAPACITIES, get_available_room

LECTORS = ['TE', 'ZZ', 'AA', 'UN', 'MB', 'BB', 'MI', 'NT', 'SA']
STUDENT_DIR = 'students'
DEFAULT_EXAM_DATETIME = datetime(2024, 12, 7, 9, 0, 0)

# BB	Байсаков Бейсенбек Миятбекович
# MB	Мухсимбаев Бобур Абдирахимович
# UN	Усюкин Никита Александрович
# ZZ	Жиенбеков Жалғас Жұмағалиұлы
# AA	Ақша Аян Әділетұлы
# SA	Садуақас Алмас Ардақұлы
# TE	Эм Тимур Олегович
# MI	Меңлібай Ислам Ерденұлы
# NT	Нұржігіт Төленді

def read_lector_students(lector: str) -> list:
    """
    Reads student data for a specific lector from a CSV file.
    """
    file_path = os.path.join(STUDENT_DIR, f'{lector}.csv')
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File does not exist: {file_path}')

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        return [{'lector': lector, 'id': row[0].strip(), 'name': row[1].strip()} for row in reader]


def read_all_teacher_groups() -> list:
    """
    Reads students for all lectors.
    """
    students = []
    for lector in LECTORS:
        try:
            students.extend(read_lector_students(lector))
        except FileNotFoundError as e:
            print(e)

    return students


def generate_timetable(students: list) -> list:
    """
    Generates a timetable with available rooms and exam times.
    """
    final_data = []
    remaining_places = ROOM_CAPACITIES.copy()
    exam_datetime = DEFAULT_EXAM_DATETIME

    for student in students:
        available_room, remaining_places, isAvailableSeat = get_available_room(remaining_places)
        
        if not isAvailableSeat:
            exam_datetime += timedelta(minutes=90)
            remaining_places = ROOM_CAPACITIES.copy()
            available_room, remaining_places, _ = get_available_room(remaining_places)

        final_data.append([student['lector'], student['id'], student['name'], 
                           exam_datetime.strftime('%d.%m.%Y / %H:%M'), available_room])
    
    return final_data


def save_file(filename='final_data.csv', data=None):
    """
    Saves the timetable data to a CSV file.
    """
    data = data or []
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(data)   



students = read_all_teacher_groups()
timetable = generate_timetable(students)
save_file(data=timetable)
