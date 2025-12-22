---
id: 3f3c90bf-f871-46dd-806a-d334a030c7fb
name: Clickjacking-to-Change-User-Email-via-Prefilled-Form
type: procedure
verified: true
submitted: true
created_at: '2020-08-30T17:52:59.129259+00:00'
updated_at: '2023-05-26T01:37:07.208976+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - clickjacking
  - web-applications
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Clickjacking-to-Change-User-Email-via-Prefilled-Form

## Summary

This procedure demonstrates how an attacker can use clickjacking to trick a victim into changing their email address on a web application by overlaying a malicious clickable element on top of the legitimate 'Change Email' button, while pre-filling the new email via URL parameters in an invisible iframe.

## Description

Clickjacking exploits the lack of frame-busting protections or X-Frame-Options headers to embed the target application in an iframe, making it invisible (low opacity) while positioning a visible bait element (e.g., 'Click me') over sensitive UI controls. In this scenario, the attacker crafts an HTML page that loads the target's email change form in an iframe with a pre-filled malicious email parameter (e.g., hacker@attacker-website.com). When the victim interacts with the bait, it submits the form, updating their account email to the attacker's controlled address. This technique requires the target site to allow framing and to accept email changes via GET parameters without additional validation. It is effective against users who are already authenticated and accessing the change email feature.

## Requirements

1. Valid credentials for an attacker account on the target web application to observe the email change flow.
2. Knowledge of the target application's 'Change Email' endpoint URL and its parameters (e.g., email=).
3. A web server to host the malicious HTML exploit page.
4. The target site must not implement X-Frame-Options: DENY or SAMEORIGIN, or Content-Security-Policy frame-ancestors restrictions.
5. Victim must be authenticated in the application for the form submission to succeed.

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages to prevent framing.
- Use Content-Security-Policy with frame-ancestors 'none' or 'self' to restrict embedding.
- Validate all form submissions server-side, requiring CSRF tokens and rejecting GET-based parameter changes for sensitive actions.
- Monitor for unusual email changes and alert users via out-of-band notifications (e.g., original email).
- Educate users on phishing and suspicious links; use client-side frame-busting JavaScript.

## Objectives

1. Trick the victim into submitting a pre-filled email change form without their awareness.
2. Gain control over the victim's account recovery by setting the email to an attacker-controlled address.
3. Maintain stealth by making the interaction appear innocuous (e.g., a simple click).

## Instructions

### Step 1: Authenticate and Analyze the Email Change Flow

**Context**: Log in to the target application with attacker credentials to identify the 'Change Email' endpoint, observe the form parameters, and confirm how email updates are processed via URL or POST requests.

Navigate to the account settings or profile page, access the 'Change Email' tab, and use browser developer tools or a proxy like Burp Suite to intercept the request. Note the URL structure, such as /email?email=newemail@domain.com, and verify if the site allows framing by attempting to embed it in a test iframe.

### Step 2: Craft the Malicious Clickjacking HTML

**Context**: Create an HTML page that embeds the target in a transparent iframe, positions a bait div over the submit button, and pre-fills the malicious email via the URL parameter to automate the change upon click.

Use the following code snippet [[codes/Clickjacking-HTML-with-Prefilled-Email-Form]] to build the exploit. Adjust the iframe src to match the target's email change URL and set the email parameter to the attacker's desired address.

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
<iframe src="https://target-site.web-security-academy.net/email?email=hacker@attacker-website.com"></iframe>
```

Host this HTML on an attacker-controlled server (e.g., via GitHub Pages or a simple HTTP server).

### Step 3: Deliver and Execute the Exploit

**Context**: Send the exploit page to the victim via phishing email, social engineering, or a malicious link, ensuring they are authenticated in the target application (e.g., by directing them to log in first).

When the victim loads the page and clicks the bait element ('Click me'), it aligns with and triggers the 'Update Email' button in the invisible iframe, submitting the pre-filled form and changing their email to the attacker's.

Verify success by attempting account recovery on the victim's account using the new email.
