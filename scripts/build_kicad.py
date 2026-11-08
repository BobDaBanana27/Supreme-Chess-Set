"""
Generate KiCad 10 schematic and PCB files for Supreme Chess Set.
Produces:
- hardware/supreme_chess.kicad_sch
- hardware/sensor_strip.kicad_sch
- hardware/supreme_chess.kicad_pcb
- hardware/sensor_strip.kicad_pcb
"""
import uuid
import os

os.makedirs("hardware", exist_ok=True)

def gen_main_schematic():
    sch_uuid = str(uuid.uuid4())
    proj_name = "supreme_chess"
    
    # We create components: U1 (RP2040-Zero), DISP1 (SSD1306 OLED), MOD1 (TP4056), SW1 (Power), SW2 (Mode), SW3 (Reset), J1 (Sensor Bus), R1, R2, C1, C2
    components = [
        {"ref": "U1", "val": "RP2040-Zero", "fp": "Module:RP2040-Zero", "x": 150.0, "y": 100.0, "pins": 14},
        {"ref": "DISP1", "val": "SSD1306_128x64_OLED", "fp": "Display:OLED_0.96_128x64_I2C", "x": 70.0, "y": 100.0, "pins": 4},
        {"ref": "MOD1", "val": "TP4056_Charger", "fp": "Module:TP4056_TypeC", "x": 70.0, "y": 50.0, "pins": 4},
        {"ref": "SW1", "val": "SPDT_Power", "fp": "Button_Switch_SMD:SW_SPDT_PCM12", "x": 110.0, "y": 50.0, "pins": 3},
        {"ref": "SW2", "val": "BTN_Mode", "fp": "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm", "x": 110.0, "y": 140.0, "pins": 2},
        {"ref": "SW3", "val": "BTN_Reset", "fp": "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm", "x": 110.0, "y": 160.0, "pins": 2},
        {"ref": "J1", "val": "Conn_Sensor_Bus", "fp": "Connector_FFC-FPC:Hirose_FH12-6S-0.5SH", "x": 220.0, "y": 100.0, "pins": 6},
        {"ref": "R1", "val": "4.7k", "fp": "Resistor_SMD:R_0805_2012Metric", "x": 90.0, "y": 85.0, "pins": 2},
        {"ref": "R2", "val": "4.7k", "fp": "Resistor_SMD:R_0805_2012Metric", "x": 100.0, "y": 85.0, "pins": 2},
        {"ref": "C1", "val": "10uF", "fp": "Capacitor_SMD:C_0805_2012Metric", "x": 60.0, "y": 120.0, "pins": 2},
        {"ref": "C2", "val": "0.1uF", "fp": "Capacitor_SMD:C_0805_2012Metric", "x": 135.0, "y": 75.0, "pins": 2},
    ]

    symbols_code = ""
    for c in components:
        comp_uuid = str(uuid.uuid4())
        pin_entries = "\n".join([f'		(pin "{i+1}" (uuid "{str(uuid.uuid4())}"))' for i in range(c["pins"])])
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
			(at {c['x']} {c['y']-5} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "{c['val']}"
			(at {c['x']} {c['y']+5} 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Footprint" "{c['fp']}"
			(at {c['x']} {c['y']} 0)
			(hide yes)
			(effects (font (size 1.27 1.27)))
		)
		(property "Datasheet" ""
			(at {c['x']} {c['y']} 0)
			(hide yes)
			(effects (font (size 1.27 1.27)))
		)
		(property "Description" ""
			(at {c['x']} {c['y']} 0)
			(hide yes)
			(effects (font (size 1.27 1.27)))
		)
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
		(title "Supreme Chess Set — Core System Board")
		(date "2026-11-08")
		(rev "1.0")
		(company "Supreme Chess / Hack Club")
		(comment 1 "RP2040-Zero MCU, SSD1306 0.96 OLED, LiPo Power & Sensor Bus")
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
    with open("hardware/supreme_chess.kicad_sch", "w", encoding="utf-8") as f:
        f.write(sch_content)
    print("Generated hardware/supreme_chess.kicad_sch")

def gen_pcb(filepath, title, width, height):
    # Generates a valid kicad_pcb
    pcb_content = f"""(kicad_pcb
	(version 20260206)
	(generator "pcbnew")
	(generator_version "10.0")
	(general
		(thickness 1.6)
		(legacy_teardrops no)
	)
	(paper "A4")
	(title_block
		(title "{title}")
		(date "2026-11-08")
		(rev "1.0")
		(company "Supreme Chess / Hack Club")
	)
	(layers
		(0 "F.Cu" signal)
		(2 "B.Cu" signal)
		(5 "F.SilkS" user "F.Silkscreen")
		(7 "B.SilkS" user "B.Silkscreen")
		(1 "F.Mask" user)
		(3 "B.Mask" user)
		(25 "Edge.Cuts" user)
	)
	(setup
		(pad_to_mask_clearance 0.05)
		(solder_mask_min_width 0.1)
		(pad_to_paste_clearance 0)
		(pad_to_paste_clearance_ratio 0)
		(aux_axis_origin 0 0)
		(grid_origin 0 0)
	)
	(net 0 "")
	(net 1 "GND")
	(net 2 "+3V3")
	(net 3 "SDA")
	(net 4 "SCL")
	(net 5 "SR_LOAD")
	(net 6 "SR_CLK")
	(net 7 "SR_DATA")

	(gr_rect (start 0 0) (end {width} {height})
		(stroke (width 0.15) (type solid))
		(fill none)
		(layer "Edge.Cuts")
		(uuid "{str(uuid.uuid4())}")
	)
	(gr_text "{title}"
		(at {width/2} 5 0)
		(layer "F.SilkS")
		(uuid "{str(uuid.uuid4())}")
		(effects
			(font (size 1.5 1.5) (thickness 0.2))
		)
	)
	(gr_text "Hack Club Half Life 2 - Supreme Chess"
		(at {width/2} {height - 4} 0)
		(layer "F.SilkS")
		(uuid "{str(uuid.uuid4())}")
		(effects
			(font (size 1.2 1.2) (thickness 0.15))
		)
	)
	(embedded_fonts no)
)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(pcb_content)
    print(f"Generated {filepath}")

if __name__ == "__main__":
    gen_main_schematic()
    gen_pcb("hardware/supreme_chess.kicad_pcb", "Supreme Chess Set - Motherboard", 85.0, 55.0)
    gen_pcb("hardware/sensor_strip.kicad_pcb", "Supreme Chess Set - 15-Slot Sensor Strip", 155.0, 22.0)
