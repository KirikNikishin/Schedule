import json
from prettytable import PrettyTable
import random
from datetime import date
buildings = {0: "Old", 1: "New", 2: "Frezer", 3: "Stadium"}
auditoriums_buildings = {"Buildings": {"Old": {
    "Lection_big": ["431"],
    "Lection_small": ["305", "342", "409", "445", "447", "502",],
    "Seminar": ["201", "202", "235_1", "235_6", "238", "239", "240_2", "240_4", "256",
                 "302", "306", "306_1", "307", "308", "309", "310", "311", "312", "324", "333", "341", "343", "346/1", "357_7",
                 "405", "409", "410", "416", "417", "419", "420", "441", "442", "443", "445", "447", "449", "455", "457",
                 "501", "501-7", "502", "504", "505", "506", "508", "509",
                 "340_1", "340_2", "340_3",],
    "Laboratory": ["106",
                   "201", "202", "209", "210", "211", "214", "216", "217", "234", "234_1", "235_1", "235_3", "235_5", "235_8", "235_9", "240_1", "246", "247", "249_2",
                   "313", "322", "323", "332",   "346/2", "346/4", "346/5", "346/6", "350", "351", "355", "357_3", "357_8",
                   "408", "415",  "417", "419", "420",  "443", "445", "449", "450", "450_2", "450_3",
                   "501-7", "501-8",
                   "340_4",
                   "5", "5_1", "6", "7", "9", "11", "15", "16", "20"],
    "Sport": ["328/329"]},
              "New": {
                  "Lection_big": ["206", "208", "209",
                                  "308",
                                  "408", "410", "411",
                                  "801", "806", "811"],
                  "Lection_small": ["204", "207",
                                    "306", "309",
                                    "406", "409",
                                    "801", "803"],
                  "Seminar": ["202", "204", "207",
                              "301", "303", "306", "309",
                              "402", "404", "406", "409",
                              "804", "805"],
                  "Laboratory": ["205", "407"]},
              "Frezer": {
                  "Lection_big": ["303_M"],
                  "Lection_small": ["301",
                                    "401", "404"],
                  "Seminar": ["202", "206", "210", "215",
                              "301", "302", "303",  "305", "310", "311", "312",
                              "401", "402", "403", "404", "405", "406", "412"],
                  "Laboratory": ["202", "203"]
              },
              "Stadium": {
                  "Sport": ["Stadium_1", "Stadium_2"]
              }
              }
             }


groups = {"09.03.03-01": {"ИДБ-21-09", "ИДБ-21-10"},
          "09.03.03-02": {"ИДБ-21-11"},
          "09.03.04": {"ИДБ-21-12"}}

study_plan = {"09.03.03-01": {"Геометрическое моделирование и компьютерная графика": {"Lection": 14,
                                                                                      "Seminar": 6,
                                                                                      "Lab": 4,
                                                                                      "Teachers": ["Толок А.В."]},
                              "Машинное обучение и интеллектуальные системы": {"Lection": 14,
                                                                               "Seminar": 4,
                                                                               "Lab": 4,
                                                                               "Teachers": ["Ибатулин М.Ю.", "Биннятов Р.А.", "Верещагин Н.М."]},
                              "Проектирование информационных систем": {"Lection": 12,
                                                                       "Seminar": 6,
                                                                       "Lab": 3,
                                                                       "Teachers": ["Бычкова Н.А.", "Бычков С.Ю."]},
                              "Реинжиниринг и управление бизнес-процессами": {"Lection": 10,
                                                                              "Seminar": 4,
                                                                              "Lab": 3,
                                                                              "Teachers": ["Елисеева Н.В."]},
                              "Проектирование человеко-машинного взаимодействия": {"Lection": 14,
                                                                                   "Seminar": 4,
                                                                                   "Lab": 5,
                                                                                   "Teachers": ["Елисеева Н.В."]},
                              "Информационные системы и технологии": {"Lection": 14,
                                                                      "Seminar": 4,
                                                                      "Lab": 5,
                                                                      "Teachers": ["Бычков С.Ю."]},
                              "Основы теории надёжности": {"Lection": 10,
                                                           "Seminar": 4,
                                                           "Lab": 3,
                                                           "Teachers": ["Петров В.Е."]},
                              "Прикладная физическая культура": {"Lection": 2,
                                                                 "Seminar": 14,
                                                                "Teachers": ["Рожнова С.Г."]}
                              }
              }

