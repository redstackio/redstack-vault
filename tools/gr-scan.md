---
id: f30f1122-240b-4f10-9436-98e7f2c0c603
type: tool
verified: true
created_at: '2019-08-28T21:17:28.659231+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - wireless
  - reconnaissance
  - sdr
  - gnu-radio
url: 'https://github.com/ghostop/gr-scan'
commands:
  - '[[commands/gr-scan-basic-frequency-scan]]'
  - '[[commands/gr-scan-scan-with-gain]]'
validated: true
---

# gr-scan

**Status**: Unverified

## Overview

gr-scan is a C++ program built on GNU Radio, rtl-sdr, and the OsmoSDR Source Block. It scans specified frequency ranges to detect and list radio signals, making it suitable for wireless reconnaissance and spectrum analysis in security testing. It works with compatible SDR devices, such as Realtek RTL2832U-based dongles with tuners like the E4000.

## Description

gr-scan automates the detection of active transmissions across a frequency band by continuously sampling the spectrum and reporting signal presence. Developed for use with affordable hardware like the Compro U620F or NooElec NESDR, it is particularly useful in red team operations involving RF signal hunting, such as identifying unauthorized wireless devices or mapping spectrum usage in a target environment.

## Features

- Frequency range scanning with customizable start and end points
- Real-time signal detection and logging
- Support for OsmoSDR-compatible devices (RTL-SDR, HackRF, etc.)
- Adjustable RF gain for sensitivity tuning
- Simple output format for scripting and integration

## Installation

### Requirements

- GNU Radio (version 3.7+)
- gr-osmosdr
- librtlsdr (for RTL-SDR support)
- CMake and build essentials
- Compatible SDR hardware (e.g., RTL2832U dongle)

### Install Commands

On Kali Linux or Ubuntu:

```bash
# Install dependencies
sudo apt update
sudo apt install gnuradio gnuradio-dev gr-osmosdr librtlsdr-dev cmake build-essential git

# Clone and build gr-scan
git clone https://github.com/ghostop/gr-scan.git
git -C gr-scan submodule update --init
cd gr-scan
mkdir build && cd build
cmake ..
make
sudo make install
sudo ldconfig
```

Ensure your SDR device is connected and recognized (e.g., `rtl_test -t` for RTL-SDR).

## Basic Usage

```bash
gr-scan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --freq | Frequency range (e.g., 88M:108M) |
| -g, --gain | Set RF gain in dB |
| -d, --device | Specify SDR device index (default 0) |
| -s, --samp-rate | Sample rate (default 2M) |
| -h, --help | Show help |

## Examples

### Example 1: Basic Usage

Scan the FM radio band:

```bash
gr-scan -f 88M:108M
```

### Example 2: Advanced Usage

Scan ISM band with gain adjustment:

```bash
gr-scan -f 2.4G:2.5G -g 30 -s 2M
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Hardware]] Gather Victim Network Information: Wireless

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device connections (RTL-SDR dongles) on monitored systems
- High CPU usage from GNU Radio processes (gr-scan, gnuradio-companion)
- RF emissions or interference patterns during scans
- Log entries for librtlsdr or OsmoSDR library loads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rtl-sdr]]
- [[tools/gnuradio]]
- [[tools/Universal-Radio-Hacker]]

## References

- Official GitHub: https://github.com/ghostop/gr-scan
- GNU Radio Documentation: https://wiki.gnuradio.org
- RTL-SDR Blog: https://www.rtl-sdr.com
