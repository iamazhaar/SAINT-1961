from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.parser import string_to_saint_tree, inspect_structure

# Initialize the router. We add a prefix so all routes in this file start with /api
router = APIRouter(
    prefix="/api",
    tags=["Integration Engine"]
)

# Define the structured data contract the frontend must follow
class IntegrationRequest(BaseModel):
    expression: str

@router.post("/integrate")
async def integrate_expression(payload: IntegrationRequest):
    try:
        # Step 1: Parse string to internal expression structure
        parsed_tree = string_to_saint_tree(payload.expression)
        
        # Print structural breakdown to your backend terminal terminal for debugging
        print(f"\n[SAINT] Received Raw Text: {payload.expression}")
        print(f"[SAINT] Internal Structural Tree: {inspect_structure(parsed_tree)}")
        
        # Placeholder for Step 2/3/4 - right now returning the parsed math back
        return {"integrated_result": f"Parsed successfully as structural tree: {str(parsed_tree)}"}
        
    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal processing fault inside SAINT core.")