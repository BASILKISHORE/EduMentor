# EduMentor: Your Personalized Learning Companion with Azure

## Project Overview
**EduMentor** is a Python-based AI agent built for the **AI Agents Hackathon** (Python track). It leverages **Azure Blob Storage** for content storage and **Azure Functions** for agent processing, delivering personalized study plans, curated resources, and motivational feedback in a cloud-based environment.

### The Challenge
Education lacks scalable, personalized tools, especially for diverse student needs, often requiring complex infrastructure.

### Our Solution
EduMentor uses a cloud-native approach:
- **Content Retriever Agent**: Fetches resources from Azure Blob Storage.
- **Learning Planner Agent**: Generates study schedules via Azure Functions.
- **Motivator Agent**: Provides feedback, also hosted on Azure Functions.
The Flask web app orchestrates these agents, accessible at `http://localhost:5000` (or deployed URL).

### Why It’s Innovative
- **Cloud Integration**: Utilizes Azure for scalability and reliability.
- **Agentic Design**: Separates agent logic into independent Functions.
- **Accessible Data**: Blob Storage ensures content is centrally managed.

### Impact
EduMentor scales education personalization, benefiting students and teachers with a robust, cloud-backed solution.

### Usability
- **Real-World Fit**: Supports large-scale educational deployments.
- **Practical Features**: Web interface with cloud-powered agents.
- **Scalability**: Azure ensures performance under load.

### Technical Quality
- **Repository**: [EduMentor GitHub](https://github.com/yourusername/EduMentor) (replace with your link).
- **Codebase**: Python with Azure integration, including tests.
- **Documentation**: Comprehensive README and setup guide.
- **Architecture Diagram**: Included (see below).
- **Implementation**: Azure Functions and Blob Storage for agent and data management.

### Architecture
- **Frontend**: Flask web app.
- **Agents**: Azure Functions (retrieveContent, generateStudyPlan, motivateUser).
- **Storage**: Azure Blob Storage for educational content.
- **Flow**: User input → Azure Functions → Blob Storage → Response.

**Architecture Diagram**:
![EduMentor Architecture](architecture_diagram.png)

### Demo Video
Our 3-minute demo video ([demo_video.mp4](https://github.com/yourusername/EduMentor/demo_video.mp4)) demonstrates:
- A student querying, “Help me study for physics.”
- Retrieval from Azure Blob Storage.
- A study plan from an Azure Function.
- Motivational feedback displayed.
- Teacher interface interaction.

### Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` with Azure endpoints and SAS token (see README).
3. Deploy to Azure using `deploy_azure.sh` (requires Azure CLI).
4. Run locally (simulation): Set `AZURE_FUNCTION_ENDPOINT` to `http://localhost:7071/api` and run `python app.py`.
5. Access at `http://localhost:5000`.

### Future Plans
- Add Azure Cosmos DB for user profiles.
- Implement real-time analytics with Azure Monitor.
- Expand to multiple languages.

---

**Team**: Solo developer  
**Contact**: Reach out via GitHub issues or email (your.email@example.com).