schedule = {
    "Monday": {
        "8:30 - 10:10": "-",
        "10:20 - 12:00": "-",
        "12:20 - 14:00": "-",
        "14:10 - 15:50": "-",
        "16:00 - 17:40": "-",
        "18:00 - 19:30": "-",
        "19:40 - 21:10": "-",
        "21:20 - 22:50": "-"
    },

    "Tuesday": {
        "8:30 - 10:10": "-",
        "10:20 - 12:00": "-",
        "12:20 - 14:00": "-",
        "14:10 - 15:50": "-",
        "16:00 - 17:40": "-",
        "18:00 - 19:30": "-",
        "19:40 - 21:10": "-",
        "21:20 - 22:50": "-"
    },
    "Wednesday": {
        "8:30 - 10:10": "-",
        "10:20 - 12:00": "-",
        "12:20 - 14:00": "-",
        "14:10 - 15:50": "-",
        "16:00 - 17:40": "-",
        "18:00 - 19:30": "-",
        "19:40 - 21:10": "-",
        "21:20 - 22:50": "-"
    },
    "Thursday": {
        "8:30 - 10:10": "-",
        "10:20 - 12:00": "-",
        "12:20 - 14:00": "-",
        "14:10 - 15:50": "-",
        "16:00 - 17:40": "-",
        "18:00 - 19:30": "-",
        "19:40 - 21:10": "-",
        "21:20 - 22:50": "-"
    },
    "Friday" : {
        "8:30 - 10:10": "-",
        "10:20 - 12:00": "-",
        "12:20 - 14:00": "-",
        "14:10 - 15:50": "-",
        "16:00 - 17:40": "-",
        "18:00 - 19:30": "-",
        "19:40 - 21:10": "-",
        "21:20 - 22:50": "-"
    },
    "Saturday": {
        "8:30 - 10:10": "-",
        "10:20 - 12:00": "-",
        "12:20 - 14:00": "-",
        "14:10 - 15:50": "-",
        "16:00 - 17:40": "-",
        "18:00 - 19:30": "-",
        "19:40 - 21:10": "-",
        "21:20 - 22:50": "-"
    }
}
directions = study_plan.keys()
##print (groups['09.03.03-01'])
start = date(2024, 2, 12)
end = date(2024, 6, 10)
delta_1_week = date(2024, 2, 19) - date(2024, 2, 12)
#print(delta_1_week)
delta_1_day = date(2024, 2, 13) - date(2024, 2, 12)
delta_start_end = end - start
##print (delta_start_end.days / 7)
present_time = start

# for week in range (int(delta_start_end.days/7)):
#     pass

##print (present_time)
#================================================================================================================================
#Лекции
number_of_lections = []
all_teachers = []
for direction in directions:
    subjects = study_plan[direction].keys()
    #print(subjects)
    for subject in subjects:
        lessons = study_plan[direction][subject].keys()
        for lesson in lessons:
            if lesson == "Lection":
                number_of_lections.append(study_plan[direction][subject][lesson])
            if lesson == "Teachers":
                teachers = study_plan[direction][subject][lesson]
                all_teachers.append(teachers)
    #print(number_of_lections)
    #print(all_teachers)


all_lessons_week = []
all_durations_week = []
end_lesson = []
arr_buildings = []
for day in schedule:
    couples = schedule[day]
    all_lessons_day = []
    all_durations_day = []
    all_ending = []
    number_building = random.randint(0, 2)
    building_str = buildings[number_building]
    arr_buildings.append(building_str)
    #print(arr_buildings)
    for couple in couples:
        all_lessons_day.append(schedule[day][couple])
        all_durations_day.append('-')
        all_ending.append('-')
    all_lessons_week.append(all_lessons_day)
    all_durations_week.append(all_durations_day)
    end_lesson.append(all_ending)
    #print(all_lessons_day)
#print(all_lessons_week)


auditorium_arr = []

