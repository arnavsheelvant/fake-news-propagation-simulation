# Fake News Propagation Simulator

Agent-based simulation of misinformation diffusion in social networks using graph-based models.

Developed as part of the **Social Computing course (Mahindra University, Semester 5)**.

---

## Overview

Misinformation spreads rapidly across social media platforms, often faster than verified information.  
Echo chambers and repeated exposure amplify the spread, making misinformation difficult to contain.

This project implements a **network-based simulation framework** that models how fake and real information propagate through different social network structures and how interventions such as fact-checking influence diffusion dynamics.

---

## Network Models

The simulator generates synthetic social networks using classical graph models:

- **Erdős–Rényi (Random Graph)**
- **Watts–Strogatz (Small-World Network)**
- **Barabási–Albert (Scale-Free Network)**

These models capture different patterns of real-world social connectivity.

---

## Node States

Each node represents a social media user and can be in one of five states:

| State | Meaning |
|------|--------|
| Gray | Unreached |
| Green | Real Information |
| Red | Fake Information |
| Blue | Fact-Checker |
| Purple | Immune |

---

## Diffusion Model

Information spreads through probabilistic transitions between nodes.

Key parameters:

- **p_fake** — fake news transmission probability  
- **p_real** — real news transmission probability  
- **p_c** — fact-checker conversion probability  
- **F** — number of fact-checkers  
- **I** — number of immune users  
- **L** — forwarding limit per user  

Example transition rules:

Fake → Unreached  
First share: probability = 1  
Subsequent shares: probability = p_fake  

Real → Unreached  
Probability = p_real  

Fact-checker → Fake  
Conversion probability = p_c  

---

## Metrics Tracked

The simulation records diffusion statistics across time steps:

- Fake news prevalence
- Real information adoption
- Peak misinformation spread
- Convergence step of the network
- Final distribution of node states

Key metrics:
│   ├── metrics.py
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## How the Simulation Works

1. The user chooses parameters from the UI.
2. Frontend sends parameters to `/simulate` via POST.
3. Backend:

   * Generates a network (random, small-world, or scale-free)
   * Assigns initial states to nodes
   * Simulates spread step-by-step
   * Tracks statistics
4. Backend returns:

   * Network structure
   * Timeline of node states
   * Stats
5. Frontend animates the graph and updates stats.

---

## Running the Project

### **1️Backend Setup**

Inside `/backend`:

```bash
pip install fastapi uvicorn networkx matplotlib
uvicorn main:app --reload --port 8000
```

Visit:
[http://localhost:8000/](http://localhost:8000/)
(You should see: `{ "message": "Backend running" }`)

---

### **2️Frontend Setup**

#### Option A — Simple

Open `frontend/index.html` in a browser.

#### Option B — Recommended (Local Server)

```bash
cd frontend
python -m http.server 5500
```

Visit:
[http://localhost:5500/](http://localhost:5500/)

---

## Testing the Simulator

1. Adjust sliders (p_fake, p_real, network size)
2. Enable/disable interventions
3. Click **Start Simulation**
4. Watch nodes animate over time
5. View updated stats in panel

Try experimenting with:

* High fake probability
* Fact-checkers ON vs OFF
* Large vs small networks
* Forward limit changes

---

## Team BallBusters

* **Manogna** — UI/UX, frontend, backend and frontend integration
* **Anushka** — Spread model logic, research
* **Arnav** — Data analysis, simulation metrics
* **Manjari** — Backend implementation, hosting

---

## License

Academic project (Mahindra University — Social Computing Course, 2025)
