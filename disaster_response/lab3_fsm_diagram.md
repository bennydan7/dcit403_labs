# LAB 3 FSM Diagram

```mermaid
stateDiagram-v2
    [*] --> MONITORING

        MONITORING --> ASSESSING: DISASTER_DETECTED\nTEMP_SPIKE\nWATER_RISE
            ASSESSING --> DISPATCHING: Assessment complete
                DISPATCHING --> RECOVERY: Resources dispatched
                    RECOVERY --> MONITORING: Recovery cycle complete

                        MONITORING --> MONITORING: No trigger events
                        ```

                        ## Event Triggers

                        - `DISASTER_DETECTED`: New disaster appears in sensor report
                        - `SEVERITY_ESCALATION`: Disaster severity is `CRITICAL` or `CATASTROPHIC`
                        - `RESOURCE_SHORTAGE`: Rescue team demand is high
                        - `TEMP_SPIKE`: Sensor temperature exceeds threshold
                        - `WATER_RISE`: Sensor water level exceeds threshold

                        ## Goals Linked to Reactive Actions

                        - Rescue people rapidly
                        - Stabilize infrastructure impacts
                        - Optimize resource allocation
                        