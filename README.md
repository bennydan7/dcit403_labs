# Disaster Response & Relief Coordination System
## Laboratory Sessions 1 & 2

**Course:** Intelligent Agent Systems  
**Programming Language:** Python  
**Agent Framework:** SPADE (Smart Python Agent Development Environment)  
**Platform:** GitHub Codespaces

---

## Project Overview

This project implements a decentralized intelligent multi-agent system for disaster response and relief coordination. The system uses autonomous agents to detect disaster events, assess damage severity, and coordinate response operations under conditions of uncertainty and limited resources.

---

## Lab 1: Environment and Agent Platform Setup

### Objective
Configure the Python agent development environment and deploy a basic intelligent agent.

### Implementation Details

**File:** `disaster_response/lab1_basic_agent_simple.py`

The basic agent demonstrates:
- Agent lifecycle management (setup → start → stop)
- One-shot behaviors (execute once)
- Periodic/cyclic behaviors (execute repeatedly)
- Autonomous operation without external control

### Key Components

1. **Agent Class:** `SimulatedAgent`
   - Manages agent state and behaviors
   - Implements setup and lifecycle methods

2. **Behaviors:**
   - `hello_behaviour()`: Executes once at startup
   - `periodic_behaviour()`: Executes every 2 seconds (5 iterations)

3. **Features Demonstrated:**
   - Asynchronous execution using `asyncio`
   - Timestamped logging
   - Self-termination after task completion

### Running Lab 1

```bash
cd /workspaces/codespaces-blank
python3 disaster_response/lab1_basic_agent_simple.py
```

### Expected Output

The agent will:
1. Display startup information
2. Execute the hello behavior once
3. Perform 5 periodic checks (every 2 seconds)
4. Stop automatically
5. Display summary of demonstrated concepts

---

## Lab 2: Perception and Environment Modeling

### Objective
Implement agent perception of environmental and disaster-related events through a simulated disaster environment.

### Implementation Details

#### Files Created:

1. **`disaster_response/environment.py`** - Disaster Environment Simulator
   - Simulates dynamic disaster scenarios
   - Models environmental conditions
   - Generates random disaster events

2. **`disaster_response/lab2_sensor_agent.py`** - Sensor Agent Implementation
   - Monitors environmental conditions
   - Detects disaster events
   - Logs sensor readings and events

### Environment Components

#### DisasterType Enum
- FLOOD
- EARTHQUAKE
- FIRE
- DROUGHT
- STORM

#### Severity Levels
- LOW (1)
- MODERATE (2)
- HIGH (3)
- CRITICAL (4)
- CATASTROPHIC (5)

#### Location Class
Represents geographical locations with:
- Latitude and longitude coordinates
- Location name
- Ghanaian cities: Accra, Kumasi, Tema, Tamale, Cape Coast

#### DisasterEvent Class
Complete disaster event representation:
- Event ID
- Disaster type
- Location
- Severity level
- Timestamp
- Affected area (km²)
- Casualties count
- Infrastructure damage percentage
- Required resources (medical kits, food, water, rescue teams)

#### EnvironmentPercept Class
Sensor readings that agents perceive:
- Temperature (°C)
- Humidity (%)
- Wind speed (km/h)
- Air quality index (AQI)
- Seismic activity (Richter scale)
- Water level (meters above normal)
- Smoke detection (boolean)
- Active disasters list

### SensorAgent Capabilities

#### Perception
- Reads environmental conditions at assigned location
- Samples every 3 seconds (configurable)

#### Analysis
- Detects anomalies:
  - High temperature (> 40°C)
  - Strong winds (> 60 km/h)
  - Poor air quality (> 200 AQI)
  - Seismic activity (> 3.0 magnitude)
  - Water level rise (> 0.5m)
  - Smoke detection

#### Event Detection
- Identifies new disaster events
- Prevents duplicate alerts
- Logs all detections

#### Logging System
- Text logs: `logs/SENSOR-XXX_log.txt`
  - Timestamped entries
  - Percept readings
  - Anomaly detections
  - Disaster alerts with people affected and resources needed
  
- JSON events: `logs/SENSOR-XXX_events.json`
  - Structured disaster data
  - Complete event metadata
  - Resources needed tracking

#### Alert System
- CRITICAL alerts for high-severity disasters
- WARNING alerts for lower-severity events

### Running Lab 2

```bash
cd /workspaces/codespaces-blank
python3 disaster_response/lab2_sensor_agent.py
```

### Expected Output

The simulation will:
1. Create a disaster environment
2. Deploy 3 sensor agents to different locations
3. Monitor for 20 seconds
4. Detect and log any disasters that occur
5. Generate log files and event JSON files
6. Display agent summaries

### Generated Deliverables

#### Log Files (in `logs/` directory):
- `SENSOR-001_log.txt` - Accra monitoring log
- `SENSOR-002_log.txt` - Kumasi monitoring log
- `SENSOR-003_log.txt` - Tema monitoring log
- `SENSOR-XXX_events.json` - Detected disaster events (JSON format)

#### Example Log Entry:
```
[10:52:08] SENSOR-001: Percept | Temp: 59°C | Wind: 27km/h | AQI: 215 | Humidity: 83%
[10:52:08] SENSOR-001: CRITICAL | Fire at Accra | Severity: CATASTROPHIC | People Affected: 109 | Resources: 13 teams
```

