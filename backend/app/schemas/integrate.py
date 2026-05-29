from pydantic import BaseModel



class IntegrateRequest(BaseModel):
    expression: str