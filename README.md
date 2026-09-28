# Autonomous AI Agent-to-Agent Service Escrow Primitive

## Overview
This repository contains a production-ready **GenLayer Intelligent Contract** designed for autonomous **Agent-to-Agent (A2A)** B2B service transactions.

As AI agents become economic actors, they require trustless mechanisms to contract, deliver, and settle payments for digital services. This contract enables Buyer Agents to lock escrow funds, Seller Agents to deliver work via API endpoints, and GenLayer validators to verify service compliance via live web consensus before releasing funds.

## Key Architecture
- **Escrow Fund Locking:** Secures funds until execution requirements are fulfilled.
- **Web-Enabled Consensus:** GenLayer validators independently query off-chain URLs/deliverables to verify quality and correctness against the contract spec.
- **Automatic Settlement:** Funds are released or refunded autonomously based on validator equivalence checks.

## Repository Contents
- `contract.py`: The core GenLayer Intelligent Contract implementation.
- `test_contract.py`: Pytest suite verifying execution paths and state transitions.
- `index.html`: Interactive Web Dashboard for visualizing agent-to-agent transactions.

## How to Run & Test
1. Run local contract simulation:
   ```bash
   python contract.py
