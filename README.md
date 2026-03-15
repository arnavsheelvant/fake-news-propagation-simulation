# Modeling Fake News Spread and Containment in Social Networks

This project implements an agent-based simulation to analyze how misinformation propagates through social networks and how interventions such as fact-checking and immune users affect its spread.

The simulator models realistic social media behavior using graph-based network structures and probabilistic information diffusion dynamics.

---

## Problem Motivation

Fake news spreads rapidly on social media, often faster than verified information.  
Echo chambers and repeated exposure to misinformation can distort public understanding and influence decision-making.

This project explores how network structure and intervention strategies affect misinformation spread.

---

## Methodology

A social network with **N users** is generated using three classical network models:

- Erdős–Rényi (random networks)
- Watts–Strogatz (small-world networks)
- Barabási–Albert (scale-free networks)

Each node represents a user and can exist in one of five states:

```
0 → Unreached  
1 → Real information  
2 → Fake information  
3 → Fact-checker  
4 → Immune
```

Information spreads according to probabilistic transmission rules:

- Fake → Unreached: first share = 1, subsequent shares = \(p_f\)
- Real → Unreached: probability \(p_r\)
- Fact-checkers convert fake nodes with probability \(p_c\)

Additional behavioral constraints include:

- forwarding limits
- immune users resistant to misinformation
- intervention by fact-checking agents

---

## Metrics Tracked

The simulation records several propagation metrics:

- Fake news prevalence over time  
- Real information adoption rate  
- Convergence step of the network  
- Peak misinformation percentage  

Key equations:

```
Fake%(t) = (F_t / N) × 100
Real%(t) = (R_t / N) × 100
```

---

## Technologies Used

- Python
- NetworkX
- NumPy
- FastAPI
- Matplotlib / Seaborn

---

## Example Applications

- Studying misinformation containment strategies
- Evaluating fact-checking interventions
- Understanding echo chamber dynamics
- Designing safer social media information systems

---

## Future Improvements

- Multi-layer social networks
- Temporal interaction graphs
- Reinforcement learning intervention policies
