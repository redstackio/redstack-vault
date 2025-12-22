---
tags:
  - xss
  - injection
  - google-contacts
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.322Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1a175da2-140f-4ea6-9082-f7e89d527617
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Contact-in-Google-Contacts

## Summary

This procedure involves creating a contact in Google Contacts with a malicious name containing an XSS payload, such as an HTML-breaking script tag or onerror event, to exploit downstream applications that import and display unsanitized contact data without proper escaping.

## Description

In the context of attacking web applications like Openfolio that integrate with Google Contacts, the attacker uses the Google Contacts web interface to add a new contact. The name field is set to a payload like '><img src=x onerror=prompt(1)>', which breaks out of HTML context and injects executable JavaScript. This payload is designed to execute when the name is rendered unsafely in the target application. Prerequisites include a valid Google account. Expected outcomes include the payload surviving import and triggering XSS upon interaction.

## Requirements

1. Valid Google account with access to Contacts
2. Web browser for accessing https://contacts.google.com
3. No special permissions beyond standard user access

## Defense

Defensive measures and detection strategies:

- Sanitize all imported contact data on the application side using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous contact creations in Google Workspace logs

## Objectives

1. Embed XSS payload in contact data for later exploitation
2. Ensure payload compatibility with target application's rendering
3. Prepare for sync and execution phases

## Instructions

### Step 1: Access Google Contacts

**Context**: Log in to Google and navigate to the Contacts interface to begin creating the malicious entry.

Visit https://contacts.google.com in your browser and sign in if prompted.

### Step 2: Create New Contact

**Context**: Add a new contact with the malicious payload in the name field to inject the XSS vector.

Click the "Create contact" button, set the name to '><img src=x onerror=prompt(1)>', add a random email like test@example.com, and save the contact.

> This injects an <img> tag that executes prompt(1) on error, demonstrating XSS. The payload breaks out of any quoting and injects directly into HTML.

**Expected Output**: Contact saved and listed in Google Contacts.

### Step 3: Verify Contact Creation

**Context**: Confirm the malicious contact is present and the payload is intact.

Search for the contact name in the list to ensure it displays correctly without Google sanitizing it prematurely.

**Expected Output**: Contact appears with the full payload string visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[google-contacts]]
