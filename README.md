# Sense SDK for Python

In order to run Sense SDK, you would require SDK key and Sense SDK Python package. Please contact us by e-mail (support@cochlear.ai) to get your key, which is mandatory to use Sense SDK.

## Service
### Emergency
Sense API Emergency can detect sounds that can be a clue for an emergency occurring in our daily lives. For instance, it can be used for detecting domestic violence, physical altercation, house break-in, or fire alerts.

- Fire_smoke_alarm
- Glassbreak
- Scream
- Siren

### Human-interaction
Sense API Human-interaction allows computers to understand various human-generated sounds that can be used for interaction. For instance, you can make a system that turns on light with a finger snap, or whistling to call a horse in a game.

- Clap
- Finger_snap
- Knock
- Whisper
- Whistling

> **_Note:_** Clap sounds are well recognized when there is a clean single clap or double clap

## Getting started

### 1. Prerequisites and Dependencies

Install system packages as required by Sense SDK Python. It depends on the target system.

  * **Ubuntu 18.04 (x86-64)**

```sh
$ sudo apt-get update
$ sudo apt-get install ffmpeg sox portaudio19-dev virtualenv libssl-dev libcurl4-openssl-dev python3-dev
```

  * **Mac OS X (x86-64)**

Install brew(https://brew.sh/) first.
```sh
$ brew update
$ brew install openssl portaudio pyenv python3 wget ffmpeg sox
```

  * **Raspberry Pi 3 (ARM 32)**

```sh
$ sudo apt-get update
$ sudo apt-get install ffmpeg sox portaudio19-dev virtualenv libatlas-base-dev libssl-dev libcurl4-openssl-dev python3-pyaudio python3-dev

```

  * **NVIDIA Jetson Nano (ARM 64)**
```sh
$ sudo apt-get update
$ sudo apt-get install ffmpeg sox portaudio19-dev virtualenv python3-dev libffi-dev libssl-dev libcurl4-openssl-dev
```

### 2. Setting Python virtual environment

Create a new virtual environment by choosing a Python interpreter and making a `./venv` directory to hold it:
```sh
$ virtualenv -p python3 --no-site-packages ./venv
```

Activate the virtual environment using a shell-specific command:
```sh
$ source ./venv/bin/activate  # sh, bash, ksh, zsh, ...
```

When virtualenv is active, your shell prompt is prefixed with `(venv)`.
Install packages within a virtual environment without affecting the host system setup. Start by upgrading `pip`:
```sh
(venv) $ pip install --upgrade pip
```

### 3. Installing Sense SDK Python

To install Sense SDK Python, download the appropriate Python wheel for your system from the following table, and then install it with the `pip install` command.

For example, if you're setting up a Jetson Nano (which has Python 3.7), install the Python wheel as follows (after you click to download the .whl file below):

```sh
(venv) $ pip install sense_sdk-0.4.2-cp37-cp37m-linux_aarch64.whl
```
<br />

  * __Supported Targets and Package Files__

|            | Ubuntu 18.04 or higher | Mac OS X |
| :---: | :---  | :---  |
| __Python 3.6__ | sense_sdk-0.4.2-cp36-cp36m-linux_x86_64.whl | sense_sdk-0.4.2-cp36-cp36m-macosx_10_10_x86_64.whl |
| __Python 3.7__ | sense_sdk-0.4.2-cp37-cp37m-linux_x86_64.whl | sense_sdk-0.4.2-cp37-cp37m-macosx_10_10_x86_64.whl |
| __Python 3.8__ | sense_sdk-0.4.2-cp38-cp38m-linux_x86_64.whl | sense_sdk-0.4.2-cp38-cp38-macosx_10_10_x86_64.whl |

| | ARM 64 (Jetson Nano, Coral) | ARM 32 (Raspberry Pi 3)  |
| :---: | :---  | :---   |
| __Python 3.6__ | sense_sdk-0.4.2-cp36-cp36m-linux_aarch64.whl | sense_sdk-0.4.2-cp36-cp36m-linux_armv7l.whl |
| __Python 3.7__ | sense_sdk-0.4.2-cp37-cp37m-linux_aarch64.whl | sense_sdk-0.4.2-cp37-cp37m-linux_armv7l.whl |
| __Python 3.8__ | sense_sdk-0.4.2-cp38-cp38-linux_aarch64.whl | sense_sdk-0.4.2-cp38-cp38-linux_armv7l.whl |

## Launch Examples

Please **set your SDK key** as the environment variable before executing this example.
```sh
$ export SENSE_SDK_KEY=<YOUR SDK KEY>
```

For testing an audio file prediction, run
```sh
(venv) $ python examples/simple_file.py
```

For testing an audio stream prediction from your microphone, run
```sh
(venv) $ python examples/simple_stream.py
```

## How to use Sense SDK Python
Even through _Sense SDK Python_ provides similar API as _Sense API Python_, they are not the same. It is easy to use because of a simple API.

### Audio file prediction

Import `SenseFile` into your program:
```python
from cochl.sense_sdk import SenseFile
```

Create SenseFile object with _SDK key_ and _task_ parameters:
```python
import os
sdk_key = os.environ['SENSE_SDK_KEY']
task = 'emergency'

sense_file = SenseFile(sdk_key, task)
```

Add the audio file name as a parameter of `predict()` method. Then the prediction result about the audio file will be returned.

  * **Supported audio file formats**: `mp3`, `wav`, `ogg`, `flac`, `mp4`
```python
result = sense_file.predict('some_audio_file.wav')
```

The result format is [JSON](https://en.wikipedia.org/wiki/JSON). You can use conveniently the result using `json.loads()`:
```python
import json
import pprint

result = json.loads(result)
pprint.pprint(result)
```

Note that the below JSON structure is the same as that of Sense API, while its analysis results may slightly differ.

  * JSON result format
```xml
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
The full example code is shown below:

  * example_file.py
```python
import json
import os
import pprint
from cochl.sense_sdk import SenseFile

sdkkey = os.environ['SENSE_SDK_KEY']
filename = 'examples/sample_audio/glassbreak.wav'
task = 'emergency'

sense_file = SenseFile(sdkkey, task)
result = sense_file.predict(filename)
result = json.loads(result)
pprint.pprint(result)
```

  * result
```bash
(venv) $ python example_file.py
INFO: Initialized TensorFlow Lite runtime.
{'result': {'frames': [{'end_time': '1.0',
                        'probability': '0.9407',
                        'start_time': '0.0',
                        'tag': 'Glass_break'},
                       {'end_time': '1.5',
                        'probability': '0.9445',
                        'start_time': '0.5',
                        'tag': 'Glass_break'}],
            'summary': [{'end_time': 1.5,
                         'probability': 0.9426,
                         'start_time': 0.0,
                         'tag': 'Glass_break'}],
            'task': 'emergency'},
 'status': {'code': 200, 'description': 'OK'}}
```

### Audio stream prediction

**Check whether your microphone is working or not** before doing audio stream prediction.

Import `SenseStreamer` into your program:
```python
from cochl.sense_sdk import SenseStreamer
```

SenseStreamer object records the audio via the microphone and returns the result of prediction about the audio data each half-second.
We recommend using `with` statement of the SenseStreamer object. SenseStreamer object supports `record()` method to record real-time audio and `predict()` method to predict the audio stream data.

  * example_stream.py
```python
import json
import pprint
from cochl.sense_sdk import SenseStreamer

sdkkey = os.environ['SENSE_SDK_KEY']
task = 'human-interaction'

with SenseStreamer(sdkkey, task) as stream:
    audio_generator = stream.generator()
    for stream_data in stream.record(audio_generator):
        result = stream.predict(stream_data)
        result = json.loads(result)
        pprint.pprint(result)
```

  * result
```bash
(venv) $ python example_stream.py
INFO: Initialized TensorFlow Lite runtime.
{'result': {'frames': [{'end_time': '1.0',
                        'probability': '0.9023',
                        'start_time': '0.0',
                        'tag': None}],
            'summary': [],
            'task': 'human-interaction'},
 'status': {'code': 200, 'description': 'OK'}}
{'result': {'frames': [{'end_time': '1.5',
                        'probability': '0.8562',
                        'start_time': '0.5',
                        'tag': 'Whistling'}],
            'summary': [],
            'task': 'human-interaction'},
 'status': {'code': 200, 'description': 'OK'}}
{'result': {'frames': [{'end_time': '2.0',
                        'probability': '0.8946',
                        'start_time': '1.0',
                        'tag': 'Whistling'}],
            'summary': [],
            'task': 'human-interaction'},
(......)
```

The input device can be a parameter of `generator()` method:
```python
    audio_generator = stream.generator(input_device='USB Audio')
```
  * **NOTE**: you can check the input audio device name using `arecord -l` command.

## Reference
### SenseFile
```
cochl.sense_sdk
  Sense
    SenseFile
```
Audio file prediction model class.

#### `__init__`
```python
__init__(self, sdkkey, task)
```
Creates an `SenseFile` object.

**Args:**
  * **`sdkkey`**: Your SDk key to authenticate SDK
  * **`task`**: Task means what kinds of service you use.
    * *Current supported tasks = [**"emergency", "human-interaction"**]*

#### `predict`
```python
predict(self, file_name)
```
Returns the result of the audio file prediction (JSON format).

**Args:**
  * **`file_name`**: Audio file name to predict

### SenseStreamer
```
cochl.sense_sdk
  Sense
    SenseStreamer
```
Audio stream prediction model class.

#### `__init__`
```python
__init__(self, sdkkey, task)
```
Creates an `SenseStreamer` object.

**Args:**
  * **`sdkkey`**: Your SDk key to authenticate SDK
  * **`task`**: Task means what kinds of service you use.
    * *Current supported tasks = [**"emergency", "human-interaction"**]*

#### `generator`
```python
generator(self, input_device=None)
```
Returns the recorded audio data generator.

**Args:**
  * **`input_device`**: Recording device like a microphone

#### `record`
```python
record(self, generator)
```
Returns the recorded audio data list.

**Args:**
  * **`generator`**: Audio data generator of SenseStreamer

#### `predict`
```python
predict(self, stream_data)
```
Returns the result of the audio stream prediction (JSON format).

**Args:**
  * **`stream_data`**: Audio stream data to predict

#### `stop`
```python
stop(self)
```
Stop the recording audio stream
