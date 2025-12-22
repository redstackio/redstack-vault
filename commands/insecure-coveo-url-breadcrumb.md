---
id: cmd-insecure-coveo
data: >-
  strChild = '<a href="' + varCoveoSearchResultPageURL + '" style="color:#999
  !important;" >Search Results</a>';
tags:
  - insecure-html
type: command
output: Vulnerable string for innerHTML
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.699Z'
verified: false
validated: true
submitted: true
---
# insecure-coveo-url-breadcrumb

## Command

```javascript
strChild = '<a href="' + varCoveoSearchResultPageURL + '" style="color:#999 !important;" >Search Results</a>';
```

## Description

Insecure construction using unencoded varCoveoSearchResultPageURL for the href.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| varCoveoSearchResultPageURL | URL variable | Yes |

## Examples

### Basic Usage

```javascript
strChild = '<a href="' + varCoveoSearchResultPageURL + '">Link</a>';
```

### Advanced Usage

```javascript
// Set variable first
varCoveoSearchResultPageURL = maliciousUrl;
```

## Expected Output

Injectable HTML string.

## Related

- [[Related Procedure: Hover-to-Execute-XSS-Payload]]
