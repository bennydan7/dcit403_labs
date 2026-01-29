"""
LAB 2: Perception and Environment Modeling
Disaster Response & Relief Coordination System

This module implements a simulated disaster environment with various
disaster scenarios and environmental conditions.
"""

import random
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional


class DisasterType(Enum):
    """Types of disasters that can occur."""
    FLOOD = "Flood"
    EARTHQUAKE = "Earthquake"
    FIRE = "Fire"
    DROUGHT = "Drought"
    STORM = "Storm"


class Severity(Enum):
    """Severity levels for disasters."""
    LOW = 1
    MODERATE = 2
    HIGH = 3
    CRITICAL = 4
    CATASTROPHIC = 5


@dataclass
class Location:
    """Represents a geographical location."""
    latitude: float
    longitude: float
    name: str
    
    def __str__(self):
        return f"{self.name} ({self.latitude:.4f}, {self.longitude:.4f})"


@dataclass
class DisasterEvent:
    """Represents a disaster event in the environment."""
    event_id: str
    disaster_type: DisasterType
    location: Location
    severity: Severity
    timestamp: datetime
    affected_area: float  # in square kilometers
    casualties: int
    infrastructure_damage: float  # percentage (0-100)
    resources_needed: Dict[str, int]
    
    def __str__(self):
        return (f"Event #{self.event_id}: {self.disaster_type.value} "
                f"[Severity: {self.severity.name}] at {self.location.name}")


@dataclass
class EnvironmentPercept:
    """
    Represents what a sensor agent perceives from the environment.
    This is the input that agents receive from their sensors.
    """
    timestamp: datetime
    location: Location
    temperature: float  # Celsius
    humidity: float  # percentage
    wind_speed: float  # km/h
    air_quality: float  # AQI (0-500)
    seismic_activity: float  # Richter scale (0-10)
    water_level: float  # meters above normal
    smoke_detected: bool
    active_disasters: List[DisasterEvent]
    
    def __str__(self):
        return (f"Percept @ {self.timestamp.strftime('%H:%M:%S')} - "
                f"{self.location.name}: Temp={self.temperature:.1f}°C, "
                f"Humidity={self.humidity:.0f}%, Active Disasters={len(self.active_disasters)}")


