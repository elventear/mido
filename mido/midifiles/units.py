def tick2second(tick, ticks_per_beat, tempo, time_signature):
    """Convert absolute time in ticks to seconds.

    Returns absolute time in seconds for a chosen MIDI file time
    resolution (ticks per beat, also called PPQN or pulses per quarter
    note) and tempo (microseconds per beat).
    """
    return tick * tempo * 1e-6 / ticks_per_beat * time_signature[1] / 4.


def second2tick(second, ticks_per_beat, tempo, time_signature):
    """Convert absolute time in seconds to ticks.

    Returns absolute time in ticks for a chosen MIDI file time
    resolution (ticks per beat, also called PPQN or pulses per quarter
    note) and tempo (microseconds per beat).
    """
    return int(second / tempo * 1e-6 / ticks_per_beat * time_signature[1] / 4.)


def bpm2tempo(bpm, time_signature):
    """Convert beats per minute to MIDI file tempo.

    Returns microseconds per beat as an integer::

        240 => 250000
        120 => 500000
        60 => 1000000
    """
    # One minute is 60 million microseconds.
    return int(60 * 1e6 / bpm * time_signature[1] / 4.)


def tempo2bpm(tempo, time_signature):
    """Convert MIDI file tempo to BPM.

    Returns BPM as an integer or float::

        250000 => 240
        500000 => 120
        1000000 => 60
    """
    # One minute is 60 million microseconds.
    return 60 * 1e6 / tempo * time_signature[1] / 4.


def beats2ticks(beats, ticks_per_beat, time_signature):
    """Convert beats to ticks."""
    return int(ticks_per_beat * time_signature[1] / 4. / beats)


def ticks2beats(tick, ticks_per_beat, time_signature):
    """Convert ticks to beats."""
    return tick / ticks_per_beat * time_signature[1] / 4.
