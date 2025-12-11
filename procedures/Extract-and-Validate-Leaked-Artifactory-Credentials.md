---
tags:
  - credential-validation
  - artifactory
type: procedure
tools:
  - '[[tools/Git]]'
  - '[[tools/Grep]]'
  - '[[tools/Curl]]'
  - '[[tools/JFrog-CLI]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - JFrog Artifactory
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: beac0151-5a1e-4841-827d-a0a60671ff1c
created_at: '2025-12-11T03:47:56.554Z'
updated_at: '2025-12-11T03:47:56.554Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Extract and Validate Leaked Artifactory Credentials

## Summary

This procedure extracts leaked username and password from discovered files and validates them against the target JFrog Artifactory instance to confirm unauthorized access.

## Description

After discovering leaked credentials, manually extract them and test authentication via API calls or CLI tools. This targets JFrog Artifactory instances like https://snapchat.jfrog.io. Successful validation grants access to internal resources, leading to potential data exfiltration or further compromise.

## Requirements

1. Extracted username and password
2. Access to the target Artifactory URL
3. Curl or JFrog CLI installed

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication on Artifactory
- Rotate credentials regularly and monitor login attempts
- Use API keys instead of username/password

## Objectives

1. Confirm credential validity
2. Establish authenticated session
3. Prepare for artifact access

## Instructions

### Step 1: Test Basic Authentication

**Context**: Use Curl to send an authenticated request to verify credentials.

**Command** ([[commands/curl-test-credentials]]):
```bash
curl -u 'username:password' https://snapchat.jfrog.io/artifactory/api/system/ping
```

> Expect a 'OK' response if credentials are valid.

### Step 2: Configure and Test JFrog CLI

**Context**: Set up JFrog CLI for more advanced validation.

**Command** ([[commands/jfrog-cli-login]]):
```bash
jfrog rt config --url=https://snapchat.jfrog.io/artifactory --user=username --password=password
jfrog rt ping
```

> This configures the CLI and pings the server to confirm access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-credentials]]
- [[commands/jfrog-cli-login]]

## Tools Used

- [[tools/Curl]]
- [[tools/JFrog-CLI]]

## Tags

- #credential-validation
- #artifactory
