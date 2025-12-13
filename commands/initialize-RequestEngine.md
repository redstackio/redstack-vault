---
data: >-
  engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=5,
  requestsPerConnection=1, resumeSSL=False, timeout=10, pipeline=False,
  maxRetriesPerRequest=0, engine=Engine.THREADED,)
tags:
  - scripting
  - turbo-intruder
type: command
executor: python
platforms:
  - Web
id: 76306d9e-e402-4a46-8fd9-8d707cc3e1b6
created_at: '2025-12-13T09:01:22.495Z'
updated_at: '2025-12-13T09:01:22.495Z'
verified: false
validated: true
submitted: true
---
# Initialize RequestEngine

## Command

```python
engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=5, requestsPerConnection=1, resumeSSL=False, timeout=10, pipeline=False, maxRetriesPerRequest=0, engine=Engine.THREADED,)
```

## Description

Initializes the RequestEngine in Turbo Intruder for managing concurrent HTTP requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `endpoint` | Target endpoint | Yes |
| `concurrentConnections` | Number of connections (5) | Yes |
| `requestsPerConnection` | Requests per connection (1) | Yes |
| `resumeSSL` | Resume SSL (False) | Yes |
| `timeout` | Timeout (10) | Yes |
| `pipeline` | Pipeline (False) | Yes |
| `maxRetriesPerRequest` | Max retries (0) | Yes |
| `engine` | Engine type (THREADED) | Yes |

## Examples

### Basic Usage

```python
engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=5, requestsPerConnection=1, resumeSSL=False, timeout=10, pipeline=False, maxRetriesPerRequest=0, engine=Engine.THREADED,)
```

## Expected Output

Engine initialized; no direct output.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
