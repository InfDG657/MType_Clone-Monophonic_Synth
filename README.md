# MTypeClone - Monophonic Synthesizer

A Python-based monophonic synthesizer with a visual keyboard interface, built using tkinter and ttkbootstrap.

## Features

- **3 Independent Oscillators** with multiple waveform types:
  - Sine wave
  - Square wave
  - Sawtooth wave
  - Triangle wave
- **ADSR Envelope** (Attack, Decay, Sustain, Release) with toggleable filter
- **Octave Control** (-4 to +4 octave range) with keyboard shortcuts
- **Noise Generator** for adding texture and grit
- **Visual Piano Keyboard** with computer keyboard input
- **Phase-Continuous Synthesis** - no clicking or popping during note transitions
- **Real-time Audio Output** with low latency

## Requirements

- Python 3.7+
- Audio output device

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/synth_project.git
cd synth_project
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the synthesizer:
```bash
python SynthCode.py
```

## Usage

### Keyboard Controls

**White Keys (Natural Notes):**
- `A` - C
- `S` - D
- `D` - E
- `F` - F
- `G` - G
- `H` - A
- `J` - B
- `K` - C (next octave)

**Black Keys (Sharps/Flats):**
- `W` - C#/Db
- `E` - D#/Eb
- `T` - F#/Gb
- `Y` - G#/Ab
- `U` - A#/Bb

**Octave Shifting:**
- `Left Arrow` - Decrease octave
- `Right Arrow` - Increase octave

### Synth Controls

**Oscillators (Osc1, Osc2, Osc3):**
- Select waveform type using the toggle buttons
- Adjust volume using the vertical slider
- Multiple oscillators can be active simultaneously

**Envelope (Env):**
- Toggle the envelope on/off with the switch
- Adjust Attack, Decay, Sustain, and Release using the circular meters

**Noise Generator:**
- Adjust the noise slider to add white noise to your sound

## How It Works

This synthesizer uses phase accumulation for continuous waveform generation, ensuring smooth transitions between notes without clicks or pops. The ADSR envelope shapes the amplitude over time, and multiple oscillators can be layered for complex timbres.

Audio is generated in real-time using a callback-based approach with the sounddevice library, providing low-latency performance.

## License

This project is open source and available for anyone to use, modify, and learn from.

## Acknowledgments

Built with Python, tkinter, ttkbootstrap, NumPy, and sounddevice.
