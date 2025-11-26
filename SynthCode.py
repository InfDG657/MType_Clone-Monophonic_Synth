
#Add noise Generator

#Submit to GitHub!

import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import numpy as np
import sounddevice as sd


class VolOctFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.octave = tk.IntVar(value=0)
        self.noise = tk.DoubleVar(value=0)
        self.widgets()
        self.placement()
        self.bindings()

    def widgets(self):
        self.label1 = ttk.Label(self, text='Noise:')
        self.scale1 = ttk.Scale(self, from_= 0, to = 10, value=0, variable= self.noise, bootstyle = 'light')
        self.label2 = ttk.Label(self, text='Octave:')
        self.btn1 = ttk.Button(self, text='-', bootstyle='secondary', command=lambda e=1: self.handle_octave_down(e))
        self.entry1 = ttk.Entry(self, textvariable=self.octave, width=2)
        self.btn2 = ttk.Button(self, text='+', bootstyle='secondary', command=lambda e=1: self.handle_octave_up(e))
        

    def placement(self):
        self.rowconfigure((0,1), weight=1, uniform='a')
        self.columnconfigure((0,1,2,3), weight=1, uniform='a')
        self.label1.grid(row=0, column=0)
        self.scale1.grid(row=0, column = 1, columnspan=3, sticky='ew')
        self.label2.grid(row=1, column= 0)
        self.btn1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.btn2.grid(row=1, column=3)
        

    def bindings(self):
        self.master.bind('<Left>', self.handle_octave_down)
        self.master.bind('<Right>', self.handle_octave_down)

    def handle_octave_up(self, event):
        pass

    def handle_octave_down(self, event):
        pass
    
class ADSRFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief='solid')
        self.widgets()
        self.placement()
        self.obtain_values()

    def widgets(self):
        self.filter_enabled = tk.BooleanVar(value=False)
        self.title = ttk.Label(self, text='Env')
        self.label1 = ttk.Label(self, text='Attack')
        # Create attack meter with range 0-1 seconds
        self.meter1 = ttk.Meter(self, bootstyle='light', amounttotal=10, amountused=1, metersize=30, showtext=False, meterthickness=5, arcrange=270, arcoffset=135, interactive=True)
        # Link meter to attack DoubleVar so user adjustments update the ADSR parameter
        self.label2 = ttk.Label(self, text='Decay')
        # Create decay meter with range 0-1 seconds
        self.meter2 = ttk.Meter(self, bootstyle='light', amounttotal=10, amountused=1, metersize=30, showtext=False, meterthickness=5, arcrange=270, arcoffset=135, interactive=True)
        # Link meter to decay DoubleVar so user adjustments update the ADSR parameter
        self.label3 = ttk.Label(self, text='Sustain')
        # Create sustain meter with range 0-1 (amplitude level, not time)
        self.meter3 = ttk.Meter(self, bootstyle='light', amounttotal=10, amountused=1, metersize=30, showtext=False, meterthickness=5, arcrange=270, arcoffset=135, interactive=True)
        # Link meter to sustain DoubleVar so user adjustments update the ADSR parameter
        self.label4 = ttk.Label(self, text='Release')
        # Create release meter with range 0-1 seconds
        self.meter4 = ttk.Meter(self, bootstyle='light', amounttotal=10, amountused=1, metersize=30, showtext=False, meterthickness=5, arcrange=270, arcoffset=135, interactive=True)
        # Link meter to release DoubleVar so user adjustments update the ADSR parameter
        self.label5 = ttk.Label(self, text='On')
        self.filter_switch = ttk.Checkbutton(self, bootstyle='round-toggle', variable=self.filter_enabled)
    
    def obtain_values(self): 
        self.attack = self.meter1.amountusedvar.get()
        self.decay = self.meter2.amountusedvar.get()
        self.sustain = self.meter3.amountusedvar.get()
        self.release = self.meter4.amountusedvar.get()
        self.after(50, self.obtain_values)

    def placement(self):
        self.rowconfigure((0,1,2,3,4,5), weight=1)
        self.columnconfigure((0,1), weight=1)
        self.title.grid(row=0, column=0, columnspan=2, sticky='nesw', padx=5, pady=5)
        self.label5.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)
        self.filter_switch.grid(row=1, column=1, sticky='nesw', padx=5, pady=5)
        self.label1.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)
        self.meter1.grid(row=2, column=1, sticky='nesw', padx=5, pady=5)
        self.label2.grid(row=3, column=0, sticky='nesw', padx=5, pady=5)
        self.meter2.grid(row=3, column=1, sticky='nesw', padx=5, pady=5)
        self.label3.grid(row=4, column=0, sticky='nesw', padx=5, pady=5)
        self.meter3.grid(row=4, column=1, sticky='nesw', padx=5, pady=5)
        self.label4.grid(row=5, column=0, sticky='nesw', padx=5, pady=5)
        self.meter4.grid(row=5, column=1, sticky='nesw', padx=5, pady=5)

