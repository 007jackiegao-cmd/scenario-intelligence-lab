# Scenario Intelligence Lab

A map-based event explorer with scenario comparison and per-event contribution breakdowns.

[Open app](https://007jackiegao-cmd.github.io/scenario-intelligence-lab/)

## Run

```sh
npm ci
npm run dev
node test-scenario.js
npm run build
```

Select an event category and switch between base, disruption and recovery. Each score is the sum of `category weight × event shock × scenario multiplier`. The table shows the signed components; opposing effects are marked beside the totals.

`scenario-engine.js` handles the calculation and duplicate IDs. `scenario-app.js` holds six sample events and the interface. Leaflet and world-atlas provide the map. Scores use model units.
