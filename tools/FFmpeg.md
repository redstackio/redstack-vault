---
url: 'https://ffmpeg.org/'
tags:
  - media
  - processing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.569Z'
id: 99776027-6ee2-41cb-b020-c9465098a259
validated: true
submitted: true
---
# ffmpeg

**Status**: Unverified

## Overview

FFmpeg is a multimedia framework for handling video, audio, and other streams, exploited here as the target-side tool in Imgur's processing pipeline due to its m3u8 parsing leading to SSRF, LFE, and DoS.

## Description

Version Lavf/55.48.100 (disclosed via User-Agent) supports protocols like file://, http://, concat, allowing attackers to chain exploits. Vulnerabilities in parsing enable hangs and segfaults.

## Features

- Feature 1: Protocol support (HTTP, file, concat)
- Feature 2: Content-based parsing ignoring headers
- Feature 3: Playlist handling for m3u8/HLS

## Installation

### Requirements

- Build tools for compilation

### Install Commands

```bash
# On Ubuntu
apt install ffmpeg

# From source
git clone https://git.ffmpeg.org/ffmpeg.git
cd ffmpeg
./configure && make && sudo make install
```

## Basic Usage

```bash
ffmpeg -help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i` | Input file |
| `-f` | Format |
| `-t` | Duration |

## Examples

### Example 1: Basic Usage

```bash
ffmpeg -i input.mp4 output.gif
```

### Example 2: Advanced Usage

```bash
ffmpeg -f concat -i playlist.m3u8 -t 10 output.gif
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Execution]] Execution
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Hanging processes with high CPU usage
- Outbound requests to unusual URLs
- Segfault logs in system dmesg

## Related Procedures

- [[procedures/Craft-DoS-Payload-to-Hang-FFmpeg]]

## Related Tools

- [[tools/libav]]

## References

- Official documentation: https://ffmpeg.org/documentation.html
- Related resources: CVE databases for ffmpeg vulnerabilities
