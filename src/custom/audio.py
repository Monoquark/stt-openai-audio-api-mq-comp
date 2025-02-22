import io
import wave

def pcm_to_wave_filelike(str_bytes, src_sr, src_sw, src_channels):
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wav_file:
            wav_file.setnchannels(src_channels)
            wav_file.setsampwidth(src_sw)
            wav_file.setframerate(src_sr)
            wav_file.writeframes(str_bytes)
        wav_buffer.seek(0)
        # Set file name since this is how OpenAI identifies the format
        wav_buffer.name = "audio.wav"
        return wav_buffer