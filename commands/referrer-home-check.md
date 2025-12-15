---
id: cmd-referrer-home
data: >-
  var previousUrl = document.referrer.toLowerCase();
  if(previousUrl.indexOf('/home.aspx')>-1){ ... } else { ... }
tags:
  - referrer-validation
type: command
output: Skips referrer use if contains /home.aspx
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.713Z'
verified: false
validated: true
submitted: true
---
# referrer-home-check

## Command

```javascript
var previousUrl = document.referrer.toLowerCase(); if(previousUrl.indexOf('/home.aspx')>-1){ /* skip */ } else { /* proceed */ }
```

## Description

Case-insensitive check to avoid using referrer if it originates from /home.aspx, allowing malicious referrers to pass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.referrer | Current referrer string | No |

## Examples

### Basic Usage

```javascript
var previousUrl = document.referrer.toLowerCase(); if(previousUrl.indexOf('/home.aspx')>-1){ return; }
```

### Advanced Usage

```javascript
if(!previousUrl.includes('/home.aspx')){ processReferrer(); }
```

## Expected Output

Proceeds to use referrer if no /home.aspx match.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
