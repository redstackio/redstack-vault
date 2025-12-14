---
id: cmd-insecure-url
data: >-
  strChild = '<a href="' + document.URL + '" style="color:#fff
  !important;font-size:10px">Search Results</a>';
tags:
  - insecure-html
type: command
output: Vulnerable string for innerHTML
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.701Z'
verified: false
validated: true
submitted: true
---
# insecure-url-breadcrumb

## Command

```javascript
strChild = '<a href="' + document.URL + '" style="color:#fff !important;font-size:10px">Search Results</a>';
```

## Description

Builds a breadcrumb link using unencoded document.URL, vulnerable to similar XSS if URL controlled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.URL | Current URL to insert | Yes |

## Examples

### Basic Usage

```javascript
let strChild = '<a href="' + document.URL + '">Link</a>';
```

### Advanced Usage

```javascript
li.innerHTML = strChild;
```

## Expected Output

String with potentially injectable href.

## Related

- [[Related Procedure: Hover-to-Execute-XSS-Payload]]
