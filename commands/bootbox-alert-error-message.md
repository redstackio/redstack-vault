---
id: cmd-bootbox-alert-error
data: bootbox.alert(error.message);
tags:
  - xss
  - unsafe
  - bootbox
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.818Z'
verified: false
validated: true
submitted: true
---
# bootbox-alert-error-message

## Command

```javascript
bootbox.alert(error.message);
```

## Description

This command shows unsafe usage where a potentially malicious error.message (user-controlled input) is passed directly to Bootbox alert, allowing XSS if it contains scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| error.message | Dynamic string assumed to be user-controlled | Yes |

## Examples

### Basic Usage

```javascript
let error = {message: '<script>alert(1);</script>'};
bootbox.alert(error.message);
```

### Advanced Usage

```javascript
bootbox.alert(`Error: ${userInput}`);
```

## Expected Output

Error message rendered as HTML; if containing script tags, they execute upon dialog display.

## Related

- [[commands/bootbox-alert-script-injection]]
- [[procedures/Inject-Malicious-Payload-into-Bootbox-Message]]
