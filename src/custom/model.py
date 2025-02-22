import logging
import openai
from dotenv import load_dotenv
from custom.audio import pcm_to_wave_filelike
from .config import config

load_dotenv(dotenv_path=config['env'])
client = openai.OpenAI(base_url=config['endpoint'])

class STTModel():
    def __init__(self):
        logging.debug("STTModel initialized!")

    '''
    Transcribes an input WAV file that contains speech.

    Returns (str) the transcribed text.
    '''
    def __call__(self, audio, sample_rate, sample_width, channels):
        logging.debug("Got transcription request.")
        wav_buffer = pcm_to_wave_filelike(audio, sample_rate, sample_width, channels)
        result = client.audio.transcriptions.create(
            model=config['model'],
            file=wav_buffer,
            language=config['language'],
            prompt=config['prompt'],
            temperature=config['temperature'],
            response_format="verbose_json"
        )

        logging.debug(f"Got transcription result: {result}")
        return result.text