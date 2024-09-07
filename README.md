# Football API

This project is a serverless API for retrieving football club and player information, built using FastAPI, Firestore, and Google Cloud Platform (GCP). It includes endpoints for getting details on football clubs, players, and tactics, as well as a fan comment submission system.

## Features
- Get detailed information about football clubs, including key players and tactics.
- Retrieve player statistics such as goals, assists, and appearances.
- Submit fan comments related to clubs and players.
- Integrated with Google Cloud Storage for handling images and Firestore for managing data.
- Streamlit front-end for a user-friendly interface.

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)
- Google Cloud SDK installed and set up
- Git installed
- FastAPI installed (`pip install fastapi`)
- Streamlit installed (`pip install streamlit`)
- Firestore Client Library (`pip install google-cloud-firestore`)
- Firebase setup for Firestore (NoSQL database)
- Google Cloud Storage (for images)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/football-api.git
   cd football-api

2. **Set up a virtual environment**:
   python3 -m venv football
   source football/bin/activate

3. Install dependencies:

	pip install -r requirements.txt

4. Run the FastAPI app:

   uvicorn main:app --reload

5. Run the Streamlit front-end:

   streamlit run app.py


## API Endpoints
 
GET /clubs
Fetch a list of all football clubs.

GET /players
Fetch a list of all players with statistics.

GET /club_tactics/{club_id}
Retrieve tactical information for a specific club.

POST /fan_comment
Submit a comment from a fan.


## Contributing

1. Fork the repository.
2. Create a new branch:
	git checkout -b feature-branch
3. Make your changes and commit:
	git commit -m "Your message"
4. Push to your branch:
	git push origin feature-branch
5. Create a pull request.
