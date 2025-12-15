---
id: cmd-fngetsearchpagename
data: >-
  function fnGetSearchPageName(){ var searchPageName =
  GetKBCookieValue('CoveoSearchUrl'); if(searchPageName !=""){ searchPageName =
  searchPageName.split('/').slice(-1)[0].split('?')[0]; } return searchPageName;
  }
tags:
  - helper-function
type: command
output: Returns page name string or empty
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.709Z'
verified: false
validated: true
submitted: true
---
# fngetsearchpagename

## Command

```javascript
function fnGetSearchPageName(){ var searchPageName = GetKBCookieValue('CoveoSearchUrl'); if(searchPageName !=""){ searchPageName = searchPageName.split('/').slice(-1)[0].split('?')[0]; } return searchPageName; }
```

## Description

Helper function to extract the filename from the CoveoSearchUrl cookie by splitting the path and removing the query string.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CoveoSearchUrl | Cookie name to retrieve | Yes |

## Examples

### Basic Usage

```javascript
let name = fnGetSearchPageName();
```

### Advanced Usage

```javascript
// With cookie set
fnGetSearchPageName(); // Returns 'page.aspx'
```

## Expected Output

Clean page name like 'search.aspx' or empty string.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
