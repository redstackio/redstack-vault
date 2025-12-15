---
id: cmd-insecure-static-coveo
data: >-
  strChild = '<a href="' + varStaticCoveoSearchResultPageURL + '"
  style="color:#999 !important;" >Search Results</a>';
tags:
  - insecure-html
type: command
output: Vulnerable string for innerHTML
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.697Z'
verified: false
validated: true
submitted: true
---
# insecure-static-coveo-url-breadcrumb

## Command

```javascript
strChild = '<a href="' + varStaticCoveoSearchResultPageURL + '" style="color:#999 !important;" >Search Results</a>';
```

## Description

Builds link with unencoded varStaticCoveoSearchResultPageURL, another injection point.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| varStaticCoveoSearchResultPageURL | Static URL variable | Yes |

## Examples

### Basic Usage

```javascript
strChild = '<a href="' + varStaticCoveoSearchResultPageURL + '">Link</a>';
```

### Advanced Usage

```javascript
li.innerHTML = strChild; // Append to DOM
```

## Expected Output

Vulnerable href string ready for injection.

## Related

- [[Related Procedure: Hover-to-Execute-XSS-Payload]]
