---
id: uuid-add-noreferrer
data: '$(document).ready(function(){ $("a").attr(''rel'',''noreferrer''); });'
tags:
  - defense
  - javascript
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.824Z'
verified: false
validated: true
submitted: true
---
# add-noreferrer-to-links

## Command

```javascript
$(document).ready(function(){ $("a").attr('rel','noreferrer'); });
```

## Description

jQuery script to dynamically add rel='noreferrer' to all anchor tags on page load, preventing Referer header leakage of sensitive URL params like OAuth codes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.ready | Waits for DOM load | Yes |
| a | Selector for all links | Yes |
| attr('rel','noreferrer') | Sets attribute | Yes |

## Examples

### Basic Usage

```javascript
$(document).ready(function(){ $("a").attr('rel','noreferrer'); });
```

### Advanced Usage

Target specific links: $("a[href^='http']").attr('rel','noreferrer');

## Expected Output

All <a> tags updated with rel='noreferrer'; subsequent clicks omit Referer.

## Related

- [[procedures/Test-Redirect-on-Pages-with-External-Links]]
- [[procedures/Initiate-OAuth-and-Leak-Code-via-Referer]]
