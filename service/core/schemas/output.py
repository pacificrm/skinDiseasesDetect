from pydantic import BaseModel

class APIOutput(BaseModel):
    disease:str 
    time: str