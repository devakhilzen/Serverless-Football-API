from fastapi import FastAPI, HTTPException
from google.cloud import firestore
from models import Fan
import requests

app=FastAPI()

db= firestore.Client()

@app.get("/club/{club_name}/")

async def get_clubs(club_name):

    try:
        club = db.collection("Clubs").document(club_name)
        doc = club.get()
        if doc.exists:
            return doc.to_dict()

        else:
            return ("club not found")

    
    except HTTPException:
        raise HTTPException(status_code=404,detail="not found")



@app.get("/players/{player}/")

async def get_players(player):
    try:
        name= db.collection("Players").document(player)
        name_doc= name.get()


        if name_doc.exists:
            return name_doc.to_dict()
        else:
            return ("not found")


    except HTTPException:
        raise HTTPException(status_code=404, detail="not found")





@app.get("/tactics/{tactics}/")
async def get_club_tacticts(tactics):
    try:
        name= db.collection("Club Tactics").document(tactics)
        name_doc= name.get()


        if name_doc.exists:
            return name_doc.to_dict()
        else:
            return ("not found")


    except HTTPException:
        raise HTTPException(status_code=404, detail="not found")
                                    


@app.post("/fans/")
async def post_comments(fan :Fan):

    try:
        doc_id = fan.fan_name
        comment= db.collection("Fan Comment").document(doc_id)
        comment.set(fan.dict())
        return ("Comment Added Successfully,", doc_id)

    except HTTPException:

        raise HTTPException(status_code= 500, detail= "Sorry an Error Occured")


