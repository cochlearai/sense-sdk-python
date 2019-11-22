import json
import os
import pprint
from os.path import isfile, join
from cochl.sense_sdk import SenseFile

sdkkey = os.environ['SENSE_SDK_KEY']
file_path = os.path.dirname(os.path.abspath(__file__)) + '/sample_audio'
task = 'event'

audio_files = [f for f in os.listdir(file_path) if isfile(join(file_path, f))]
sense_file = SenseFile(sdkkey, task)


def main():
    for wav_file in audio_files:
        print("< {} >".format(wav_file))
        result = sense_file.predict(join(file_path, wav_file))
        result = json.loads(result)
        pprint.pprint(result)


if __name__ == "__main__":
    main()
