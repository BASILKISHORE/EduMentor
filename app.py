"""
EduMentor: AI-Powered Educational Assistant with Azure
Main application script orchestrating agents via Azure Functions and Blob Storage.
"""

import os
import requests
import asyncio
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Azure configuration (to be set in .env)
AZURE_FUNCTION_ENDPOINT = os.getenv("AZURE_FUNCTION_ENDPOINT", "http://localhost:7071/api")
AZURE_BLOB_STORAGE_URL = os.getenv("AZURE_BLOB_STORAGE_URL", "https://yourstorageaccount.blob.core.windows.net/content")
AZURE_BLOB_SAS_TOKEN = os.getenv("AZURE_BLOB_SAS_TOKEN", "")

async def call_azure_function(function_name: str, data: dict) -> dict:
    """Call an Azure Function with the given data."""
    url = f"{AZURE_FUNCTION_ENDPOINT}/{function_name}"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route("/")
def index():
    """Render the main student interface."""
    return render_template("index.html")

@app.route("/admin")
def admin():
    """Render the teacher admin interface."""
    return render_template("admin.html")

@app.route("/query", methods=["POST"])
async def process_query():
    """Handle user queries and orchestrate agent responses via Azure Functions."""
    try:
        data = request.json
        user_id = data.get("user_id", "default_user")
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query is required"}), 400

        # Call Azure Functions for each agent
        tasks = {
            "content": call_azure_function("retrieveContent", {"query": query}),
            "plan": call_azure_function("generateStudyPlan", {"user_id": user_id, "query": query}),
            "motivation": call_azure_function("motivateUser", {"content": query})
        }
        results = await asyncio.gather(*(tasks.values()), return_exceptions=True)

        response = {
            "content": results[0].get("content", ["Error retrieving content"]) if not isinstance(results[0], Exception) else ["Service unavailable"],
            "study_plan": results[1].get("plan", "Error generating plan") if not isinstance(results[1], Exception) else "Service unavailable",
            "motivation": results[2].get("motivation", "Error generating motivation") if not isinstance(results[2], Exception) else "Service unavailable"
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)