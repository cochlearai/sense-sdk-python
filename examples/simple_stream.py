import json
import os
import pprint

from cochl.sense_sdk import SenseStreamer

sdkkey = os.environ['SENSE_SDK_KEY']
task = 'event'


def main():
    with SenseStreamer(sdkkey, task) as sense_stream:
        audio_generator = sense_stream.generator()
        for stream_data in sense_stream.record(audio_generator):
            result = sense_stream.predict(stream_data)
            result = json.loads(result)
            pprint.pprint(result)


if __name__ == "__main__":
    main()
