---
tags:
  - phishing
  - file-sharing
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-18T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T03:16:25.149Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
id: 20bd855d-a519-44a6-b7a1-c4bf6a70e2ab
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Share-Malicious-File-with-Victim

## Summary

This procedure uses Nextcloud's built-in sharing features to distribute the uploaded malicious HTML file to a target user, enabling social engineering to prompt opening in the iOS app.

## Description

Nextcloud provides secure file sharing via links or direct user shares. After uploading the payload file, generate a share that notifies or links to the victim. This step relies on the victim's trust in shared files from Nextcloud. The share does not execute the payload but positions it for the final trigger. Prerequisites: The malicious file must already be uploaded, and the attacker's account must have sharing permissions with the victim.

## Requirements

1. Uploaded malicious file in Nextcloud
2. Victim's Nextcloud username or email for direct sharing
3. Sharing permissions enabled on the Nextcloud instance

## Defense

Defensive measures and detection strategies:

- Educate users on verifying shared files before opening, especially HTML types
- Implement share approval workflows for sensitive files
- Log and alert on shares of executable or script-like file types (e.g., HTML)

## Objectives

1. Deliver the malicious file to the victim without arousing suspicion
2. Ensure accessibility via the Nextcloud iOS app
3. Set up for victim interaction to trigger exploitation

## Instructions

### Step 1: Select and Share the File

**Context**: Initiate sharing from the web interface to reach the victim.

In Nextcloud files view, right-click the `malicious.html` file, select "Share", and choose direct share to the victim's account or generate a public link with password/view-only permissions.

> Confirm the share by checking notifications or the link functionality.

### Step 2: Notify the Victim

**Context**: Prompt the victim to access the file, ideally via the iOS app.

Send a message or email referencing the shared file, e.g., "Check out this document I shared on Nextcloud."

> Monitor for victim access logs if available in Nextcloud admin settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[file-sharing]]
- [[nextcloud]]
