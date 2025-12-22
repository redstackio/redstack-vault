---
id: cmd-set-variable-b-2024
data: b='#roomtitle';0
tags:
  - xss
  - variable-setup
  - dom-reference
type: command
output: Sets variable b without visible output
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.463Z'
verified: false
validated: true
submitted: true
---
# set-variable-b-roomtitle

## Command

```javascript
b='#roomtitle';0
```

## Description

Sets a global variable `b` to the CSS selector for the room title element, with '0' as a no-op padding for syntax in URI context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| b | Variable name for element ID | Yes |
| '#roomtitle' | Selector for target element | Yes |

## Examples

### Basic Usage

```javascript
b='#roomtitle';0
```

### Advanced Usage

```javascript
b='#custom-element';0
```

## Expected Output

No visible output; variable `b` is set in global scope, verifiable in browser console.

## Related

- [[commands/eval-jquery-text]]
