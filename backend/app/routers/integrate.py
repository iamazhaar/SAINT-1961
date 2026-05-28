from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.parser import string_to_saint_tree, inspect_structure
from app.services.simplifier import integrate_linear_expression

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
        

        # Step 3: Pass the tree into the Linear Simplifier (which calls the Matcher automatically [Step 2])
        integrated_expr = integrate_linear_expression(parsed_tree)

        if integrated_expr is not None:
            return {
                "status": "success",
                "engine": "Linear Simplifier & Standard Forms",
                "integrated_result": str(integrated_expr)
            }
        
        return {
            "status": "pending",
            "engine": "Heuristic Goal Tree [Awaiting Implementation]",
            "integrated_result": f"Requires heuristic methods to solve: {parsed_tree}"
        }
        
    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Core Fault: {str(e)}")