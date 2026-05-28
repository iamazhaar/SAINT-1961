from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import integrate  # Import your new route module

app = FastAPI(
    title="SAINT AI Backend",
    description="Modern reconstruction of James R. Slagle's 1961 Symbolic Automatic INTegrator",
    version="1.0.0"
)

# Configure Cross-Origin Resource Sharing (CORS) for your React frontend
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # Allows all headers
)

# Register the integrate router into the core FastAPI app
app.include_router(integrate.router)

@app.get("/")
def home():
    return {"status": "online", "message": "SAINT Core System Operational"}