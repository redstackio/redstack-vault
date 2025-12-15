---
id: tool-twitter-csrf-poc-95555
url: 'http://innerht.ml/pocs/twitter-cards-csrf/'
tags:
  - csrf
  - poc
  - twitter
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.982Z'
validated: true
submitted: true
---
# Twitter Cards CSRF PoC

**Status**: Unverified

## Overview

A web-based proof-of-concept tool for generating and executing CSRF attacks on Twitter poll cards by inputting parameters and triggering silent requests to the bypassed API endpoint.

## Description

This online tool allows attackers to specify poll details and auto-generates an HTML/JS payload that submits a POST request to /i/cards/api/v1, exploiting the CSRF bypass to force votes in a victim's browser session.

## Features

- Feature 1: Input fields for tweet_id, card_uri, selected_choice
- Feature 2: One-click generation of attack payload
- Feature 3: Silent submission without user interaction

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation; access via URL.

```bash
# Open in browser
curl -s http://innerht.ml/pocs/twitter-cards-csrf/ > poc.html  # Optional local save
```

## Basic Usage

Visit the URL and fill form.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web form-based |

## Examples

### Example 1: Basic Usage

Input tweet_id=657629231309041664, card_uri=card://657629230759415808, selected_choice=2; click activate.

### Example 2: Advanced Usage

Host generated HTML on attacker's server and link to victim.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious form submissions to Twitter API from external domains
- Unexpected poll vote changes

## Related Procedures


## Related Tools

- [[tools/Intercept-Vote-Request-Tool]]

## References

- PoC URL: http://innerht.ml/pocs/twitter-cards-csrf/
- HackerOne Report: https://hackerone.com/reports/95555
