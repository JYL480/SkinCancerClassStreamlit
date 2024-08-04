import streamlit as st
from PIL import Image
import torch
from time import perf_counter as timer
from model import createModel
import os

# Define the path to your model's parameters and the class names
param_path = "SkinCancerClassification7Classes.pth"
class_names_large = ['melanocytic_Nevi', "melanoma", "benign_keratosis-like_lesions",
                     'basal_cell_carcinoma', 'actinic_keratoses', "vascular_lesions",
                     'dermatofibroma']

class_names = class_names_large

# Load the model and its transforms
VitModel, VitModel_Transforms = createModel(len(class_names), 42)
VitModel.load_state_dict(torch.load(param_path, map_location=torch.device("cpu")))

def predict(image):
    start_time = timer()
    # Transform and prepare the image
    image = VitModel_Transforms(image).unsqueeze(0)
    VitModel.eval()
    with torch.inference_mode():
        # Get the prediction probabilities
        pred_probs = torch.softmax(VitModel(image), dim=1)
    # Map predictions to class names
    pred_labels_and_probs = {class_names[i]: float(pred_probs[0][i]) for i in range(len(class_names))}
    pred_time = round(timer() - start_time, 5)
    return pred_labels_and_probs, pred_time

# Streamlit app layout
st.title("Skin Cancer Classification")
st.write("Upload an image to classify the type of skin cancer, or choose one of the example images below.")

# Provide example images
example_images = {
    "Melanoma": "./images/melanoma.jpg",
    "melanocytic_Nevi": "./images/melanocytic_Nevi.jpg",
    "benign_keratosis-like_lesions": "./images/benign_keratosis-like_lesions.jpg",
}

example_selected = st.checkbox("Use an example image")

if example_selected:
    selected_example = st.selectbox("Choose an example image:", list(example_images.keys()))
    if selected_example:
        image = Image.open(example_images[selected_example])
        st.image(image, caption=f"Example Image: {selected_example}", use_column_width=True)
else:
    uploaded_file = st.file_uploader("Or upload your own image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# Prediction
if (example_selected and selected_example) or uploaded_file:
    pred_labels_and_probs, pred_time = predict(image)
    st.write(f"Prediction time: {pred_time} seconds")
    st.write("Predicted probabilities:")
    for label, prob in pred_labels_and_probs.items():
        st.write(f"{label}: {prob:.4f}")