---
type: procedure
description: >-
  This procedure demonstrates how to perform a clickjacking attack to trick a
  logged-in user into deleting their account, even when CSRF protection is
  enabled on the target page.
verified: true
submitted: true
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - clickjacking
  - csrf-bypass
  - web-applications
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
created_at: '2020-08-05T19:10:56.237124+00:00'
updated_at: '2023-05-26T01:32:33.498880+00:00'
validated: true
---

# Clickjacking-to-Bypass-CSRF-and-Delete-Account

## Summary

This procedure outlines a clickjacking attack that overlays a deceptive clickable element on a target web application's account deletion button, tricking a logged-in victim into performing the action unintentionally. Despite CSRF tokens protecting the form, the attack succeeds because clickjacking exploits user interface manipulation rather than form submission forgery. The malicious page uses an iframe to embed the target site with low opacity and positions a fake button to align with the real delete button, delivered via social engineering.

## Description

Clickjacking, also known as a UI redress attack, involves embedding the target application in an iframe on a malicious page and overlaying invisible or semi-transparent elements to lure the victim into clicking on hidden actions. In this scenario, the target is a web application with a protected account deletion feature that includes a CSRF token in the form. The attacker creates a malicious HTML page that loads the target's account page in an iframe, sets its opacity to 0.1 to make it nearly invisible, and places a prominent "Click here for prize" div exactly over the delete button. When the victim, who must be logged in to the target site, visits the malicious page and clicks the lure, they inadvertently submit the delete form. This bypasses CSRF because the click originates from the legitimate iframe context, including the valid token. The attack requires social engineering to get the victim to visit the page while authenticated and relies on the absence of frame-busting protections like X-Frame-Options.

## Requirements

1. Access to create a legitimate user account on the target web application.
2. Knowledge of the target's account management page URL, specifically the path containing the delete account button (e.g., /account).
3. A web server to host the malicious HTML page (local or remote, such as Apache or a simple Python HTTP server).
4. Social engineering capabilities to deliver the malicious link to the victim (e.g., email phishing).
5. The victim must be logged in to the target application in their browser session when accessing the malicious page.
6. No browser extensions or settings that block iframes or detect clickjacking (common in standard user browsers).

## Defense

Defensive measures and detection strategies:

- Implement frame-busting headers like X-Frame-Options: DENY or SAMEORIGIN to prevent embedding in iframes.
- Use Content Security Policy (CSP) with frame-ancestors 'none' or 'self' to restrict framing.
- Educate users on phishing and suspicious links; promote verification of URLs before clicking.
- Monitor for unusual account deletion patterns, such as sudden spikes from specific IPs or user agents.
- Deploy client-side JavaScript checks for iframe embedding and alert or block if detected.
- Use multi-factor authentication (MFA) for sensitive actions like account deletion to add an extra layer even if clicked accidentally.

## Objectives

1. Primary objective: Trick the authenticated victim into clicking the hidden delete account button via UI overlay.
2. Secondary objective: Demonstrate that CSRF tokens do not mitigate clickjacking, as the submission occurs in the legitimate context.
3. Expected outcome: Victim's account is deleted, resulting in loss of access and an "Unauthorized" error on subsequent login attempts.

## Instructions

### Step 1: Create and Authenticate a Legitimate Account

**Context**: Establish baseline access to the target application to understand the account deletion interface and ensure the victim can be in an authenticated state.

Log in to the target web application using a test account. Navigate to the account settings or profile page to locate the delete account option. This step verifies the presence of the CSRF token in the form (inspect the element to confirm a hidden input field with a token value).

### Step 2: Inspect the Delete Account Button

**Context**: Analyze the DOM structure to determine the exact positioning needed for the overlay in the malicious page.

Right-click the "Delete account" button and select "Inspect Element." Observe the button's coordinates relative to the page (e.g., using browser dev tools to measure offsets). Note the CSRF token in the surrounding form, confirming it's present but irrelevant to the clickjacking vector.

### Step 3: Create the Malicious Clickjacking Page

**Context**: Build the HTML page that embeds the target in an iframe and overlays the deceptive element to align with the delete button.

Create an HTML file using the provided code snippet [[codes/Clickjacking-HTML-Overlay-for-Account-Deletion]]. Adjust the iframe src to the target's account page URL if needed (replace the hardcoded URL). Set the div position (top and left offsets) based on Step 2 inspection to ensure perfect alignment. The iframe opacity of 0.1 makes the target nearly invisible. Save the file (e.g., as clickjack.html) and host it on a web server.

**Code** ([[codes/Clickjacking-HTML-Overlay-for-Account-Deletion]]):

```
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

Host the page and test locally: Open in a browser while logged in to the target site. Hover over the div to confirm cursor changes to a hand icon, indicating clickability.

### Step 4: Deliver the Malicious Page to the Victim

**Context**: Use social engineering to entice the victim to visit the page while authenticated to the target application.

Send the URL of the hosted malicious page to the victim via email, chat, or other means, framing it as an opportunity (e.g., "Click here to claim your prize!") Ensure the victim is already logged in to the target site in the same browser session.

### Step 5: Verify Account Deletion

**Context**: Confirm the attack's success by checking the victim's access post-click.

After the victim clicks the lure, have them attempt to access the target application. They should receive an "Unauthorized" message, indicating the account deletion succeeded. On the attacker side, monitor server logs for the page load if applicable.

Expected Output: The victim's session ends with account removal; no direct output from the malicious page, but browser dev tools on the iframe show the form submission with the CSRF token.
