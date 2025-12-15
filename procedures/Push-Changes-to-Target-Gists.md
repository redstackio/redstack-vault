---
id: 123e4567-e89b-12d3-a456-426614174004
name: Push-Changes-to-Target-Gists
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.894Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - gists
  - impersonation
  - data-tampering
commands: []
platforms:
  - Web
  - Cloud (GitHub Enterprise)
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Push-Changes-to-Target-Gists

## Summary

This procedure uses a forged SSH certificate to authenticate as a target user and push unauthorized changes to their gists on gist.github.com, exploiting the authentication bypass.

## Description

With the malicious certificate configured, the attacker clones the target gist (requiring URL knowledge), makes changes, and pushes them back. This works for both secret and public gists in GitHub Enterprise Server < 3.9, leading to data tampering without detection if not monitored.

## Requirements

1. Malicious SSH certificate from prior procedure
2. SSH config pointing to the certificate
3. Known URL of the target gist
4. Git installed

## Defense

Defensive measures and detection strategies:

- Enable gist access logging and review for anomalous pushes
- Restrict SSH cert usage to repositories only
- Use webhooks or audits for gist modifications

## Objectives

1. Authenticate to gist.github.com as the impersonated user
2. Modify and push changes to secret/public gists
3. Achieve unauthorized data access and tampering

## Instructions

### Step 1: Configure SSH for Certificate

**Context**: Set up SSH to use the malicious certificate for GitHub connections.

Edit `~/.ssh/config` to include:

```bash
Host gist.github.com
  HostName gist.github.com
  User git
  IdentityFile ~/.ssh/target_key
  IdentitiesOnly yes
  CertificateFile ~/.ssh/target_key.pub-cert.pub
```

### Step 2: Clone and Push to Gist

**Context**: Access the target gist and perform the push.

Clone the gist using its URL (e.g., git@gist.github.com:abc123.git):

```bash
git clone git@gist.github.com:abc123.git target_gist
cd target_gist
# Make changes, e.g., echo "malicious content" > file.txt
git add .
git commit -m "Unauthorized change"
git push origin main
```

The push authenticates via the certificate, succeeding due to the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[git-clone]]
- [[git-push]]

## Tools Used

- [[Git]]
- [[OpenSSH]]

## Tags

- [[gists]]
- [[impersonation]]
- [[data-tampering]]
