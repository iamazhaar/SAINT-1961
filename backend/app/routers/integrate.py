from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Initialize the router. We add a prefix so all routes in this file start with /api
router = APIRouter(
    prefix="/api",
    tags=["Integration Engine"]
)

# Define the structured data contract the frontend must follow
class IntegrationRequest(BaseModel):
    expression: str

@router.post("/integrate")
async def perform_integration(payload: IntegrationRequest):
    user_input = payload.expression.strip()
    
    if not user_input:
        raise HTTPException(status_code=400, detail="Mathematical expression cannot be empty.")
        
    # Tracer Bullet Strategy: Mocking responses to match the screenshot example
    # This allows you to build the frontend interface completely before finishing the math parser
    if "x^2" in user_input and "sin" in user_input:
        mock_result = "-x^2 * cos(x) + 2*x * sin(x) + 2 * cos(x) + C"
    elif "x^2" in user_input:
        mock_result = "(1/3) * x^3 + C"
    elif "sin" in user_input:
        mock_result = "-cos(x) + C"
    else:
        mock_result = f"∫({user_input})dx ➔ [SAINT Heuristic Solver Template Ready]"
        
    return {
        "status": "success",
        "input_expression": user_input,
        "integrated_result": mock_result,
        "engine": "SAINT-1961-Core"
    }