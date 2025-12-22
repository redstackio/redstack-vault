---
tags:
  - http-request-smuggling
  - response-hijacking
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/turbo-intruder-http-smuggling-script]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 205fe4b2-c4b3-49ef-9cf5-006187ee41fb
created_at: '2025-12-13T09:01:22.000Z'
updated_at: '2025-12-13T09:01:22.000Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Queue Victim Requests for Poisoned Response Observation

## Summary

This procedure queues multiple simulated victim requests using Turbo Intruder to observe the effects of the poisoned backend socket, such as hijacked responses with redirects.

## Description

After poisoning the socket, legitimate-like requests are sent to trigger the smuggled response, demonstrating the impact like random redirects. This helps verify the exploitation in a controlled manner.

## Requirements

1. Turbo Intruder session from previous step
2. Target endpoint accessible
3. Burp Collaborator for detecting interactions if needed

## Defense

Defensive measures and detection strategies:

- Implement strict request validation and reject ambiguous headers
- Log and alert on unexpected redirects or chunked encoding anomalies

## Objectives

1. Simulate user traffic
2. Observe hijacked responses
3. Confirm redirect to malicious site

## Instructions

### Step 1: Queue Victim Requests

**Context**: Send looped GET requests to simulate traffic and check responses.

**Command** ([[commands/turbo-intruder-http-smuggling-script]] victim portion):
```python
victim = '''GET /foo.jpg?x=%s HTTP/1.1 Host: stage.████████ Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) Connection: keep-alive ''' for i in range(15): engine.queue(victim, i) time.sleep(0.2)
```

> This queues 15 victim requests, with one expected to receive the poisoned 302 redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/turbo-intruder-http-smuggling-script]]

## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- response-hijacking
- web-vulnerability
