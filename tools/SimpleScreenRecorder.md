---
id: tool-simplescreenrecorder
url: 'https://www.maartenbaert.be/simplescreenrecorder/'
tags:
  - screen-recording
  - poc
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:05.016Z'
validated: true
submitted: true
---
# SimpleScreenRecorder

**Status**: Unverified

## Overview

SimpleScreenRecorder is a lightweight screen recording tool primarily used on Linux to capture video demonstrations, ideal for creating proof-of-concept (PoC) videos in security testing, such as recording clickjacking exploits.

## Description

It supports recording desktop sessions, specific windows, or areas, with options for audio, frame rates, and codecs. In offensive security, it's used to document attacks like UI redressing by capturing user interactions in real-time, providing visual evidence of vulnerabilities without complex setups.

## Features

- Feature 1: Area/window selection for targeted recording
- Feature 2: Pause/resume functionality for step-by-step captures
- Feature 3: Export to common formats like MP4 for easy sharing

## Installation

### Requirements

- Linux distribution (e.g., Ubuntu)
- Qt libraries

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install simplescreenrecorder
```

## Basic Usage

```bash
simplescreenrecorder
```

### Common Options

| Option | Description |
|--------|-------------|
| No CLI options; GUI-based | Launch the application |
| --help | Show basic help |

## Examples

### Example 1: Basic Usage

```bash
simplescreenrecorder
```
Select area, start recording, perform actions, then stop and save.

### Example 2: Advanced Usage

Launch via GUI, choose 'Record a fixed rectangle', set dimensions to match browser window, include audio if narrating the PoC.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'simplescreenrecorder' on Linux systems
- Unusual video file creation in temp directories during testing

## Related Procedures


## Related Tools

- [[Related Tool 1|OBS Studio]]
- [[Related Tool 2|Kazam]]

## References

- Official documentation: https://www.maartenbaert.be/simplescreenrecorder/
- Related resources: Linux screen recording guides
