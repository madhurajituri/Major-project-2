import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

def model(inputs):
    df = pd.read_csv("students_mental_health_survey.csv")
    df = df.dropna()
    df = df.drop(['Gender','CGPA', 'Substance_Use','Family_History','Semester_Credit_Load', 'Residence_Type'], axis=1)

    ratings = df[['Stress_Level', 'Depression_Score', 'Anxiety_Score']].values
    features = df.drop(['Stress_Level', 'Depression_Score', 'Anxiety_Score'], axis=1).values

    ratings_train, ratings_temp, features_train, features_temp = train_test_split(ratings, features, test_size=0.3, random_state=42)
    ratings_test, ratings_val, features_test, features_val = train_test_split(ratings_temp, features_temp, test_size=0.5, random_state=42)

    U, sigma, VT = np.linalg.svd(ratings_train)
    k = 3
    U_k = U[:, :k]
    sigma_k = np.diag(sigma[:k])
    VT_k = VT[:k, :]

    ratings_train_pred = np.dot(np.dot(U_k, sigma_k), VT_k)

    svd_model_filename = "svd_model.pkl"
    joblib.dump((U_k, sigma_k, VT_k), svd_model_filename)

    df.shape

    ratings_test_pred = np.dot(np.dot(U_k, sigma_k), VT_k)
    ratings_test_pred_int = ratings_test_pred.round().astype(int)
    ratings_test_pred_int = ratings_test_pred_int[:ratings_test.shape[0], :]
    accuracy = np.mean(np.abs(ratings_test - ratings_test_pred_int))-1

    print("Accuracy on Test Set (Integer Predictions):", accuracy)

    loaded_U_k, loaded_sigma_k, loaded_VT_k = joblib.load(svd_model_filename)

    example_features = np.array(inputs)
    example_df = pd.DataFrame([example_features])
    example_df = pd.get_dummies(example_df)
    example_df = example_df.reindex(columns=df.columns.drop(['Stress_Level', 'Depression_Score', 'Anxiety_Score']), fill_value=0)
    example_ratings_pred = np.dot(np.dot(loaded_U_k, loaded_sigma_k), loaded_VT_k)
    predicted_ratings_example = example_ratings_pred[0]
    predicted_ratings_example_int = predicted_ratings_example.round().astype(int)

    return predicted_ratings_example_int
