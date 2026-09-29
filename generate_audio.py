import math
import struct
import wave
import os

def create_spiderman_theme_wav(filepath):
    sample_rate = 44100
    bpm = 132
    beat_dur = 60.0 / bpm
    
    # Note Frequencies
    N = {
        'REST': 0,
        'C3': 130.81, 'D3': 146.83, 'Eb3': 155.56, 'E3': 164.81, 'F3': 174.61, 'G3': 196.00, 'A3': 220.00, 'Bb3': 233.08, 'B3': 246.94,
        'C4': 261.63, 'D4': 293.66, 'Eb4': 311.13, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'Bb4': 466.16, 'B4': 493.88,
        'C5': 523.25, 'D5': 587.33, 'Eb5': 622.25, 'E5': 659.25, 'F5': 698.46, 'G5': 783.99, 'A5': 880.00, 'Bb5': 932.33, 'C6': 1046.50
    }
    
    # [lead_note, bass_note, beats, chord_type]
    score = [
        # Intro Drum / Bass groove (2 bars)
        ('REST', 'E3', 0.5, 'e_min'),
        ('REST', 'E3', 0.5, 'e_min'),
        ('REST', 'G3', 0.5, 'e_min'),
        ('REST', 'A3', 0.5, 'e_min'),
        ('REST', 'E3', 0.5, 'e_min'),
        ('REST', 'E3', 0.5, 'e_min'),
        ('REST', 'D3', 0.5, 'e_min'),
        ('REST', 'B2', 0.5, 'e_min'),

        # Verse 1: "Spider-Man, Spider-Man"
        ('E4', 'E3', 0.75, 'e_min'),
        ('G4', 'E3', 0.75, 'e_min'),
        ('A4', 'A3', 1.5, 'a_min'),
        ('REST', 'A3', 0.5, 'a_min'),

        ('E4', 'E3', 0.75, 'e_min'),
        ('G4', 'E3', 0.75, 'e_min'),
        ('A4', 'A3', 1.5, 'a_min'),
        ('REST', 'A3', 0.5, 'a_min'),

        # "Does whatever a spider can"
        ('C5', 'C4', 0.5, 'c_maj'),
        ('B4', 'B3', 0.5, 'b_dom'),
        ('A4', 'A3', 0.5, 'a_min'),
        ('G4', 'E3', 0.5, 'e_min'),
        ('A4', 'A3', 0.5, 'a_min'),
        ('G4', 'E3', 0.5, 'e_min'),
        ('E4', 'E3', 1.75, 'e_min'),
        ('REST', 'E3', 0.25, 'e_min'),

        # Verse 2: "Spins a web, any size"
        ('A4', 'A3', 0.75, 'a_min'),
        ('C5', 'A3', 0.75, 'a_min'),
        ('D5', 'D4', 1.5, 'd_min'),
        ('REST', 'D3', 0.5, 'd_min'),

        ('A4', 'A3', 0.75, 'a_min'),
        ('C5', 'A3', 0.75, 'a_min'),
        ('D5', 'D4', 1.5, 'd_min'),
        ('REST', 'D3', 0.5, 'd_min'),

        # "Catches thieves just like flies"
        ('F5', 'F4', 0.5, 'f_maj'),
        ('E5', 'E4', 0.5, 'e_min'),
        ('D5', 'D4', 0.5, 'd_min'),
        ('C5', 'A3', 0.5, 'a_min'),
        ('D5', 'D4', 0.5, 'd_min'),
        ('C5', 'A3', 0.5, 'a_min'),
        ('A4', 'A3', 1.75, 'a_min'),
        ('REST', 'A2', 0.25, 'a_min'),

        # Climax: "Look out! Here comes the Spider-Man!"
        ('E4', 'E3', 0.75, 'e_min'),
        ('G4', 'E3', 0.75, 'e_min'),
        ('A4', 'A3', 1.0, 'a_min'),
        ('C5', 'C4', 1.0, 'c_maj'),
        ('B4', 'B3', 1.0, 'b_dom'),
        ('A4', 'A3', 2.0, 'a_min'),
        ('REST', 'A2', 1.0, 'a_min'),
    ]

    total_duration = sum(item[2] * beat_dur for item in score)
    total_samples = int(total_duration * sample_rate)
    
    samples = [0.0] * total_samples
    
    current_sample = 0
    for lead_note, bass_note, beats, chord_type in score:
        dur_sec = beats * beat_dur
        num_samples = int(dur_sec * sample_rate)
        
        f_lead = N.get(lead_note, 0)
        f_bass = N.get(bass_note, 0)
        
        for i in range(num_samples):
            idx = current_sample + i
            if idx >= total_samples:
                break
            
            t = i / sample_rate
            val = 0.0
            
            # Envelope
            env = math.exp(-t * 1.8) if t < dur_sec else 0.0
            if t < 0.03:
                env *= (t / 0.03) # quick attack
                
            # 1. Heroic Brass Lead (Sawtooth + Triangle + Harmonic)
            if f_lead > 0:
                # Primary saw
                saw = 2.0 * ( (t * f_lead) - math.floor(0.5 + t * f_lead) )
                # Triangle octave harmonic
                tri = 2.0 * abs( 2.0 * (t * (f_lead * 2) - math.floor(t * (f_lead * 2) + 0.5)) ) - 1.0
                # Warm Sine Body
                sine = math.sin(2.0 * math.pi * f_lead * t)
                
                lead_sig = (saw * 0.45 + tri * 0.35 + sine * 0.2) * env
                val += lead_sig * 0.55
                
            # 2. Punchy Electric Bass (Square + Sub sine)
            if f_bass > 0:
                bass_env = math.exp(-t * 3.5)
                if t < 0.02:
                    bass_env *= (t / 0.02)
                sqr = 1.0 if math.sin(2.0 * math.pi * f_bass * t) > 0 else -1.0
                sub = math.sin(2.0 * math.pi * (f_bass / 2) * t)
                val += (sqr * 0.3 + sub * 0.7) * bass_env * 0.35
                
            # 3. Drum beat (Kick on beat 1 & 3, Snare/Hi-hat on 2 & 4)
            beat_pos = (t / beat_dur) % 1.0
            if beat_pos < 0.15:
                # Kick drum
                kick_t = beat_pos * beat_dur
                kick_f = max(40.0, 150.0 - kick_t * 600.0)
                kick_env = math.exp(-kick_t * 28.0)
                val += math.sin(2.0 * math.pi * kick_f * kick_t) * kick_env * 0.3
            
            # Snare click
            if 0.45 <= (t / beat_dur) % 1.0 <= 0.65:
                snare_t = ((t / beat_dur) % 1.0 - 0.45) * beat_dur
                noise = ((math.sin(i * 9999.0) * 43758.5453) % 1.0) * 2.0 - 1.0
                snare_env = math.exp(-snare_t * 35.0)
                val += noise * snare_env * 0.18

            samples[idx] += val
            
        current_sample += num_samples

    # Normalize samples to avoid clipping
    max_val = max(abs(s) for s in samples) or 1.0
    norm_factor = 0.88 / max_val
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(1) # Mono
        wav_file.setsampwidth(2) # 16-bit
        wav_file.setframerate(sample_rate)
        
        packed_frames = bytearray()
        for s in samples:
            sample_val = int(max(-32767, min(32767, s * norm_factor * 32767)))
            packed_frames.extend(struct.pack('<h', sample_val))
            
        wav_file.writeframes(packed_frames)
    print(f"Generated Spider-Man theme: {filepath}, Duration: {total_duration:.2f}s")

if __name__ == '__main__':
    target = r"C:\Users\Sachin\.gemini\antigravity\scratch\sachin_portfolio\static\audio\spiderman_theme.wav"
    create_spiderman_theme_wav(target)
