# Fake News Spread Simulator

*A Social Computing Course Project — Semester 5*

This project simulates how fake news and real news spread through a social network.
It allows users to adjust parameters (probabilities, network size, interventions) and visualize diffusion over time using an animated graph.

---

## Features

###  Interactive Controls

* Fake news spread probability
* Real news spread probability
* Network size
* Fact-checker toggle
* Forward limit toggle

###  Network Visualization

* vis-network interactive graph
* Node states:

  * **Gray** — Unreached
  * **Green** — Real news
  * **Red** — Fake news
  * **Purple** — Immune
  * **Blue** — Fact-Checker

###  Simulation Statistics

* Fake reach percentage
* Real reach percentage
* Number of time steps
* Peak fake spread
* Final state distribution

---

## Tech Stack

### **Frontend**

* HTML, CSS, JavaScript
* vis-network.js

### **Backend**

* Python
* FastAPI
* NetworkX
* Matplotlib

---

## 📁 Folder Structure

```
/project-root
│
├── backend/
│   ├── main.py
│   ├── simulation.py
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
