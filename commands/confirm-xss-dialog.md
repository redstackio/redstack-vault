---
id: cmd-confirm-xss-001
data: confirm('XSS')
tags:
  - xss
  - test
type: command
output: Alert box with 'XSS' appears
executor: javascript
platforms:
  - Desktop
  - Electron
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.397Z'
verified: false
validated: true
submitted: true
---
# confirm-xss-dialog

## Command

```javascript
confirm('XSS')
```

## Description

Triggers a browser confirm dialog to demonstrate XSS execution in the Simplenote print context, verifying JavaScript injection success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| message | The text displayed in the dialog | Yes |

## Examples

### Basic Usage

```javascript
confirm('XSS')
```

### Advanced Usage

```javascript
confirm('Stored XSS Confirmed in Simplenote')
```

## Expected Output

A confirm dialog box appears with the message 'XSS', confirming JS execution during print.

## Related

- [[Related Procedure: Inject-Stored-XSS-Payload-in-Note]]
