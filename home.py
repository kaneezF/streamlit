import streamlit as st
from streamlit_option_menu import option_menu
#mysql
import mysql.connector
import hashlib
import re
#predict disease
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

random_seed = 42

with st.sidebar:
    selected=option_menu(
        menu_title="Patient",
        options=["Home" , "Predict Disease" , "Find Doc" , "Book an Ambulance" , "Ask Bot" , "SignUp" , "Login" , "Logout"],
        menu_icon="clipboard-check-fill",
    )

#database connection
# Initialize session state

if "login" not in st.session_state:
    st.session_state.login = False


# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PHW#84#jeor",
    database="demodb"
)
cursor = db.cursor()

# Hashing Function
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Password validation function
def is_valid_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check for at least one special character (e.g., !, @, #, $, %)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

# DB Functions
def create_usertable():
    cursor.execute('CREATE TABLE IF NOT EXISTS demotable(username VARCHAR(255), password VARCHAR(255))')

def add_userdata(username, password):
    cursor.execute('INSERT INTO demotable(username, password) VALUES (%s, %s)', (username, password))
    db.commit()

def login_user(username, password):
    cursor.execute('SELECT * FROM demotable WHERE username = BINARY %s', (username,))
    user = cursor.fetchone()
    if user and check_hashes(password, user[1]):
        return True
    return False

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

# Define the is_user_logged_in function
def is_user_logged_in():
    return st.session_state.login

def main():
    if selected == "Home":
        st.write("Home page")

    elif selected in ["Predict Disease", "Ask Bot", "Find Doc" , "Book an Ambulance"]:
        if is_user_logged_in():
            st.write(f"Welcome to the {selected} section. This is only accessible to registered users.")
        else:
            st.warning("Please log in to access this section.")

    elif selected == "Predict Disease":
        if is_user_logged_in():
            st.write(f"Welcome to the Predict Disease section. This is only accessible to registered users.")
            # Add your "Predict Disease" functionality here
            # Load the dataset
            st.write("jhjwhdch")
            try:
                df = pd.read_csv("F:\\newapp\\Training.csv")
                df.drop('Unnamed: 133', axis=1, inplace=True)
            except FileNotFoundError:
                st.error("Could not find the dataset file. Please make sure the file path is correct.")

            x = df.drop('prognosis', axis=1)
            y = df['prognosis']

            # Split the data into training and testing sets
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=random_seed)


            # Random Forest Classifier
            random_forest = RandomForestClassifier(random_state=random_seed)
            random_forest.fit(x_train.values, y_train)
            random_forest_pred = random_forest.predict(x_test.values)

            # Streamlit app
            st.title("Disease Predictor System")

            # Sidebar
            st.header("Select Symptoms")
            symptoms = []
            for i in range(5):
                symptom = st.selectbox(f"Symptom {i+1}", [''] + sorted(x.columns))
                if symptom:
                    symptoms.append(symptom)

            # Analyze Button
            if st.button("Analyze"):
                selected_symptoms = ", ".join(symptoms)
                st.write(f"Selected Symptoms: {selected_symptoms}")

                l2 = [1 if symptom in symptoms else 0 for symptom in x.columns]
                inputtest = [l2]

                # Predictions 
                predicted_disease_random_forest = random_forest.predict(inputtest)[0]
                st.write(f"Predicted Disease (Random Forest): {predicted_disease_random_forest}")

        else:
            st.warning("Please log in to access this section.")
    elif selected == "Login":
        if is_user_logged_in():
            st.write("You are already logged in.")
        else:
            st.subheader("Login")
            username = st.text_input("User Name")
            password = st.text_input("Password", type='password')
            if st.checkbox("Login"):
                create_usertable()

                if login_user(username, password):
                    st.success("Logged In as {}".format(username))
                    st.session_state.login = True
                    st.session_state.username = username
                    st.write("Click on Login Again")
                else:
                    st.warning("Incorrect Username/Password")

    elif selected == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            if is_valid_password(new_password):
                hashed_password = make_hashes(new_password)
                add_userdata(new_user, hashed_password)
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")
            else:
                st.warning("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one special character.")

    elif selected =="Logout":
        #logout = st.button("Logout")
        #if logout:
        st.session_state.login = False
        st.session_state.username = None
        st.write("Logged out")
    


if __name__ == "__main__":
    main()