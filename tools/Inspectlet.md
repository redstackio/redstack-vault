---
id: tool-inspectlet
url: 'https://www.inspectlet.com'
tags:
  - session-recording
  - analytics
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.362Z'
validated: true
submitted: true
---
# Inspectlet

**Status**: Unverified

## Overview

Inspectlet is a web analytics and session recording tool that captures user interactions on websites, including mouse movements, clicks, and network requests, allowing replay for debugging or malicious data extraction in security contexts.

## Description

Inspectlet provides heatmaps, session recordings, and form analytics. In offensive security, it's abused to record hidden actions like iframe loads in clickjacking attacks, capturing responses such as geolocation JSON. It uses an asynchronous JavaScript snippet for non-blocking integration. Common in web pentesting for exfiltrating data from victim browsers without direct server access.

## Features

- Feature 1: Full session replay with video-like playback of user actions
- Feature 2: Network request logging, including API responses like JSON payloads
- Feature 3: Asynchronous loading to avoid performance impact

## Installation

### Requirements

- Web browser for dashboard
- JavaScript-enabled site for integration

### Install Commands

No installation; embed script in HTML.

## Basic Usage

Embed the tracking script in <head>:

```html
<script type="text/javascript">(function() { window.__insp = window.__insp || []; __insp.push(['wid', 2060137667]); var ldinsp = function(){ if(typeof window.__inspld != "undefined") return; window.__inspld = 1; var insp = document.createElement('script'); insp.type = 'text/javascript'; insp.async = true; insp.id = "inspsync"; insp.src = ('https:' == document.location.protocol ? 'https' : 'http') + '://cdn.inspectlet.com/inspectlet.js?wid=2060137667&r=' + Math.floor(new Date().getTime()/3600000); var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(insp, x); }; setTimeout(ldinsp, 0); })();</script>
```

### Common Options

| Option | Description |
|--------|-------------|
| wid | Widget ID from account dashboard |
| async | Loads script without blocking page |

## Examples

### Example 1: Basic Usage

Insert script into HTML head for session start on load.

### Example 2: Advanced Usage

Configure via dashboard for rage clicks or error tracking, but for attacks, focus on network capture.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Automated Collection]]
- [[Drive-by Compromise]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to cdn.inspectlet.com
- __insp JavaScript variables in page source
- Unusual session recording traffic from analytics domains

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://www.inspectlet.com/docs
- Related resources: Web analytics abuse in pentesting
