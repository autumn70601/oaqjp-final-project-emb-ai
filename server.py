"""Module providing an emotion detector."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """sent_analyzer"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    # Return a formatted string with the result
    # pylint: disable=line-too-long
    return "For the given statement, the system response is " + str(response)[1:108] + ". The dominant emotion is " + str(response['dominant_emotion']) +"."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
