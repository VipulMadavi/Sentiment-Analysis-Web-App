from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text: str):
    """
    Analyze sentiment of the given text using TextBlob.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing polarity, subjectivity, and sentiment label
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2),
        "label": label
    }


@app.route("/", methods=["GET"])
def home():
    """Render the home page with input form."""
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyze sentiment of user-entered text.
    
    Returns:
        Rendered template with analysis results or error message
    """
    text = request.form.get("text", "").strip()

    if not text:
        return render_template("index.html", error="Please enter some text.")

    result = analyze_sentiment(text)

    return render_template(
        "index.html",
        input_text=text,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
