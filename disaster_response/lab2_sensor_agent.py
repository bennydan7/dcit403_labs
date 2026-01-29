"""
LAB 2: Perception and Environment Modeling
Disaster Response & Relief Coordination System

This module implements SensorAgent that monitors the environment
and detects disaster events.
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path
from environment import DisasterEnvironment, Location, EnvironmentPercept, DisasterEvent


class SensorAgent:
    """
    Sensor Agent that monitors environmental conditions and detects disasters.
    
    Responsibilities:
    - Periodically sense the environment
    - Detect disaster events
    - Log sensor readings and events
    - Report anomalies and critical conditions
    """
    
    def __init__(self, agent_id: str, monitored_location: Location, environment: DisasterEnvironment):
        self.agent_id = agent_id
        self.location = monitored_location
        self.environment = environment
        self.is_running = False
        self.sensor_readings = []
        self.detected_events = []
        self.log_file = Path(f"logs/{agent_id}_log.txt")
        self.events_file = Path(f"logs/{agent_id}_events.json")
        
        # Create logs directory if it doesn't exist
        self.log_file.parent.mkdir(exist_ok=True)
        
    def _log_message(self, message: str):
        """Log a message to the agent's log file and console."""
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f"[{timestamp}] {self.agent_id}: {message}"
        print(log_entry)
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry + '\n')
    
    def _save_event(self, event: DisasterEvent):
        """Save a detected disaster event to JSON file."""
        event_data = {
            'event_id': event.event_id,
            'disaster_type': event.disaster_type.value,
            'location': str(event.location),
            'severity': event.severity.name,
            'timestamp': event.timestamp.isoformat(),
            'affected_area_km2': event.affected_area,
            'casualties': event.casualties,
            'infrastructure_damage_pct': event.infrastructure_damage,
            'resources_needed': event.resources_needed,
            'detected_by': self.agent_id
        }
        
        # Read existing events
        events = []
        if self.events_file.exists():
            with open(self.events_file, 'r') as f:
                events = json.load(f)
        
        # Add new event
        events.append(event_data)
        
        # Save updated events
        with open(self.events_file, 'w') as f:
            json.dump(events, f, indent=2)
    
    def perceive(self) -> EnvironmentPercept:
        """
        Perceive the environment at the monitored location.
        This simulates sensor readings.
        """
        return self.environment.sense(self.location)
    
    def analyze_percept(self, percept: EnvironmentPercept):
        """
        Analyze a percept to detect anomalies and disasters.
        """
        self.sensor_readings.append(percept)
        
        # Detailed sensor log - show when anomalies detected
        if percept.temperature > 40 or percept.wind_speed > 60 or percept.air_quality > 200 or percept.seismic_activity > 3.0 or percept.water_level > 0.5 or percept.smoke_detected:
            self._log_message(
                f"Percept | Temp: {percept.temperature:.0f}°C | Wind: {percept.wind_speed:.0f}km/h | AQI: {percept.air_quality:.0f} | Humidity: {percept.humidity:.0f}%"
            )
        
        # Check for active disasters
        if percept.active_disasters:
            for disaster in percept.active_disasters:
                # Check if this is a new disaster (not previously detected)
                if disaster not in self.detected_events:
                    self.detected_events.append(disaster)
                    self._save_event(disaster)
                    self.raise_alert(disaster)
    
    def raise_alert(self, disaster: DisasterEvent):
        """Raise an alert for a detected disaster with full details."""
        if disaster.severity.value >= 4:
            alert_level = "CRITICAL"
        else:
            alert_level = "WARNING"
        
        self._log_message(
            f"{alert_level} | {disaster.disaster_type.value} at {disaster.location.name} | Severity: {disaster.severity.name} | People Affected: {disaster.casualties} | Resources: {disaster.resources_needed['rescue_teams']} teams"
        )
    
    async def monitor_continuously(self, duration_seconds: int = 30, interval_seconds: int = 3):
        """
        Continuously monitor the environment for a specified duration.
        
        Args:
            duration_seconds: How long to monitor (in seconds)
            interval_seconds: Time between sensor readings (in seconds)
        """
        self.is_running = True
        print(f"\n{self.agent_id}: Monitoring {self.location.name}...")
        
        start_time = datetime.now()
        iteration = 0
        
        while self.is_running and (datetime.now() - start_time).total_seconds() < duration_seconds:
            iteration += 1
            
            # Update environment (new disasters may occur)
            self.environment.update_environment()
            
            # Perceive the environment
            percept = self.perceive()
            
            # Analyze what was perceived
            self.analyze_percept(percept)
            
            # Wait before next reading
            await asyncio.sleep(interval_seconds)
        
        self.is_running = False
    
    async def stop(self):
        """Stop the sensor agent."""
        self.is_running = False
        self._log_message("Sensor agent stopped")
    
    def get_summary(self) -> str:
        """Generate a summary of the sensor agent's activities."""
        summary = "\n" + "="*80 + "\n"
        summary += f"SENSOR: {self.agent_id} | EVENTS DETECTED: {len(self.detected_events)} | READINGS: {len(self.sensor_readings)}\n"
        summary += "="*80 + "\n"
        
        if self.detected_events:
            for i, event in enumerate(self.detected_events, 1):
                summary += f"\nEvent {i}:\n"
                summary += f"  Timestamp:      {event.timestamp.strftime('%H:%M:%S')}\n"
                summary += f"  Type:           {event.disaster_type.value}\n"
                summary += f"  Location:       {event.location.name}\n"
                summary += f"  Severity:       {event.severity.name} (Level {event.severity.value})\n"
                summary += f"  People Affected: {event.casualties}\n"
                summary += f"  Resources:      {event.resources_needed['rescue_teams']} rescue teams\n"
        else:
            summary += "STATUS: No disasters detected during monitoring period.\n"
        summary += "="*80 + "\n"
        
        return summary


async def main():
    """Main function to demonstrate the SensorAgent."""
    print("\nLAB 2: Perception and Environment Modeling")
    print("Disaster Response & Relief Coordination System\n")
    
    # Create the disaster environment
    environment = DisasterEnvironment()
    
    # Create sensor agents for different locations
    sensor_agents = []
    for i, location in enumerate(environment.locations[:3], 1):
        agent = SensorAgent(
            agent_id=f"SENSOR-{i:03d}",
            monitored_location=location,
            environment=environment
        )
        sensor_agents.append(agent)
    
    # Start all sensor agents concurrently
    monitoring_tasks = [
        agent.monitor_continuously(duration_seconds=20, interval_seconds=3)
        for agent in sensor_agents
    ]
    
    await asyncio.gather(*monitoring_tasks)
    
    # Display summaries
    for agent in sensor_agents:
        print(agent.get_summary())


if __name__ == "__main__":
    asyncio.run(main())
