
from inputs_manager import load_inputs
from pathlib import Path

file_path = Path(r"D:\beno.co\My_Python_Project\LeatherPilot2025\inputs.xlsx.xlsx")
inputs = load_inputs(file_path)

print(inputs)
