---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - github
  - lfs
  - deploy-key
  - information-disclosure
  - access-control
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-lfs-enumerate]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:39.512Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate Private Repos via LFS API

## Summary

This procedure exploits an improper access control vulnerability in GitHub Enterprise Server's internal Large File Storage (LFS) API to enumerate the names and owners (NWOs) of private repositories associated with deploy keys. Discovered by researcher ahacker1 and reported on April 18, 2024, it allows unauthorized disclosure of repository metadata without accessing contents, affecting versions prior to 3.14 with medium severity.

## Description

In GitHub Enterprise Server, deploy keys are SSH keys for repository-specific access, often used for automated deployments. The internal LFS API, intended for handling large files, lacks adequate restrictions, enabling attackers to query and list private repositories linked to these keys. This leads to reconnaissance of an organization's private project structure. The attack requires network access to the server but no elevated privileges, making it suitable for internal or pivoted attackers. Expected outcomes include a list of private repo NWOs, aiding further targeting like phishing or social engineering based on project names.

## Requirements

1. Network access to GitHub Enterprise Server instance (e.g., via VPN or direct connectivity)
2. Knowledge of the internal API base URL (typically https://<enterprise-host>/api/v3/)
3. curl or similar HTTP client for API requests
4. Target running vulnerable version (pre-3.14, unpatched)

## Defense

Defensive measures and detection strategies:

- Patch to GitHub Enterprise Server 3.14 or later to enforce proper API restrictions
- Monitor LFS API logs for anomalous GET requests to deploy key endpoints
- Implement API rate limiting and require authentication for all internal endpoints
- Use network segmentation to restrict access to LFS API from unauthorized sources

## Objectives

1. Discover private repository names and owners linked to deploy keys
2. Map organizational project structure for reconnaissance
3. Achieve information disclosure without triggering content access alerts

## Instructions

### Step 1: Identify LFS API Endpoint

**Context**: Locate the vulnerable internal LFS API endpoint for deploy keys, which exposes repository associations due to missing access controls.

**Command** ([[commands/curl-lfs-enumerate]]):
```bash
curl -X GET 'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H 'Accept: application/vnd.github.v3+json' -v
```

> This command sends a GET request to the deploy keys LFS repos endpoint. The -v flag provides verbose output for debugging. In vulnerable setups, it returns JSON without auth errors, listing NWOs. Replace github-enterprise.example.com with the target host.

### Step 2: Parse and Validate Response

**Context**: Extract and verify the enumerated private repository details from the API response to confirm disclosure.

**Command** ([[commands/curl-lfs-enumerate]] with jq for parsing):
```bash
curl -s -X GET 'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H 'Accept: application/vnd.github.v3+json' | jq '.repos[] | {name: .name, owner: .owner.login}'
```

> Pipe the response to jq (install via package manager if needed) to filter repository names and owners. Successful output shows private repo metadata, e.g., {"name": "secret-project", "owner": "org-name"}. If empty or errored, the endpoint may be patched.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-lfs-enumerate]]

## Tools Used


## Tags

- [[github]]
- [[lfs]]
- [[deploy-key]]
- [[information-disclosure]]
- [[access-control]]
