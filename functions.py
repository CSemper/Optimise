from datetime import date
from classes import Answers

def check_age(year_born, month_born, day_born):
    """Check Age"""
    today = date.today()
    age = today.year - year_born - ((today.month, today.day) < (month_born, day_born)) 
    return age

def create_list_of_candidates_to_remove(answers_list):
    red = {}
    for answer in answers_list:
        if answer.age < 18 or answer.age > 35:
            red[answer.name] = f"Age Restrictions"
            continue
        elif 30 <= answer.age <= 35 and answer.city == "Willing to Relocate":
            red[answer.name] = f"Commuting Restrictions"
            continue
        elif answer.full_part_time == "Part-Time (afternoons or weekends only)":
            red[answer.name] = f"Availability Restrictions"
            continue
        elif answer.city == "No":
            red[answer.name] = f"Commuting Restrictions"
            continue
    return red

def create_list_of_candidates_to_book(answers_list):
    green = {}
    for answer in answers_list:
        if 18 <= answer.age <= 29 and answer.city == "Yes":
            name = answer.name
            if answer.full_part_time == "Full-Time" or answer.full_part_time == "Part-Time (4+ days per week)":
                green[name] = f"{answer.age}, Easy Commute, & {answer.full_part_time}"
                continue
    return green

def create_list_of_potential_candidates(answers_list):
    yellow = {}
    for answer in answers_list:
        if 30 <= answer.age <= 35 and answer.city == "Yes" and answer.full_part_time == "Full-Time":
            entrepreneur = answer.entrepreneur
            if entrepreneur == "Yes":
                yellow[answer.name] = f"{answer.age}, Full-Time, & Entrepreneur"
                continue     
        elif 18 <= answer.age <= 29 and answer.full_part_time == "Full-Time":
            location = answer.city
            if location == "Willing to Relocate":
                yellow[answer.name] = f"{answer.age}, Full-Time, Willing to Relocate"
                continue  
    return yellow
