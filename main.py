import csv
from read import read_from_csv, get_file_name
from functions import create_list_of_candidates_to_remove, create_list_of_candidates_to_book, create_list_of_potential_candidates

filename = get_file_name()
answers_list = read_from_csv(filename)

red_list = create_list_of_candidates_to_remove(answers_list)
green_list = create_list_of_candidates_to_book(answers_list)
yellow_list = create_list_of_potential_candidates(answers_list)