#for lections
i = 0
for subject in subjects:
    random_day = random.randint(0, len(all_lessons_week)-1)
    random_couple = random.randint(0, len(all_lessons_week[random_day])-1)
    if all_lessons_week[random_day][random_couple] == '-':
        all_durations_week[random_day][random_couple] = str(number_of_lections[i])
        i += 1
        all_lessons_week[random_day][random_couple] = subject
        all_lessons_week[random_day][random_couple] += " Лекции"
        all_lessons_week[random_day][random_couple] += " "
        for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
            random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
        all_lessons_week[random_day][random_couple] += study_plan[direction][subject]["Teachers"][random_teacher]
        all_lessons_week[random_day][random_couple] += " "
        for building in arr_buildings:
            auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Lection_big"])
            if len(auditorium_arr) < 6:
                auditorium_arr.append(auditorium_id)
                #print(auditorium_arr)
    else:
        if random_couple != len(all_lessons_week[random_day])-1:
            all_durations_week[random_day][random_couple + 1] = str(number_of_lections[i])
            i += 1
            all_lessons_week[random_day][random_couple + 1] = subject
            all_lessons_week[random_day][random_couple + 1] += " Лекции"
            all_lessons_week[random_day][random_couple + 1] += " "
            for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
                random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
            all_lessons_week[random_day][random_couple + 1] += study_plan[direction][subject]["Teachers"][random_teacher]
            all_lessons_week[random_day][random_couple + 1] += " "
            for building in arr_buildings:
                auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Lection_big"])
                if len(auditorium_arr) < 6:
                    auditorium_arr.append(auditorium_id)
                    #print(auditorium_arr)
        else:
            all_durations_week[random_day][random_couple - 1] = str(number_of_lections[i])
            i += 1
            all_lessons_week[random_day][random_couple - 1] = subject
            all_lessons_week[random_day][random_couple - 1] += " Лекции"
            all_lessons_week[random_day][random_couple - 1] += " "
            for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
                random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
            all_lessons_week[random_day][random_couple - 1] += study_plan[direction][subject]["Teachers"][random_teacher]
            all_lessons_week[random_day][random_couple - 1] += " "
            for building in arr_buildings:
                auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Lection_big"])
                if len(auditorium_arr) < 6:
                    auditorium_arr.append(auditorium_id)
                    #print(auditorium_arr)

#print(all_lessons_week)

for elem_1 in range (0, len(all_lessons_week)):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        if all_lessons_week[elem_1][elem_2] != '-':
            all_lessons_week[elem_1][elem_2] += auditorium_arr[elem_1]
            # all_lessons_week[elem_1][elem_2] += " "

#print(all_lessons_week)

start_ = start
flag = False
for elem_1 in range (0, len(all_lessons_week)):
    if flag == True:
        start_ = start_ + delta_1_day
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        flag = True
        if all_lessons_week[elem_1][elem_2] != '-':
            all_lessons_week[elem_1][elem_2] += " "
            all_lessons_week[elem_1][elem_2] += "["
            all_lessons_week[elem_1][elem_2] += str(start_.day)
            all_lessons_week[elem_1][elem_2] += "."
            all_lessons_week[elem_1][elem_2] += str(start_.month)
            all_lessons_week[elem_1][elem_2] += " - "


#print(all_lessons_week)
#print(all_durations_week)

start = date(2024, 2, 12)
end = date(2024, 6, 10)
start_ = start
flag = False
for elem_1 in range (0, len(all_durations_week)):
    if flag == True:
        start_ += delta_1_day
    for elem_2 in range(0, len(all_durations_week[elem_1])):
        flag = True
        if all_durations_week[elem_1][elem_2] != '-':
            end_ = start_
            ##print(start)
            for i in range (1, int(all_durations_week[elem_1][elem_2])+1):
                ##print (i)
                end_ = end_ + delta_1_week
                ##print(end_)
            end_lesson[elem_1][elem_2] = end_
#print (end_lesson)

for elem_1 in range (0, len(all_lessons_week)):
    if flag == True:
        start = start + delta_1_day
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        if all_lessons_week[elem_1][elem_2] != '-':
            all_lessons_week[elem_1][elem_2] += str(end_lesson[elem_1][elem_2].day)
            all_lessons_week[elem_1][elem_2] += "."
            all_lessons_week[elem_1][elem_2] += str(end_lesson[elem_1][elem_2].month)
            all_lessons_week[elem_1][elem_2] += "]"
#print(all_lessons_week)
#print("=====================================================================================================")
#================================================================================================================================
#Семинары

number_of_seminars = []
all_teachers = []
for direction in directions:
    subjects = study_plan[direction].keys()
    #print(subjects)
    for subject in subjects:
        lessons = study_plan[direction][subject].keys()
        for lesson in lessons:
            if lesson == "Seminar":
                number_of_seminars.append(study_plan[direction][subject][lesson])
            if lesson == "Teachers":
                teachers = study_plan[direction][subject][lesson]
                all_teachers.append(teachers)
    #print(number_of_seminars)
    #print(all_teachers)


