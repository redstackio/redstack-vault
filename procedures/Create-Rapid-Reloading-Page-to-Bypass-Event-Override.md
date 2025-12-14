---
tags:
  - bypass
  - timing-attack
  - iframe
  - flash
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash (SWF)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.435Z'
skill_level: advanced
impact_level: medium
detection_risk: high
sub_techniques: []
id: 6fa86f26-947e-44f9-9c63-67d7bb372918
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Rapid Reloading Page to Bypass Event Override

## Summary

This procedure generates an HTML page that embeds the vulnerable SWF in an iframe and uses JavaScript to reload it every 300ms, creating a timing window where the injected HTML's MouseClick event can execute before the SWF's button logic overrides it.

## Description

Flash SWFs typically capture MouseClick events for their buttons, overriding injected HTML events. Rapid reloading disrupts this, allowing occasional execution of injected javascript: links. This 'epileptic' flickering is key to bypassing the protection in components like Imgur's swfupload.swf.

## Requirements

1. Text editor for HTML/JS
2. Local web server or file:// access
3. Malicious SWF URL from prior step

## Defense

Defensive measures and detection strategies:

- Remove Flash dependencies
- Implement event validation in SWF code
- Detect rapid iframe reloads via client-side monitoring

## Objectives

1. Embed SWF in reloading iframe
2. Achieve intermittent event capture on injected elements
3. Set up for timed payload trigger

## Instructions

### Step 1: Create HTML Structure

**Context**: Build page with iframe.

<html><body><iframe id="swf" src="[malicious-url]"></iframe><script>...</script></body></html>

**Expected Output**: Basic page with embedded SWF.

### Step 2: Implement Reloading Logic

**Context**: Add JavaScript interval for reloads.

Use: setInterval(function(){document.getElementById('swf').src = '[malicious-url]';}, 300);

**Expected Output**: Iframe flickers every 300ms, showing injected text briefly.

### Step 3: Verify Bypass Potential

**Context**: Observe during reloads for clickable windows.

Load page; note 'CLICKME' appears/disappears rapidly, creating moments where click might hit HTML event.

**Expected Output**: Visual confirmation of timing disruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
- [[timing-attack]]
