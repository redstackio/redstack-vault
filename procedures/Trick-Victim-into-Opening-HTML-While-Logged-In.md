---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
tags:
  - social-engineering
  - csrf-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.862Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victim-into-Opening-HTML-While-Logged-In

## Summary

Socially engineer the victim to open the malicious HTML file while authenticated in their Shopify store, executing the CSRF transfer.

## Description

Delivery via email, USB, or download link tricks the victim into loading the file in a browser session with active Shopify cookies, triggering the img src request to complete the transfer without alerts.

## Requirements

1. Crafted `csrf.html` file
2. Victim contact method (email, etc.)
3. Victim's Shopify login session active

## Defense

Defensive measures and detection strategies:

- User training on suspicious files/links
- Email filters for HTML attachments
- Session timeout policies

## Objectives

1. Ensure victim authentication
2. Trigger silent request
3. Avoid detection

## Instructions

### Step 1: Deliver File

**Context**: Send the HTML to the victim disguised (e.g., as invoice.html).

Email or host `csrf.html` and share link: "Please view this report: [link to csrf.html]".

> Expected: Victim downloads/opens file.

### Step 2: Confirm Execution

**Context**: Test in incognito with victim creds if possible.

Victim opens in browser logged into store (no prior sessions for clean test); monitor network for request.

> Expected: Domain transfer initiates automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[social-engineering]]
- [[session-hijack]]
