# Sentiment Analysis Web App

### **Overview**

This project is a **Sentiment Analysis Web Application** built using **Flask** and **TextBlob**. It analyzes user-entered text to determine the sentiment (Positive, Negative, or Neutral) and provides detailed insights such as polarity and subjectivity scores.

### **Features**

- **Sentiment Classification**: Classifies text into Positive, Negative, or Neutral.
- **Polarity Score**: Measures how positive or negative the text is (range: -1 to +1).
- **Subjectivity Score**: Measures how subjective or objective the text is (range: 0 to 1).
- **Interactive UI**: Modern, responsive design with real-time feedback.
- **Error Handling**: Displays warnings for empty input.
- **Character & Word Counter**: Tracks input length dynamically.

### **Tech Stack**

- **Backend**: Python 3.10+, Flask, TextBlob
- **Frontend**: HTML, CSS, Bootstrap, Font Awesome

### **How It Works**

1. **User Input**: Enter text in the provided textarea.
2. **Analyze Sentiment**: Click the "Analyze" button to process the text.
3. **Results Display**:
   - Sentiment label (Positive/Negative/Neutral) with emoji indicators.
   - Polarity and subjectivity scores with progress bars.
   - Interpretation of the sentiment.
4. **Clear Input**: Use the "Clear" button to reset the form.

### **Project Structure**

```
Sentiment-Analysis-Web-App/
├── app.py                # Flask application
├── requirements.txt      # Dependencies
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── style.css         # Custom styles
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

### **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/VipulMadavi/Sentiment-Analysis-Web-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Sentiment-Analysis-Web-App
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Download TextBlob corpora:
   ```bash
   python -m textblob.download_corpora
   ```
6. Run the application:
   ```bash
   python app.py
   ```
7. Open the app in your browser:
   ```
   http://127.0.0.1:5000/
   ```

### **Sample Inputs & Outputs**

| Input Text                     | Sentiment | Polarity | Subjectivity |
| ------------------------------ | --------- | -------- | ------------ |
| "I love this project!"         | Positive  | 0.85     | 0.75         |
| "This is the worst experience" | Negative  | -0.9     | 0.8          |
| "This is a notebook."          | Neutral   | 0.0      | 0.1          |

### **Future Enhancements**

- Add multi-language support.
- Deploy the app to a cloud platform (e.g., Render, Railway).
- Implement an API endpoint for programmatic access.
- Add session-based history tracking.

### **Acknowledgments**

This project was developed as part of the internship submission for **QSkills**. Special thanks to the mentors and the QSkills team for their guidance and support.

---

**Submitted By**: Vipul Madavi  
**Date**: January 28 , 2026
