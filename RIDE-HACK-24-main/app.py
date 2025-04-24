from flask import Flask, render_template, request


# def therapy(L):
#     x, y, z = int(L[4]), int(L[5]), int(L[6])
#     if x == 5 and y == 5 and z == 5:
#         return "Consult a Doctor"
#     elif x == 0 and y == 0 and z == 0:
#         return "Audio Therapy"
#     elif x == 0 and y == 0 and z > 0:
#         return "Reading Therapy"
#     elif x == 0 and y > 0 and z == 0:
#         return "Yoga Therapy"
#     elif x > 0 and y == 0 and z == 0:
#         return "Laughing Therapy"
#     elif x == 0 and y > 0 and z > 0:
#         return "Talking Therapy"
#     elif x > 0 and y == 0 and z > 0:
#         return "Child Therapy"
#     elif x > 0 and y > 0 and z == 0:
#         return "Spiritual Therapy"
#     else:
#         return "Special Therapy"

import random


def therapy(L):
    stress = int(L[4])
    depression = int(L[5])
    anxiety = int(L[6])

    total_score = stress + depression + anxiety

    if stress == 5 and depression == 5 and anxiety == 5:
        return "Consult a Doctor"

    # Defined patterns
    if total_score <= 3:
        return "Audio Therapy"
    elif stress <= 1 and depression <= 1 and anxiety >= 3:
        return "Reading Therapy"
    elif stress <= 1 and depression >= 2 and anxiety <= 1:
        return "Yoga Therapy"
    elif stress >= 2 and depression <= 1 and anxiety <= 1:
        return "Laughing Therapy"
    elif stress <= 2 and depression >= 2 and anxiety >= 2:
        return "Talking Therapy"
    elif stress >= 2 and depression <= 2 and anxiety >= 2:
        return "Child Therapy"
    elif stress >= 2 and depression >= 2 and anxiety <= 1:
        return "Spiritual Therapy"
    elif total_score >= 12:
        return "Consult a Doctor"

    # Balanced fallback options including Special Therapy
    return random.choice([
        "Audio Therapy",
        "Reading Therapy",
        "Yoga Therapy",
        "Laughing Therapy",
        "Talking Therapy",
        "Child Therapy",
        "Spiritual Therapy",
        "Special Therapy"
    ])


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/read_form', methods=['POST'])
def read_form():
    # Get data from the form
    age = request.form['age']
    course = request.form['course']
    gender = request.form['gender']
    cgpa = request.form['cgpa']
    stress_level = request.form['stressLevel']
    depression_score = request.form['depressionScore']
    anxiety_score = request.form['anxietyScore']
    sleep_quality = request.form['sleepQuality']
    physical_activity = request.form['physicalActivity']
    diet_quality = request.form['dietQuality']
    social_support = request.form['socialSupport']
    relationship_status = request.form['relationshipStatus']
    substance_use = request.form['substanceUse']
    counseling_service_use = request.form['counselingServiceUse']
    family_history = request.form['familyHistory']
    chronic_illness = request.form['chronicIllness']
    financial_stress = request.form['financialStress']
    extracurricular_involvement = request.form['extracurricularInvolvement']
    semester_credit_load = request.form['semesterCreditLoad']
    residence_type = request.form['residenceType']
    L = [age, course, gender, cgpa, stress_level, depression_score, anxiety_score, sleep_quality, physical_activity, diet_quality, social_support, relationship_status,
         substance_use, counseling_service_use, family_history, chronic_illness, financial_stress, extracurricular_involvement, semester_credit_load, residence_type]
    ans = therapy(L)

    return render_template('result.html', ans=ans)


if __name__ == '__main__':
    app.run(host='localhost', port=5200)
