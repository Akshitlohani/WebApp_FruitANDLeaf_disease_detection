from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm, ImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image
from django.http import HttpResponse

# ML INTEGRATION
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow import keras
from tensorflow.keras.models import load_model
import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Pomegranate Integration

classesPom = ['Alternaria', 'Anthracnose', 'Bacterial_Blight', 'Cercospora', 'Healthy']
model_path_pom = os.path.join(BASE_DIR, 'model_pom.h5')
model_pom = load_model(model_path_pom)

def return_prediction_pom(img):
    # Convert image to RGB if it's in RGBA format
    if img.shape[-1] == 4:  # Check if the image has 4 channels (RGBA)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
    # Preprocess the image
    img_size = (256, 256)  # Define the input size expected by your model
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    
    # Perform prediction
    pred = model_pom.predict(img)
    index = np.argmax(pred)
    klass = classesPom[index]
    
    return [klass]

@csrf_exempt  
def detection_pomegranate(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            form.save()
            obj = form.instance
            
            # Read the image file from the form instance
            img_path = obj.image.path  # Assuming your form saves the file in the Image model with a field called 'image'
            img = plt.imread(img_path)
            
            # Perform prediction
            # result = return_prediction(model, img)
            result_list = return_prediction_pom(img)
            result = result_list[0]

            # Return the results in the template
            return render(request, 'finalPom.html', {"result": result})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "detection_pomegranate.html", {"img": img, "form": form})


# Tomato Integration

classesTom = ["Bacterial spot", "Early blight", "Late blight", "Leaf Mold", "Septoria leaf spot", "Spider mites Two-spotted spider mite", "Target Spot", "Tomato Yellow Leaf Curl Virus", "Tomato mosaic virus", "Healthy"]
model_path_tom = os.path.join(BASE_DIR, 'TomatoModel2.h5')
model_tom = load_model(model_path_tom)

def return_prediction_tom(img):
    # Convert image to RGB if it's in RGBA format
    if img.shape[-1] == 4:  # Check if the image has 4 channels (RGBA)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
    # Preprocess the image
    img_size = (256, 256)  # Define the input size expected by your model
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    
    # Perform prediction
    pred = model_tom.predict(img)
    index = np.argmax(pred)
    klass = classesTom[index]
    
    return [klass]

@csrf_exempt  
def detection_tomato(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            form.save()
            obj = form.instance
            
            # Read the image file from the form instance
            img_path = obj.image.path 
            img = plt.imread(img_path)
            
            # Perform prediction
            # result = return_prediction(model, img)
            result_list = return_prediction_tom(img)
            result = result_list[0]

            # Return the results in the template
            return render(request, 'finalTom.html', {"result": result})
    form = ImageForm()
    return render(request, "detection_tomato.html", {"form": form})


# Orange Integration

classesOrange = ["Citrus_leaf_miner", "Greasy_spot", "Healthy", "iron_deficiency", "magnesium_deficiency"]
model_path_orange = os.path.join(BASE_DIR, 'orange_leaf_disease_model.h5') 
model_orange = load_model(model_path_orange)

def return_prediction_orange(img):
    # Convert image to RGB if it's in RGBA format
    if img.shape[-1] == 4:  # Check if the image has 4 channels (RGBA)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
    # Preprocess the image
    img_size = (224, 224)  
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32') / 255.0 
    # Perform prediction
    pred = model_orange.predict(img)
    print("Prediction output:", pred)
    
    index = np.argmax(pred)
    klass = classesOrange[index]
    
    return [klass]

@csrf_exempt  
def detection_orange(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            form.save()
            obj = form.instance
            
            # Read the image file from the form instance
            img_path = obj.image.path  # Assuming your form saves the file in the Image model with a field called 'image'
            print("Image path:", img_path)
            img = plt.imread(img_path)
            print("Image shape:", img.shape)
            
            # Perform prediction
            # result = return_prediction(model, img)
            result_list = return_prediction_orange(img)
            result = result_list[0]

            # Return the results in the template
            return render(request, 'finalOrange.html', {"result": result})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "detection_orange.html", {"img": img, "form": form})


# Dragon Fruit Integration

classesDragon = ['Anthracnose', 'Bacterial Soft Rot', 'Fresh']
model_path_dragon = os.path.join(BASE_DIR, 'dragonfruit1.h5')
model_dragon = load_model(model_path_dragon)

def return_prediction_dragon(img):
    # Convert image to RGB if it's in RGBA format
    if img.shape[-1] == 4:  # Check if the image has 4 channels (RGBA)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
    # Preprocess the image
    img_size = (256, 256)  # Define the input size expected by your model
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    
    # Perform prediction
    pred = model_dragon.predict(img)
    index = np.argmax(pred)
    klass = classesDragon[index]
    
    return [klass]

@csrf_exempt  
def detection_dragonfruit(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            form.save()
            obj = form.instance
            
            # Read the image file from the form instance
            img_path = obj.image.path  
            img = plt.imread(img_path)
            
            # Perform prediction
            # result = return_prediction(model, img)
            result_list = return_prediction_dragon(img)
            result = result_list[0]

            # Return the results in the template
            return render(request, 'finalDragon.html', {"result": result})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "detection_dragonfruit.html", {"img": img, "form": form})


# Papaya Integration

classesPapaya = ['Anthracnose', 'Curl', 'Healthy', 'BacterialSpot', 'RingSpot']
model_path_papaya = os.path.join(BASE_DIR, 'papaya_model.h5')
model_papaya = load_model(model_path_papaya)

def return_prediction_papaya(img):
    # Convert image to RGB if it's in RGBA format
    if img.shape[-1] == 4:  # Check if the image has 4 channels (RGBA)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        
    # Preprocess the image
    img_size = (256, 256)  # Define the input size expected by your model
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    
    # Perform prediction
    pred = model_papaya.predict(img)
    index = np.argmax(pred)
    klass = classesPapaya[index]
    
    return [klass]

@csrf_exempt  
def detection_papaya(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the image
            form.save()
            obj = form.instance
            
            # Read the image file from the form instance
            img_path = obj.image.path  
            img = plt.imread(img_path)
            
            # Perform prediction
            # result = return_prediction(model, img)
            result_list = return_prediction_papaya(img)
            result = result_list[0]

            # Return the results in the template
            return render(request, 'finalPapaya.html', {"result": result})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "detection_papaya.html", {"img": img, "form": form})


def home(request):
    return render(request, 'home.html', {})

def diseases_papaya(request):
    return render(request, 'diseases_papaya.html', {})

def diseases_pomegranate(request):
    return render(request, 'diseases_pomegranate.html', {})

def diseases_orange(request):
    return render(request, 'diseases_orange.html', {})

def diseases_dragonfruit(request):
    return render(request, 'diseases_dragonfruit.html', {})

def diseases_tomato(request):
    return render(request, 'diseases_tomato.html', {})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Either username or password is incorrect')
        return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('home')

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Hey, {user} Your account has been created successfully! Please Login to continue.')
                return redirect('login')
        return render(request, 'signup.html', {'form': form})

def handler404(request, exception):
    return render(request, 'errorhandling.html', {})
