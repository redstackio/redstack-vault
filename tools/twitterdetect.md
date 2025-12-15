---
url: 'http://homakov.github.io/twitterdetect.html'
tags:
  - recon
  - side-channel
  - twitter
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.483Z'
id: 58c1336a-b446-4097-999b-f21a997e4eaa
validated: true
submitted: true
---
# twitterdetect

**Status**: Unverified

## Overview

twitterdetect.html is a demo tool for probing Twitter usernames via a side-channel attack exploiting window.close() behavior on followed and favorited tweets. It was used in the context of discovering the XSS vulnerability.

## Description

The tool leverages timing differences or close behaviors when accessing tweet pages for followed vs. non-followed users, enabling username enumeration without direct access. Primarily for reconnaissance in Twitter security testing.

## Features

- Side-channel username probing
- Detection of follow/favorite status
- Simple HTML-based demo for browser execution

## Installation

### Requirements

- Web browser
- Access to Twitter

### Install Commands

No installation needed; load the HTML file directly.

## Basic Usage

Open http://homakov.github.io/twitterdetect.html in a browser and input target usernames to probe.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Browser-based; no CLI options |

## Examples

### Example 1: Basic Usage

Load the page and enter a username to test follow status via side-channel.

### Example 2: Advanced Usage

Use in conjunction with scripts to automate probing multiple usernames.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Twitter page loads and close attempts
- Network traffic to Twitter intent endpoints
- Browser console errors from side-channel timing

## Related Procedures


## Related Tools


## References

- HackerOne Report #48516
