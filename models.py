from pydantic import BaseModel

class Fan (BaseModel):
    fan_name : str
    fav_club : str
    best_match : str
    comment : str
    