---
type: tool
description: >-
  Kalibrate (kal) is a tool for scanning GSM base stations and calibrating
  RTL-SDR devices to detect cellular infrastructure.
url: 'https://github.com/steve-m/kalibrate-rtl'
tags:
  - reconnaissance
  - wireless
  - gsm
  - sdr
platforms:
  - Linux
verified: true
validated: true
---

# kal

**Status**: Unverified

## Overview

Kalibrate, commonly referred to as kal, is a software tool designed for use with RTL-SDR (Software Defined Radio) devices to scan for GSM base stations within specified frequency bands. It identifies active cell towers by analyzing broadcast control channels (BCCH) and can calculate the local oscillator frequency offset for improved tuning accuracy. In security testing, it's used for reconnaissance of cellular networks, mapping base station locations, and assessing wireless infrastructure vulnerabilities.

## Description

Kal works by tuning into GSM frequency bands (such as 850 MHz, 900 MHz, 1800 MHz, or 1900 MHz) and demodulating signals to extract information like Absolute Radio Frequency Channel Numbers (ARFCN), frequencies, and signal strengths. This enables pentesters to locate and characterize GSM infrastructure, which can be part of broader wireless security assessments, such as identifying IMSI catcher risks or mapping operator coverage. It requires an RTL-SDR dongle and is particularly useful in mobile or RF-focused red team operations.

## Features

- Feature 1: Scans multiple GSM bands (GSM850, GSM900, DCS1800, PCS1900) for base station detection.
- Feature 2: Calculates and applies local oscillator corrections for precise frequency tuning.
- Feature 3: Outputs signal power levels and channel details for triangulation and analysis.
- Feature 4: Supports RTL-SDR hardware with configurable gain and sample rates.

## Installation

### Requirements

- RTL-SDR compatible USB dongle (e.g., NooElec NESDR).
- Linux kernel with USB support.
- Dependencies: librtlsdr-dev, libfftw3-dev, build-essential.

### Install Commands

```bash
# On Ubuntu/Debian/Kali
sudo apt update
sudo apt install git build-essential libfftw3-dev librtlsdr-dev

# Clone and build kalibrate-rtl
git clone https://github.com/steve-m/kalibrate-rtl.git
cd kalibrate-rtl/src/
make
sudo make install
```

## Basic Usage

```bash
kal --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -s, --band | Specify GSM band (e.g., GSM900).
| -g, --gain | Set RTL-SDR gain in dB.
| -c, --cal | Calibrate using a specific channel.
| -v, --verbose | Increase output verbosity.

## Examples

### Example 1: Basic Usage

Scan for base stations in the GSM900 band:

```bash
kal -s GSM900
```

### Example 2: Advanced Usage

Scan with custom gain and sample rate:

```bash
kal -s GSM900 -g 40 --srate 250000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Network Service Scanning (for RF/cellular recon).
- [[Hardware]] Gather Victim Network Information: Network Trust Dependencies.

### Tactics

- [[Reconnaissance]] Reconnaissance.

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual USB device connections (RTL-SDR dongles) monitored via USB logs (e.g., udev rules).
- Detection method 2: High CPU usage from signal processing or network logs showing SDR-related processes (kal, rtl_tcp).
- Detection method 3: RF spectrum anomalies or interference patterns in monitored GSM bands.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official GitHub: https://github.com/steve-m/kalibrate-rtl
- RTL-SDR Documentation: https://osmocom.org/projects/sdr/wiki/rtl-sdr

## Related Commands

- [[commands/kal-scan-gsm-frequency-band]]
- [[commands/kal-calibrate-local-oscillator]]
