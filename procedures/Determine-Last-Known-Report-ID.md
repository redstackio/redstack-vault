---
id: proc-hackerone-last-id-001
tags:
  - api-enumeration
  - polling
  - reconnaissance
type: procedure
tools:
  - '[[tools/python-requests]]'
  - '[[tools/h1-py2-script]]'
  - '[[tools/h1-py3-script]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/python-requests-get]]'
  - '[[commands/python-raw-input]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:29:28.106Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Determine Last Known Report ID

## Summary

This procedure scans sequentially from a known starting report ID to identify the highest submitted ID on HackerOne by checking for empty responses, establishing a baseline for real-time monitoring.

## Description

Using iterative HTTP requests, the procedure probes IDs upwards until the last one with length 0 is found, indicating the most recent submission. This targets the /reports/[report_id].json endpoint and requires Python scripting. Outcomes include the last known ID, enabling efficient polling without redundant scans.

## Requirements

1. Starting ID (e.g., 159874 from public knowledge)
2. Python environment with requests
3. Custom script like h1-py2.py or h1-py3.py

## Defense

Defensive measures and detection strategies:

- Rate limit sequential requests to the endpoint
- Use consistent response lengths to obscure existence
- Log and alert on iterative ID probing

## Objectives

1. Find the current highest submitted report ID
2. Avoid scanning from zero for efficiency
3. Set up for continuous monitoring

## Instructions

### Step 1: Prompt for Starting ID

**Context**: Allow user input for the last known ID to begin scanning.

**Command** ([[commands/python-raw-input]]):
```python
last_id = raw_input("\nEnter the last report you know about [Ignore if before #159875]: ") or "159874"
```

> Prompts for input, defaults to 159874 if empty.

### Step 2: Iterate and Check Responses

**Context**: Loop from starting ID +1, checking lengths until no more empty responses.

**Command** ([[commands/python-requests-get]]):
```python
import requests
current_id = int(last_id) + 1
while True:
    response = requests.get(f'https://hackerone.com/reports/{current_id}.json')
    if len(response.text) == 0:
        current_id += 1
    else:
        print(f"Last known ID: {current_id - 1}")
        break
```

> Continues until length != 0, outputs the last valid ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/python-requests-get]]
- [[commands/python-raw-input]]

## Tools Used

- [[tools/python-requests]]
- [[tools/h1-py2-script]]
- [[tools/h1-py3-script]]

## Tags

- api-enumeration
- polling
