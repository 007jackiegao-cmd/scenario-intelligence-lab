from pathlib import Path

for filename in ['ARCHITECTURE.md', 'METHODOLOGY.md', 'PROVENANCE.md', 'VALIDATION.md', 'leaflet.css', 'leaflet.js', 'topojson-client.js']:
    Path(filename).unlink(missing_ok=True)
Path(__file__).unlink()
