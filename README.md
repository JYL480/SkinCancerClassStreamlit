<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JYL480/RAGResume">
  </a>

<h3 align="center">Skin Cancer Classification with ViT</h3>


  <p align="center">
     Used https://huggingface.co/datasets/marmal88/skin_cancer dataset to train the Vision Transformer model
    <br />
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
![image](https://github.com/user-attachments/assets/4de29fa7-2c42-4701-bdcf-30c8b5258843)

**5 classes**: melanocytic_Nevi, melanoma, benign_keratosis-like_lesions, basal_cell_carcinoma, actinic_keratoses,vascular_lesions, dermatofibroma
     
### Try it yourself

**Visit the link**: https://huggingface.co/spaces/JYL480/SkinCancerClassification

**Inference Model on HuggingFace**: https://huggingface.co/JYL480/vit-base-images 


### Features

- **Vision Transformer ViT_B_16**: Utilizes ViT to classify skin cancer images
- **User-friendly Interface**: Simple input interface for providing questions and associated context, with immediate response generation.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Gradio

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
**Requirements**
- torch == 2.4.0
- pillow == 10.4.0
- torchvision == 0.19.0

## Installation

Clone the repo:
```sh
git clone https://github.com/JYL480/SkinCancerClassStreamlit.git
```
Install requirements:
```sh
pip install -r requirements.txt
```
## Usage
```sh
streamlit run app.py
```

- Run locally with streamlit provided that you have the trained parameters to be loaded into ViT model.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
