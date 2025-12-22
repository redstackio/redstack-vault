---
url: 'https://www.youtube.com/watch?v=doLHsUqnvgE'
tags:
  - xss
  - demonstration
  - video
type: tool
verified: false
platforms:
  - Web
id: 6ec326ea-0eb3-4673-85c7-af7cf7c5548e
created_at: '2025-12-13T23:52:34.098Z'
updated_at: '2025-12-13T23:52:34.098Z'
validated: true
submitted: true
---
# YouTube-XSS-Demonstration

**Status**: Unverified

## Overview

This YouTube video provides a visual walkthrough and demonstration of the XSS vulnerability in the MTN Play search form, showing step-by-step navigation, payload injection, and execution for educational purposes in security testing.

## Description

The video details the exploitation process on mtnplay.co.zm, highlighting the lack of sanitization in filter fields. It's useful for red teamers or bug bounty hunters to understand the attack vector without performing live tests. No installation required; access via any browser.

## Features

- Feature 1: Screen-recorded browser interaction showing payload injection
- Feature 2: Explanation of impact, including potential for session hijacking
- Feature 3: Tips for crafting effective XSS payloads

## Installation

### Requirements

- Internet connection
- Web browser or YouTube app

### Install Commands

No installation needed; visit the URL directly.

## Basic Usage

Open https://www.youtube.com/watch?v=doLHsUqnvgE and watch the video.

### Common Options

N/A (video playback controls: play, pause, seek)

## Examples

### Example 1: Basic Usage

Navigate to the video URL and play to follow the demo.

### Example 2: Advanced Usage

Pause at key timestamps to replicate steps in your browser session.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- N/A (passive video resource; no runtime detection)
- Monitor for video embeds or links in security reports

## Related Procedures

- [[procedures/Exploit-Reflected-XSS-in-Search-Filters]]

## Related Tools


## References

- HackerOne Report #761573
- Original video source on YouTube
