from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import simulation + conversion utilities
from simulation import run_simulation
from metrics import build_frontend_payload

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/simulate")
async def simulate(payload: dict):

    sim_result = run_simulation(payload)

    output = build_frontend_payload(sim_result)
    return output