class DisasterEnvironment:
    """
    Simulates a disaster-prone environment with dynamic conditions.
    Agents perceive this environment through sensors.
    """
    
    def __init__(self):
        self.event_counter = 0
        self.active_disasters: List[DisasterEvent] = []
        self.locations = self._initialize_locations()
        self.current_conditions = self._initialize_conditions()
        
    def _initialize_locations(self) -> List[Location]:
        """Initialize monitored locations."""
        return [
            Location(5.6037, -0.1870, "Accra"),
            Location(6.6944, -1.5547, "Kumasi"),
            Location(5.6260, 0.0091, "Tema"),
            Location(9.2619, -0.8406, "Tamale"),
            Location(5.1143, -1.2440, "Cape Coast"),
        ]
    
    def _initialize_conditions(self) -> Dict[str, Dict]:
        """Initialize environmental conditions for each location."""
        conditions = {}
        for location in self.locations:
            conditions[location.name] = {
                'temperature': random.uniform(25, 35),
                'humidity': random.uniform(60, 90),
                'wind_speed': random.uniform(0, 30),
                'air_quality': random.uniform(50, 150),
                'seismic_activity': 0.0,
                'water_level': 0.0,
                'smoke_detected': False,
            }
        return conditions
    
    def update_environment(self):
        """
        Update environmental conditions and potentially generate new disasters.
        This simulates the dynamic nature of the environment.
        """
        # Update base conditions
        for location_name in self.current_conditions:
            cond = self.current_conditions[location_name]
            cond['temperature'] += random.uniform(-2, 2)
            cond['humidity'] += random.uniform(-5, 5)
            cond['wind_speed'] = max(0, cond['wind_speed'] + random.uniform(-5, 5))
            cond['air_quality'] += random.uniform(-10, 10)
            
            # Clip values to realistic ranges
            cond['temperature'] = max(20, min(45, cond['temperature']))
            cond['humidity'] = max(30, min(100, cond['humidity']))
            cond['air_quality'] = max(0, min(500, cond['air_quality']))
        
        # Randomly generate new disasters (80% chance per update for demonstration)
        if random.random() < 0.80:
            self._generate_disaster()
        
        # Update existing disasters (they may intensify or subside)
        self._update_disasters()
    
    def _generate_disaster(self):
        """Generate a new random disaster event."""
        self.event_counter += 1
        
        disaster_type = random.choice(list(DisasterType))
        location = random.choice(self.locations)
        severity = random.choice(list(Severity))
        
        # Update environmental conditions based on disaster type
        cond = self.current_conditions[location.name]
        
        if disaster_type == DisasterType.FLOOD:
            cond['water_level'] = random.uniform(1, 5)
            cond['humidity'] = min(100, cond['humidity'] + 20)
        elif disaster_type == DisasterType.FIRE:
            cond['smoke_detected'] = True
            cond['temperature'] += random.uniform(10, 30)
            cond['air_quality'] += random.uniform(100, 300)
        elif disaster_type == DisasterType.EARTHQUAKE:
            cond['seismic_activity'] = random.uniform(3, 8)
        elif disaster_type == DisasterType.DROUGHT:
            cond['temperature'] += random.uniform(5, 15)
            cond['humidity'] = max(20, cond['humidity'] - 30)
        elif disaster_type == DisasterType.STORM:
            cond['wind_speed'] = random.uniform(50, 150)
            cond['humidity'] = min(100, cond['humidity'] + 15)
        
        # Create disaster event
        event = DisasterEvent(
            event_id=f"D{self.event_counter:04d}",
            disaster_type=disaster_type,
            location=location,
            severity=severity,
            timestamp=datetime.now(),
            affected_area=random.uniform(0.5, 50),
            casualties=random.randint(0, severity.value * 50),
            infrastructure_damage=random.uniform(severity.value * 5, severity.value * 20),
            resources_needed={
                'medical_kits': random.randint(10, 100),
                'food_packages': random.randint(50, 500),
                'water_bottles': random.randint(100, 1000),
                'rescue_teams': random.randint(2, 20),
            }
        )
        
        self.active_disasters.append(event)
        return event
    
    def _update_disasters(self):
        """Update existing disasters - they may resolve over time."""
        disasters_to_remove = []
        
        for disaster in self.active_disasters:
            # 20% chance a disaster resolves
            if random.random() < 0.20:
                disasters_to_remove.append(disaster)
                # Reset environmental conditions
                cond = self.current_conditions[disaster.location.name]
                if disaster.disaster_type == DisasterType.FLOOD:
                    cond['water_level'] = 0.0
                elif disaster.disaster_type == DisasterType.FIRE:
                    cond['smoke_detected'] = False
                elif disaster.disaster_type == DisasterType.EARTHQUAKE:
                    cond['seismic_activity'] = 0.0
        
        for disaster in disasters_to_remove:
            self.active_disasters.remove(disaster)
    
    def sense(self, location: Location) -> EnvironmentPercept:
        """
        Get a percept (sensor reading) for a specific location.
        This is what a SensorAgent would perceive.
        """
        cond = self.current_conditions[location.name]
        
        # Get disasters affecting this location
        local_disasters = [d for d in self.active_disasters if d.location.name == location.name]
        
        return EnvironmentPercept(
            timestamp=datetime.now(),
            location=location,
            temperature=cond['temperature'],
            humidity=cond['humidity'],
            wind_speed=cond['wind_speed'],
            air_quality=cond['air_quality'],
            seismic_activity=cond['seismic_activity'],
            water_level=cond['water_level'],
            smoke_detected=cond['smoke_detected'],
            active_disasters=local_disasters
        )
    
    def get_all_percepts(self) -> List[EnvironmentPercept]:
        """Get percepts for all monitored locations."""
        return [self.sense(loc) for loc in self.locations]
    
    def get_summary(self) -> str:
        """Get a summary of the current environment state."""
        summary = "\n" + "="*70 + "\n"
        summary += "ENVIRONMENT STATUS SUMMARY\n"
        summary += "="*70 + "\n"
        summary += f"Active Disasters: {len(self.active_disasters)}\n"
        summary += f"Monitored Locations: {len(self.locations)}\n"
        summary += f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        summary += "="*70 + "\n\n"
        
        if self.active_disasters:
            summary += "ACTIVE DISASTERS:\n"
            summary += "-"*70 + "\n"
            for disaster in self.active_disasters:
                summary += f"{disaster}\n"
                summary += f"  Casualties: {disaster.casualties}, "
                summary += f"Damage: {disaster.infrastructure_damage:.1f}%, "
                summary += f"Area: {disaster.affected_area:.1f} km²\n"
            summary += "-"*70 + "\n"
        else:
            summary += "No active disasters - All locations clear\n"
            summary += "-"*70 + "\n"
        
        return summary
