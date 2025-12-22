---
id: proc-uuid-2
tags:
  - xss
  - sharing
  - nextcloud
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile App
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:42.905Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Malicious-HTML-File-with-Victim-via-Nextcloud

## Summary

This procedure uses Nextcloud's built-in sharing features to deliver the uploaded malicious HTML file to a victim, encouraging them to open it in the iOS app where the XSS will trigger.

## Description

Nextcloud allows easy sharing of files via links, emails, or direct attachments. The attacker generates a share link for the malicious HTML and sends it to the victim, often via email or chat, disguised as a legitimate document. When the victim accesses it through the Nextcloud iOS App, the WebView loads the unsanitized content. This step relies on social engineering to ensure the victim uses the mobile app.

## Requirements

1. Uploaded malicious file in Nextcloud
2. Victim's contact details (email or Nextcloud username)
3. Sharing permissions enabled on the file

## Defense

Defensive measures and detection strategies:

- Review and approve shared files before access
- Warn users about unexpected file shares
- Log and alert on shares of HTML or script-containing files

## Objectives

1. Deliver payload to victim without direct interaction
2. Prompt victim to open in vulnerable iOS app
3. Maintain plausible deniability in sharing

## Instructions

### Step 1: Generate Share Link

**Context**: In Nextcloud, select the malicious file and create a public or user-specific share.

Right-click the file > Share > Create share link (set to public or specific user).

> Expected output: Share URL generated, e.g., https://nextcloud.example.com/s/abc123.

### Step 2: Distribute to Victim

**Context**: Send the share link via email, chat, or Nextcloud notification to entice opening.

Compose a message like "Please review this document in the app" and include the link.

> Expected output: Victim receives and clicks the link, accessing via iOS app.

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
- [[sharing]]
- [[nextcloud]]
