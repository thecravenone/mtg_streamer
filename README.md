# mtg_streamer

v0.0.1

## About

This is the begining of my attempt to create an easy way for amateurs to stream live Magic: The Gathering tournaments.

This version is little more than proof of concept.

NB: This has only been tested with my Ubuntu desktop with the following version:

* Ubuntu 18.04.2
* Python 3.6.7
* Tkinter 8.6
* OBS 0.0.1 (I know that's weird but that's what's in the Ubuntu repos)

## To use

### Setup

1. Clone the repo with `git clone https://github.com/thecravenone/mtg_streamer`
2. Navigate into the directory that's been downloaded.
3. Run `bash setup.sh` - This updates the OBS scene file with the full path to the output files.
4. Open OBS.
5. Import the OBS scene file via **Scene Collection** > **Import** > (Navigate to your `obs_setup.json`)
6. Switch to the new scene via **Scene Collection** > **MTG_Streamer**
7. Launch the Scorekeeper's GUI with `python3 mtg.py`

### While Streaming

**Note that OBS only polls files once per second so there will be delay in your changes being reflected on stream**

To edit player names or decks, fill the appropriate text fields and click **Save Changes**. Note that this will update the information from _all_ text fields.

To adjust life, click the appropriate player's **+** or **-** symbol once for each life gained or lost.

To reset to default, close the GUI and relaunch with `python3 mtg.py`.

## TODO

* Reset players to 20-20 button
* Reset player/deck names to default
* Display changes in UI only with a click button to send all changes at once
* More Windows-friendly build
