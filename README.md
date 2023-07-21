ECU Simulator

Requirements: Python

Install: `pip install -r requirements.txt`

Start API: `python3 -m flask --app main run --host=0.0.0.0`

ECU URL: When you start the API, the ECU URL will be printed in the terminal as `Access http://{localNetAddr}:5000/ecu on your mobile`. Access the link in your cell phone's browser, rotate to horizontal and set the full screen, not all browsers allow full screen mode, I use Opera.


| Game            | Support | ECUs  |
|-----------------|---------|-------|
| Assetto Corsa   | yes     | FT550 |
| Forza Horizon 5 | not     |       |
| BeamNG.drive    | not     |       |
| F1 23           | not     |       |