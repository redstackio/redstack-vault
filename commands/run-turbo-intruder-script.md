---
data: |-
  def queueRequests(target, wordlists):
      engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10, requestsPerConnection=100)
      for word in wordlists:
          req = target.req.replace('%s', word)
          engine.queue(req)
tags:
  - burp
  - script
type: command
executor: python
platforms:
  - Web
id: a8e67cfc-3c5f-482c-be75-0e1d59c9eec7
created_at: '2025-12-13T09:01:17.579Z'
updated_at: '2025-12-13T09:01:17.579Z'
verified: false
validated: true
submitted: true
---
# Run Turbo Intruder Script

## Command

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10, requestsPerConnection=100)
    for word in wordlists:
        req = target.req.replace('%s', word)
        engine.queue(req)
```

## Description

Executes a Turbo Intruder script to send multiple request variations using a wordlist for payload testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target` | Burp target object | Yes |
| `wordlists` | List of payloads | Yes |

## Examples

### Basic Usage

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint)
    for word in wordlists:
        engine.queue(target.req.replace('%s', word))
```

### Advanced Usage

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=50)
    for word in wordlists:
        engine.queue(target.req.replace('%s', word))
```

## Expected Output

Queued requests sent to the target endpoint.

## Related

- [[commands/craft-smuggled-post-request]]
- [[procedures/Exploit-HTTP-Request-Smuggling-CL-TE]]
