---
id: proc-hackerone-polling-001
tags:
  - polling
  - information-disclosure
  - real-time-monitoring
type: procedure
tools:
  - '[[tools/python-requests]]'
  - '[[tools/h1-py2-script]]'
  - '[[tools/h1-py3-script]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/python-requests-get]]'
  - '[[commands/python-time-sleep]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:29:28.101Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Poll for New Report Submissions

## Summary

This procedure implements a polling loop starting from the last known report ID +1, querying sequential IDs and detecting new submissions when response length shifts from 36 to 0, with delays to avoid detection.

## Description

The polling targets HackerOne's report endpoint, retrying on 404s after a 30-second sleep, and advancing on detections. It requires the baseline ID from prior steps and Python scripting. Outcomes: Real-time alerts on new private reports, exposing submission timing.

## Requirements

1. Last known report ID from previous procedure
2. Python with requests and time modules
3. Script execution environment (Windows for py2, Linux for py3)

## Defense

Defensive measures and detection strategies:

- Enforce strict rate limits (e.g., 1 req/min per IP)
- Randomize response lengths or formats
- Deploy WAF rules for sequential endpoint access

## Objectives

1. Detect new report IDs as they are submitted
2. Maintain low detection risk via delays
3. Enable ongoing surveillance of platform activity

## Instructions

### Step 1: Initialize Polling Loop

**Context**: Start from last ID +1 and enter continuous loop.

**Command** ([[commands/python-requests-get]]):
```python
current_id = last_known_id + 1
while True:
    response = requests.get(f'https://hackerone.com/reports/{current_id}.json')
    if len(response.text) == 36:
        # Non-existent, sleep and retry same ID
        time.sleep(30)
    else:
        # Length 0, new submission detected
        print(f"New report at ID {current_id}")
        current_id += 1
```

> Loops indefinitely, detecting transitions.

### Step 2: Implement Delay on Miss

**Context**: Pause 30 seconds when no submission found to reduce request volume.

**Command** ([[commands/python-time-sleep]]):
```python
time.sleep(30)
```

> Delays execution for 30 seconds on length 36 responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/python-requests-get]]
- [[commands/python-time-sleep]]

## Tools Used

- [[tools/python-requests]]
- [[tools/h1-py2-script]]
- [[tools/h1-py3-script]]

## Tags

- polling
- real-time-monitoring
