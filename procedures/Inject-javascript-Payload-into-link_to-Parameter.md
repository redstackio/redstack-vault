---
tags:
  - xss
  - ruby-on-rails
  - link_to
  - javascript
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.083Z'
sub_techniques: []
id: 1445a3bb-b2d6-49f2-b0f4-8832f37717e3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-javascript-Payload-into-link_to-Parameter

## Summary

This procedure exploits the lack of sanitization in Rails link_to by injecting a javascript: URL scheme into a user-controlled parameter, resulting in a clickable link that executes arbitrary JavaScript code in the browser context upon interaction.

## Description

The attack leverages the direct insertion of untrusted params into the href attribute of link_to, allowing schemes like javascript: to bypass typical escaping. In a Rails app, this occurs when code like `<%= link_to 'Back', params[:back] %>` is used without validation. The target is a web browser interacting with the Rails view. Prerequisites include access to the vulnerable endpoint. Outcomes include JS execution for data exfiltration, phishing, or defacement.

## Requirements

1. Confirmed vulnerable view from prior access
2. Web browser to construct and visit modified URLs
3. URL encoding knowledge for payloads (e.g., %3A for :)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize link parameters to allow only http/https schemes
- Use Rails' safe helpers or gems like rails-html-sanitizer
- Enable strict CSP headers to prevent JS execution from links
- Log and alert on javascript: or data: schemes in parameters

## Objectives

1. Generate a malicious link via parameter manipulation
2. Execute JavaScript in the victim's session
3. Demonstrate impact like domain alerting or cookie theft

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Encode a javascript: payload to evade basic filters and insert it into the parameter.

Construct the URL: `http://target-app.com/path?back=javascript%3Aalert%28document.domain%29%3B`. The %3A encodes :, and %28/%29 for parentheses.

> This payload alerts the current domain; replace with more malicious code like `javascript:fetch('/steal?cookie='+document.cookie)` for exfiltration.

### Step 2: Trigger and Verify Execution

**Context**: Load the page and interact with the rendered link to execute the payload.

Visit the crafted URL, inspect the source for `<a href="javascript:alert(document.domain);">Back</a>`, then click the link.

> Successful execution shows an alert popup. In a real attack, this could run silently in an iframe or auto-click context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[ruby-on-rails]]
- [[JavaScript]]
- [[payload-injection]]
