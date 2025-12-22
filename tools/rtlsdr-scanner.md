---
id: bba42689-cd9d-4486-987b-f79bed3237aa
type: tool
verified: true
created_at: '2019-08-28T21:17:23.126709+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - rf
  - sdr
  - reconnaissance
  - wireless
  - spectrum-analysis
url: 'https://github.com/EarToEarOak/rtl-sdr-scanner'
commands:
  - '[[commands/install-librtlsdr-ubuntu]]'
  - '[[commands/install-rtlsdr-scanner-pip]]'
  - '[[commands/run-rtlsdr-scanner-basic]]'
validated: true
---

# rtlsdr-scanner

**Status**: Unverified

## Overview

rtl-sdr-scanner is a cross-platform Python-based graphical user interface (GUI) tool for frequency scanning using affordable USB TV tuner dongles (RTL-SDR devices). It functions as a simple spectrum analyzer, enabling users to visualize and analyze radio frequency (RF) signals across a specified range. In security testing, it's commonly used for RF reconnaissance, identifying wireless signals, detecting hidden devices, or analyzing spectrum activity in red team operations involving wireless communications.

## Description

The tool leverages the OsmoSDR rtl-sdr library to interface with RTL-SDR hardware, allowing real-time scanning of frequency bands. It compensates for the tuner's frequency response limitations by averaging data from positive and negative frequency offsets of the baseband signal. This makes it suitable for passive RF monitoring in environments like wireless network assessments, IoT device discovery, or detecting unauthorized transmissions. The GUI provides an intuitive interface for setting scan parameters, viewing waterfalls, and exporting data, without requiring deep programming knowledge.

## Features

- **GUI-Based Scanning**: Interactive interface for real-time frequency sweeps and signal visualization.
- **Frequency Offset Averaging**: Improves accuracy by mitigating tuner biases through dual-offset scanning.
- **Customizable Parameters**: Adjustable gain, frequency range, dwell time, and bandwidth settings.
- **Data Export**: Save scans as images, CSV files, or raw IQ data for further analysis.
- **Cross-Platform Support**: Works on Linux, Windows, and macOS with compatible RTL-SDR hardware.
- **Plugin Extensibility**: Supports additional processing via Python scripts for custom signal detection.

## Installation

### Requirements

- RTL-SDR compatible USB dongle (e.g., NooElec NESDR or RTL2832U-based tuner).
- Python 3.6+ with pip.
- librtlsdr library (backend for hardware access).
- USB access permissions for the dongle (e.g., udev rules on Linux).

### Install Commands

For Ubuntu/Debian-based systems, first install the RTL-SDR library dependencies using [[commands/install-librtlsdr-ubuntu]]:

Then install the Python package using [[commands/install-rtlsdr-scanner-pip]]:

On Windows, use Zadig to install WinUSB drivers for the dongle, then run the pip install.
On macOS, use Homebrew: `brew install rtl-sdr`, followed by pip install.

## Basic Usage

```bash
rtl_sdr_scanner
```

This launches the GUI. Connect your RTL-SDR dongle, select the frequency range (e.g., 24-1760 MHz), set gain, and start scanning.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and available options |
| `-f FREQ, --freq FREQ` | Starting frequency in MHz (default: 100) |
| `-g GAIN, --gain GAIN` | RTL-SDR gain in dB (0-50) |
| `-b BW, --bw BW` | Sample bandwidth in Hz (default: 2.4e6) |
| `-s RATE, --samp-rate RATE` | Sample rate in Hz (default: 2.4e6) |

## Examples

### Example 1: Basic Usage

Launch with default settings for a quick ISM band scan (e.g., 2.4 GHz WiFi):

```bash
rtl_sdr_scanner -f 2400 -t 2500
```

This scans from 2400 to 2500 MHz.

### Example 2: Advanced Usage

Run with custom gain and export to CSV:

```bash
rtl_sdr_scanner -f 400 -t 500 -g 40 --export csv --output scan_results.csv
```

Scans 400-500 MHz at 40 dB gain and saves peaks to CSV.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for RF/wireless spectrum reconnaissance)
- [[Network Sniffing]] Network Sniffing (extended to RF signal capture)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device connections (RTL-SDR dongles) via USB logs or device manager.
- High CPU usage from Python processes with rtl-sdr library imports.
- Network traffic if scanning involves IP-based tools, or RF emissions if active probing is enabled.
- Process monitoring for `rtl_sdr_scanner.py` or `python rtl_sdr_scanner.py` executions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[rtl-sdr]] (Core RTL-SDR library and CLI tools)
- [[gnuradio]] (Advanced SDR signal processing framework)
- [[dump1090]] (ADS-B decoder for aviation signals)

## References

- Official GitHub Repository: https://github.com/EarToEarOak/rtl-sdr-scanner
- RTL-SDR Documentation: https://osmocom.org/projects/rtl-sdr/wiki
- Usage Guide: Included in the repository README
