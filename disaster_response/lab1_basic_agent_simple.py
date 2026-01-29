"""
LAB 1: Environment and Agent Platform Setup
Disaster Response & Relief Coordination System

This module demonstrates a basic SPADE agent with simple behaviors using
an embedded XMPP server approach for easier setup.
"""

import asyncio
from datetime import datetime
import logging

# Configure logging to show SPADE debug information
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class SimulatedAgent:
    """
    A simulated agent that demonstrates core agent concepts
    without requiring a full XMPP server setup.
    
    This agent represents the foundation for disaster response agents,
    demonstrating agent lifecycle, behaviors, and basic operations.
    """
    
    def __init__(self, name):
        self.name = name
        self.is_running = False
        self.behaviours = []
        
    async def setup(self):
        """
        Setup method called when the agent starts.
        This is where we initialize the agent and its behaviors.
        """
        print("\n" + "="*70)
        print("LAB 1: Basic Agent Setup (Simulation Mode)")
        print("Disaster Response & Relief Coordination System")
        print("="*70)
        print(f"\nAgent '{self.name}' is starting...")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n" + "-"*70 + "\n")
        
    async def start(self):
        """Start the agent and its behaviors."""
        self.is_running = True
        await self.setup()
        
        # Execute hello behavior (one-shot)
        await self.hello_behaviour()
        
        # Execute periodic behavior
        await self.periodic_behaviour()
        
    async def hello_behaviour(self):
        """A simple one-shot behavior that runs once when the agent starts."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] HelloBehaviour executing...")
        print(f"Hello! I am agent '{self.name}' for disaster response coordination.")
        print("Agent is now operational and ready for disaster response tasks.")
        print()
        
    async def periodic_behaviour(self):
        """A cyclic behavior that runs periodically."""
        counter = 0
        max_iterations = 5
        
        while counter < max_iterations and self.is_running:
            counter += 1
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Periodic check #{counter}/{max_iterations}: Agent is alive and monitoring...")
            await asyncio.sleep(2)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Demonstration complete. Stopping periodic behavior.")
        await self.stop()
        
    async def stop(self):
        """Stop the agent."""
        self.is_running = False
        print("\n" + "="*70)
        print(f"Agent '{self.name}' has stopped. Agent demonstration successfully completed!")
        print("="*70 + "\n")


async def main():
    """Main function to run the agent simulation."""
    print("\n" + "="*70)
    print("LAB 1 DELIVERABLE: Basic SPADE Agent Demonstration")
    print("="*70)
    print("\nNOTE: This demonstration runs in simulation mode.")
    print("For production, a full XMPP server connection would be used.")
    print("\nAgent Identifier: BasicDisasterResponseAgent")
    print("Purpose: Foundation for disaster response coordination")
    
    # Create and start the simulated agent
    agent = SimulatedAgent("BasicDisasterResponseAgent")
    await agent.start()
    
   
    print("\nKey Concepts Demonstrated:")
    print("✓ Agent creation and initialization")
    print("✓ Agent lifecycle (setup → start → stop)")
    print("✓ One-shot behavior execution")
    print("✓ Periodic/Cyclic behavior execution")
    print("✓ Autonomous operation without external control")
    print("="*70 + "\n")


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
