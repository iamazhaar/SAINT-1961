from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.parser import string_to_saint_tree, inspect_structure
from app.services.matcher import match_standard_form

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
        
        # ======== For Testing Purpose ==============
        # Print structural breakdown to your backend terminal terminal for debugging
        print(f"\n[SAINT] Received Raw Text: {payload.expression}")
        print(f"[SAINT] Internal Structural Tree: {inspect_structure(parsed_tree)}")
        # ======================================================================
        

        # Step 2: Attempt Immediate Standard Form Match
        integrated_expr = match_standard_form(parsed_tree)

        if integrated_expr is not None:
            # Successfully hit a standard form! Convert back to string for the frontend.
            return {
                "status": "success",
                "engine": "Standard Form Matcher",
                "integrated_result": str(integrated_expr)
            }
        
        # If we reach here, it failed Step 2 and needs Heuristics (Step 3/4)
        return {
            "status": "pending",
            "engine": "Heuristic Goal Tree [Awaiting Implementation]",
            "integrated_result": f"Could not immediately integrate: {parsed_tree}"
        }
        
    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Core Fault: {str(e)}")