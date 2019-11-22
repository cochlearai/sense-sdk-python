import json
from cochl.sense_sdk import sense
import pprint
import time

sdkkey ='ENTER YOUR SDK KEY'
filename = 'test_samples/event/babycry.wav'
task = 'event'

result = sense(filename, sdkkey, task)
result = json.loads(result.outputs)
pprint.pprint(result)
