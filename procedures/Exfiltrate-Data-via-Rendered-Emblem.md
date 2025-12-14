---
id: proc-uuid-004
name: Exfiltrate-Data-via-Rendered-Emblem
tags:
  - exfiltration
  - xxe
  - emblem
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.426Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Exfiltrate-Data-via-Rendered-Emblem

## Summary

This procedure finalizes the attack by submitting the malicious SVG to the Rockstar emblem editor for PNG conversion, causing ImageMagick to render exfiltrated LFI/SSRF data visibly in the crew emblem for attacker capture.

## Description

After injecting XXE or XInclude payloads, the editor's conversion feature processes the SVG with ImageMagick, expanding entities or includes into visible text within the PNG output. The attacker views or downloads the emblem to obtain sensitive data, completing the exfiltration without direct server access.

## Requirements

1. Malicious SVG with payloads prepared
2. User session in the emblem editor
3. Ability to view/download generated emblems

## Defense

Defensive measures and detection strategies:

- Limit emblem rendering to sandboxed environments
- Scan generated images for anomalous text content
- Rate-limit SVG submissions to detect abuse

## Objectives

1. Trigger processing to include exfiltrated data
2. Render data visibly for capture
3. Obtain sensitive information without alerts

## Instructions

### Step 1: Submit Malicious SVG

**Context**: Input the crafted SVG into the editor.

Paste the full SVG code into the input field.

> Ensures payloads are included.

### Step 2: Initiate Conversion

**Context**: Convert to PNG to trigger ImageMagick.

Click the "Generate Emblem" or PNG conversion button.

> Processing expands payloads into renderable content.

### Step 3: Capture Output

**Context**: Retrieve the emblem image.

View or save the rendered PNG from the editor.

> Screenshot or download to extract visible data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[Exfiltration]]
- [[xxe]]
- [[emblem]]
