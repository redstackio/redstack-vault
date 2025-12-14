---
url: 'https://steamidfinder.com/'
tags:
  - recon
  - steam
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.952Z'
id: d7830c34-277d-4290-81c9-954690b62bf6
validated: true
submitted: true
---
# Steam-ID-Finder

**Status**: Unverified

## Overview

Web-based tool for discovering Steam user IDs from usernames, profiles, or community links, useful in reconnaissance for Steam-integrated application exploits like IDOR.

## Description

Steam ID Finder is a free online service that converts human-readable Steam identifiers (e.g., custom URLs) to 64-bit SteamIDs. It's commonly used in security testing to identify targets for session manipulation or account discovery without needing API access. No installation required; operates via browser.

## Features

- Feature 1: Input validation for various Steam ID formats (URL, username, 32-bit/64-bit)
- Feature 2: Instant conversion and display of profile details
- Feature 3: No login required; supports batch lookups indirectly via scripting

## Installation

### Requirements

- Web browser
- Internet connection

### Install Commands

No installation; access via https://steamidfinder.com/.

## Basic Usage

Visit https://steamidfinder.com/ and enter a Steam profile URL or username.

### Common Options

| Option | Description |
|--------|-------------|
| Profile URL Input | Paste Steam community link for conversion |
| Username Search | Enter custom name to find ID |

## Examples

### Example 1: Basic Usage

Enter https://steamcommunity.com/id/exampleuser into the tool.

### Example 2: Advanced Usage

Use browser automation (e.g., Selenium) to query multiple profiles:

```python
# Pseudo-code for automation
import requests
response = requests.get('https://steamidfinder.com/lookup', params={'input': 'profile_url'})
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to steamidfinder.com from security testing IPs
- Logs of Steam profile queries in bulk

## Related Procedures


## Related Tools

- Steam Web API (official alternative)
- SteamID.io

## References

- Official site: https://steamidfinder.com/
- Steam documentation on IDs
