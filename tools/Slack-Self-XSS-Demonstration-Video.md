---
url: 'https://youtu.be/dIvNeb2aRrU'
tags:
  - demonstration
  - video
  - xss
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.782Z'
id: d99c69c5-5366-42db-a41c-2744b51ba3b3
validated: true
submitted: true
---
# Slack-Self-XSS-Demonstration-Video

**Status**: Unverified

## Overview

This YouTube video provides a visual demonstration of reproducing the self-XSS vulnerability in Slack's post creation feature, useful for understanding the UI interactions and execution flow in security testing.

## Description

The video walks through the steps of accessing Slack, creating a post, entering and formatting the payload, and triggering the alert. It is intended for educational purposes in offensive security, highlighting the vulnerability reported on HackerOne. No installation is required; it serves as a reference for manual reproduction.

## Features

- Step-by-step visual guide to the exploit
- Shows browser-specific behavior (Firefox)
- Includes payload execution confirmation

## Installation

### Requirements

- Internet access
- Web browser or YouTube app

### Install Commands

No installation needed; access via URL.

## Basic Usage

Visit the URL to watch the demonstration.

### Common Options

N/A (video playback)

## Examples

### Example 1: Basic Usage

Open `https://youtu.be/dIvNeb2aRrU` in a browser and play the video.

### Example 2: Advanced Usage

Pause at key steps (e.g., formatting) to replicate manually.

## Expected Output

Video playback showing the full exploit chain, ending with the alert popup.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to YouTube domains during testing
- Video embeds or links in reports

## Related Procedures


## Related Tools


## References

- HackerOne Report #89505
