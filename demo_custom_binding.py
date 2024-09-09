from pyboy import PyBoy
from pyboy.plugins.window_sdl2 import set_keybinding
import sdl2

pyboy = PyBoy("Tetris.gb")
state = {"emulation_speed": 1}
pyboy.set_emulation_speed(state["emulation_speed"])

def no_action():
    pass

def speed_up():
	state["emulation_speed"] = min(10, state["emulation_speed"] + 1)
	pyboy.set_emulation_speed(state["emulation_speed"])
	print("New speed: ", state["emulation_speed"])

def slow_down():
	state["emulation_speed"] = max(1, state["emulation_speed"] - 1)
	pyboy.set_emulation_speed(state["emulation_speed"])
	print("New speed: ", state["emulation_speed"])

set_keybinding(sdl2.SDLK_b, speed_up, no_action)
set_keybinding(sdl2.SDLK_v, slow_down, no_action)

while pyboy.tick():
	pass
pyboy.stop()
