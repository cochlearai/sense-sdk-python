# Sense SDK for Python

In order to run Sense SDK, you would require SDK key and Sense SDK Python package. Please contact us by e-mail (support@cochlear.ai) to get your key, which is mandatory to use Sense SDK.

## Getting started

### Ubuntu 18.04
#### 1. Prerequisites and Dependencies

Install system packages as required by Sense SDK Python:
```
$ sudo apt-get update
$ sudo apt-get install build-essential libffi-dev libssl-dev swig python3 python3-dev python3-pip python3-virtualenv ffmpeg sox portaudio19-dev virtualenv
```

#### 2. Setting Python virtual environment

```
$ virtualenv -p python3 --no-site-packages venv
$ . venv/bin/activate
(venv) $ pip install -U pip
```

#### 3. Installing Sense SDK Python

```
(venv) $ pip install sense_sdk_python-0.1-py3-none-linux_x86_64.whl
```

### NVIDIA Jetson Nano
#### 1. Prerequisites and Dependencies

Sense SDK Python uses TensorFlow as the deep learning engine to predict the audio data. So, it is necessary to install TensorFlow first before the Sense SDK Python installation.

Install system packages as required by TensorFlow:
```
$ sudo apt-get update
$ sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
```

Install system packages as required by Sense SDK Python:
```
$ sudo apt-get install build-essential libffi-dev libssl-dev swig python3 python3-dev python3-pip python3-venv ffmpeg sox portaudio19-dev virtualenv
```

#### 2. Setting Python virtual environment
```
$ virtualenv -p python3 --no-site-packages venv
$ . venv/bin/activate
(venv) $ pip install -U pip
```

#### 3. Installing Sense SDK Python

Install customized TensorFlow for Nvidia Jetson Nano:
```
(venv) $ pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu==1.14.0+nv19.9
```
Refer to [this guide](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html) for more details.


Install Sense SDK Python now:
```
(venv) $ pip install sense_sdk_python-0.1-py3-none-linux_aarch64.whl
```

## Launch Examples

Please **enter your SDK key** in the source code before executing this example.

For testing a audio file, run 
```
(venv) $ python example_file.py
```

For testing a audio stream from your microphone, run 
```
(venv) $ python example_stream.py
```

## How to use Sense SDK Python
Even through _Sense SDK Python_ provides similar API as _Sense API Python_, they are not the same. It is easy to use because of a simple API.

### Audio file prediction

  * example_file.py
```
import json
from cochl.sense_sdk import sense
import pprint
import time

sdkkey = 'ENTER YOUR SDK KEY'
filename = 'AUDIO FILE NAME (.wav, .mp3, .mp4, ...)'
task = 'event'

result = sense(filename, sdkkey, task)
result = json.loads(result.outputs)
pprint.pprint(result)
```

Create the **sense** object and get the **output** member variable of _sense_ object. That's all.

### Audio stream prediction

  * example_stream.py
```
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
```
**Check whether your microphone is working or not** before doing audio stream prediction. SenseStreamer object records the audio via the microphone and returns the result of prediction about the audio data each half-second.

Note that the below JSON structure is the same as that of Sense API, while its analysis results may slightly differ. 

  * JSON result format
```
{
    "status"        : {
        "code"          : <Status code>,
        "description"   : "<Status code description>"
    },
    "result": {
        "task"      : "<TASK NAME>",
        "frames"    : [
            {
                "tag"           : "<CLASS NAME>",
                "probability"   : <Probability value (float) for 'CLASS NAME'>,
                "start_time"    : <Prediction start time in audio file>,
                "end_time"      : <Prediction end time in audio file>,
            },
            (...)
        ],
        "summary"   : [
            {
                "tag"           : "<CLASS NAME>",
                "probability"   : <Probability mean value (float) for continuous tags>,
                "start_time"    : <Prediction start time in first tag>,
                "end_time"      : <Prediction end time in last tag>,
            },
            (...)
        ]
    }
}
```
