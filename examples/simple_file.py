import json
import os
import pprint
from cochl.sense_sdk import SenseFile

sdkkey = os.environ['SENSE_SDK_KEY']
audio_file_path = os.path.dirname(os.path.abspath(__file__)) + '/sample_audio'
audio_file_name = 'babycry.wav'
task = 'event'

sense_file = SenseFile(sdkkey, task)


def main():
    file_path = os.path.join(audio_file_path, audio_file_name)
    result = sense_file.predict(file_path)
    result = json.loads(result)
    pprint.pprint(result)


if __name__ == "__main__":
    main()
