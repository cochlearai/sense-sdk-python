import json
import os
import pprint
import threading
import sys

from cochl.sense_sdk import SenseStreamer

sdkkey = os.environ['SENSE_SDK_KEY']
task = 'human-interaction'

wait_event = threading.Event()
is_pause = False
is_quit = False


def key_handler():
    global is_pause
    global is_quit
    while True:
        ch = sys.stdin.read(1)
        if ch == 'p':  # Pause key
            is_pause = True
        elif ch == 'r':  # Resume key
            is_pause = False
            wait_event.set()
        elif ch == 'q':  # Quit key
            is_quit = True
            break


def main():
    threading.Thread(target=key_handler).start()

    with SenseStreamer(sdkkey, task) as sense_stream:
        audio_generator = sense_stream.generator(input_device='USB Audio')
        for stream_data in sense_stream.record(audio_generator):
            # Key event handling
            if is_pause:  # Pause audio stream prediction
                print("Press 'r' key to resume audio stream prediction")
                wait_event.wait()
                wait_event.clear()
            elif is_quit:
                sense_stream.stop()

            result = sense_stream.predict(stream_data)
            result = json.loads(result)
            pprint.pprint(result)
            print("Press 'p' key to pause audio stream prediction "
                  "('q' for quit)")


if __name__ == "__main__":
    main()
