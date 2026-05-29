from fastapi import APIRouter, HTTPException
from app.schemas.integrate import IntegrateRequest
from app.services.parser import parse_infix_expression
from app.services.simplifier import integrate_linear_expression



router = APIRouter(
    prefix="/api",
    tags=["Integration Engine"]
)

@router.post("/integrate")
async def integrate_expression(payload: IntegrateRequest):
    try:
        ## STEP 1: EXPRESSION TREE CONSTRUCTION ##
        parsed_expression_tree = parse_infix_expression(payload.expression)
        
        ## STEP 2,3: LINEARITY & STANDARD FORM MATCHER ##
        integrated_expr = integrate_linear_expression(parsed_expression_tree)

        if integrated_expr is not None:
            return {
                "status": "success",
                "engine": "Linear Simplifier & Standard Forms",
                "integrated_result": str(integrated_expr)
            }
        
        return {
            "status": "pending",
            "engine": "Heuristic Goal Tree [Awaiting Implementation]",
            "integrated_result": f"Requires heuristic methods to solve: {parsed_expression_tree}"
        }
        
    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Core Fault: {str(e)}")