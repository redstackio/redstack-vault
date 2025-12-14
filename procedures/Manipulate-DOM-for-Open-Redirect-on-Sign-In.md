---
tags:
  - open-redirect
  - dom-manipulation
  - phishing
  - client-side
  - self-xss
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
  - '[[tools/Mozilla-Firefox-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.443Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: eb7e5adc-83c0-4077-b306-ee4e12b62612
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-DOM-for-Open-Redirect-on-Sign-In

## Summary

This procedure exploits a client-side open redirect vulnerability on the Coinbase sign-in page by using browser developer tools to modify the DOM, altering the post-login redirect URI to an attacker-controlled phishing site. It requires physical access to the victim's device or social engineering and is akin to Self-XSS, as the manipulation occurs client-side without server validation.

## Description

In this attack scenario, the target is the Coinbase sign-in page (https://www.coinbase.com/signin?locale=en), where the form or button element's redirect attribute can be tampered with via DOM inspection. The attacker inspects the element, edits the URI (e.g., action or href), and saves the change, causing the legitimate login flow to redirect to a phishing page after credential entry. Expected outcomes include potential credential theft if the victim submits the form on the manipulated page. Prerequisites include an unlocked victim device and browser access; no server-side exploitation is involved.

## Requirements

1. Mozilla Firefox browser (version 45.9.0 or similar) installed on the victim's machine
2. Physical or engineered access to the unlocked device
3. Internet connectivity to load the Coinbase page and host the phishing site
4. An attacker-controlled domain for the phishing redirect

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict DOM modifications and redirects
- Server-side validation of all post-login redirect URIs against a whitelist
- User education on avoiding developer tools tampering and verifying URLs
- Browser extensions or policies to disable dev tools in sensitive environments
- Monitoring for anomalous redirects in client-side logs

## Objectives

1. Alter the sign-in form's redirect URI to an attacker site
2. Facilitate phishing after credential submission
3. Demonstrate client-side vulnerability equivalent to Self-XSS

## Instructions

### Step 1: Launch and Navigate

**Context**: Start the browser and load the target page to prepare for inspection.

Launch [[tools/Mozilla-Firefox]] and navigate to https://www.coinbase.com/signin?locale=en.

> The page loads the login form; verify the URL in the address bar.

### Step 2: Access Developer Tools

**Context**: Open inspection tools to view the DOM structure.

Right-click on the page and select "Inspect Element" using [[tools/Mozilla-Firefox-Developer-Tools]].

> The inspector panel opens, displaying the HTML elements.

### Step 3: Inspect and Modify Element

**Context**: Locate and edit the sign-in button or form's redirect attribute.

Select the <button> or <form> element for sign-in, hover to reveal attributes, click to edit, and change the URI to https://attacker-phishing-site.com/callback.

> The DOM updates; close tools and test by entering dummy credentials and submitting.

### Step 4: Verify Redirect

**Context**: Confirm the manipulation leads to the phishing site.

Submit the form; observe the redirect behavior.

> Successful execution redirects to the attacker site instead of Coinbase.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]
- [[tools/Mozilla-Firefox-Developer-Tools]]

## Tags

- open-redirect
- dom-manipulation
- phishing
- client-side
- self-xss
