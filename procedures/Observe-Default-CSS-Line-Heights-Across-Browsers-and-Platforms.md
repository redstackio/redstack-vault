---
id: proc-observe-css-lineheights-baseline
tags:
  - tor-browser
  - fingerprinting
  - css
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web Browser
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:46:31.485Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Observe Default CSS Line-Heights Across Browsers and Platforms

## Summary

This procedure involves inspecting and documenting the default CSS line-height values in various web browsers across different operating systems to identify inherent variations that can be exploited for fingerprinting.

## Description

In the context of browser fingerprinting attacks, understanding platform-specific rendering behaviors is crucial. This step establishes a baseline by measuring the computed line-height for elements with the 'normal' CSS value in browsers like IE, Chrome, Safari, and Firefox on Windows, Linux, and macOS. Variations arise from underlying OS font metrics and browser engines, such as Gecko in Firefox. The target environment is any modern web browser, with no special access required. Expected outcomes include a table of values highlighting differences, like 18px on Safari/Mac vs. 20px on Firefox/Windows, setting the stage for Tor-specific analysis.

## Requirements

1. Access to multiple operating systems (Linux, Windows, macOS) with web browsers installed (Chrome, Firefox, Safari, IE).
2. Browser developer tools enabled for inspecting computed styles.
3. Basic HTML file with sample text for measurement.

## Defense

Defensive measures and detection strategies:

- Browser extensions like uBlock Origin or NoScript to block suspicious JavaScript.
- Use of privacy-focused browsers that uniformize CSS properties (e.g., future Tor updates).
- Monitor for anomalous web traffic to fingerprinting sites.

## Objectives

1. Document line-height variations to identify exploitable inconsistencies.
2. Confirm browser-engine influences on rendering.
3. Prepare baseline for Tor Browser inheritance analysis.

## Instructions

### Step 1: Prepare Test HTML Page

**Context**: Create a simple page to measure line-height without custom styles interfering.

Create an HTML file:

```html
<!DOCTYPE html>
<html>
<head><title>Line-Height Test</title></head>
<body>
  <p style="line-height: normal;">Test text line one.<br>Test text line two.</p>
  <script>
    const p = document.querySelector('p');
    const style = window.getComputedStyle(p);
    const lineHeight = style.lineHeight;
    console.log('Line-height: ' + lineHeight);
  </script>
</body>
</html>
```

> This script logs the computed line-height to the console for inspection.

### Step 2: Inspect Across Browsers and Platforms

**Context**: Run the test on each combination and record values.

Open the HTML in each browser on different OSes and check the console or developer tools for values such as 'normal' (IE/Chrome), 18px (Safari/Mac), 19px (Firefox/Linux), 19.2px (Tor/Windows), 19.5167px (Tor/Mac), 20px (Firefox/Windows).

> Expected output: Variations logged, e.g., "Line-height: 19.2px" on Windows Chrome.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[tor-browser]]
- [[fingerprinting]]
- [[css]]
