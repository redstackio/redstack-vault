---
url: 'https://github.com/cshold/jQuery-Facebook-Photo-Selector'
tags:
  - javascript
  - library
  - vulnerable
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.052Z'
id: b9137ff0-d5a9-484d-807b-d6374921655e
validated: true
submitted: true
---
# jQuery-Facebook-Photo-Selector

**Status**: Unverified

## Overview

jQuery-Facebook-Photo-Selector is a third-party JavaScript library for integrating Facebook photo selection into web applications, commonly used for importing user photos. In security testing, it is notable for vulnerabilities like unsanitized rendering of album metadata.

## Description

This library leverages the Facebook Graph API to fetch and display photo albums and images. It is integrated into applications like Slack for social photo imports but fails to sanitize inputs such as album names, enabling stored XSS attacks when malicious data is reflected in the UI.

## Features

- Feature 1: Fetches Facebook albums and photos via API
- Feature 2: Renders selectable photo grids in jQuery UI
- Feature 3: Supports authentication via Facebook OAuth

## Installation

### Requirements

- jQuery library
- Facebook App ID for API access

### Install Commands

```bash
# Clone from GitHub
 git clone https://github.com/cshold/jQuery-Facebook-Photo-Selector.git
 cd jQuery-Facebook-Photo-Selector
 # Include in HTML: <script src="jquery.facebook.photo.selector.js"></script>
```

## Basic Usage

```javascript
$('#photo-selector').facebookPhotoSelector({
  appId: 'YOUR_APP_ID',
  accessToken: 'USER_TOKEN'
});
```

### Common Options

| Option | Description |
|--------|-------------|
| `appId` | Facebook application ID |
| `accessToken` | User access token for API calls |
| `onSelect` | Callback for selected photos |

## Examples

### Example 1: Basic Usage

```javascript
$('#selector').facebookPhotoSelector({ appId: '12345' });
```

### Example 2: Advanced Usage

```javascript
$('#selector').facebookPhotoSelector({
  appId: '12345',
  accessToken: 'token',
  onError: function(err) { console.log(err); }
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to graph.facebook.com from web apps
- DOM inspection for unsanitized album name rendering
- JavaScript errors from malformed HTML in photo selectors

## Related Procedures


## Related Tools

- [[Facebook Graph API]]

## References

- Official GitHub repository
- Facebook Developer Documentation
