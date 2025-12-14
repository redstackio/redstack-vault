---
id: 123e4567-e89b-12d3-a456-426614174003
name: Share-Malicious-File-URL-with-Victim
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.221Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Phishing]]'
tags:
  - phishing
  - url-sharing
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---

# Share-Malicious-File-URL-with-Victim

## Summary

This procedure distributes the uploaded malicious file's view URL to a victim admin, tricking them into accessing it and triggering the stored XSS.

## Description

After upload, the 'downloadUrl?action=view' is shared via Dust conversations or external means. This lures the admin into rendering the HTML, executing the payload in their session. Prerequisites: downloadUrl from upload; victim contact. Outcomes: Victim views file, enabling escalation.

## Requirements

1. downloadUrl from successful upload
2. Access to workspace chat or victim communication channel
3. Social engineering pretext (e.g., 'Check this image')

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious file shares
- Preview files without rendering HTML
- Monitor file view logs for unusual patterns

## Objectives

1. Induce victim to access malicious URL
2. Ensure execution in authenticated admin session
3. Set stage for JavaScript payload trigger

## Instructions

### Step 1: Extract View URL

**Context**: From the upload response, identify the shareable link.

**Instructions**: Parse the JSON response for 'file.downloadUrl' and append '?action=view' if needed.

> URL like https://dust.tt/w/<workspace_sid>/files/<file_id>?action=view is ready for sharing.

### Step 2: Distribute to Victim

**Context**: Send the URL to the admin via in-app message or email.

**Instructions**: In Dust conversation, post: 'Hey, take a look at this image: [URL]'. Wait for victim click.

> Victim browser requests the URL, rendering the HTML and executing script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[url-sharing]]
