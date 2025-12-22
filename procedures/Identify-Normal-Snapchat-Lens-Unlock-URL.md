---
id: p-snapchat-identify-unlock-url
tags:
  - csrf
  - snapchat
  - recon
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.601Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify Normal Snapchat Lens Unlock URL

## Summary

This procedure involves locating the standard URL format used by Snapchat for unlocking lenses, which includes a user confirmation prompt, serving as the baseline for CSRF exploitation.

## Description

In the context of Snapchat's lens system, lenses are shared via specific unlock URLs that integrate with the app. The normal format requires user interaction to confirm installation, preventing unauthorized adds. This step is reconnaissance to understand the endpoint before modification. It targets the web-based unlock mechanism accessible via links.

## Requirements

1. Access to a Snapchat lens share link or UUID
2. Web browser or Snapchat app for testing
3. No special credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor for unusual lens unlock requests in app logs
- Implement CSRF tokens on all state-changing endpoints
- Educate users on verifying lens sources

## Objectives

1. Obtain the baseline unlock URL with prompt
2. Verify prompt behavior on target device
3. Prepare for parameter tampering

## Instructions

### Step 1: Locate Lens UUID

**Context**: Snapchat lenses have unique identifiers (UUIDs) used in unlock URLs. Obtain one from a public lens or developer resources.

**Instructions**: Search for a lens in Snapchat and inspect the share link to extract the UUID, e.g., 6ff5a565fca249a1948b1963ee2881b4.

### Step 2: Construct and Test Normal URL

**Context**: Build the standard unlock URL and test it to confirm the prompt appears.

**Instructions**: Form the URL as https://www.snapchat.com/unlock/?type=SNAPCODE&uuid=<UUID>&metadata=01. Open it on a device with Snapchat to see the confirmation prompt.

> The URL will redirect to the app and display a dialog asking to unlock the lens.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[snapchat]]
