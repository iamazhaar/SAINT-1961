from pydantic import BaseModel



class IntegrateRequest(BaseModel):
    expr: str