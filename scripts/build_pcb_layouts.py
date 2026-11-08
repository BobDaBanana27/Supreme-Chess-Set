import uuid
import os

os.makedirs("hardware", exist_ok=True)

def gen_motherboard_pcb():
    w, h = 75.0, 48.0
    u1_x, u1_y = 25.0, 24.0
    disp_x, disp_y = 55.0, 24.0
    
    pcb = f"""(kicad_pcb
	(version 20260206)
	(generator "pcbnew")
	(generator_version "10.0")
	(general
		(thickness 1.6)
		(legacy_teardrops no)
	)
	(paper "A4")
	(title_block
		(title "Supreme Chess Set — Core Motherboard PCB")
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
	)
	(net 0 "")
	(net 1 "GND")
	(net 2 "+3V3")
	(net 3 "SDA")
	(net 4 "SCL")
	(net 5 "SR_LOAD")
	(net 6 "SR_CLK")
	(net 7 "SR_DATA")

	(gr_rect (start 0 0) (end {w} {h})
		(stroke (width 0.15) (type solid))
		(fill none)
		(layer "Edge.Cuts")
		(uuid "{str(uuid.uuid4())}")
	)

	(gr_text "SUPREME CHESS CORE V1.0" (at {w/2} 4 0) (layer "F.SilkS") (uuid "{str(uuid.uuid4())}") (effects (font (size 1.5 1.5) (thickness 0.2))))
	(gr_text "Hack Club Half Life 2" (at {w/2} {h-3} 0) (layer "F.SilkS") (uuid "{str(uuid.uuid4())}") (effects (font (size 1.2 1.2) (thickness 0.15))))

	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu") (at 4 4)
		(pad "1" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)
	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu") (at {w-4} 4)
		(pad "1" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)
	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu") (at 4 {h-4})
		(pad "1" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)
	(footprint "MountingHole:MountingHole_2.7mm_M2.5" (layer "F.Cu") (at {w-4} {h-4})
		(pad "1" np_thru_hole circle (at 0 0) (size 2.7 2.7) (drill 2.7) (layers "*.Cu" "*.Mask"))
	)

	(footprint "Module:RP2040-Zero" (layer "F.Cu") (at {u1_x} {u1_y})
		(property "Reference" "U1" (at 0 -12 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(property "Value" "RP2040-Zero" (at 0 12 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(fp_rect (start -9 -11.5) (end 9 11.5) (stroke (width 0.15)) (fill none) (layer "F.SilkS"))
		(pad "1" smd rect (at -8.5 -8) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at -8.5 -5.5) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
		(pad "3" smd rect (at -8.5 -3) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 3 "SDA"))
		(pad "4" smd rect (at -8.5 -0.5) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 4 "SCL"))
		(pad "5" smd rect (at -8.5 2) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "6" smd rect (at -8.5 4.5) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "7" smd rect (at -8.5 7) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "8" smd rect (at 8.5 -8) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "SR_LOAD"))
		(pad "9" smd rect (at 8.5 -5.5) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "SR_CLK"))
		(pad "10" smd rect (at 8.5 -3) (size 2.0 1.0) (layers "F.Cu" "F.Paste" "F.Mask") (net 7 "SR_DATA"))
	)

	(footprint "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" (layer "F.Cu") (at {disp_x} {disp_y})
		(property "Reference" "DISP1" (at 0 -6 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(property "Value" "OLED_0.96" (at 0 6 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" thru_hole rect (at 0 -3.81) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
		(pad "2" thru_hole circle (at 0 -1.27) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 2 "+3V3"))
		(pad "3" thru_hole circle (at 0 1.27) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 4 "SCL"))
		(pad "4" thru_hole circle (at 0 3.81) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 3 "SDA"))
	)

	(footprint "Connector_FFC-FPC:Hirose_FH12-6S-0.5SH" (layer "F.Cu") (at 25 40)
		(property "Reference" "J1" (at 0 -3 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(property "Value" "FFC_SENSOR_BUS" (at 0 3 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))
		(pad "1" smd rect (at -1.25 0) (size 0.3 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at -0.75 0) (size 0.3 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
		(pad "3" smd rect (at -0.25 0) (size 0.3 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "SR_LOAD"))
		(pad "4" smd rect (at 0.25 0) (size 0.3 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "SR_CLK"))
		(pad "5" smd rect (at 0.75 0) (size 0.3 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 7 "SR_DATA"))
		(pad "6" smd rect (at 1.25 0) (size 0.3 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
	)

	(footprint "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm" (layer "F.Cu") (at 65 10)
		(property "Reference" "SW2" (at 0 -4 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
		(pad "1" smd rect (at -2.5 -1.5) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at 2.5 1.5) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
	)
	(footprint "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm" (layer "F.Cu") (at 65 38)
		(property "Reference" "SW3" (at 0 4 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
		(pad "1" smd rect (at -2.5 -1.5) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at 2.5 1.5) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
	)

	(segment (start {u1_x-8.5} {u1_y-3}) (end {disp_x} {disp_y+3.81}) (width 0.25) (layer "F.Cu") (net 3))
	(segment (start {u1_x-8.5} {u1_y-0.5}) (end {disp_x} {disp_y+1.27}) (width 0.25) (layer "F.Cu") (net 4))
	(segment (start {u1_x+8.5} {u1_y-8}) (end 25 38.5) (width 0.25) (layer "F.Cu") (net 5))
	(segment (start {u1_x+8.5} {u1_y-5.5}) (end 25.5 38.5) (width 0.25) (layer "F.Cu") (net 6))
	(segment (start {u1_x+8.5} {u1_y-3}) (end 26 38.5) (width 0.25) (layer "F.Cu") (net 7))

	(embedded_fonts no)
)
"""
    with open("hardware/supreme_chess.kicad_pcb", "w", encoding="utf-8") as f:
        f.write(pcb)
    print("Generated hardware/supreme_chess.kicad_pcb")

