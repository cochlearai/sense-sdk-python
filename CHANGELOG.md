# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.1] - 2020-04-08
### Changed
- Supported model
  - `event` -> `emergency` and `human-interaction`

## [0.4.0] - 2020-02-10
### Added
- Multi-threads inference
- Mac OS X support
- Ubuntu 16.04 support

## [0.3.1] - 2020-01-22
### Changed
- .whl file name of Python abi part, `py3-none` to `cp36-cp36m`, `cp37-cp37m`, `cp38-cp38m`

### Fixed
- .whl package installation problem due to the new pip version >= 20.0.x

## [0.3.0] - 2020-01-17
### Added
- More sound event detection by the event model (`14` new classes, `34` total classes)
  - 'Bicycle_belli', 'Birds', 'Burping', 'Cat_meow', 'Clap', 'Crowd_applause', 'Crowd_scream'
  - 'Explosion', 'Finger_snap', 'Keyboard_mouse', 'Mosquito', 'Sigh', 'Whisper', 'Wind_noise'
- New library dependencies
  - `libcurl`, `libssl`
- Supported sound events label file

### Changed
- Audio recording package `sounddevice` to `pyaudio`
- Authorization routine as native C++
- Result post-processing to more simplify
- Deep learning inference part as native C++

### Fixed
- Audio stream accuracy drop from the poor audio recording method

## [0.2.0] - 2019-11-22
### Added
- New event model which is improved performance about 4% in the internal test set
- Support ARM 32 architecture including Raspberry Pi 3.
- TFLite runtime deep learning engine as built-in.
- REST call parameters for SDK authentication - 'version' and 'sdk_type'
- Multiple files inference example
- Audio stream pause & resume example
- `predict()` method in SenseFile class
- `./examples` directory to contain example source files

### Changed
- Sense SDK Python package name is changed from `sense-sdk-python` to `sense-sdk`
- `sense` class name is change to `SenseFile`
- `SenseFile` constructor parameter is changed `__init__(filename, sdkkey, task)` to `__init__(sdkkey, task)`
- `generator()` method interface in SenseStreamer, `generator()` to `generator(input_device=None)`
- Class hierarchy

### Fixed
- Invalid SDK key handling

### Removed
- Tensorflow package dependency

## [0.1.1] - 2019-10-11
### Added
- First release
