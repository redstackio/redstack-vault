---
data: var c = d.querySelector("#newcontent")
tags:
  - dom
  - select
type: command
executor: javascript
platforms:
  - Web
id: 5f7823be-32d6-4441-8f85-214fd0f48da7
created_at: '2025-12-14T17:23:20.653Z'
updated_at: '2025-12-14T17:23:20.653Z'
verified: false
validated: true
submitted: true
---
# select-newcontent-textarea

## Command

```javascript
var c = d.querySelector("#newcontent")
```

## Description

This JavaScript command queries the DOM (from iframe document d) for the textarea element with ID 'newcontent' in the WordPress plugin editor, targeting the file content input field.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| d | Pre-defined iframe document object | Yes |
| "#newcontent" | CSS selector for the textarea | Yes |

## Examples

### Basic Usage

```javascript
var c = d.querySelector("#newcontent")
```

### Advanced Usage

```javascript
var c = d.querySelector("textarea[name='newcontent']")
```

## Expected Output

Variable c set to the textarea element. Use c.value to read/write content.

## Related

- [[commands/set-textarea-value]]
