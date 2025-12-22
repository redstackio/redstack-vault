---
id: 1f1c3fdb-9b71-4cc2-b4e2-a258cc2737f9
name: Clickjacking-to-Trigger-DOM-XSS
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T13:44:54.835230+00:00'
updated_at: '2023-05-26T01:08:24.176872+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - clickjacking
  - dom-xss
  - web-applications
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Clickjacking-to-Trigger-DOM-XSS

## Summary

This procedure demonstrates how to craft and deliver a clickjacking attack that overlays a malicious iframe on a legitimate web application, tricking the victim into clicking a disguised element that triggers a DOM-based XSS payload to alert or steal document cookies.

## Description

Clickjacking involves embedding the target web page in an invisible or low-opacity iframe and overlaying it with a fake clickable element to induce the victim to perform an unintended action. In this case, the action triggers a DOM XSS vulnerability in the target's feedback form by injecting a payload into the 'name' field, causing an alert of document.cookie. This can lead to session hijacking if the victim is authenticated. The attack requires social engineering to lure the victim to the attacker's hosted page and assumes the target application has a reflected DOM XSS in its client-side processing of form inputs.

## Requirements

1. Access to a vulnerable web application with a DOM XSS in form handling (e.g., feedback form that unsafely processes 'name' input).
2. Ability to host an HTML page on a server accessible to the victim (e.g., via GitHub Pages or a personal web server).
3. Knowledge of the target's URL and the exact DOM XSS payload that works (e.g., <img src=1 onerror=alert(document.cookie)>).
4. Social engineering capabilities to deliver the malicious page link to the victim (e.g., via email or phishing).

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers to prevent framing.
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict embedding.
- Sanitize and validate all client-side inputs to prevent DOM XSS, using libraries like DOMPurify.
- Monitor for anomalous network requests to feedback endpoints with suspicious payloads.
- Educate users on phishing and verify links before clicking.

## Objectives

1. Trick the victim into interacting with a framed legitimate page without awareness.
2. Trigger a DOM XSS payload to execute JavaScript in the context of the target's site.
3. Steal session cookies or sensitive data if the victim is authenticated.
4. Achieve session hijacking or further exploitation.

## Instructions

### Step 1: Analyze the Target Application

**Context**: Identify the vulnerable form and confirm the DOM XSS payload works by observing how the feedback form processes inputs client-side.

Manually test the feedback form on the target site (e.g., https://example.com/feedback) by submitting a payload like <img src=1 onerror=alert(document.cookie)> in the 'name' field to verify it triggers an alert without server-side filtering.

### Step 2: Craft the Clickjacking HTML Page

**Context**: Create an HTML page that frames the target, pre-fills the form with the XSS payload, and overlays a deceptive element to induce a click on the submit button.

Use the code snippet [[codes/Clickjacking-HTML-Page-for-DOM-XSS-Trigger]] to build the page. Adjust the iframe src to include the target's feedback URL with pre-filled malicious parameters (name payload, fake email/subject/message). Set low opacity for the iframe to hide it, and position a div overlay saying "Click here for prize" over the submit button area.

Host the HTML file on your server and note the URL for delivery.

### Step 3: Deliver the Malicious Page

**Context**: Use social engineering to get the victim to visit and interact with the page, ensuring they are logged into the target application.

Send the hosted HTML page URL to the victim via email, chat, or phishing site, claiming it leads to a prize or urgent action. Observe if the victim clicks the overlay, which submits the form and triggers the DOM XSS in the framed target.

### Step 4: Verify Exploitation

**Context**: Confirm the payload execution by checking for the alert or exfiltrated data if modified to send cookies to your server.

If the payload is set to alert(document.cookie), the victim's browser will pop up the alert with session data. For stealth, modify to send cookies via an image src to your logging server and monitor incoming requests.

**Expected Output**: Successful click results in DOM XSS execution, alerting cookies or sending them to attacker-controlled endpoint.