class OscFrame(ttk.Frame):
    def __init__(self, parent, text):
        super().__init__(parent, borderwidth=2, relief='solid')
        self.text = text
        self.wave_type = tk.IntVar(value=0)
        self.volume = tk.DoubleVar(value=0)
        self.widgets()
        self.placement()

    def widgets(self):
        self.title = ttk.Label(self, text=self.text)
        self.switch1 = ttk.Checkbutton(self, bootstyle='round-toggle', command=lambda: self.select_wave(1))
        self.label1 = ttk.Label(self, text='∿')
        self.switch2 = ttk.Checkbutton(self, bootstyle='round-toggle', command=lambda: self.select_wave(2))
        self.label2 = ttk.Label(self, text='⊓')
        self.switch3 = ttk.Checkbutton(self, bootstyle='round-toggle', command=lambda: self.select_wave(3))
        self.label3 = ttk.Label(self, text='╱')
        self.switch4 = ttk.Checkbutton(self, bootstyle='round-toggle', command=lambda: self.select_wave(4))
        self.label4 = ttk.Label(self, text='⋀⋁')
        self.volume_slider = ttk.Scale(self, from_=0.0, to=1.0, orient='vertical', bootstyle='light', variable=self.volume)

    def placement(self):
        self.rowconfigure((0,1,2,3,4), weight=1)
        self.columnconfigure((0,1,2), weight=1)
        self.title.grid(row=0, column=0, columnspan=2, sticky='nesw', padx=5, pady=5)
        self.switch1.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)
        self.label1.grid(row=1, column=1, sticky='nesw', padx=5, pady=5)
        self.switch2.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)
        self.label2.grid(row=2, column=1, sticky='nesw', padx=5, pady=5)
        self.switch3.grid(row=3, column=0, sticky='nesw', padx=5, pady=5)
        self.label3.grid(row=3, column=1, sticky='nesw', padx=5, pady=5)
        self.switch4.grid(row=4, column=0, sticky='nesw', padx=5, pady=5)
        self.label4.grid(row=4, column=1, sticky='nesw', padx=5, pady=5)
        self.volume_slider.grid(row=0, column=2, rowspan=5, sticky='ns', padx=5, pady=5)

    def select_wave(self, wave_num):
        if self.wave_type.get() == wave_num:
            self.wave_type.set(0)
            self.deselect_all()
        else:
            previous = self.wave_type.get()
            self.wave_type.set(wave_num)
            self.deselect_all()
            if wave_num == 1:
                self.switch1.state(['selected'])
            elif wave_num == 2:
                self.switch2.state(['selected'])
            elif wave_num == 3:
                self.switch3.state(['selected'])
            elif wave_num == 4:
                self.switch4.state(['selected'])

    def deselect_all(self):
        self.switch1.state(['!selected'])
        self.switch2.state(['!selected'])
        self.switch3.state(['!selected'])
        self.switch4.state(['!selected'])
class SynthFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, width=1000, height=250)
        self.controller = controller
        self.sample_rate = 48000
        self.amplitude = 0.3
        self.stream = None
        self.is_running = True
        # Phase accumulator dictionary: stores current phase (0 to 2π) for each frequency being played
        # This prevents phase discontinuities between audio blocks and eliminates clicking/buzzing
        self.phase_accumulators = {}
        self.previous_frequency = None
        self.phase_cleanup_delay = {}
        # Dictionary to track how many samples have elapsed since each note was pressed (for ADSR timing)
        self.note_press_times = {}
        # Dictionary to track when notes were released (stores sample position at release time)
        self.note_release_times = {}
        # Dictionary to store the current envelope amplitude for each note (0.0 to 1.0)
        self.note_envelope_positions = {}
        self.frames()
        self.placement()
        self.start_audio_stream()
        

    def frames(self):
        self.osc1 = OscFrame(self, 'Osc1')
        self.osc2 = OscFrame(self, 'Osc2')
        self.osc3 = OscFrame(self, 'Osc3')
        self.adsr = ADSRFrame(self)
        self.vol_oct = VolOctFrame(self)

    def placement(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4,5), weight=1, uniform='a')

        self.osc1.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)
        self.osc2.grid(row=0, column=1, sticky='nesw', padx=5, pady=5)
        self.osc3.grid(row=0, column=2, sticky='nesw', padx=5, pady=5)
        self.adsr.grid(row=0, column=3, sticky='nesw', padx=5, pady=5)
        self.vol_oct.grid(row=0, column=4, columnspan=2, sticky='nesw', padx=5, pady=5)

    def generate_adsr_envelope(self, frequency, num_samples, current_sample_position):
        # Get current ADSR parameter values from the UI controls
        attack = self.adsr.attack / 10
        decay = self.adsr.decay / 10
        sustain = self.adsr.sustain / 10
        release = self.adsr.release / 10

        # Convert time values (seconds) to number of samples
        attack_samples = int(attack * self.sample_rate)
        decay_samples = int(decay * self.sample_rate)
        release_samples = int(release * self.sample_rate)

        # Create array to hold envelope values for this audio block
        envelope = np.ones(num_samples)

        # Check if this note has been released
        is_released = frequency in self.note_release_times

        # Calculate envelope value for each sample in this block
        for i in range(num_samples):
            # Get absolute sample position since note was pressed
            sample_pos = current_sample_position + i

            if is_released:
                # Release phase: fade from current level to 0
                release_start_pos = self.note_release_times[frequency]
                samples_since_release = sample_pos - release_start_pos

                # Linear fade from release level to 0 over release_samples
                if samples_since_release < release_samples:
                    release_level = self.note_envelope_positions.get(frequency, sustain)
                    envelope[i] = release_level * (1.0 - samples_since_release / release_samples)
                else:
                    # Release phase complete, envelope at 0
                    envelope[i] = 0.0
            else:
                # Attack phase: ramp from 0 to 1
                if sample_pos < attack_samples:
                    envelope[i] = sample_pos / attack_samples
                # Decay phase: ramp from 1 down to sustain level
                elif sample_pos < attack_samples + decay_samples:
                    decay_progress = (sample_pos - attack_samples) / decay_samples
                    envelope[i] = 1.0 - (1.0 - sustain) * decay_progress
                # Sustain phase: hold at sustain level
                else:
                    envelope[i] = sustain

        return envelope

    #Refactor these
    def generate_wave(self, frequency, num_samples, start_phase, wave_type):
        # Phase-based sine wave generation for continuous synthesis without clicking
        # Calculate how much phase advances per sample: 2π * frequency / sample_rate
        phase_increment = 2 * np.pi * frequency / self.sample_rate
        # Create array of phase values starting from start_phase and incrementing by phase_increment
        phases = start_phase + np.arange(num_samples) * phase_increment
        # Generate sine wave from phase values
        if wave_type == 1:
            wave = np.sin(phases)
        elif wave_type == 2:
            wave = np.sign(np.sin(phases))
        elif wave_type == 3:
            wave = 2 * (phases / (2 * np.pi) % 1.0) - 1
        elif wave_type == 4:
            sawtooth = 2 * (phases / (2 * np.pi) % 1.0) - 1
            wave = 2 * np.abs(sawtooth) - 1
        
        return wave, phases[-1] % (2 * np.pi)


    def audio_callback(self, outdata, frames, time_info, status):
        # This callback runs in a separate thread and is called automatically by sounddevice
        # It must fill outdata with exactly 'frames' samples

        # Get list of currently pressed note frequencies from keyboard
        music = self.controller.notes_played[:]

        # For monophonic mode: only play the most recently pressed note
        if len(music) > 0:
            current_frequency = music[-1]
            music = [current_frequency]

            # Transfer phase from previous note to new note for smooth transition
            if self.previous_frequency is not None and current_frequency != self.previous_frequency:
                if self.previous_frequency in self.phase_accumulators and current_frequency not in self.phase_accumulators:
                    self.phase_accumulators[current_frequency] = self.phase_accumulators[self.previous_frequency]

            self.previous_frequency = current_frequency
        else:
            self.previous_frequency = None

        # Track note press times for ADSR envelope timing
        active_frequencies = set(music)
        for freq in active_frequencies:
            # Initialize timing for newly pressed notes
            if freq not in self.note_press_times:
                self.note_press_times[freq] = 0
                self.note_envelope_positions[freq] = 0.0
            # If note was released but is now pressed again, remove release state
            if freq in self.note_release_times:
                del self.note_release_times[freq]

        # Track note release times for release phase of ADSR
        for freq in list(self.note_press_times.keys()):
            # If note is no longer active and hasn't been marked as released yet
            if freq not in active_frequencies and freq not in self.note_release_times:
                # Mark release time and save current envelope level for release fade
                self.note_release_times[freq] = self.note_press_times[freq]
                current_env = self.note_envelope_positions.get(freq, 0.0)
                self.note_envelope_positions[freq] = current_env

        # Mark inactive frequencies for delayed cleanup
        for freq in list(self.phase_accumulators.keys()):
            if freq not in active_frequencies:
                if freq not in self.phase_cleanup_delay:
                    self.phase_cleanup_delay[freq] = 0
                self.phase_cleanup_delay[freq] += 1

        # Remove phase accumulators after 10 blocks of inactivity
        keys_to_remove = [freq for freq, count in self.phase_cleanup_delay.items() if count > 10]
        for freq in keys_to_remove:
            del self.phase_accumulators[freq]
            del self.phase_cleanup_delay[freq]
            # Clean up ADSR tracking dictionaries for removed notes
            if freq in self.note_press_times:
                del self.note_press_times[freq]
            if freq in self.note_release_times:
                del self.note_release_times[freq]
            if freq in self.note_envelope_positions:
                del self.note_envelope_positions[freq]

        # Reset cleanup counter for active frequencies
        for freq in active_frequencies:
            if freq in self.phase_cleanup_delay:
                del self.phase_cleanup_delay[freq]

        # Collect all frequencies to render (active notes + notes in release phase)
        all_frequencies = set(music) | set(self.note_release_times.keys())

        # If no notes are being played or releasing, send silence
        if len(all_frequencies) == 0:
            outdata[:] = np.zeros((frames, 1), dtype='float32')
        else:
            oscillators = [self.osc1, self.osc2, self.osc3]
            active_oscillators = [osc for osc in oscillators if osc.wave_type.get() != 0]

            # If no oscillators are active, send silence
            if len(active_oscillators) == 0:
                outdata[:] = np.zeros((frames, 1), dtype='float32')
            else:
                combined_wave = np.zeros(frames)

                for frequency in all_frequencies:
                    if frequency not in self.phase_accumulators:
                        self.phase_accumulators[frequency] = 0.0

                    current_phase = self.phase_accumulators[frequency]
                    note_wave = np.zeros(frames)

                    for osc in active_oscillators:
                        wave_type = osc.wave_type.get()
                        if wave_type < 1:
                            wave = np.zeros(frames)
                            final_phase = current_phase

                        else:
                            wave, final_phase = self.generate_wave(frequency, frames, current_phase, wave_type)
                        wave *= osc.volume.get()
                        note_wave += wave

                    self.phase_accumulators[frequency] = final_phase
                    note_wave /= len(active_oscillators)

                    if self.adsr.filter_enabled.get():
                        current_sample_position = self.note_press_times[frequency]
                        envelope = self.generate_adsr_envelope(frequency, frames, current_sample_position)
                        self.note_envelope_positions[frequency] = envelope[-1]
                        note_wave *= envelope

                    self.note_press_times[frequency] += frames
                    if frequency in self.note_release_times:
                        self.note_release_times[frequency] += frames

                    combined_wave += note_wave

                combined_wave /= max(len(all_frequencies), 1)
                combined_wave *= self.amplitude
                max_val = np.max(np.abs(combined_wave))
                if max_val > 1.0:
                    combined_wave /= max_val

                outdata[:] = combined_wave.reshape(-1, 1).astype('float32')

    def start_audio_stream(self):
        # Create audio output stream with callback
        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype='float32',
            blocksize=480,
            latency='low',  # Larger blocksize for more stable audio
            callback=self.audio_callback
        )
        self.stream.start()

class KeyboardFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent, width=1000, height=500)

        image_original = Image.open(r'Assets/piano.jpg').resize((1000,500))
        self.keyboard_img = ImageTk.PhotoImage(image_original)
        self.notes_played = []
        self.widgets()
        self.placement()
        self.bindings()

    def widgets(self):
        self.keyboard = ttk.Label(self, image=self.keyboard_img)
        self.label1 = ttk.Label(self, text='A', font='fixedsys 24 bold')
        self.label2 = ttk.Label(self, text='S', font='fixedsys 24 bold')
        self.label3 = ttk.Label(self, text='D', font='fixedsys 24 bold')
        self.label4 = ttk.Label(self, text='F', font='fixedsys 24 bold')
        self.label5 = ttk.Label(self, text='G', font='fixedsys 24 bold')
        self.label6 = ttk.Label(self, text='H', font='fixedsys 24 bold')
        self.label7 = ttk.Label(self, text='J', font='fixedsys 24 bold')
        self.label8 = ttk.Label(self, text='K', font='fixedsys 24 bold')
        self.label9 = ttk.Label(self, text='W', font='fixedsys 24 bold', background='white', foreground='black')
        self.label10 = ttk.Label(self, text='E', font='fixedsys 24 bold', background='white', foreground='black')
        self.label11 = ttk.Label(self, text='T', font='fixedsys 24 bold', background='white', foreground='black')
        self.label12 = ttk.Label(self, text='Y', font='fixedsys 24 bold', background='white', foreground='black')
        self.label13 = ttk.Label(self, text='U', font='fixedsys 24 bold', background='white', foreground='black')

        self.original_bg = self.label1.cget('background')

        self.key_map = {
            'a': (self.label1, self.original_bg, 261.63),
            's': (self.label2, self.original_bg, 293.66),
            'd': (self.label3, self.original_bg, 329.63),
            'f': (self.label4, self.original_bg, 349.23),
            'g': (self.label5, self.original_bg, 392.00),
            'h': (self.label6, self.original_bg, 440.00),
            'j': (self.label7, self.original_bg, 493.88),
            'k': (self.label8, self.original_bg, 523.25),
            'w': (self.label9, 'white', 277.18),
            'e': (self.label10, 'white', 311.13),
            't': (self.label11, 'white', 369.99),
            'y': (self.label12, 'white', 415.30),
            'u': (self.label13, 'white', 466.16)
        }
    def placement(self):
        self.keyboard.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.label1.place(relx=0.0625, rely=.75, anchor='center')
        self.label2.place(relx=0.1875, rely=.75, anchor='center')
        self.label3.place(relx=0.3125, rely=.75, anchor='center')
        self.label4.place(relx=0.4375, rely=.75, anchor='center')
        self.label5.place(relx=0.5625, rely=.75, anchor='center')
        self.label6.place(relx=0.6875, rely=.75, anchor='center')
        self.label7.place(relx=0.8125, rely=.75, anchor='center')
        self.label8.place(relx=0.9375, rely=.75, anchor='center')
        self.label9.place(relx=0.125, rely=.5, anchor='center')
        self.label10.place(relx=0.25, rely=.5, anchor='center')
        self.label11.place(relx=0.5, rely=.5, anchor='center')
        self.label12.place(relx=0.625, rely=.5, anchor='center')
        self.label13.place(relx=0.75, rely=.5, anchor='center')

    def bindings(self):
        keylist = ['a', 'A', 's', 'S', 'd', 'D','f', 'F','g', 'G', 'h', 'H','j', 'J','k', 'K','w', 'W','e', 'E','t', 'T','y', 'Y', 'u', 'U']
        for key in keylist: 
            self.master.bind(f'<KeyPress-{key}>', self.handle_key_press)
            self.master.bind(f'<KeyRelease-{key}>', self.handle_key_release)
        
    def handle_key_press(self, event):
        key = event.char.lower()
        if key in self.key_map:
            label, original_bg, frequency = self.key_map[key]
            label.config(background='blue')
            if frequency not in self.notes_played:
                self.notes_played.append(frequency)

    def handle_key_release(self, event):
        key = event.char.lower()
        if key in self.key_map:
            label, original_bg, frequency = self.key_map[key]
            label.config(background=original_bg)
            self.notes_played = [i for i in self.notes_played if i != frequency]
class MainWin(ttk.Window):
    def __init__(self):
        super().__init__(themename='cyborg')
        self.resizable(False, False)

        self.frames()
        self.placement()
        self.mainloop()

    def frames(self):
        self.keyboard = KeyboardFrame(self)
        self.synth = SynthFrame(self, self.keyboard)

    def placement(self):
        self.synth.pack()
        self.keyboard.pack()

if __name__ == '__main__':
    sd.default.device = (sd.default.device[0], 8)
    window = MainWin()