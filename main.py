import pandas as pd
def convert_series_to_string(series):
    return ', '.join(map(str, series))
data = pd.read_excel('./lab_pi_101.xlsx')
# group_name = input ("Введите номер группы ")
all_marks = data["Оценка"]
pi101_marks = data[data["Группа"] == "ПИ101"].shape[0]
students_count = data[data["Группа"] == "ПИ101"]["Личный номер студента"]
unique_student_count = students_count.unique()
unique_control_level = data["Уровень контроля"].unique()
unique_years = sorted(data["Год"].unique())
output_string = (f"В исходном датасете содержалось {all_marks.size} оценок, из них {pi101_marks} оценок относятся к группе ПИ101\n"
f"В датасете находятся оценки {unique_student_count.size} студентов со следующими личными номерами (по ПИ101): {convert_series_to_string(unique_student_count)}\n"
f"Используемые формы контроля: {convert_series_to_string(unique_control_level)}\n"
f"Данные представлены по следующим учебным годам: {convert_series_to_string(sorted(unique_years))}")
print(output_string)