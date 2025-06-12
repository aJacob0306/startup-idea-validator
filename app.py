from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
import re
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    feedback = ""
    if request.method == "POST":
        idea = request.form["idea"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a startup idea validator. Rate the idea from 1 to 10 and explain why."},
                {"role": "user", "content": idea}
            ]
        )

        feedback = response.choices[0].message.content
        score_match = re.search(r"\b([1-9]|10)\s*/\s*10\b", feedback)
        score = score_match.group(0) if score_match else "N/A"

        with open("history.txt", "a") as f:
            f.write(f"\n--- {datetime.now()} ---\n")
            f.write(f"Idea: {idea}\nFeedback: {feedback}\n")

    return render_template("index.html", feedback=feedback, score=score)
if __name__ == "__main__":
    app.run(debug=True)


