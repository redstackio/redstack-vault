---
id: proc-imgur-page-detection
tags:
  - frame-detection
  - navigation-monitor
  - firefox
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/iframe-frame-count-log]]'
  - '[[commands/frame-count-monitor-interval]]'
  - '[[commands/postmessage-handler]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.876Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Detect-Navigation-to-Vulnerable-Upload-Page

## Summary

This procedure monitors the number of frames in the ClickJacked Imgur iframe to detect when the victim navigates to the beta image upload page, which has a unique frame count of 1 compared to normal pages (>3), triggering UI updates for further exploitation.

## Description

In the Firefox-specific context, Imgur's beta upload page loads with minimal frames, allowing attackers to poll ifr.contentWindow.frames.length via JavaScript. This is chained from ClickJacking setup and uses inter-frame communication for synchronization. Prerequisites: Framed Imgur page active and victim interacting. Expected outcome: Detection of vulnerable state to proceed to payload delivery.

## Requirements

1. Active ClickJacking iframe from prior procedure
2. Firefox for accurate frame counting
3. JavaScript execution in attacker page
4. Victim must navigate within the framed Imgur site

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize frame structures to evade counting
- Implement anti-framing scripts that detect polling attempts
- Log unusual JavaScript access to frame properties
- Browser extensions to warn on frame manipulation

## Objectives

1. Identify transition to exploitable upload page
2. Update malicious UI based on detection
3. Synchronize with victim actions for timing

## Instructions

### Step 1: Log Initial Frame Count

**Context**: On iframe load, log the frame count to baseline normal vs. vulnerable pages.

**Command** ([[commands/iframe-frame-count-log]]):
```html
<iframe id="ifr"></iframe><script>ifr.onload=function(){console.log(ifr.contentWindow.frames.length);}</script>
```

> Sets up iframe with ID and onload handler. Expected output: Console log of frames.length (e.g., >3 for normal).

### Step 2: Monitor Frame Changes

**Context**: Poll every second to detect drop to 1 frame, updating UI.

**Command** ([[commands/frame-count-monitor-interval]]):
```javascript
setInterval(function(){if(i==2){console.log("stop counter...");}if(x!=1){if(ifr.contentWindow.frames.length==1){console.log("page change!");btn1.innerHTML="drag the image to here!";x=1;}}},1000)
```

> Interval check with variables i and x for state. Expected output: "page change!" log and button text update.

### Step 3: Handle Messages

**Context**: Listen for postMessage events from framed content.

**Command** ([[commands/postmessage-handler]]):
```javascript
onmessage=function(event){console.log(event);i++;}
```

> Increments counter i on messages. Expected output: Logged events and incremented i.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/iframe-frame-count-log]]
- [[commands/frame-count-monitor-interval]]
- [[commands/postmessage-handler]]

## Tools Used

- [[tools/Firefox]]

## Tags

- frame-detection
- navigation-monitor
- firefox
