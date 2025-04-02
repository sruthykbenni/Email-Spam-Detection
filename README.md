# Email Spam Detection using NLP and Naive Bayes

## Overview
This project is a **Spam Detection System** that leverages **Natural Language Processing (NLP)** and **Naive Bayes Classification** to classify emails as spam or legitimate. The model is deployed using **Streamlit**, allowing users to input email text and get real-time predictions.

## Features
- **Text Preprocessing:** Tokenization, stopword removal, and vectorization using CountVectorizer.
- **Naive Bayes Classifier:** A probabilistic approach for effective spam classification.
- **Machine Learning with Scikit-learn:** Training and evaluation of the model for high accuracy.
- **Interactive Web Application:** Built using **Streamlit** for easy user interaction.

## Technologies Used
- **Python**
- **Natural Language Processing (NLP)**
- **Scikit-learn**
- **Pandas & NumPy**
- **Streamlit**

## Installation
To run this project locally, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/sruthykbenni/email-spam-detection.git
cd email-spam-detection
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Streamlit App**
```bash
streamlit run app.py
```

## Dataset
The project uses the **Spam/Ham dataset** from UCI Machine Learning Repository. The dataset contains:
- **Label:** 'spam' or 'ham' (legitimate)
- **Message:** The actual email text

## Model Training
The model follows these steps:
1. **Data Cleaning:** Removing duplicates and converting text to lowercase.
2. **Text Processing:** Removing punctuation, tokenization, and vectorization using CountVectorizer.
3. **Splitting Data:** 80% for training and 20% for testing.
4. **Training the Model:** Using the **Multinomial Naive Bayes** algorithm.
5. **Evaluating the Model:** Checking accuracy, precision, and recall.

## Deployment
The application is deployed on **Streamlit Cloud**. You can access the live demo here:  
[🔗 Live App](https://email-spam-detection-e8qufw5fj7tvsyujubgynj.streamlit.app/)

## Usage
1. Open the web app.
2. Enter or paste an email message.
3. Click on **'Predict'** to check if it's spam or legitimate.

## Future Improvements
- Adding support for deep learning models (e.g., LSTMs or BERT).
- Implementing real-time email scanning using APIs.
- Enhancing the UI with better visualizations.

## Contributing
Feel free to contribute! Fork the repository, make your changes, and submit a pull request.
