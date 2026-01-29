# Disaster Response & Relief Coordination System

A Python implementation of an intelligent multi-agent system for detecting and responding to disaster events.

**Course:** DCIT 403 - Designing Intelligent Systems  
**Language:** Python | **Framework:** SPADE (Smart Python Agent Development Environment)

---

## Overview

This project implements a decentralized multi-agent system that:
- Detects disaster events in real-time
- Assesses damage severity
- Monitors multiple geographic locations simultaneously
- Logs all findings for analysis and response coordination

---

## Lab 1: Environment and Agent Platform Setup

**Objective**

Configure the Python agent development environment and deploy a basic agent.

**Background**

The Smart Python Agent Development Environment (SPADE) enables the creation of intelligent agents using asynchronous behaviors and message-based interaction over the Extensible Messaging and Presence Protocol (XMPP).

**Practical Tasks**

1. Launch the provided GitHub Codespaces environment
2. Verify Python and SPADE installation
3. Start the embedded XMPP server
4. Create agent credentials
5. Implement and execute a basic SPADE agent

**File:** `disaster_response/lab1_basic_agent_simple.py`

**Execution**

```bash
python3 disaster_response/lab1_basic_agent_simple.py
```

**Deliverables**

- Screenshot of running agent in GitHub Codespaces
- Python source code
- Environment setup report

---

## Lab 2: Perception and Environment Modeling

**Objective**

Implement agent perception of environmental and disaster-related events.

**Background**

Agents must sense their environment to guide decision-making and react to changes.

**Practical Tasks**

1. Implement a simulated disaster environment
2. Create a SensorAgent that periodically monitors conditions
3. Generate and log disaster events such as damage severity levels

**Files**

- `disaster_response/environment.py` — Simulated disaster environment
- `disaster_response/lab2_sensor_agent.py` — SensorAgent implementation

**Environment**

The system simulates a dynamic environment containing:

**Disaster Types:** Flood, Fire, Earthquake, Drought, Storm

**Severity Levels:** Low, Moderate, High, Critical, Catastrophic

**Monitored Locations:** Accra, Kumasi, Tema, Tamale, Cape Coast (Ghana)

**Event Parameters:**
- Location coordinates
- Casualty estimates
- Infrastructure damage percentage
- Required resources (medical supplies, food, water, rescue teams)

**Agent Perception**

Environmental sensing includes:
- Temperature monitoring
- Humidity measurement
- Wind speed detection
- Air quality index analysis
- Seismic activity measurement
- Water level monitoring
- Smoke detection

**Execution**

```bash
python3 disaster_response/lab2_sensor_agent.py
```

The system will deploy 3 sensor agents across different locations and monitor for 20 seconds. All detected events are saved to the `logs/` directory.

**Output Format**

**Text Logs** (`logs/SENSOR-001_log.txt`)
```
[10:52:08] SENSOR-001: Percept | Temp: 59°C | Wind: 27km/h | AQI: 215 | Humidity: 83%
[10:52:08] SENSOR-001: CRITICAL | Fire at Accra | Severity: CATASTROPHIC | People Affected: 109
```

**Event Data** (`logs/SENSOR-001_events.json`)
```json
{
  "event_id": "D0001",
  "disaster_type": "Fire",
  "location": "Accra",
  "severity": "CATASTROPHIC",
  "casualties": 66,
  "resources_needed": {
    "medical_kits": 77,
    "rescue_teams": 14
  }
}
```

**Deliverables**

- SensorAgent code
- Event logs (text format)
- Event data (JSON format)
- Brief explanation of percepts

---

## Project Structure

```
disaster_response/
├── lab1_basic_agent_simple.py    - Basic agent implementation
├── lab2_sensor_agent.py          - Sensor agent implementation
└── environment.py                - Environment simulation

logs/
├── SENSOR-001_log.txt            - Agent monitoring logs
├── SENSOR-001_events.json        - Detected events
└── ... (additional sensor logs)
```

---

## Core Agent Principles

**Autonomy:** Agents operate independently without continuous external control

**Reactivity:** Agents perceive and respond to environmental state changes

**Proactivity:** Agents take initiative in monitoring and initiating actions

**Concurrency:** Multiple agents execute simultaneously across different locations

---

## Implementation Approach

**Asynchronous Execution:** Uses Python's `asyncio` for concurrent agent operation

**Object-Oriented Design:** Clean separation of concerns with reusable components

**Data Persistence:** Dual logging approach—text format for human review, JSON for structured data processing

**Simulation Environment:** Controlled testing environment with realistic disaster scenarios

---


## Notes

**Simulation Mode:** This implementation uses simulation rather than full XMPP server integration to facilitate demonstration and testing. The agent principles remain applicable to distributed multi-agent systems.

**Randomization:** Disaster events are generated randomly to simulate unpredictable real-world conditions and test agent response to unexpected scenarios.

---

## Author

Bernard Owusu-Dankwah  
January 29, 2026
