from typing import List
from pydantic import BaseModel, Field


class Song(BaseModel):
    name: str

class SetGroup(BaseModel):
    song: List[Song] = Field(default_factory=list)

class Sets(BaseModel):
    set: List[SetGroup] = Field(default_factory=list)

class Setlist(BaseModel):
    sets: Sets

class SetlistSearchResponse(BaseModel):
    setlist: List[Setlist] = Field(default_factory=list)