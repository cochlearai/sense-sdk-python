# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
