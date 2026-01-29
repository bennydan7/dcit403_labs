# 🚨 Disaster Response & Relief Coordination System

A hands-on Python project building intelligent agents that detect and respond to disaster events in real-time.

**Course:** DCIT 403 - Designing Intelligent Systems  
**Language:** Python | **Framework:** SPADE (Smart Python Agent Development Environment)

---

## What This Project Does

Imagine having smart robots that can detect floods, earthquakes, and fires automatically, then alert humans with critical information. That's what this project builds—a team of intelligent agents that work together to:
- 🔍 Detect disaster events as they happen
- 📊 Assess how severe the damage is
- 🗺️ Work across multiple locations at once
- 📋 Log everything so humans know what happened

---

## Lab 1: Hello Agent World 👋

**What You'll Learn:** How to create an agent and make it do something

This is the "Hello, World!" of multi-agent systems. You'll create a basic agent that:
- Wakes up and says hello
- Does a task repeatedly every 2 seconds
- Shuts down cleanly when done

**File:** `disaster_response/lab1_basic_agent_simple.py`

### Quick Start
```bash
python3 disaster_response/lab1_basic_agent_simple.py
```

You'll see the agent print messages showing it's alive and working!

---

## Lab 2: Sensor Agents Detecting Disasters 🚨

**What You'll Learn:** How to make agents that sense their environment and detect problems

This is where it gets real. You'll deploy 3 sensor agents across different cities in Ghana, and they'll:
- Monitor temperature, humidity, wind, air quality, and water levels
- Spot disasters like fires, floods, and earthquakes
- Alert humans with critical information
- Save all findings to logs and JSON files

**Files:**
- `disaster_response/environment.py` — The fake disaster world
- `disaster_response/lab2_sensor_agent.py` — The agents that watch it

### How It Works

**The Environment:**
The simulator randomly creates disasters at different locations. Each disaster has:
- 🏷️ Type (Flood, Fire, Earthquake, Drought, Storm)
- 📍 Location (Cities in Ghana like Accra, Kumasi, Tema)
- ⚠️ Severity (Low → Catastrophic)
- 👥 Impact (casualties, infrastructure damage, resources needed)

**The Sensors:**
Three agents are placed in different cities. Every 3 seconds they:
1. Read environmental conditions (temp, humidity, wind, air quality, etc.)
2. Check if something looks wrong
3. Search for active disasters
4. Log findings to files

### Quick Start
```bash
python3 disaster_response/lab2_sensor_agent.py
```

The agents will run for 20 seconds, detect disasters, and save everything to the `logs/` folder.

### What Gets Saved

**Log Files** (`logs/SENSOR-001_log.txt`, etc.)
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

---

## 📁 Project Structure

```
disaster_response/
├── lab1_basic_agent_simple.py    ← Start here (Hello, agent!)
├── lab2_sensor_agent.py          ← Then here (Smart detection)
└── environment.py                ← The simulated world

logs/
├── SENSOR-001_log.txt            ← What agent 1 saw
├── SENSOR-001_events.json        ← Disasters detected by agent 1
├── SENSOR-002_log.txt            ← What agent 2 saw
└── ... (more logs)
```

---

## 🧠 Key Concepts

### Autonomy
Agents work on their own without being told what to do each step

### Reactivity
Agents respond immediately when something important happens (like a disaster)

### Proactivity
Agents constantly monitor and look for problems before being asked

### Concurrency
Multiple agents can run and monitor different places at the same time

---

## 🛠️ Technical Stuff

- **Asynchronous Code:** Python's `asyncio` lets agents do multiple things at once
- **Object-Oriented Design:** Clean code with reusable pieces
- **Logging:** Human-readable text logs + machine-readable JSON files
- **Simulation:** Fake (but realistic) disaster events for safe testing

---


## Notes

### Simulation Mode
The current implementation uses simulation mode instead of full SPADE/XMPP integration for easier demonstration. The core agent concepts remain valid and can be extended to full SPADE agents when XMPP connectivity is required.

---

## 👤 Author

**Bernard Owusu-Dankwah**  
January 29, 2026
