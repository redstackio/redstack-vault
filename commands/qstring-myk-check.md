---
id: cmd-qstring-myk
data: 'if(qString(''myk'')!=''''){ ... }'
tags:
  - param-check
type: command
output: Branches into referrer handling if true
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.715Z'
verified: false
validated: true
submitted: true
---
# qstring-myk-check

## Command

```javascript
if(qString('myk')!=''){ /* process */ }
```

## Description

Checks if the 'myk' query string parameter is non-empty to proceed with vulnerable referrer processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| myk | Query parameter value | Yes |

## Examples

### Basic Usage

```javascript
if(qString('myk')!=''){ console.log('Proceed'); }
```

### Advanced Usage

```javascript
if(qString('myk')!=''){ bindBreadCrumbReferrer(); }
```

## Expected Output

True branch taken if myk present, enabling further execution.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
