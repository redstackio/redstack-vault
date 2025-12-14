---
id: proc-mapbox-xss-test-firefox
tags:
  - xss
  - execution-test
  - firefox
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.074Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-XSS-Execution-in-Firefox-Browser

## Summary

This procedure tests the crafted XSS payload by loading the vulnerable URL in Firefox, confirming JavaScript execution due to the unencoded single quote handling, which does not occur in other browsers.

## Description

Load the POC URL in Firefox version 38.0.5 on Linux or 46.0 on macOS to trigger the payload. The alert(document.domain) executes in the page context, demonstrating the vulnerability's impact on session data or cookies. Fixed in Mapbox on April 29, 2016, by using escaped templates.

## Requirements

1. Firefox browser (e.g., 38.0.5 on Fedora Core 20 Linux)
2. Crafted POC URL from previous procedure
3. No network restrictions to api.tiles.mapbox.com

## Defense

Defensive measures and detection strategies:

- Browser-specific testing in security audits
- Implement strict CSP headers
- Log and alert on script execution anomalies

## Objectives

1. Verify payload triggers in Firefox
2. Confirm non-execution in other browsers
3. Assess impact on page context

## Instructions

### Step 1: Load POC URL

**Context**: Enter the full URL in Firefox's address bar to initiate the request.

URL: https://api.tiles.mapbox.com/v4/ctswebrequest.m4ga59jd/page.html?access_token=pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw.htaccess.aspx'%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

> Firefox processes the single quote without encoding, breaking out.

### Step 2: Observe Execution

**Context**: Monitor for the alert dialog to confirm success.

Expected: Alert box pops up showing 'api.tiles.mapbox.com'.

> Test in Chrome/Safari to verify browser specificity.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[execution-test]]
