---
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - radio
  - sigint
  - decoding
  - pocsag
  - afsk
url: 'https://github.com/EliasOenal/multimonNG'
commands:
  - '[[commands/multimon-ng-decode-pocsag-from-wav]]'
  - '[[commands/multimon-ng-realtime-pocsag-decoding]]'
  - '[[commands/multimon-ng-decode-multiple-modes]]'
validated: true
---

# multimon-ng

**Status**: Unverified

## Overview

Multimon-ng is an enhanced fork of the original multimon tool, specialized in decoding various digital radio transmission modes. It is primarily used in signals intelligence (SIGINT), radio frequency (RF) reconnaissance, and security testing to intercept and interpret unencrypted radio communications such as pager messages, emergency alerts, and control signals.

## Description

Multimon-ng processes audio inputs to demodulate and decode protocols like POCSAG (for pagers), EAS (Emergency Alert System), multiple FSK/AFSK variants, DTMF tones, ZVEI signaling, and Morse code. It supports both file-based analysis and real-time monitoring, making it a key tool for passive collection in environments with radio-based systems, such as industrial controls or emergency services.

## Features

- Demodulation of POCSAG512, POCSAG1200, POCSAG2400 for pager decoding
- EAS support for emergency broadcast interpretation
- UFSK1200, CLIPFSK, AFSK1200/2400 variants for frequency-shift keying signals
- HAPN4800, FSK9600 for higher-speed digital modes
- DTMF, ZVEI1/2/3, DZVEI, PZVEI for tone-based signaling
- EEA, EIA, CCIR for European radio standards
- MORSE and CW (Continuous Wave) decoding
- Multi-mode simultaneous processing
- Audio input from files (WAV/raw) or live sources (stdin/microphone)

## Installation

### Requirements

- Linux system with audio libraries (ALSA/PulseAudio)
- Build essentials: gcc, make, libfftw3-dev, libx11-dev, libpulse-dev

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install git build-essential libfftw3-dev libx11-dev libpulse-dev

git clone https://github.com/EliasOenal/multimonNG.git
cd multimonNG
make
sudo make install
```

On Kali Linux (often pre-installed):

```bash
sudo apt update
sudo apt install multimon-ng
```

For macOS (via Homebrew, experimental):

```bash
brew install multimon-ng
```

## Basic Usage

```bash
multimon-ng -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -a <mode> | Demodulation mode (e.g., -a POCSAG512) |
| -t <type> | Input type (wav, raw) |
| -i <file> | Input audio file |
| -A | Audio from stdin (for piping from mic) |
| -f | Force raw audio format |
| -v | Verbose output (if compiled with debug) |

## Examples

### Example 1: Basic Usage

Decode a POCSAG signal from a WAV file:

See [[commands/multimon-ng-decode-pocsag-from-wav]]

### Example 2: Advanced Usage

Real-time monitoring:

See [[commands/multimon-ng-realtime-pocsag-decoding]]

Multiple modes:

See [[commands/multimon-ng-decode-multiple-modes]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing (extended to radio signal interception)
- [[Gather Victim Host Information]] Gather Victim Host Information (via signal decoding)

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control (intercepting radio C2)

## Detection

Indicators and methods for detecting this tool's usage:

- Running processes: `multimon-ng` with audio device access
- Audio captures in /tmp or working directories
- High CPU usage during real-time decoding
- Log entries for audio library interactions (ALSA/PulseAudio)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rtl-sdr]] (for RF signal capture to audio)
- [[tools/gnuradio]] (advanced RF processing)
- [[tools/audacity]] (audio file editing and export)

## References

- Official GitHub Repository: https://github.com/EliasOenal/multimonNG
- Original Multimon: http://www.baycom.de/hardware/multimon/
- RF Decoding Guide: https://www.rtl-sdr.com/
