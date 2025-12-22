---
url: 'https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/'
tags:
  - http-intercept
  - proxy
  - debug
type: tool
verified: false
platforms:
  - Web
  - Firefox
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.570Z'
id: 29cc99e3-6bfe-4880-a4e8-81f45cbce42e
validated: true
submitted: true
---
# LiveHTTPHeaders

**Status**: Unverified

## Overview

LiveHTTPHeaders is a Firefox extension designed for capturing, viewing, and editing HTTP requests and responses in real-time, commonly used in web security testing to intercept and modify traffic for vulnerability discovery like XSS.

## Description

This tool acts as a lightweight proxy within the browser, allowing users to monitor live HTTP/HTTPS traffic, pause requests for editing, and replay them. It's particularly useful for testing file uploads, form submissions, and API calls where parameters like filenames can be manipulated. In offensive security, it's employed for manual request tampering without needing full proxy setups like Burp Suite.

## Features

- Feature 1: Real-time HTTP traffic capture and display
- Feature 2: Request pausing, editing (headers, body, parameters), and resuming
- Feature 3: Response viewing with syntax highlighting for JSON/HTML

## Installation

### Requirements

- Firefox browser version 50 or later

### Install Commands

No command-line install; use Firefox Add-ons:

1. Visit https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/
2. Click 'Add to Firefox' and confirm installation
3. Restart browser if prompted

## Basic Usage

Open Firefox Developer Tools or access via toolbar icon to toggle monitoring. Upload a file on the target site to see requests appear.

### Common Options

| Option | Description |
|--------|-------------|
| Toolbar Icon | Toggle capture on/off |
| Pause Button | Freeze request for editing |
| Resume | Send modified request |

## Examples

### Example 1: Basic Usage

1. Enable LiveHTTPHeaders
2. Navigate to Udemy file upload
3. Select and upload a file; request appears in the log

### Example 2: Advanced Usage

1. Capture upload request
2. Pause, edit filename to payload
3. Resume to trigger response

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual pauses in HTTP traffic from browser
- Modified requests in server logs (e.g., anomalous filenames)
- Extension presence in browser profiles

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Fiddler]]

## References

- Official documentation: https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/
- Related resources: Mozilla Add-ons guidelines
