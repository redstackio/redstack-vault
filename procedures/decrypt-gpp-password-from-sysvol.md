---
id: b84cf1aa-9379-4fdf-8b0b-1da6ce4658ad
name: decrypt-gpp-password-from-sysvol
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T18:34:03.961833+00:00'
updated_at: '2023-05-25T19:53:01.794693+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques:
  - '[[NTDS]]'
tags:
  - cryptography
  - data-encryption
  - known-vulnerability
  - gpp
commands:
  - '[[commands/gpp-decrypt-extract-password]]'
platforms:
  - Windows
tools:
  - '[[tools/gpp-decrypt]]'
validated: true
---

# Decrypt GPP Password from SYSVOL

## Summary

This procedure decrypts passwords stored in Group Policy Preferences (GPP) XML files from SYSVOL shares using the publicly known AES key. GPP was a legacy feature (disabled post-2012) but persists in many environments, yielding domain admin creds.

## Description

GPP files in SYSVOL/{GUID}/Machine/Preferences store settings like local admin passwords in cPassword attributes, encrypted with a static AES-256 key Microsoft released in 2012 (MS14-025). Tools like gpp-decrypt reverse this trivially, providing initial domain creds for escalation.

## Requirements

1. Downloaded GPP XML file (e.g., Groups.xml) from SYSVOL
2. gpp-decrypt tool (Ruby-based, install via apt or gem)
3. Extracted cPassword string from XML

## Defense

- Migrate away from GPP; use GPO preferences securely or alternatives
- Monitor SYSVOL access and XML modifications
- Patch MS14-025 and audit for legacy GPP usage with PowerShell

## Objectives

1. Extract encrypted cPassword from GPP XML
2. Decrypt to plaintext password
3. Validate creds against domain

## Instructions

### Step 1: Extract cPassword from XML

**Context**: Parse the downloaded file for the encrypted attribute.

```bash
grep -o 'cpassword="[^"]*"' Groups.xml
```

> Outputs: cPassword="CiDUq6tbrBL1m/js9DmZNIydXpsE69WB9JrhwYRW9xywOz1/0W5VCUz8tBPXUkk9y80n4vw74KeUWc2+BeOVDQ"

### Step 2: Decrypt the String

**Context**: Use gpp-decrypt with the extracted value.

**Command** ([[commands/gpp-decrypt-extract-password]]):
```bash
gpp-decrypt '$_ENCRYPTED_CPASSWORD'
```

> Expected: Plaintext like 'MyUnclesAreMarioAndLuigi!!1!'.

### Step 3: Test Credentials

**Context**: Verify with a simple AD query.

Use net ads info or similar; if valid, proceed to auth steps.
