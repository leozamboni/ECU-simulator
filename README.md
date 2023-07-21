ECU Simulator

Requirements: Python

Install: `pip install -r requirements.txt`

Start API: `python3 -m flask --app main run --host=0.0.0.0`

ECU URL: `http://{localNetAddr}:5000/ecu`


| Game            | Support | ECUs  |
|-----------------|---------|-------|
| Assetto Corsa   | yes     | FT550 |
| Forza Horizon 5 | not     |       |
| BeamNG.drive    | not     |       |
| F1 23           | not     |       |