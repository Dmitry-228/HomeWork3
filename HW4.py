days = int(input("Количество дней: "))
cereals = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
timetable = []
for i in range(days):
    cereal_index = i % len(cereals)
    timetable.append(cereals[cereal_index])
for cereal in timetable:
    print(cereal)