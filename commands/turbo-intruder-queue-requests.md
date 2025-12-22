---
id: 58bc12fb-c849-478e-9673-3188afdec321
name: turbo-intruder-queue-requests
type: command
executor: python
data: |+
  def queueRequests(target, wordlists):
      engine = RequestEngine(endpoint=target.endpoint,
                          concurrentConnections=30,
                          requestsPerConnection=30,
                          pipeline=False
                          )

      # Queue multiple requests with different parameters
      for i in range(30):
          engine.queue(target.req, i)
          engine.queue(target.req, target.baseInput, gate='race1')

      # Start the engine and open gate for race condition
      engine.start(timeout=5)
      engine.openGate('race1')
      engine.complete(timeout=60)

output: null
created_at: '2023-04-06T03:56:31.880462+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - race-condition
  - turbo-intruder
verified: true
validated: true
---

# turbo-intruder-queue-requests

## Command

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                        concurrentConnections=30,
                        requestsPerConnection=30,
                        pipeline=False
                        )

    # Queue multiple requests with different parameters
    for i in range(30):
        engine.queue(target.req, i)
        engine.queue(target.req, target.baseInput, gate='race1')

    # Start the engine and open gate for race condition
    engine.start(timeout=5)
    engine.openGate('race1')
    engine.complete(timeout=60)
```

## Description

This Python function is used within Turbo Intruder to queue multiple concurrent HTTP requests, creating a race condition by releasing gated requests simultaneously. It sets up an engine with configurable concurrency and pipelines requests to the target endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| target | Turbo Intruder target object with endpoint, req, and baseInput | Yes |
| wordlists | List of wordlists (unused in this basic race but extensible for fuzzing) | No |
| concurrentConnections=30 | Number of simultaneous connections | No (default 30) |
| requestsPerConnection=30 | Requests per connection | No (default 30) |
| pipeline=False | Disable HTTP pipelining for better race control | No (default False) |
| timeout=5 | Engine start timeout in seconds | No (default 5) |
| gate='race1' | Gate name for synchronizing requests | No (default 'race1') |
| timeout=60 | Completion timeout in seconds | No (default 60) |

## Examples

### Basic Usage

Paste directly into Turbo Intruder's queueRequests function editor after sending a request to Intruder.

### Advanced Usage

Increase concurrency for aggressive attacks:

```python
engine = RequestEngine(..., concurrentConnections=100, requestsPerConnection=100)
```

## Expected Output

Turbo Intruder console logs: "Engine started", "Gate 'race1' opened", followed by request/response counts. No errors if queuing succeeds; results appear in the attack table upon completion.

## Related

- [[procedures/Exploit-Race-Condition-with-Turbo-Intruder]]
- [[commands/turbo-intruder-handle-response]]
