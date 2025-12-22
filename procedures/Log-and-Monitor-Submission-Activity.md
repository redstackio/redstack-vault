---
id: proc-hackerone-logging-001
tags:
  - logging
  - activity-monitoring
  - metadata-disclosure
type: procedure
tools:
  - '[[tools/h1-py2-script]]'
  - '[[tools/h1-py3-script]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/python-datetime-now]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:29:28.096Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Log and Monitor Submission Activity

## Summary

This procedure logs timestamps for each detected new report submission, allowing analysis of patterns like frequency and timing to infer platform and hacker engagement metrics.

## Description

Integrated into the polling script, it captures datetime on detections and outputs to console or file. Requires prior polling setup and Python's datetime module. Outcomes: Dataset of submission events for metadata extraction, such as peak activity hours.

## Requirements

1. Active polling loop from previous procedure
2. Python with datetime module
3. File I/O for persistent logging (optional)

## Defense

Defensive measures and detection strategies:

- Audit logs for anomalous access patterns
- Obfuscate submission metadata in responses
- Use CAPTCHA or auth for high-volume queries

## Objectives

1. Timestamp each new report detection
2. Compile logs for pattern analysis
3. Reveal undisclosed platform activity insights

## Instructions

### Step 1: Timestamp Detection

**Context**: On length 0 response, record current time.

**Command** ([[commands/python-datetime-now]]):
```python
from datetime import datetime
if len(response.text) == 0:
    timestamp = datetime.now()
    print(f"New report submitted at {timestamp} for ID {current_id}")
```

> Outputs formatted timestamp with ID on detection.

### Step 2: Output for Analysis

**Context**: Log to file or console for ongoing monitoring.

**Command** (Integrated logging):
```python
with open('submissions.log', 'a') as f:
    f.write(f"{timestamp}: ID {current_id}\n")
```

> Appends to log file for historical analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/python-datetime-now]]

## Tools Used

- [[tools/h1-py2-script]]
- [[tools/h1-py3-script]]

## Tags

- logging
- metadata-disclosure
