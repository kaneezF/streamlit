import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("C:\\Users\\KAZIM\\Desktop\\newstreamlit\\Training.csv")
df.drop('Unnamed: 133', axis=1, inplace=True)

x = df.drop('prognosis', axis=1)
y = df['prognosis']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Decision Tree Classifier
tree = DecisionTreeClassifier()
tree.fit(x_train, y_train)
tree_pred = tree.predict(x_test)
tree_acc = accuracy_score(y_test, tree_pred)

# Streamlit app
st.title("Decision Tree Classifier")
st.write("Accuracy on test set: {:.2f}%".format(tree_acc * 100))


# Streamlit UI
st.title("Disease Predictor System")

# Sidebar
st.header("Select Symptoms")
symptoms = []
for i in range(5):
    symptom = st.selectbox(f"Symptom {i+1}", sorted(x))
    symptoms.append(symptom)

# Analyze Button
if st.button("Analyze"):
    l2 = [1 if symptom in symptoms else 0 for symptom in x]
    inputtest = [l2]
    predict = tree.predict(inputtest)
    predicted_disease = predict[0]
    #predicted_disease = disease[predicted]
    st.write(f"Predicted Disease: {predicted_disease}")

# Footer
st.write("Select All 5 symptoms")