# import os
# from flask import Flask, render_template, request
# import openai
# from dotenv import load_dotenv

# # Load environment variables (for storing API key securely)
# load_dotenv()

# # Initialize Flask app
# app = Flask(__name__)

# # Set up OpenAI API key from environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Therapy function based on form data
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

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')

# @app.route('/read_form', methods=['POST'])
# def read_form():
#     # Get data from the form
#     form_data = {
#         'age': request.form['age'],
#         'course': request.form['course'],
#         'gender': request.form['gender'],
#         'cgpa': request.form['cgpa'],
#         'stress_level': request.form['stressLevel'],
#         'depression_score': request.form['depressionScore'],
#         'anxiety_score': request.form['anxietyScore'],
#         'sleep_quality': request.form['sleepQuality'],
#         'physical_activity': request.form['physicalActivity'],
#         'diet_quality': request.form['dietQuality'],
#         'social_support': request.form['socialSupport'],
#         'relationship_status': request.form['relationshipStatus'],
#         'substance_use': request.form['substanceUse'],
#         'counseling_service_use': request.form['counselingServiceUse'],
#         'family_history': request.form['familyHistory'],
#         'chronic_illness': request.form['chronicIllness'],
#         'financial_stress': request.form['financialStress'],
#         'extracurricular_involvement': request.form['extracurricularInvolvement'],
#         'semester_credit_load': request.form['semesterCreditLoad'],
#         'residence_type': request.form['residenceType']
#     }

#     L = list(form_data.values())
#     ans = therapy(L)

#     # Generate prompt for text generation
#     prompt = f"""
#     User Profile:
#     - Age: {form_data['age']}
#     - Course: {form_data['course']}
#     - Gender: {form_data['gender']}
#     - cgpa: {form_data['cgpa']}
#     - stress_level: {form_data['stress_level']}
#     - anxiety_score: {form_data['anxiety_score']}
#     - depression_score: {form_data['depression_score']}
#     - sleep_quality: {form_data['sleep_quality']}
#     - physical_activity: {form_data['physical_activity']}
#     - diet_quality: {form_data['diet_quality']}
#     - social_support: {form_data['social_support']}
#     - relationship_status: {form_data['relationship_status']}
#     - substance_use: {form_data['substance_use']}
#     - counseling_service_use: {form_data['counseling_service_use']}
#     - family_history: {form_data['family_history']}
#     - chronic_illness: {form_data['chronic_illness']}
#     - financial_stress: {form_data['financial_stress']}
#     - extracurricular_involvement: {form_data['extracurricular_involvement']}
#     - semester_credit_load: {form_data['semester_credit_load']}
#     - Residence Type: {form_data['residence_type']}
#     Therapy Type: {ans}

#     Generate a personalized 7-day therapy planner using the above user data to represent 7 days planning according to days, which will include some:
#     - Daily activities
#     - Motivation tips
#     - Self-care suggestions
#     - Balanced emotional wellness tasks
#     """

#     try:
#         # OpenAI Gemini model text generation
#         response = openai.Completion.create(
#             model="gpt-4",  # or the specific Gemini model you have access to
#             prompt=prompt,
#             max_tokens=500,
#             temperature=0.7,
#             top_p=0.95,
#             n=1,
#             stop=None
#         )

#         # Get the generated text from OpenAI API response
#         result = response.choices[0].text.strip()
#         routine = result

#     except Exception as e:
#         routine = f"Error generating planner: {str(e)}"

#     return render_template('result.html', ans=ans, routine=routine)

# if __name__ == '__main__':
#     app.run(host='localhost', port=5200, debug=True)






from google import genai
import os
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv

# Load environment variables (for storing API key securely)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Therapy function based on form data
def therapy(L):
    x, y, z = int(L[4]), int(L[5]), int(L[6])
    if x == 5 and y == 5 and z == 5:
        return "Consult a Doctor"
    elif x == 0 and y == 0 and z == 0:
        return "Audio Therapy"
    elif x == 0 and y == 0 and z > 0:
        return "Reading Therapy"
    elif x == 0 and y > 0 and z == 0:
        return "Yoga Therapy"
    elif x > 0 and y == 0 and z == 0:
        return "Laughing Therapy"
    elif x == 0 and y > 0 and z > 0:
        return "Talking Therapy"
    elif x > 0 and y == 0 and z > 0:
        return "Child Therapy"
    elif x > 0 and y > 0 and z == 0:
        return "Spiritual Therapy"
    else:
        return "Special Therapy"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/read_form', methods=['POST'])
def read_form():
    # Get data from the form
    form_data = {
        'age': request.form['age'],
        'course': request.form['course'],
        'gender': request.form['gender'],
        'cgpa': request.form['cgpa'],
        'stress_level': request.form['stressLevel'],
        'depression_score': request.form['depressionScore'],
        'anxiety_score': request.form['anxietyScore'],
        'sleep_quality': request.form['sleepQuality'],
        'physical_activity': request.form['physicalActivity'],
        'diet_quality': request.form['dietQuality'],
        'social_support': request.form['socialSupport'],
        'relationship_status': request.form['relationshipStatus'],
        'substance_use': request.form['substanceUse'],
        'counseling_service_use': request.form['counselingServiceUse'],
        'family_history': request.form['familyHistory'],
        'chronic_illness': request.form['chronicIllness'],
        'financial_stress': request.form['financialStress'],
        'extracurricular_involvement': request.form['extracurricularInvolvement'],
        'semester_credit_load': request.form['semesterCreditLoad'],
        'residence_type': request.form['residenceType']
    }

    L = list(form_data.values())
    ans = therapy(L)



    # Generate prompt for text generation
    prompt = f"""
    User Profile:
    - Age: {form_data['age']}
    - Course: {form_data['course']}
    - Gender: {form_data['gender']}
    - cgpa: {form_data['cgpa']}
    - stress_level: {form_data['stress_level']}
    - anxiety_score: {form_data['anxiety_score']}
    - depression_score: {form_data['depression_score']}
    - sleep_quality: {form_data['sleep_quality']}
    - physical_activity: {form_data['physical_activity']}
    - diet_quality: {form_data['diet_quality']}
    - social_support: {form_data['social_support']}
    - relationship_status: {form_data['relationship_status']}
    - substance_use: {form_data['substance_use']}
    - counseling_service_use: {form_data['counseling_service_use']}
    - family_history: {form_data['family_history']}
    - chronic_illness: {form_data['chronic_illness']}
    - financial_stress: {form_data['financial_stress']}
    - extracurricular_involvement: {form_data['extracurricular_involvement']}
    - semester_credit_load: {form_data['semester_credit_load']}
    - Residence Type: {form_data['residence_type']}
    Therapy Type: {ans}

    Generate a personalized 7-day therapy planner using the above user data to represent 7 days planning according to days, which will include some:
    - Daily activities
    - Motivation tips
    - Self-care suggestions
    - Balanced emotional wellness tasks

    Directly start from 7 day planning dont write anything else.
    """

    try:
        # OpenAI Gemini model text generation
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        print(response.text)
        
        # Get the generated text from OpenAI API response
        result = response.text
        routine = result

    except Exception as e:
        routine = f"Error generating planner: {str(e)}"

    return render_template('result.html', ans=ans, routine=routine)

if __name__ == '__main__':
    app.run(host='localhost', port=5200, debug=True)
