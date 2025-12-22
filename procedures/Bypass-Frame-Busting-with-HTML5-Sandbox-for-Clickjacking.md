---
id: 942d4857-3198-4444-81aa-8724bc120614
name: Bypass-Frame-Busting-with-HTML5-Sandbox-for-Clickjacking
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T12:45:20.713986+00:00'
updated_at: '2023-05-26T01:04:39.765777+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/Clickjacking]]'
  - '[[tags/frame-buster]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# Bypass-Frame-Busting-with-HTML5-Sandbox-for-Clickjacking

## Summary

This procedure demonstrates how to perform a clickjacking attack by bypassing frame-busting scripts using the HTML5 sandbox attribute set to 'allow-forms'. It tricks a victim into interacting with a hidden iframe containing the target application's sensitive form, such as an email change feature, without their awareness.

## Description

Frame-busting scripts are client-side defenses that prevent a webpage from being loaded inside an iframe to mitigate clickjacking attacks. However, the HTML5 sandbox attribute can be used to restrict the iframe's capabilities while allowing form submissions, effectively bypassing these protections. This technique targets web applications with weak frame-busting implementations, enabling an attacker to overlay a malicious page on top of the target's interface. The attack relies on social engineering to lure the victim into clicking a disguised element, leading to unauthorized actions like account modification. It is particularly effective against applications handling user data changes, such as email updates, and assumes the attacker has no direct access but can host a malicious HTML page.

## Requirements

1. Access to a web server or hosting service to serve the malicious HTML page.
2. Knowledge of the target application's URL and sensitive endpoint (e.g., email change form).
3. Ability to perform social engineering to deliver the link to the victim (e.g., via email or phishing).
4. A legitimate user account on the target application for reconnaissance (optional but recommended to observe the interface).
5. Basic HTML knowledge to customize the overlay and positioning.

## Defense

Defensive measures and detection strategies:

- Implement Content-Security-Policy (CSP) headers with 'frame-ancestors' directive to restrict framing.
- Use X-Frame-Options: DENY or SAMEORIGIN headers to prevent iframing.
- Monitor for unusual form submissions or account changes from unexpected IPs.
- Educate users on phishing and suspicious links.
- Employ client-side JavaScript to detect overlay attempts or anomalous clicks.

## Objectives

1. Bypass frame-busting protections to load the target page in an iframe.
2. Overlay a deceptive element to trick the victim into submitting a form.
3. Achieve unauthorized action, such as changing the victim's email to the attacker's.
4. Maintain low visibility by adjusting iframe opacity and positioning.

## Instructions

### Step 1: Reconnaissance on Target Application

**Context**: Log in as a legitimate user to identify the sensitive endpoint and observe the interface layout, ensuring the attack can be positioned accurately.

Navigate to the target application's login page, create or use an existing account, and access the sensitive feature (e.g., 'Change Email'). Note the exact URL, form elements, and positioning of the submit button.

### Step 2: Create Malicious HTML Page

**Context**: Build an HTML page that embeds the target endpoint in an iframe with the sandbox attribute to allow form interactions while bypassing frame-busting.

Use the following code snippet to create the page: [[codes/Clickjacking-HTML-Page-with-Sandbox-Bypass]]. Save it as an .html file and host it on a server accessible via a public URL. Customize the src attribute with the target's sensitive URL, pre-filling any parameters (e.g., attacker's email). Adjust opacity, position, and overlay text to disguise the interaction.

### Step 3: Deliver the Malicious Link

**Context**: Use social engineering to entice the victim to visit the hosted page, ensuring they click the overlaid element which submits the hidden form.

Send the URL of the hosted HTML page to the victim via email, chat, or other means, using a pretext like 'Click here for a prize' or urgent notification. Ensure the iframe is nearly invisible (e.g., opacity 0.1) so the victim doesn't notice the underlying content.

### Step 4: Verify Attack Success

**Context**: Monitor the target application for the unauthorized change to confirm the victim interacted with the hidden form.

After the victim clicks, check the application (using your legitimate account or notifications) for the email update to your attacker's address. If successful, the change occurs without alerting the victim to the clickjacking.
