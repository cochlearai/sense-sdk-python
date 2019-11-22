import json
import pprint

from cochl.sense_sdk import SenseStreamer

sdkkey = 'ENTER YOUR SDK KEY'
task = 'event'

with SenseStreamer(sdkkey, task) as stream:
    audio_generator = stream.generator()
    for stream_data in stream.record(audio_generator):
        result = stream.predict(stream_data)
        result = json.loads(result)
        pprint.pprint(result)
