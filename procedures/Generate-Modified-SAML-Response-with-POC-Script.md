---
tags:
  - saml
  - poc-script
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/samlbypasspoc-py]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python-samlbypass-poc]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 20702655-6cc4-4ed3-8635-45a7aa6aa1ed
created_at: '2025-12-13T09:01:26.304Z'
updated_at: '2025-12-13T09:01:26.304Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Generate Modified SAML Response with POC Script

## Summary

This procedure uses a Python POC script to inject a malicious unsigned Response into the original SAMLResponse, allowing custom assertions for authentication bypass.

## Description

The script takes the original URL-encoded SAMLResponse, decodes it, injects a new Response element with desired attributes (e.g., NameID as 'admin'), and re-encodes it. Modifications start from line 25 in the script.

## Requirements

1. Python3 installed
2. samlbypasspoc.py script downloaded
3. Original URL-encoded SAMLResponse

## Defense

Defensive measures and detection strategies:

- Implement strict XML parsing and signature validation
- Log and alert on malformed SAML responses

## Objectives

1. Inject malicious Response element
2. Set custom assertions for target user
3. Generate tampered SAMLResponse

## Instructions

### Step 1: Prepare the Script

**Context**: Download and modify the POC script.

Download [[tools/samlbypasspoc-py]] and edit from line 25 to set OrganizationName, Email, and NameID.

> Customize for the desired user (e.g., admin).

### Step 2: Execute the Script

**Context**: Run the script with the input SAMLResponse.

Execute [[commands/python-samlbypass-poc]]:

```bash
python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
```

> The script outputs the modified SAMLResponse.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/python-samlbypass-poc]]

## Tools Used

- [[tools/Python3]]
- [[tools/samlbypasspoc-py]]

## Tags

- saml
- poc-script
