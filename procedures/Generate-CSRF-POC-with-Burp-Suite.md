---
id: proc-003
tags:
  - csrf
  - web
  - poc-generation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:30.007Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Generate-CSRF-POC-with-Burp-Suite

## Summary

This procedure leverages Burp Suite to automatically generate a CSRF proof-of-concept HTML page based on the intercepted request, simulating the cancellation action.

## Description

Using Burp's Engagement Tools, the attacker creates an HTML form that forges the POST request without needing authentication. This POC targets the vulnerable XVIDEOS endpoint and can be customized for the victim's session. The result is a standalone HTML file ready for delivery.

## Requirements

1. Intercepted request from previous procedure
2. Burp Suite Professional
3. Text editor for minor customizations

## Defense

Defensive measures and detection strategies:

- Validate referer headers to block cross-site requests
- Implement SameSite cookies for session management
- Scan for and block suspicious HTML forms in emails/links

## Objectives

1. Create exploitable HTML simulating the POST
2. Ensure POC works in victim's authenticated context
3. Prepare for social engineering delivery

## Instructions

### Step 1: Access Engagement Tools

**Context**: Use Burp's feature to generate the POC.

In Burp's Proxy tab, right-click the intercepted cancellation request and select Engagement tools > Generate CSRF POC.

### Step 2: Customize POC

**Context**: Adjust the generated HTML for the target.

Burp opens the POC in a viewer; copy the HTML code. Replace any placeholders with the actual user ID (e.g., USER123) in the form action URL.

### Step 3: Save as HTML File

**Context**: Create the deliverable file.

Paste the code into a new file named csrf-poc.html. Test locally if possible (ensure not submitting to real endpoint during testing).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
