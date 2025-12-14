---
id: tool-uuid-1
url: 'http://www.rtmpd.com/'
tags:
  - rtmp
  - media-server
  - streaming
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:27.051Z'
validated: true
submitted: true
---
# RTMPD-CPP-RTMP-Media-Server

**Status**: Unverified

## Overview

RTMPD is a lightweight C++ implementation of an RTMP media server designed for streaming audio/video content, commonly used in security testing to host malicious streams for exploiting media processing vulnerabilities like metadata injection in Flash players.

## Description

This tool supports RTMP protocol for real-time streaming of files like MP3s, allowing custom metadata embedding (e.g., server name, ID3 tags) that can be broadcast unescaped. In offensive security, it's used to deliver payloads via streams to vulnerable clients such as VideoJS SWF, bypassing restrictions like HTTP policy files. Features include basic authentication, stream keying, and logging; it's suitable for local or remote hosting on standard ports.

## Features

- Feature 1: RTMP stream hosting for audio/video files with metadata support
- Feature 2: Configurable ports and stream parameters for custom setups
- Feature 3: Lightweight C++ binary for quick deployment in testing environments

## Installation

### Requirements

- C++ compiler (g++)
- Git for source download
- Linux or Windows with build tools

### Install Commands

```bash
# Clone and build
mkdir rtmpd-build && cd rtmpd-build
git clone http://www.rtmpd.com/rtmpd.git src
cd src && make
```

## Basic Usage

```bash
./rtmpd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --port` | Set RTMP port (default 1935) |
| `-s, --stream` | Specify stream key (e.g., mp3:haha) |
| `-m, --metadata` | Add custom metadata strings |

## Examples

### Example 1: Basic Usage

```bash
./rtmpd -p 1935 /path/to/haha.mp3
```

### Example 2: Advanced Usage

```bash
./rtmpd -p 1935 -s mp3:haha -m "server_name=malicious" /path/to/haha.mp3
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on port 1935 with RTMP handshakes
- Process monitoring for rtmpd.exe or ./rtmpd binaries
- Log analysis for unusual stream metadata

## Related Procedures


## Related Tools

- [[FFmpeg]]
- [[Nginx-RTMP-Module]]

## References

- Official site: http://www.rtmpd.com/
- RTMP protocol docs
