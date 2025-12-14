---
id: p4b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - response-capture
  - content-disclosure
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Browser (Google Chrome)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:09.977Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture Response After Redirect

## Summary

This procedure captures the target's response after Flash follows the redirect, using the UPLOAD_COMPLETE_DATA event to disclose cross-origin content without policy checks.

## Description

After the redirect, Chrome resends the upload to the target site. Flash receives the response and exposes it via the UPLOAD_COMPLETE_DATA event, allowing the attacker to read arbitrary website content. This leads to data leakage and potential for unauthorized actions on the target.

## Requirements

1. Successful upload initiation from previous step
2. Event listener in SWF for UPLOAD_COMPLETE_DATA
3. Mechanism to log or exfiltrate captured data

## Defense

Defensive measures and detection strategies:

- Remove Flash support entirely from browsers
- Implement server-side cross-origin checks for uploads
- Detect anomalous Flash events or data exfiltration in client-side logs

## Objectives

1. Receive and process UPLOAD_COMPLETE_DATA event
2. Extract and view target content
3. Demonstrate policy bypass success

## Instructions

### Step 1: Listen for Upload Complete Event

**Context**: In SWF, handle the event to capture data.

Embedded in SWF code:

```actionscript
fileRef.addEventListener(flash.net.FileReferenceEvent.UPLOAD_COMPLETE_DATA, onUploadComplete);

function onUploadComplete(event:flash.net.FileReferenceEvent):void {
    var responseData:String = event.data;
    trace(responseData); // Or send to attacker server
}
```

> Event fires with target's HTML/response as string.

### Step 2: Validate Captured Content

**Context**: Check console or logs for disclosed data.

In Chrome dev tools console (for trace output):

```javascript
// Observe traced output containing target site content
```

> Success if cross-origin content (e.g., Google+ page HTML) appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[response-capture]]
- [[content-disclosure]]
- [[Exfiltration]]
