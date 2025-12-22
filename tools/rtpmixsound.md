---
id: b74e6226-027f-45fc-a03f-69e3e298ff58
type: tool
verified: true
created_at: '2019-08-28T21:17:32.926795+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - audio-manipulation
  - rtp
  - voip
  - social-engineering
url: 'https://tools.kali.org/information-gathering/rtpmixsound'
commands:
  - '[[commands/rtpmixsound-mix-audio-into-rtp-stream]]'
  - '[[commands/rtpmixsound-realtime-mix-from-network]]'
validated: true
---

# rtpmixsound

**Status**: Unverified

## Overview

rtpmixsound is a specialized tool for mixing pre-recorded audio files into real-time RTP (Real-time Transport Protocol) audio streams. It is commonly used in security testing for VoIP environments, social engineering simulations, or analyzing audio stream vulnerabilities by injecting custom sounds without disrupting the original stream.

## Description

The tool processes RTP streams, either from files or live network captures, and overlays audio from WAV or similar files. This can simulate voice alterations, insert alerts, or test audio integrity in communication systems. It supports both offline file-based mixing and real-time network interception, making it versatile for penetration testing involving multimedia protocols.

## Features

- Feature 1: Real-time audio mixing into live RTP streams via UDP.
- Feature 2: Offline processing of captured RTP files with sound injection.
- Feature 3: Support for looping audio files for continuous injection.
- Feature 4: Minimal latency for seamless integration in active sessions.

## Installation

### Requirements

- Linux environment with RTP support (e.g., libpcap for captures).
- Audio libraries (e.g., libav for WAV handling).
- Root privileges for network captures.

### Install Commands

```bash
# On Kali Linux (pre-installed in some versions)
sudo apt update && sudo apt install rtpmixsound

# On Ubuntu/Debian
sudo apt update && sudo apt install rtpmixsound

# From source (if not in repos)
git clone https://github.com/rtpmixsound/repo.git
cd rtpmixsound
make && sudo make install
```

## Basic Usage

```bash
rtpmixsound --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i | Input RTP source (file or udp://host:port) |
| -s | Sound file to mix (WAV format) |
| -o | Output RTP file |
| -v | Verbose output for debugging |
| --loop | Loop the sound file continuously |

## Examples

### Example 1: Basic Usage

Mix a sound into a captured RTP file:

```bash
rtpmixsound -i input.rtp -s alert.wav -o mixed.rtp
```

### Example 2: Advanced Usage

Real-time mix from network:

```bash
rtpmixsound -i udp://target:5004 -s prank.wav -o live_output.rtp --loop
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for RTP interception and modification)
- [[Forge Web Credentials]] Forge Web Credentials (audio-based social engineering)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Initial Access]] Initial Access (via manipulated communications)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual RTP traffic modifications or unexpected audio in VoIP streams using tools like Wireshark.
- Detection method 2: Network logs showing UDP port activity (e.g., 5004) with audio file access patterns on endpoints.
- Detection method 3: Process monitoring for rtpmixsound executions in system logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (for RTP capture)
- [[tools/scapy]] (for packet manipulation)

## References

- Official Kali documentation: https://tools.kali.org/information-gathering/rtpmixsound
- GitHub repository: https://github.com/related/rtpmixsound (if available)
- RTP protocol specs: RFC 3550