#all_lessons_week = []
all_durations_week = []
end_lesson = []
for day in schedule:
    couples = schedule[day]
    all_lessons_day = []
    all_durations_day = []
    all_ending = []
    for couple in couples:
        #all_lessons_day.append(schedule[day][couple])
        all_durations_day.append('-')
        all_ending.append('-')
    #all_lessons_week.append(all_lessons_day)
    all_durations_week.append(all_durations_day)
    end_lesson.append(all_ending)
    #print(all_lessons_day)
#print(all_lessons_week)


auditorium_arr = []

#for seminars
i = 0
for subject in subjects:
    random_day = random.randint(0, len(all_lessons_week)-1)
    random_couple = random.randint(0, len(all_lessons_week[random_day])-1)
    if all_lessons_week[random_day][random_couple] == '-':
        all_durations_week[random_day][random_couple] = str(number_of_seminars[i])
        i += 1
        all_lessons_week[random_day][random_couple] = subject
        all_lessons_week[random_day][random_couple] += " Семинары"
        all_lessons_week[random_day][random_couple] += " "
        for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
            random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
        all_lessons_week[random_day][random_couple] += study_plan[direction][subject]["Teachers"][random_teacher]
        all_lessons_week[random_day][random_couple] += " "
        for building in arr_buildings:
            auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Seminar"])
            if len(auditorium_arr) < 6:
                auditorium_arr.append(auditorium_id)
                #print(auditorium_arr)
    else:
        if random_couple != len(all_lessons_week[random_day])-1:
            all_durations_week[random_day][random_couple + 1] = str(number_of_seminars[i])
            i += 1
            all_lessons_week[random_day][random_couple + 1] = subject
            all_lessons_week[random_day][random_couple + 1] += " Семинары"
            all_lessons_week[random_day][random_couple + 1] += " "
            for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
                random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
            all_lessons_week[random_day][random_couple + 1] += study_plan[direction][subject]["Teachers"][random_teacher]
            all_lessons_week[random_day][random_couple + 1] += " "
            for building in arr_buildings:
                auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Seminar"])
                if len(auditorium_arr) < 6:
                    auditorium_arr.append(auditorium_id)
                    #print(auditorium_arr)
        else:
            all_durations_week[random_day][random_couple - 1] = str(number_of_seminars[i])
            i += 1
            all_lessons_week[random_day][random_couple - 1] = subject
            all_lessons_week[random_day][random_couple - 1] += " Семинары"
            all_lessons_week[random_day][random_couple - 1] += " "
            for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
                random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
            all_lessons_week[random_day][random_couple - 1] += study_plan[direction][subject]["Teachers"][random_teacher]
            all_lessons_week[random_day][random_couple - 1] += " "
            for building in arr_buildings:
                auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Seminar"])
                if len(auditorium_arr) < 6:
                    auditorium_arr.append(auditorium_id)
                    #print(auditorium_arr)

#print(all_lessons_week)

for elem_1 in range (0, len(all_lessons_week)):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        if (all_lessons_week[elem_1][elem_2] != '-') and (all_lessons_week[elem_1][elem_2].find("Лекции") == -1):
            all_lessons_week[elem_1][elem_2] += auditorium_arr[elem_1]
            # all_lessons_week[elem_1][elem_2] += " "

#print(all_lessons_week)

start_ = start
flag = False
for elem_1 in range (0, len(all_lessons_week)):
    if flag == True:
        start_ = start_ + delta_1_day
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        flag = True
        if all_lessons_week[elem_1][elem_2] != '-' and (all_lessons_week[elem_1][elem_2].find("Лекции") == -1):
            all_lessons_week[elem_1][elem_2] += " "
            all_lessons_week[elem_1][elem_2] += "["
            all_lessons_week[elem_1][elem_2] += str(start_.day)
            all_lessons_week[elem_1][elem_2] += "."
            all_lessons_week[elem_1][elem_2] += str(start_.month)
            all_lessons_week[elem_1][elem_2] += " - "


#print(all_lessons_week)
#print(all_durations_week)

start = date(2024, 2, 12)
end = date(2024, 6, 10)
start_ = start
flag = False
for elem_1 in range (0, len(all_durations_week)):
    if flag == True:
        start_ += delta_1_day
    for elem_2 in range(0, len(all_durations_week[elem_1])):
        flag = True
        if all_durations_week[elem_1][elem_2] != '-':
            end_ = start_
            ##print(start)
            for i in range (1, int(all_durations_week[elem_1][elem_2])+1):
                ##print (i)
                end_ = end_ + delta_1_week
                ##print(end_)
            end_lesson[elem_1][elem_2] = end_
