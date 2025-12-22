---
id: proc-uuid-3
tags:
  - dnn
  - machine-key
  - auth-bypass
type: procedure
tools:
  - '[[tools/dp-crypto]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.492Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-DNN-File-Manager-Access-Link

## Summary

This procedure processes the brute-forced ASP.NET machine key to create a base64-encoded link granting unauthorized access to the DNN DocumentManager, bypassing authentication via the Telerik DialogHandler.

## Description

Once the machine key is obtained, it must be encoded into parameters for the DialogHandler to simulate valid authentication. The key's repetitive nature (every 88 characters) allows flexibility in length. This step outputs a direct URL to the file manager, enabling file operations without login.

## Requirements

1. Brute-forced machine key from prior step
2. Base64 encoding capability (built into dp_crypto output)
3. Target URL knowledge

## Defense

Defensive measures and detection strategies:

- Enforce strong, unique machine keys with high entropy
- Validate all DialogHandler parameters server-side
- Log and alert on unusual base64 payloads in requests

## Objectives

1. Construct valid access link using the key
2. Test link for DocumentManager access
3. Prepare for file upload exploitation

## Instructions

### Step 1: Extract Key from Script Output

**Context**: Parse the dp_crypto output for the raw key.

No command; manually copy the 88-character key string.

> Verify repetition by testing longer keys (e.g., 128 chars) where position 89 matches position 1.

### Step 2: Generate Encoded Link

**Context**: Integrate key into base64 params; dp_crypto automates this.

The script outputs the full link. If manual, encode as: base64(machineKey=recovered_key&other_params).

**Expected Output**: URL like https://target/DialogHandler.aspx?cmd=DocumentManager&dialogValue=encoded_key.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/dp-crypto]]

## Tags

- [[dnn]]
- [[machine-key]]
- [[auth-bypass]]
