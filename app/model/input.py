from pydantic import BaseModel


class DataRequest(BaseModel):
    method: str
    text: str