#print (end_lesson)

for elem_1 in range (0, len(all_lessons_week)):
    if flag == True:
        start = start + delta_1_day
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        if end_lesson[elem_1][elem_2] != '-':
            all_lessons_week[elem_1][elem_2] += str(end_lesson[elem_1][elem_2].day)
            all_lessons_week[elem_1][elem_2] += "."
            all_lessons_week[elem_1][elem_2] += str(end_lesson[elem_1][elem_2].month)
            all_lessons_week[elem_1][elem_2] += "]"
##print(all_lessons_week)

# #================================================================================================================================
# #Лабораторные работы
#
# number_of_labs = []
# all_teachers = []
# for direction in directions:
#     subjects = study_plan[direction].keys()
#     #print(subjects)
#     for subject in subjects:
#         lessons = study_plan[direction][subject].keys()
#         for lesson in lessons:
#             if lesson == "Lab":
#                 number_of_labs.append(str(int(study_plan[direction][subject][lesson]))*2)
#             if lesson == "Teachers":
#                 teachers = study_plan[direction][subject][lesson]
#                 all_teachers.append(teachers)
#     #print(number_of_labs)
#     #print(all_teachers)
#
#
# #all_lessons_week = []
# all_durations_week = []
# end_lesson = []
# for day in schedule:
#     couples = schedule[day]
#     all_lessons_day = []
#     all_durations_day = []
#     all_ending = []
#     for couple in couples:
#         #all_lessons_day.append(schedule[day][couple])
#         all_durations_day.append('-')
#         all_ending.append('-')
#     #all_lessons_week.append(all_lessons_day)
#     all_durations_week.append(all_durations_day)
#     end_lesson.append(all_ending)
#     #print(all_lessons_day)
# #print(all_lessons_week)
#
#
# auditorium_arr = []
#
# #for seminars
# i = 0
# for subject in subjects:
#     random_day = random.randint(0, len(all_lessons_week)-1)
#     random_couple = random.randint(0, len(all_lessons_week[random_day])-1)
#     if all_lessons_week[random_day][random_couple] == '-' and all_lessons_week[random_day+1][random_couple+1] == '-':
#         all_durations_week[random_day][random_couple] = str(number_of_labs[i])
#         i += 1
#         all_lessons_week[random_day][random_couple] = subject
#         all_lessons_week[random_day][random_couple] += " Лабораторные занятия"
#         all_lessons_week[random_day][random_couple] += " "
#         all_lessons_week[random_day][random_couple + 1] = subject
#         all_lessons_week[random_day][random_couple + 1] += " Лабораторные занятия"
#         all_lessons_week[random_day][random_couple + 1] += " "
#         for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
#             random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
#         all_lessons_week[random_day][random_couple] += study_plan[direction][subject]["Teachers"][random_teacher]
#         all_lessons_week[random_day][random_couple] += " "
#         for building in arr_buildings:
#             auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]["Laboratory"])
#             if len(auditorium_arr) < 6:
#                 auditorium_arr.append(auditorium_id)
#                 #print(auditorium_arr)
#     else:
#         if random_couple != len(all_lessons_week[random_day])-1:
#             all_durations_week[random_day][random_couple + 1] = str(number_of_labs[i])
#             i += 1
#             all_lessons_week[random_day][random_couple + 1] = subject
#             all_lessons_week[random_day][random_couple + 1] += " Лабораторные занятия"
#             all_lessons_week[random_day][random_couple + 1] += " "
#             for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
#                 random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
#             all_lessons_week[random_day][random_couple + 1] += study_plan[direction][subject]["Teachers"][random_teacher]
#             all_lessons_week[random_day][random_couple + 1] += " "
#             for building in arr_buildings:
#                 auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]['Laboratory'])
#                 if len(auditorium_arr) < 6:
#                     auditorium_arr.append(auditorium_id)
#                     #print(auditorium_arr)
#         else:
#             all_durations_week[random_day][random_couple - 1] = str(number_of_labs[i])
#             i += 1
#             all_lessons_week[random_day][random_couple - 1] = subject
#             all_lessons_week[random_day][random_couple - 1] += " Лабораторные занятия"
#             all_lessons_week[random_day][random_couple - 1] += " "
#             for teacher in (0, len(study_plan[direction][subject]["Teachers"])):
#                 random_teacher = random.randint(0, len(study_plan[direction][subject]["Teachers"]) - 1)
#             all_lessons_week[random_day][random_couple - 1] += study_plan[direction][subject]["Teachers"][random_teacher]
#             all_lessons_week[random_day][random_couple - 1] += " "
#             for building in arr_buildings:
#                 auditorium_id = random.choice(auditoriums_buildings['Buildings'][building]['Laboratory'])
#                 if len(auditorium_arr) < 6:
#                     auditorium_arr.append(auditorium_id)
#                     #print(auditorium_arr)
#
# #print(all_lessons_week)
#
# for elem_1 in range (0, len(all_lessons_week)):
#     for elem_2 in range (0, len(all_lessons_week[elem_1])):
#         if (all_lessons_week[elem_1][elem_2] != '-') and (all_lessons_week[elem_1][elem_2].find("Лекции") == -1) and (all_lessons_week[elem_1][elem_2].find("Семинары") == -1):
#             all_lessons_week[elem_1][elem_2] += auditorium_arr[elem_1]
#             # all_lessons_week[elem_1][elem_2] += " "
#
# #print(all_lessons_week)
#
# start_ = start
# flag = False
# for elem_1 in range (0, len(all_lessons_week)):
#     if flag == True:
#         start_ = start_ + delta_1_day
#     for elem_2 in range (0, len(all_lessons_week[elem_1])):
#         flag = True
#         if all_lessons_week[elem_1][elem_2] != '-' and (all_lessons_week[elem_1][elem_2].find("Лекции") == -1):
#             all_lessons_week[elem_1][elem_2] += " "
#             all_lessons_week[elem_1][elem_2] += "["
#             all_lessons_week[elem_1][elem_2] += str(start_.day)
#             all_lessons_week[elem_1][elem_2] += "."
#             all_lessons_week[elem_1][elem_2] += str(start_.month)
#             all_lessons_week[elem_1][elem_2] += " - "
#
#
# #print(all_lessons_week)
# #print(all_durations_week)
#
# start = date(2024, 2, 12)
# end = date(2024, 6, 10)
# start_ = start
# flag = False
# for elem_1 in range (0, len(all_durations_week)):
#     if flag == True:
#         start_ += delta_1_day
#     for elem_2 in range(0, len(all_durations_week[elem_1])):
#         flag = True
#         if all_durations_week[elem_1][elem_2] != '-':
#             end_ = start_
#             ##print(start)
#             for i in range (1, int(all_durations_week[elem_1][elem_2])+1):
#                 ##print (i)
#                 end_ = end_ + delta_1_week
#                 ##print(end_)
#             end_lesson[elem_1][elem_2] = end_
# #print (end_lesson)
#
# for elem_1 in range (0, len(all_lessons_week)):
#     if flag == True:
#         start = start + delta_1_day
#     for elem_2 in range (0, len(all_lessons_week[elem_1])):
#         if end_lesson[elem_1][elem_2] != '-':
#             all_lessons_week[elem_1][elem_2] += str(end_lesson[elem_1][elem_2].day)
#             all_lessons_week[elem_1][elem_2] += "."
#             all_lessons_week[elem_1][elem_2] += str(end_lesson[elem_1][elem_2].month)
#             all_lessons_week[elem_1][elem_2] += "]"
# #print(all_lessons_week)

