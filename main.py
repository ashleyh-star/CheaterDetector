import requests

#API STUFF
API_KEY = "your API key"
headers = {"X-Api-Key": API_KEY}
URL = f"https://api.api-ninjas.com/v1/textsimilarity"

#file reading
student1work = ""
student2work = ""

"""
Read the content from student1 text file and make student1work equal to that, do the same for student2
"""


def readStudent1Work():
    global student1work
    with open("student1.txt", "r") as f:
        student1work = f.read()


def readStudent2Work():
    global student2work
    with open("student2.txt", "r") as f:
        student2work = f.read()


readStudent1Work()
readStudent2Work()

#additional dictionary needed to compare the two strings
body = {'text_1': student1work, 'text_2': student2work}

def getSimilarity():
    response = requests.post(url=URL, headers=headers, json=body)
    similarity = response.json()["similarity"]
    return round(float(similarity),2)*100

def threshold(t):
    if getSimilarity() >= t:
        return "Cheating detected"
    else:
        return "No Cheating detected"