def gen_sensor_strip_pcb():
    w, h = 155.0, 22.0
    
    pads_hall = ""
    # 16 Hall sensors at 8.8mm increments across the 155mm strip
    for i in range(16):
        hx = 10.0 + i * 8.8
        hy = 11.0
        pads_hall += f"""
	(footprint "Package_TO_SOT_SMD:SOT-23" (layer "F.Cu") (at {hx} {hy})
		(property "Reference" "H{i+1}" (at 0 -3 0) (layer "F.SilkS") (effects (font (size 0.7 0.7) (thickness 0.12))))
		(pad "1" smd rect (at -0.95 -1.0) (size 0.8 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
		(pad "2" smd rect (at 0.95 -1.0) (size 0.8 0.9) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "3" smd rect (at 0 1.0) (size 0.8 0.9) (layers "F.Cu" "F.Paste" "F.Mask"))
	)
	(footprint "Resistor_SMD:R_0805_2012Metric" (layer "F.Cu") (at {hx} {hy+5.5})
		(property "Reference" "R{i+1}" (at 0 2 0) (layer "F.SilkS") (effects (font (size 0.6 0.6) (thickness 0.1))))
		(pad "1" smd rect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
		(pad "2" smd rect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask"))
	)"""

    pcb = f"""(kicad_pcb
	(version 20260206)
	(generator "pcbnew")
	(generator_version "10.0")
	(general
		(thickness 1.6)
		(legacy_teardrops no)
	)
	(paper "A4")
	(title_block
		(title "Supreme Chess Set — 16-Slot Capture Sensor Strip")
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
	)
	(net 0 "")
	(net 1 "GND")
	(net 2 "+3V3")
	(net 5 "SR_LOAD")
	(net 6 "SR_CLK")
	(net 7 "SR_DATA")

	(gr_rect (start 0 0) (end {w} {h})
		(stroke (width 0.15) (type solid))
		(fill none)
		(layer "Edge.Cuts")
		(uuid "{str(uuid.uuid4())}")
	)

	(gr_text "15-SLOT CAPTURE SENSOR STRIP" (at {w/2} 3 0) (layer "F.SilkS") (uuid "{str(uuid.uuid4())}") (effects (font (size 1.2 1.2) (thickness 0.18))))

	(footprint "Connector_FFC-FPC:Hirose_FH12-6S-0.5SH" (layer "F.Cu") (at 5 11)
		(property "Reference" "J1" (at 0 -3 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
		(pad "1" smd rect (at 0 -1.25) (size 1.2 0.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "2" smd rect (at 0 -0.75) (size 1.2 0.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
		(pad "3" smd rect (at 0 -0.25) (size 1.2 0.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "SR_LOAD"))
		(pad "4" smd rect (at 0 0.25) (size 1.2 0.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "SR_CLK"))
		(pad "5" smd rect (at 0 0.75) (size 1.2 0.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 7 "SR_DATA"))
		(pad "6" smd rect (at 0 1.25) (size 1.2 0.3) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
	)

	(footprint "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm" (layer "F.Cu") (at 45 11)
		(property "Reference" "U1" (at 0 -6 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
		(property "Value" "74HC165" (at 0 6 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
		(pad "1" smd rect (at -2.5 -4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "SR_LOAD"))
		(pad "2" smd rect (at -2.5 -3.175) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "SR_CLK"))
		(pad "8" smd rect (at -2.5 4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "9" smd rect (at 2.5 4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 7 "SR_DATA"))
		(pad "16" smd rect (at 2.5 -4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
	)

	(footprint "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm" (layer "F.Cu") (at 105 11)
		(property "Reference" "U2" (at 0 -6 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
		(property "Value" "74HC165" (at 0 6 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
		(pad "1" smd rect (at -2.5 -4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "SR_LOAD"))
		(pad "2" smd rect (at -2.5 -3.175) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "SR_CLK"))
		(pad "8" smd rect (at -2.5 4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 1 "GND"))
		(pad "9" smd rect (at 2.5 4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask"))
		(pad "16" smd rect (at 2.5 -4.445) (size 1.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "+3V3"))
	)
{pads_hall}
	(embedded_fonts no)
)
"""
    with open("hardware/sensor_strip.kicad_pcb", "w", encoding="utf-8") as f:
        f.write(pcb)
    print("Generated hardware/sensor_strip.kicad_pcb")

if __name__ == "__main__":
    gen_motherboard_pcb()
    gen_sensor_strip_pcb()
