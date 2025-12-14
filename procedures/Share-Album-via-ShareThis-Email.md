---
id: proc-uzbey-xss-share-001
name: Share-Album-via-ShareThis-Email
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:35.868Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - sharing
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Share-Album-via-ShareThis-Email

## Summary

This procedure uses the ShareThis plugin's email sharing function in Uzbey's album feature to distribute a malicious album link, propagating the embedded XSS payload to a target recipient without direct impact on Uzbey users.

## Description

The ShareThis integration in Uzbey's platform allows users to share albums via email using a dedicated icon. When sharing an album with an XSS payload, the plugin fails to sanitize the content, embedding the script in the generated email or linked preview. This enables the payload to reach external ShareThis users, executing upon interaction. The procedure assumes the malicious album is already created.

## Requirements

1. Access to the malicious album on Uzbey
2. Recipient email address
3. ShareThis plugin enabled in the platform

## Defense

Defensive measures and detection strategies:

- Sanitize all shared content before processing by third-party plugins
- Audit third-party integrations like ShareThis for XSS risks
- Log sharing activities and scan for script patterns in payloads

## Objectives

1. Distribute the album link via email
2. Ensure payload is included in the shared content
3. Target ShareThis users for execution

## Instructions

### Step 1: Access Album Sharing Options

**Context**: Locate the ShareThis email function on the album page.

Navigate to the malicious album and identify the letter icon for email sharing.

### Step 2: Initiate Share

**Context**: Trigger the plugin to process and send the album content.

Click the email icon, enter the recipient's email, and optionally add a message. Submit to send.

> The ShareThis plugin generates the email with the album link and unsanitized content, propagating the XSS.

### Step 3: Confirm Delivery

**Context**: Verify the share was sent successfully.

Check for a platform notification or sent email confirmation; monitor recipient's inbox for the link.

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
