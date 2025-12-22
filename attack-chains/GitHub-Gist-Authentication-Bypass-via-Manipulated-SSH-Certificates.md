---
tags:
  - authentication-bypass
  - ssh
  - github
  - gist
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ssh-keygen-generate-certificate]]'
platforms:
  - Web
  - GitHub Enterprise Server
complexity: medium
procedures:
  - '[[procedures/Generate-SSH-Certificate-with-Arbitrary-Username-Extension]]'
  - '[[procedures/Exploit-SSH-Authentication-to-Modify-GitHub-Gists]]'
step_count: 2
techniques:
  - '[[Use Alternate Authentication Material]]'
  - '[[SSH]]'
description: >-
  Multi-stage attack chain exploiting an authentication bypass vulnerability in
  GitHub Enterprise Server to modify other users' gists using crafted SSH
  certificates.
skill_level: intermediate
impact_level: high
id: acbe6d41-0ffc-4d16-aa9f-add59fc92d73
created_at: '2025-12-11T03:47:39.351Z'
updated_at: '2025-12-11T03:47:39.351Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1550]]'
  - '[[T1021.004]]'
---
# GitHub Gist Authentication Bypass via Manipulated SSH Certificates

Multi-stage attack chain demonstrating how attackers can exploit an improper authentication vulnerability in GitHub Enterprise Server versions prior to 3.9 to bypass authentication on gist.github.com using crafted SSH certificates, enabling unauthorized modification of other users' secret and public gists if the URL is known.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Crafted SSH Certificate] --> B[Authenticate and Push Changes]
    B --> C[Unauthorized Gist Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #ssh-keygen
- #git

### Target Environment

- GitHub Enterprise Server versions prior to 3.9
- Access to gist.github.com over SSH
- Knowledge of target gist URL

### Initial Access Requirements

- Ability to generate SSH certificates (requires a CA key, but attacker can use their own)
- Network access to gist.github.com
- No prior credentials needed for bypass

## Detailed Attack Procedures

### Step 1: Create Crafted SSH Certificate - [[procedures/Generate-SSH-Certificate-with-Arbitrary-Username-Extension]]

**Procedure**: [[procedures/Generate-SSH-Certificate-with-Arbitrary-Username-Extension]]

**Objective**: Generate an SSH certificate with a custom extension that specifies an arbitrary username to authenticate as on gist.github.com.

**Expected Output**: A signed SSH certificate file that includes the extension for the target username.

First, use [[commands/ssh-keygen-generate-certificate]] to create the certificate:

```bash
ssh-keygen -s ca_key -I cert_id -n principals -O extension:login@github.com=targetusername user_key.pub
```

Verify the certificate contents to ensure the extension is present.

**Success Indicators**:
- Certificate file is generated without errors
- The extension 'login@github.com=targetusername' is visible in the certificate details

### Step 2: Authenticate and Push Changes - [[procedures/Exploit-SSH-Authentication-to-Modify-GitHub-Gists]]

**Procedure**: [[procedures/Exploit-SSH-Authentication-to-Modify-GitHub-Gists]]

**Objective**: Use the crafted SSH certificate to bypass authentication and push modifications to the target user's gist.

**Expected Output**: Successful push of changes to the target gist, confirming unauthorized access.

Clone the target gist using the crafted certificate, make changes, and push using [[commands/git-push-over-ssh]]:

```bash
git clone git@gist.github.com:target_gist_id.git
git commit -m "Unauthorized modification"
git push
```

Ensure the SSH configuration uses the crafted certificate for authentication.

**Success Indicators**:
- Git push succeeds without authentication errors
- Changes are reflected in the target gist on gist.github.com

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication using manipulated SSH certificates
2. Achieved unauthorized modification of secret and public gists
3. Demonstrated impact on GitHub Enterprise Server integrity

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Use Alternate Authentication Material]]
- [[SSH]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
