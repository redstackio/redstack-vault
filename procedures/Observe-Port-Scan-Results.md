---
tags:
  - port-scanning
  - observation
  - headless-chrome
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Network Service Scanning]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2b4277f1-ae35-4e8b-99e9-6765e4e103b7
created_at: '2025-12-14T04:08:55.336Z'
updated_at: '2025-12-14T04:08:55.336Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Observe-Port-Scan-Results

## Summary

This procedure captures the outcomes of the port scanning executed by the PoC.html in the headless Chrome environment triggered by the SSRF, identifying open localhost ports and potential service details via screenshots.

## Description

After triggering the SSRF, the PoC uses an async function like scanChromeLinux to iterate ports, create iframes for http://localhost:port, and detect opens via onload events or timeouts (500ms). Results are pushed to an array if onload fires multiple times. Due to headless timing, adjust for reliability. This reveals local services, enables brute-forcing, or leaks data through screenshots. Prerequisites: Successful SSRF trigger.

## Requirements

1. Access to the API response or screenshot output
2. Monitoring tools for JavaScript execution logs
3. Understanding of Chrome's iframe behavior in headless mode

## Defense

Defensive measures and detection strategies:

- Monitor headless rendering for anomalous JavaScript/iframe activity
- Restrict localhost access in rendering sandboxes
- Analyze screenshots for unexpected content

## Objectives

1. Identify open ports on localhost
2. Enumerate HTTP services
3. Detect potential data leaks

## Instructions

### Step 1: Analyze PoC Execution

**Context**: Review the headless Chrome behavior for port detection logic.

The PoC pushes open ports to an array based on onload events:

```javascript
// In PoC.html
if (onloadFired > 1 || !timeoutExpired) openPorts.push(port);
```

> Observe via developer tools or logs; in headless, rely on screenshot quality or exfil if implemented.

### Step 2: Adjust and Validate

**Context**: Tune timeout for accurate results in Chrome's environment.

Test with known open ports (e.g., 80) and increase timeout to 1000ms if needed.

> Expected: Array of open ports like [80, 3000], indicating services; screenshots may show local pages for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- results-analysis
- scanning