print("Расписание ИДБ-21-09")
print("Понедельник")
for elem_1 in range (0, 1):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        print (elem_2+1, "пара - ", all_lessons_week[elem_1][elem_2])

print("Вторник")
for elem_1 in range (1, 2):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        print (elem_2+1, "пара - ", all_lessons_week[elem_1][elem_2])

print("Среда")
for elem_1 in range (2, 3):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        print (elem_2+1, "пара - ", all_lessons_week[elem_1][elem_2])

print("Четверг")
for elem_1 in range (3, 4):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        print (elem_2+1, "пара - ", all_lessons_week[elem_1][elem_2])

print("Пятница")
for elem_1 in range (4, 5):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        print (elem_2+1, "пара - ", all_lessons_week[elem_1][elem_2])

print("Суббота")
for elem_1 in range (5, 6):
    for elem_2 in range (0, len(all_lessons_week[elem_1])):
        print (elem_2+1, "пара - ", all_lessons_week[elem_1][elem_2])

# t=PrettyTable(['День недели', '8:30 - 10:10', '10:20 - 12:00', '12:20 - 14:00', '14:10 - 15:50', '16:00 - 17:40', '18:00 - 19:30', '19:40 - 21:10', '21:20 - 22:50'])
# t.add_row(['Понедельник', ''])
# print (t)