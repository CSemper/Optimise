import csv
from classes import Answers
from functions import check_age

def get_file_name():
    filename = "Job_Application-2.csv"
    return filename

def read_from_csv(filename):
    answers_list = []
    with open (filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]=="Timestamp": #Skips first line of CSV so it doesn't read just column titles and it focuses on real people
                continue
            dob = row[4].split('-')
            age = check_age(int(dob[0]), int(dob[1]), int(dob[2]))
            answer = Answers(row[0], row[1], row[2], row[3], row[4], age, row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20])
            answers_list.append(answer)
    return answers_list

# def get_important_variables(answers_list):
#     filtered_list = []
#     for answer in answers_list:
#         filtered = Filter(
#             name = answer.name,
#             email = answer.email, 
#             age = answer.age, 
#             commute = answer.city  , 
#             availability = answer.full_part_time , 
#             entrepreneur = answer.entrepreneur
#         )
#         filtered_list.append(filtered)
#     return filtered_list