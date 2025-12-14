---
tags:
  - dos
  - payload-crafting
  - django
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Python
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 04fcac62-4667-418c-aece-f37d1ffe726b
created_at: '2025-12-14T17:26:48.275Z'
updated_at: '2025-12-14T17:26:48.275Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Craft-Malicious-Input-with-Unbalanced-Braces

## Summary

This procedure details creating a crafted input string designed to exploit the O(n^2) time complexity in Django's strip_punctuation function by using numerous unbalanced opening and closing braces.

## Description

The vulnerability arises from the function's while loop repeatedly trimming wrapping punctuation without efficient checks, causing quadratic performance degradation on strings like many '(' followed by ')'. This procedure generates such a payload, which can be submitted to Django applications to trigger high CPU usage when processed by urlize or urlizetrunc filters. The crafted input was demonstrated in the CVE report via attached files sent to the Django security team.

## Requirements

1. Text editor or Python script for generating long strings
2. Local Django environment for testing the payload
3. Understanding of string manipulation and performance impacts

## Defense

Defensive measures and detection strategies:

- Enforce strict input length limits (e.g., <1000 characters) for fields using urlize/urlizetrunc
- Use regex-based preprocessing to balance or limit punctuation before filtering
- Log and rate-limit inputs containing excessive repeated characters

## Objectives

1. Generate a payload that maximizes loop iterations in strip_punctuation
2. Validate the payload locally to ensure it causes resource exhaustion
3. Prepare the input for submission to target applications

## Instructions

### Step 1: Design the Payload Structure

**Context**: Create a string with unbalanced braces to force repeated trimming.

Construct a string starting with a large number of opening braces (e.g., 5000 '(') followed by closing ones (e.g., 5000 ')'), ensuring no natural balancing occurs during processing.

> Example payload snippet: '(((((' * 1000 + ')))))' * 1000 – adjust length based on testing.

### Step 2: Generate and Test the Payload

**Context**: Build the full string and test it against strip_punctuation.

In a Python script, define the payload and time its processing:

```python
from django.utils.html import strip_punctuation
import time

start = time.time()
result = strip_punctuation(payload)
end = time.time()
print(f"Time: {end - start}s")
```

> Expected: Processing takes seconds or minutes for large payloads, indicating success.

### Step 3: Refine for Application Context

**Context**: Ensure the payload fits the target input field and triggers the filters.

Embed the payload in a realistic input (e.g., a URL-like string) and test in a local Django template rendering with {{ input|urlize }}.

> Verify high CPU via tools like htop during rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[payload-generation]]
- [[exploitation]]
