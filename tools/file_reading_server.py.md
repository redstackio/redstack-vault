---
id: tool-file-server-001
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/191/999/49f0bed12d5d9e4792c9ca1e2933608f1adc692e/file_reading_server.py
tags:
  - ssrf-exploit
  - hls-server
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.394Z'
validated: true
submitted: true
---
# file_reading_server.py

**Status**: Unverified

## Overview

Custom Python script for exploiting SSRF in HLS processing; serves playlists and reconstructs local files from file:// segments fetched by FFmpeg.

## Description

Designed for this vulnerability; handles /initial.m3u?filename= queries, generates segment lists with file://, fetches on request, concatenates, and saves files. Requires Python 3.5+; runs as HTTP server.

## Features

- Feature 1: Dynamic HLS playlist generation based on filename param
- Feature 2: Automatic fetching and concatenation of local file contents via SSRF
- Feature 3: Debug logging for request tracking

## Installation

### Requirements

- Python 3.5+

### Install Commands

```bash
# Download from URL
wget https://hackerone.../file_reading_server.py
```

## Basic Usage

```bash
python3 file_reading_server.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--external-addr` | Set server IP |
| `--port` | Set listening port |

## Examples

### Example 1: Basic Usage

```bash
python3 file_reading_server.py --external-addr 203.0.113.1 --port 8080
```

### Example 2: Advanced Usage

Default port:

```bash
python3 file_reading_server.py --external-addr 203.0.113.1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound HTTP to custom ports from internal services
- Unusual .m3u requests in logs

## Related Procedures

- [[procedures/Set-Up-Exploit-Server-for-File-Disclosure]]

## Related Tools

- [[tools/gen_avi.py]]

## References

- HackerOne Report Attachment
