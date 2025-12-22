---
id: cmd-bootbox-alert-dynamic
data: 'bootbox.alert(`${username} is unavailable`);'
tags:
  - xss
  - dynamic
  - bootbox
  - template
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.814Z'
verified: false
validated: true
submitted: true
---
# bootbox-alert-dynamic-user-input

## Command

```javascript
bootbox.alert(`${username} is unavailable`);
```

## Description

This command illustrates XSS risk from dynamic user data like usernames interpolated into Bootbox messages, treated as HTML and executed if containing scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| username | Interpolated string with potential user input (e.g., containing <script>) | Yes |

## Examples

### Basic Usage

```javascript
let username = '<script>alert(1);</script>';
bootbox.alert(`${username} is unavailable`);
```

### Advanced Usage

```javascript
bootbox.alert(`Welcome, ${escapedUserInput}`);
```

## Expected Output

Message shown as HTML; if username contains script, it executes in the dialog context.

## Related

- [[commands/bootbox-alert-error-message]]
- [[procedures/Trigger-Bootbox-Dialog-to-Execute-Script]]
