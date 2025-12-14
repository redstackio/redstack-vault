---
id: proc-extract-irccloud-token
tags:
  - ios
  - token-extraction
  - plist
type: procedure
tools:
  - '[[tools/iExplorer]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:39.893Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Steal Web Session Cookie]]'
---
# Extract-Session-Token-from-Plist

## Summary

This procedure dumps the contents of the IRCCloud plist file to retrieve the session identifier, enabling unauthorized access to the user's account.

## Description

With the device locked, tools like iExplorer allow exporting the plist from the app's Preferences folder. Parsing the XML reveals the session token, which can be reused in IRCCloud's web interface or API for account takeover. No jailbreak is required due to the file's insecure storage.

## Requirements

1. Locked iOS device connected via USB
2. iExplorer tool installed
3. Prior confirmation of file accessibility

## Defense

Defensive measures and detection strategies:

- Secure session tokens with encryption and protection classes
- Audit app file permissions regularly
- Detect anomalous token usage in logs

## Objectives

1. Export and parse plist file
2. Obtain valid session token
3. Facilitate account access

## Instructions

### Step 1: Export Plist File

**Context**: Use iExplorer to dump the file.

Launch [[tools/iExplorer]], connect the device, navigate to the plist path, and select 'Export' or 'Download'.

> Output: Local copy of com.irccloud.IRCCloud.plist.

### Step 2: Parse for Session Token

**Context**: Extract the token value from the XML.

Open the plist in a text editor or use `plutil -p` on macOS:

```bash
plutil -p com.irccloud.IRCCloud.plist
```

> Look for keys like 'session' or 'token'; extract the string value.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/plutil-parse-plist]]

## Tools Used

- [[tools/iExplorer]]

## Tags

- ios
- token-extraction
- plist
