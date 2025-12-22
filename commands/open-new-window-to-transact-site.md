---
id: cmd-open-window-transact-900619
data: 'win = window.open("https://transact.playstation.com/","transact");'
tags:
  - window-open
  - bypass
type: command
output: A new window object reference (win) pointing to the opened page
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:37.705Z'
verified: false
validated: true
submitted: true
---
# open-new-window-to-transact-site

## Command

```javascript
win = window.open("https://transact.playstation.com/","transact");
```

## Description

Opens a new browser window to the PlayStation transact site with a specified name, creating an opener relationship for postMessage bypassing origin checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target URL to open | Yes |
| name | Window name for reference | Yes |

## Examples

### Basic Usage

```javascript
win = window.open("https://transact.playstation.com/","transact");
```

### Advanced Usage

```javascript
win = window.open("https://example.com", "winName", "width=800,height=600");
```

## Expected Output

Returns a window object (win) if successful; null if popup blocked.

## Related

- [[Related Procedure]]
