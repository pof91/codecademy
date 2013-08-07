lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd,alice,tyler]
# Add your function below!
def average(listNumber) :
    return sum(listNumber)/len(listNumber)
    
def get_average(studDict) :
    return average(studDict["homework"]) * 0.1 + average(studDict["quizzes"]) * 0.3 + average(studDict["tests"]) * 0.6
    
def get_letter_grade(score) :
    if score >= 90 : return 'A'
    elif 80 <= score < 90 : return 'B'
    elif 70 <= score < 80 : return 'C'
    elif 60 <= score < 70 : return 'D'
    else : return 'F'
    
print get_letter_grade(get_average(lloyd))

def get_class_average(studList) :
    score = 0
    for student in studList :
        score += get_average(student)
    return score/len(studList)

scoreClasse = get_class_average(students)
print str(scoreClasse)
print get_letter_grade(scoreClasse)