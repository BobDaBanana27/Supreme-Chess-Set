import uuid
import os

os.makedirs("hardware", exist_ok=True)

sch_uuid = str(uuid.uuid4())
proj_name = "sensor_strip"

components = []
components.append({'ref': 'U1', 'val': '74HC165_SOIC16', 'fp': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'x': 50.0, 'y': 80.0, 'pins': 16})
components.append({'ref': 'U2', 'val': '74HC165_SOIC16', 'fp': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'x': 120.0, 'y': 80.0, 'pins': 16})
components.append({'ref': 'J1', 'val': 'Conn_FFC_6P', 'fp': 'Connector_FFC-FPC:Hirose_FH12-6S-0.5SH', 'x': 15.0, 'y': 80.0, 'pins': 6})
components.append({'ref': 'C1', 'val': '0.1uF', 'fp': 'Capacitor_SMD:C_0805_2012Metric', 'x': 45.0, 'y': 65.0, 'pins': 2})
components.append({'ref': 'C2', 'val': '0.1uF', 'fp': 'Capacitor_SMD:C_0805_2012Metric', 'x': 115.0, 'y': 65.0, 'pins': 2})

for i in range(1, 17):
    components.append({'ref': f'H{i}', 'val': 'AH49E_Hall', 'fp': 'Package_TO_SOT_SMD:SOT-23', 'x': 20.0 + i * 9.0, 'y': 130.0, 'pins': 3})
    components.append({'ref': f'R{i}', 'val': '10k', 'fp': 'Resistor_SMD:R_0805_2012Metric', 'x': 20.0 + i * 9.0, 'y': 115.0, 'pins': 2})

symbols_code = ''
for c in components:
    comp_uuid = str(uuid.uuid4())
    pin_lines = []
    for p in range(c['pins']):
        p_uuid = str(uuid.uuid4())
        pin_lines.append(f'\t\t(pin "{p+1}" (uuid "{p_uuid}"))')
    pin_entries = '\n'.join(pin_lines)
    symbols_code += f"""
	(symbol
		(lib_id "Device:Generic")
		(at {c['x']} {c['y']} 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{comp_uuid}")
		(property "Reference" "{c['ref']}"
			(at {c['x']} {c['y']-4} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "{c['val']}"
			(at {c['x']} {c['y']+4} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "{c['fp']}"
			(at {c['x']} {c['y']} 0)
			(hide yes)
			(effects (font (size 1.27 1.27)))
		)
		(property "Datasheet" "" (at {c['x']} {c['y']} 0) (hide yes) (effects (font (size 1.27 1.27))))
		(property "Description" "" (at {c['x']} {c['y']} 0) (hide yes) (effects (font (size 1.27 1.27))))
{pin_entries}
		(instances
			(project "{proj_name}"
				(path "/{sch_uuid}"
					(reference "{c['ref']}")
					(unit 1)
				)
			)
		)
	)"""

sch_content = f"""(kicad_sch
	(version 20260306)
	(generator "eeschema")
	(generator_version "10.0")
	(uuid "{sch_uuid}")
	(paper "A3")
	(title_block
		(title "Supreme Chess Set — 16-Slot Capture Sensor Strip")
		(date "2026-11-08")
		(rev "1.0")
		(company "Supreme Chess / Hack Club")
		(comment 1 "2x Cascaded 74HC165 Shift Registers and 16x Digital Hall Sensors")
	)
	(lib_symbols
		(symbol "Device:Generic"
			(pin_numbers (hide yes))
			(pin_names (offset 1.016))
			(exclude_from_sim no)
			(in_bom yes)
			(on_board yes)
			(property "Reference" "U" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Generic" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(property "Footprint" "" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(property "Datasheet" "" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(property "Description" "" (at 0 0 0) (hide yes) (effects (font (size 1.27 1.27))))
			(symbol "Generic_0_1"
				(rectangle (start -10 10) (end 10 -10) (stroke (width 0.254)) (fill (type background)))
			)
		)
	)
{symbols_code}
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
	(embedded_fonts no)
)
"""

with open("hardware/sensor_strip.kicad_sch", "w", encoding="utf-8") as f:
    f.write(sch_content)
print("Successfully generated hardware/sensor_strip.kicad_sch")
