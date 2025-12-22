---
tags:
  - csrf
  - drive-by
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.891Z'
sub_techniques: []
id: fadfbed7-6dfb-4ab3-9142-a329444cc3e7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deploy-and-Execute-CSRF-Payload-in-Victim-Browser

## Summary

This procedure deploys the malicious HTML to a victim's browser, triggering the automatic execution of the CSRF login forgery, which logs the victim into the attacker's MoPub account without their knowledge or consent.

## Description

Once the HTML is prepared, it is delivered to the victim via phishing, malicious links, or embedded in a site. The browser loads the page, executes the JavaScript, and sends the POST request using the victim's cookies, exploiting the endpoint's lack of CSRF protection. This enables attacker monitoring of victim actions post-login. The attack relies on the victim having an active session or being tricked into visiting the page while authenticated elsewhere.

## Requirements

1. Hosted or shareable malicious HTML file
2. Victim interaction (e.g., clicking a link)
3. Victim's browser must support JavaScript and AJAX

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Use browser extensions to block cross-site requests
- Log and alert on anomalous login sources

## Objectives

1. Trigger forged login from victim's context
2. Achieve session takeover effects
3. Enable post-exploitation like activity monitoring

## Instructions

### Step 1: Deliver Payload to Victim

**Context**: Distribute the HTML file to entice the victim to open it in their browser.

Host the file on a web server or send via email as an attachment. For example, include a link in a phishing email: "Click here to view urgent report: [link to HTML]."

> Upon opening, the script runs silently in the background.

### Step 2: Confirm Execution

**Context**: Ensure the request is sent from the victim's side.

If possible, have the victim report any page load, or use server-side logging on the proxy/host to detect access.

> Expected: Automatic POST request without user prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- csrf
- drive-by
- execution
