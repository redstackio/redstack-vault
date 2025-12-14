---
tags:
  - github
  - privilege-escalation
  - access-control
  - token
  - github-apps
  - cve-2022-23741
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:46.959Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fa39eb91-0b51-4f8a-b90f-31c544720da2
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Install-Malicious-GitHub-App-for-Token-Escalation

## Summary

This procedure exploits an improper authorization vulnerability (CVE-2022-23741) in GitHub Enterprise Server's handling of user-to-server tokens within GitHub Apps, allowing escalation from scoped permissions to full organization admin/owner privileges. It requires an admin account capable of installing apps and targets versions before the patches in 3.3.17, 3.4.12, 3.5.9, and 3.6.5.

## Description

The vulnerability stems from flawed access controls during token issuance and validation in GitHub Apps. An attacker with admin rights to install apps can create a malicious app requesting limited scopes (e.g., metadata read access). Upon installation and authorization, the server incorrectly elevates the token, granting unrestricted organization control. This enables actions like user management, repository deletion, or billing changes. The attack assumes the target runs a vulnerable GitHub Enterprise Server instance and focuses on internal organizational compromise rather than external access.

## Requirements

1. Admin access to the target GitHub organization for app installation
2. Ability to create and register a GitHub App via GitHub developer settings
3. Network connectivity to the GitHub Enterprise Server UI/API
4. Target on vulnerable version (pre-3.3.17, 3.4.12, 3.5.9, 3.6.5)

## Defense

Defensive measures and detection strategies:

- Upgrade to patched versions (3.3.17, 3.4.12, 3.5.9, 3.6.5) immediately
- Implement strict app installation reviews and limit admin permissions for app installs
- Monitor GitHub audit logs for unusual token issuances or app installations
- Use GitHub's App Review process and enable organization-level app restrictions

## Objectives

1. Install a malicious GitHub App with minimal requested scopes
2. Exploit token handling flaw to escalate to full admin privileges
3. Validate and utilize elevated access for organizational control

## Instructions

### Step 1: Create and Register Malicious GitHub App

**Context**: Register a new GitHub App with scoped permissions to minimize suspicion during authorization.

Navigate to the GitHub developer settings (https://github.com/settings/apps) and create a new app. Set the app name, homepage URL, and webhook URL as needed. Under permissions, request minimal scopes such as 'Metadata (read)' for organization access. Generate a private key for the app and note the App ID.

No specific command required; use the web UI.

> Expected output: App registration confirmation with Client ID and private key download.

### Step 2: Install App on Target Organization

**Context**: Use an admin account to install the app, triggering the vulnerable token handling during authorization.

Log in to the target GitHub Enterprise Server with an admin account. Go to organization settings > GitHub Apps > Install App. Search for and select the registered app. Review and authorize the installation, accepting the requested scopes. The vulnerability occurs here: the server issues a user-to-server token that exceeds the scoped permissions due to improper validation.

No specific command required; use the web UI or API endpoint for installation (e.g., POST /app/installations/{installation_id}/access_tokens).

> Expected output: Installation success message. Test the token by making an API call to organization endpoints, such as GET /orgs/{org}/members, which should now return full access even if scoped to read-only.

### Step 3: Validate and Exploit Escalated Privileges

**Context**: Confirm the escalation by performing admin-only actions with the token.

Use the obtained installation access token to query organization resources via the GitHub API. For example, attempt to list all teams or update organization settings. If successful beyond the requested scope, the escalation is confirmed.

Example API call (using curl for validation, though not extracted):

```bash
curl -H "Authorization: Bearer $INSTALLATION_ACCESS_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://$GITHUB_ENTERPRISE_HOST/api/v3/orgs/$ORG/settings
```

> Expected output: JSON response with full organization settings editable, indicating owner-level access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- github
- privilege-escalation
- access-control
- token
- github-apps
- cve-2022-23741
