"""
Q1. Write a function write_lines(filename, lines) that takes a list of strings 
and writes each one on its own line in the file (overwriting any existing content). 
Use a with block.
""" 

def write_lines(filename, lines):
    with open(filename,"w") as f:
        for line in lines:
            f.write(f"{line}\n")

lines = ["aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff", ]
# write_lines("string_line.txt", lines)

"""
Q2. Write a function count_lines(filename) that returns the number of lines in a text file.
Return 0 if the file does not exist.
"""
def count_lines(filename):
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
        return len(lines)
    except FileNotFoundError:
        return 0

# print(count_lines("string_line.txt"))

"""
Q3. Write code that copies the contents of source.txt into dest.txt 
without loading the whole file into memory at once (read line by line).
"""
def copy_file(first_file, second_file):
    with open(first_file, "r") as f1:
        lines = f1.readlines()

    with open(second_file, "w") as f2:
        for line in lines:
            f2.write(line)

# copy_file("string_line.txt", "test.txt")

"""

Q4. Explain the difference between "w", "a", and "x" modes.
Then write a snippet that appends "new entry\n" to data.txt 
only if the file already exists, otherwise creates it with that line.
"""

# w - write in file from start deleting all its content
# a - In append mode given content write at end of the file
# x - create a new file and write in it

def data_entry(filename, new_entry):
    with open(filename, "a") as f:
        f.write(f"{new_entry}\n")

# data_entry("data.txt", "first_entry")


"""
Q5. Write a function read_csv_rows(filename) 
that uses csv.reader to return all rows (excluding the header) as a list of lists.
"""

import csv
def read_csv_rows(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
        return rows[1:]
            
# print(read_csv_rows("test.csv"))


"""
Q6. Using csv.DictReader, write a function average_score(filename)
that reads students.csv (columns Name, Age, Score) 
and returns the average score rounded to 1 decimal place.
"""
def average_score(filename):
    with open(filename, "r") as f:
        dictreader = csv.DictReader(f)
        total_score = 0
        no_of_lines = 0
        for row in dictreader:
            total_score += float(row["Score"])
            no_of_lines += 1
        av_score = total_score/(no_of_lines)
        return f"{av_score:.1f}"

# print(average_score("students.csv"))


"""
Q7. Write a function append_log(message, logfile="app.log") 
that appends a timestamped line in the format [YYYY-MM-DD HH:MM:SS] message.
"""
import datetime
def append_log(message, logfile="app.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"[{timestamp}] - {message}\n")

# append_log("app starting...")
# append_log("app running...")
# append_log("app closed")

"""

Q8. Write code that reads numbers.txt (one integer per line) and prints their sum.
Handle blank lines gracefully.
"""
def sum_numbers(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    summ = 0
    for line in lines:
        try:
            summ += int(line)
        except ValueError:
            continue
    return summ

# print(sum_numbers("numbers.txt"))

"""
Q9. Write a function write_students_csv(filename, data) 
that writes a list of rows to a CSV file, ensuring no blank rows appear between lines on Windows.
"""

def write_students_csv(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

data = [["std1",18,90], ["std2",19,85], ["std3",17,70], ["std4",20,65.555677]]
# write_students_csv("students.csv", data)

"""
Q10. Write a function safe_read(filename) that returns the file's content as a string,
or the string "FILE NOT FOUND" if it doesn't exist. Use os.path.exists.
"""
import os
def safe_read(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
            return data
    else:
        return "FILE NOT FOUND"
    
# print(safe_read("students.csv"))

"""
Q11. Write code that reads students.csv with DictReader and 
writes a new file top_students.csv containing only rows where Score >= 90, 
keeping the header.
"""
def top_students(student_file):
    top_stu = []
    with open(student_file, "r") as stu_f:
        reader = csv.DictReader(stu_f)
        for row in reader:
            if float(row["Score"]) > 90:
                top_stu.append(row)
    
    with open("top_students.csv", "w", newline="") as top_f:
        writer = csv.DictWriter(top_f, fieldnames=["Name", "Age", "Score"])
        writer.writeheader()
        writer.writerows(top_stu)

# top_students("students.csv")


"""
Q12. Explain what readline(), readlines(), and read() each return, 
and write a snippet showing the result of each on a 3-line file.
"""
def read(filename):
    with open(filename, "r") as f:
        read_result = f.read()
    with open(filename, "r") as f:
        readline_result = f.readline()
    with open(filename, "r") as f:
        readlines_result = f.readlines()
    
    return read_result, readline_result, readlines_result

read_result, readline_result, readlines_result = read("top_students.csv")
# print(f"read result\n{read_result}")
# print(f"readline result\n{readline_result}")
# print(f"readlines result\n{readlines_result}")

"""
Q13. Write a function word_count(filename) 
that returns a dictionary mapping each word to how many times it appears in the file 
(case-insensitive).
"""
def word_count(filename):
    with open(filename, "r") as f:
        data = f.read()
    word_map = {}
    for word in data:
        word_map[word] = data.count(word)
    return word_map

# print(word_count("paragraph.txt"))

"""
Q14. Write code using "w+" mode that writes three lines, 
then seeks back to the start and reads/prints the full content in the same with block.
"""
def write_and_read_file(filename):
    with open(filename, "w+") as f:
        f.write("'r' - open for reading (default)\n'w' - open for writing, truncating the file first\n'x' - create a new file and open it for writing")
        f.seek(0)
        data = f.read()
        print(data)

# write_and_read_file("w_and_r.txt")

"""
Q15. Write a function merge_files(file_list, output) 
that concatenates several text files into one output file, 
adding a header line --- filename --- before each file's content.
"""

def merge_files(file_list, output):
    with open(output, "a") as output_f:
        for file in file_list:
            with open(file, "r") as f:
                data = f.read()
            output_f.write(f"--- {file} ---\n{data}\n")

file_list = ["app.log", "students.csv", "paragraph.txt"]
# merge_files(file_list, "merged_file.txt")
