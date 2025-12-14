---
id: cmd-get-search-name
data: >-
  var varCoveoSearchResultPageName = fnGetSearchPageName();
  if(varCoveoSearchResultPageName !=""){ ... } else { ... }
tags:
  - cookie-parse
type: command
output: 'Uses cookie-derived name if present, else falls back to referrer'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.711Z'
verified: false
validated: true
submitted: true
---
# get-search-page-name

## Command

```javascript
var varCoveoSearchResultPageName = fnGetSearchPageName(); if(varCoveoSearchResultPageName !=""){ /* use */ } else { /* fallback */ }
```

## Description

Retrieves and checks the CoveoSearchUrl cookie for the search page name, falling back to document.referrer if empty.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CoveoSearchUrl | Cookie value to parse | No |

## Examples

### Basic Usage

```javascript
if(fnGetSearchPageName() != ""){ useIt(); }
```

### Advanced Usage

```javascript
let name = fnGetSearchPageName(); // Calls helper
```

## Expected Output

Page name string or empty, directing to referrer use.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
