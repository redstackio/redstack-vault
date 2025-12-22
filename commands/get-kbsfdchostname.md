---
id: cmd-get-kbsfdchostname
data: >-
  function fnGetKBSFDCHostName(){ ...
  if(document.location.href.indexOf('kb.informatica.com')>-1){ return
  '//search.informatica.com'; } ... }
tags:
  - hostname-check
type: command
output: Hostname string like '//search.informatica.com'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.703Z'
verified: false
validated: true
submitted: true
---
# get-kbsfdchostname

## Command

```javascript
function fnGetKBSFDCHostName(){ if(document.location.href.indexOf('kb.informatica.com')>-1){ return '//search.informatica.com'; } }
```

## Description

Returns the expected hostname based on the current location, used to validate the referrer domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.location.href | Current URL | No |

## Examples

### Basic Usage

```javascript
let host = fnGetKBSFDCHostName();
```

### Advanced Usage

```javascript
if(referrer.includes(fnGetKBSFDCHostName())){ inject(); }
```

## Expected Output

'//search.informatica.com' for kb.informatica.com.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