#### Example Event JSON:
```json
{
  "event_id": "D0001",
  "disaster_type": "Fire",
  "location": "Accra (5.6037, -0.1870)",
  "severity": "CATASTROPHIC",
  "timestamp": "2026-01-29T08:52:12.598281",
  "affected_area_km2": 5.18,
  "casualties": 66,
  "infrastructure_damage_pct": 50.28,
  "resources_needed": {
    "medical_kits": 77,
    "food_packages": 292,
    "water_bottles": 386,
    "rescue_teams": 14
  },
  "detected_by": "SENSOR-003"
}
```

---

## Environment Setup Details

### Prerequisites Installed

1. **Python:** Version 3.12.1 ✓
2. **SPADE Framework:** Version 4.1.2 ✓
3. **Prosody XMPP Server:** Installed and configured ✓

### Installation Commands Used

```bash
# Verify Python
python3 --version

# Install SPADE
pip install spade

# Install Prosody XMPP Server
sudo apt update
sudo apt install -y prosody

# Start Prosody service
sudo service prosody start

# Create agent credentials
sudo prosodyctl register testadmin localhost testpass123
sudo prosodyctl register sensor localhost sensor123
sudo prosodyctl register coordinator localhost coord123
sudo prosodyctl register rescue localhost rescue123
sudo prosodyctl register logistics localhost logis123
```

### Project Structure

```
/workspaces/codespaces-blank/
├── disaster_response/
│   ├── environment.py                  # Environment simulation
│   ├── lab1_basic_agent_simple.py     # Lab 1 implementation
│   ├── lab1_basic_agent.py            # Lab 1 (SPADE version)
│   └── lab2_sensor_agent.py           # Lab 2 implementation
├── logs/
│   ├── SensorAgent_1_log.txt          # Agent logs
│   ├── SensorAgent_2_log.txt
│   ├── SensorAgent_3_log.txt
│   └── SensorAgent_X_events.json      # Event data
└── README.md                           # This file
```

---

## Key Concepts Demonstrated

### Lab 1
✓ Agent creation and initialization  
✓ Agent lifecycle management  
✓ One-shot behavior execution  
✓ Periodic/cyclic behavior execution  
✓ Autonomous operation without external control  

### Lab 2
✓ Environment simulation with dynamic disasters  
✓ Agent perception through sensors  
✓ Periodic monitoring behavior  
✓ Event detection and classification  
✓ Multiple agents operating concurrently  
✓ Agent autonomy in disaster detection  
✓ Data persistence (logging)  
✓ Anomaly detection  

---

## Agent-Oriented Design Principles Applied

1. **Autonomy:** Agents operate independently without constant human control
2. **Reactivity:** Agents perceive and respond to environmental changes
3. **Proactivity:** Agents take initiative in monitoring and detecting disasters
4. **Temporal Continuity:** Agents run continuously over time

---

## Technical Highlights

### Asynchronous Programming
- Used Python's `asyncio` for concurrent agent execution
- Multiple agents monitoring different locations simultaneously

### Object-Oriented Design
- Clean separation of concerns
- Reusable components (Environment, Agent, Percept)
- Dataclasses for structured data

### Logging and Persistence
- Text logs for human readability
- JSON files for machine processing
- Timestamped entries for audit trail

---

## Future Extensions (Labs 3+)

The foundation laid in Labs 1 & 2 enables:
- **Lab 3:** Inter-agent communication (FIPA-ACL)
- **Lab 4:** Coordinator agents for task allocation
- **Lab 5:** Rescue agents with action capabilities
- **Lab 6:** Logistics agents for resource management
- **Lab 7:** Multi-agent coordination and negotiation
- **Lab 8:** System evaluation and performance metrics

---

## Notes

### Simulation Mode
The current implementation uses simulation mode instead of full SPADE/XMPP integration for easier demonstration. The core agent concepts remain valid and can be extended to full SPADE agents when XMPP connectivity is required.

### Randomization
Disaster generation is random for demonstration purposes. The 10% probability per environment update creates dynamic, unpredictable scenarios similar to real-world uncertainty.

---

## Author

**Laboratory Manual:** Intelligent Agent Systems Course  
**Implementation Date:** January 29, 2026  
**Platform:** GitHub Codespaces  
**Development Environment:** Ubuntu 24.04.3 LTS  

---

## Assessment Criteria Met

### Lab 1 Deliverables
✓ Screenshot of running agent (console output captured)  
✓ Python source code (lab1_basic_agent_simple.py)  
✓ Environment setup report (this document)  

### Lab 2 Deliverables
✓ SensorAgent code (lab2_sensor_agent.py)  
✓ Event logs (logs/SensorAgent_*_log.txt)  
✓ Event data (logs/SensorAgent_*_events.json)  
✓ Brief explanation of percepts (documented in code and README)  

---

## References

- SPADE Documentation: https://spade-mas.readthedocs.io/
- FIPA Standards: http://www.fipa.org/
- Prometheus Methodology: Agent-Oriented Software Engineering
- Python asyncio: https://docs.python.org/3/library/asyncio.html

---

**End of Laboratory Report**
