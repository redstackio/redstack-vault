---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - github
  - lfs
  - deploy-key
  - information-disclosure
  - access-control
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2024-10-01T12:00:00Z'
procedures:
  - '[[procedures/Enumerate-Private-Repos-via-LFS-API]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:39.516Z'
description: >-
  An improper access control vulnerability in GitHub Enterprise Server's
  internal LFS API allows unauthorized enumeration of private repository names
  and owners associated with deploy keys, leading to information disclosure
  without accessing repository contents.
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate Private GitHub Repositories via Internal LFS API Deploy Key Exposure

Multi-stage attack chain demonstrating a complete attack workflow targeting GitHub Enterprise Server's LFS API to disclose private repository details.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify LFS API Endpoint] --> B[Enumeration: Query Deploy Key Repos]
    B --> C[Objective: Disclose Private Repo NWOs]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[curl]]

### Target Environment

- GitHub Enterprise Server (versions prior to 3.14)
- Internal LFS API access (typically requires network proximity or authenticated session, but vulnerability allows unauthorized enumeration)
- Open ports: 443 (HTTPS for API)

### Initial Access Requirements

- Network access to the GitHub Enterprise Server instance
- No specific credentials needed due to the access control flaw, but basic API knowledge assumed
- Prior reconnaissance to identify deploy key usage

## Detailed Attack Procedures

### Step 1: Enumerate Private Repositories
procedure: [[procedures/Enumerate-Private-Repos-via-LFS-API]]

**Objective**: Exploit the internal LFS API to enumerate names and owners (NWOs) of private repositories using deploy keys, disclosing sensitive repository metadata without content access.

**Instructions**: Identify the internal LFS API endpoint on the GitHub Enterprise Server, typically accessible via HTTPS. Use [[commands/curl-lfs-enumerate]] to send a request that bypasses restrictions and lists associated private repositories:

```bash
curl -X GET 'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H 'Accept: application/vnd.github.v3+json'
```

If the endpoint requires minimal auth or is misconfigured, the response will include JSON with repository NWOs. Parse the output to extract private repo details.

**Expected Output**: JSON response containing an array of repository objects with names and owners, e.g., {"repos": [{"name": "private-repo-1", "owner": "user-org"}]}. No actual content is returned, only metadata.

**Success Indicators**:
- JSON response with private repository NWOs
- No authentication errors, indicating successful bypass
- Confirmation of deploy key-linked repos via response fields

## Attack Chain Summary

### Key Achievements

1. Unauthorized enumeration of private repository names and owners
2. Identification of deploy key usage patterns without content access
3. Medium-severity information disclosure affecting GitHub Enterprise Server pre-3.14

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2024-10-01T12:00:00Z*
