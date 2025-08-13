# Simulation Engine Prototype

This project demonstrates a prototype event-driven simulation engine for a ride-hailing scenario. The simulation processes events in chronological order, updating the state of cars and riders as events occur.

## Simulation Engine Prototype

The simulation engine uses a priority queue (min-heap) to manage and process events. Each event is a tuple of (timestamp, event_type, data). The main event loop pops the next event from the queue, advances the simulation clock, and calls the appropriate handler. This prototype focuses on the event engine, using simple placeholder logic for car matching and navigation.

- **Event Loop:** The `run()` method in the `Simulation` class processes events in order, ensuring correct sequencing.
- **Event Handlers:** Handlers update the state of cars and riders, link cars to riders, and schedule future events.
- **State Updates:** Car locations and statuses are updated at both pickup and dropoff to maintain consistency.

This prototype is designed to validate the event-driven approach before integrating more advanced algorithms.

## How to Run

1. Ensure you have Python 3 installed.
2. Place `simulation.py`, `car.py`, and `rider.py` in the same directory.
3. Open a terminal in that directory.
4. Run the simulation with:

    python simulation.py

You will see a text-based event log printed to the console, showing the sequence of dispatch, pickup, and dropoff events as the simulation runs.
