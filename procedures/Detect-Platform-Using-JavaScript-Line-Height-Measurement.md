---
id: proc-javascript-lineheight-detection
tags:
  - tor-browser
  - fingerprinting
  - javascript
  - css
  - os-detection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.468Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
  - '[[JavaScript]]'
---
# Detect Platform Using JavaScript Line-Height Measurement

## Summary

This procedure creates and deploys a web page that uses JavaScript to measure CSS line-height in Tor Browser, comparing it against known values to infer the user's operating system and profile them.

## Description

Building on baseline measurements, this step implements a client-side JavaScript detector that first confirms Tor Browser usage (via userAgent) and then queries getComputedStyle for line-height on a test element. Values are mapped to OS: 19px (Linux), 19.2px (Windows), 19.5167px (macOS). The scenario involves hosting this on a site frequented by Tor users, leading to information disclosure. Prerequisites include web hosting; outcomes reduce user anonymity by enabling OS-based profiling.

## Requirements

1. Web server to host the detection page.
2. Knowledge of Tor userAgent string for validation.
3. Baseline line-height values from prior steps.

## Defense

Defensive measures and detection strategies:

- Disable JavaScript or use extensions like CanvasBlocker to spoof styles.
- Tor Project patches to set fixed line-height in browser CSS.
- Server-side logging of JS execution patterns for anomaly detection.

## Objectives

1. Confirm Tor Browser presence.
2. Measure and classify line-height to detect OS.
3. Log or alert on detected platform for profiling.

## Instructions

### Step 1: Create Detection HTML Page

**Context**: Build the page with hidden test element and detection logic.

Develop the following HTML:

```html
<!DOCTYPE html>
<html>
<head><title>Platform Detector</title></head>
<body>
  <div id="test" style="line-height: normal; visibility: hidden;">Test</div>
  <script>
    if (navigator.userAgent.includes('Tor Browser')) {
      const el = document.getElementById('test');
      const style = window.getComputedStyle(el);
      const lh = parseFloat(style.lineHeight);
      let os = 'Unknown';
      if (lh === 19) os = 'Linux';
      else if (lh === 19.2) os = 'Windows';
      else if (lh === 19.5167) os = 'macOS';
      console.log('Detected OS: ' + os);
      // Could send to server: fetch('/log?os=' + os);
    }
  </script>
</body>
</html>
```

> This script detects Tor and maps line-height to OS, logging the result.

### Step 2: Host and Test the Page

**Context**: Deploy and validate against Tor Browser instances.

Upload to a web server and visit via Tor on each OS; check console for accurate OS detection.

> Expected output: "Detected OS: Windows" when tested on Windows Tor.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[tor-browser]]
- [[fingerprinting]]
- [[JavaScript]]
