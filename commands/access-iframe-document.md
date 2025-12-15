---
data: var d = document.querySelector("iframe").contentWindow.document;
tags:
  - dom
  - iframe
type: command
executor: javascript
platforms:
  - Web
id: f4c50713-80ef-4271-9dd8-6f8b5a3580b3
created_at: '2025-12-14T17:23:20.665Z'
updated_at: '2025-12-14T17:23:20.665Z'
verified: false
validated: true
submitted: true
---
# access-iframe-document

## Command

```javascript
var d = document.querySelector("iframe").contentWindow.document;
```

## Description

This JavaScript command selects the first iframe on the page and accesses its content document, enabling cross-frame DOM manipulation in same-origin scenarios like WordPress admin pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "iframe" | CSS selector for the target iframe | Yes |
| contentWindow.document | Access to iframe's DOM | Yes |

## Examples

### Basic Usage

```javascript
var d = document.querySelector("iframe").contentWindow.document;
```

### Advanced Usage

```javascript
var d = document.querySelector("#hidden-iframe").contentWindow.document;
```

## Expected Output

Variable d set to the iframe's document object, allowing queries like d.querySelector(). No console output unless logged.

## Related

- [[procedures/Inject-PHP-Code-via-Iframe-Manipulation]]
