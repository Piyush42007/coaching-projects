student_records = []

STORAGE_PATH = "student_records.csv"
#---------------------------------------------------
#----------- Helper Function -----------------------
#---------------------------------------------------

def calculate_percentage(scores):
    total_obtained_score = 0
    for score in scores.values():
        total_obtained_score += score

    total_score = len(scores)*100
    percentage = (total_obtained_score/total_score) * 100
    return percentage
def calculate_grade(percentage):
    # (A: ≥90, B: ≥80, C: ≥70, D: ≥60, F: <60)
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage < 60:
        return "F"
def generate_id():
    if not student_records:
        return 1
    return (student_records[-1]["id"]) + 1

    
#---------------------------------------------------
#----------- Logic Function ------------------------
#---------------------------------------------------

def add_students(name: str, age: int, scores: dict):
    percentage = calculate_percentage(scores)
    grade = calculate_grade(percentage)

    student_records.append({"id": generate_id(), "name":name, "age":age, "scores": scores, "percentage":percentage, "grade":grade})

def view_student_records():
    if not student_records:
        print("No records found.")
        return
    print("ID    Name        Age    Avg    Grade")
    print("-"*40)
    for std in student_records:
        print(f"{std["id"]:<6}{std["name"]:<12}{std["age"]:<7}{std["percentage"]:<9.2f}{std["grade"]}")

def search_student_by_name(name):
    if not student_records:
        print("No records found.")
        return
    
    
    result = ""
    for std in student_records:
        if name in std["name"]:
            result += f"{std["id"]:<6}{std["name"]:<12}{std["age"]:<7}{std["percentage"]:<9.2f}{std["grade"]}\n"
    
    print(f"search for '{name}'")
    if not result:
        print("No match found")
    else:
        print("ID    Name        Age    Avg    Grade")
        print("-"*40)
        print(result)

def delete_student_by_id(std_id):
    if not student_records:
        print("No records found.")
        return

    for std in student_records:
        if std_id == std["id"]:
            student_records.remove(std)


#---------------------------------------------------
#----------- Storge Function -----------------------
#--------------------------------------------------- 
# import os
# import csv

# def load_data(csvFile = STORAGE_PATH):
#     if not os.path.exists(csvFile):
#         return False
    
#     with open(csvFile, "r") as f:
#         reader = csv.DictReader()
#         for std in reader:
#             student_records.append(std)


# def save_data(csvFile = STORAGE_PATH):
#     pass


            





    








add_students("alice", 16, {"english": 85, "hindi": 75, "maths": 86, "science": 92, "sst": 81})
add_students("john", 17, {"english": 83, "hindi": 71, "maths": 76, "science": 72, "sst": 80})
add_students("tony", 16, {"english": 75, "hindi": 55, "maths": 96, "science": 93, "sst": 71})
add_students("bruce", 16, {"english": 86, "hindi": 65, "maths": 94, "science": 98, "sst": 60})
add_students("tom", 16, {"english": 80, "hindi": 71, "maths": 87, "science": 93, "sst": 84})

# view_student_records()
# search_student_by_name("alice")
# delete_student_by_id(2)
# view_student_records()
