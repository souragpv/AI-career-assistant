from flask import Flask, request, jsonify
from utils.gemini_helper import get_gemini_response
from utils.prompts import *

app = Flask(__name__)

@app.route("/api/resume-review", methods=["POST"])
def resume_review():
    data = request.json
    prompt = resume_review_prompt(data["resume_text"])
    result = get_gemini_response(prompt)
    return jsonify({"feedback": result})

@app.route("/api/interview-prep", methods=["POST"])
def interview_prep():
    data = request.json
    prompt = interview_prep_prompt(data["job_role"])
    result = get_gemini_response(prompt)
    return jsonify({"questions": result})

@app.route("/api/roadmap", methods=["POST"])
def roadmap():
    data = request.json
    prompt = roadmap_prompt(data["goal"])
    result = get_gemini_response(prompt)
    return jsonify({"roadmap": result})

@app.route("/api/jd-analysis", methods=["POST"])
def jd_analysis():
    data = request.json
    prompt = job_description_prompt(data["jd_text"], data["resume_text"])
    result = get_gemini_response(prompt)
    return jsonify({"analysis": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)