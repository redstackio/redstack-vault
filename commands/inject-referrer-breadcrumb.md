---
id: cmd-inject-referrer
data: >-
  var varDocumentReferrer = document.referrer; if(varDocumentReferrer !=""){
  if(varDocumentReferrer.toLowerCase().indexOf(fnGetKBSFDCHostName())!=-1){ var
  li = document.createElement('li'); strChild = '<a href="' +
  varDocumentReferrer + '" style="color:#999 !important;" >Search Results</a>';
  li.innerHTML = strChild;
  document.getElementById('DynamicBreadcrumb').appendChild(li); } ... }
tags:
  - xss-injection
type: command
output: 'Appends vulnerable <a> element to #DynamicBreadcrumb'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.707Z'
verified: false
validated: true
submitted: true
---
# inject-referrer-breadcrumb

## Command

```javascript
var varDocumentReferrer = document.referrer; if(varDocumentReferrer !=""){ if(varDocumentReferrer.toLowerCase().indexOf(fnGetKBSFDCHostName())!=-1){ var li = document.createElement('li'); strChild = '<a href="' + varDocumentReferrer + '" style="color:#999 !important;" >Search Results</a>'; li.innerHTML = strChild; document.getElementById('DynamicBreadcrumb').appendChild(li); } }
```

## Description

Core vulnerable code that injects the unencoded document.referrer into an HTML href attribute and appends it to the breadcrumb container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.referrer | Value to inject | Yes |
| fnGetKBSFDCHostName() | Hostname matcher | No |

## Examples

### Basic Usage

```javascript
let strChild = '<a href="' + document.referrer + '">Link</a>'; li.innerHTML = strChild;
```

### Advanced Usage

```javascript
// Full append
document.getElementById('DynamicBreadcrumb').appendChild(li);
```

## Expected Output

New <li> with malicious <a> added to DOM.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
