Web Telemetry Display

Use your mobile device as a telemetry display in racing games

| Game            | Support |
|-----------------|---------|
| Assetto Corsa   | FT550   |

Requirements

```
Python3
```

Install

```
pip install -r requirements.txt
```

Run

On Windows just open web_telemetry_display.bat or run
`python3 -m flask --app src/main run --host=0.0.0.0`

Display in your mobile device

When you start the API, the ECU URL will be printed in the terminal as `Access http://{localNetAddr}:5000/ecu on your mobile`. Access the link in your cell phone's browser, rotate to horizontal and set the full screen, not all browsers allow full screen mode, I use Opera.
