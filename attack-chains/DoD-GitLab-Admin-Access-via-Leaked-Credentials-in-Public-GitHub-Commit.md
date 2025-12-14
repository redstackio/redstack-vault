---
id: ac-uuid-placeholder
name: DoD GitLab Admin Access via Leaked Credentials in Public GitHub Commit
tags:
  - credential-leak
  - information-disclosure
  - github
  - gitlab
  - dod
type: attack_chain
tools:
  - '[[tools/GitHub]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Hosting-IP-and-Confirm-GitLab-Instance]]'
  - '[[procedures/Verify-No-Public-Content-on-GitLab]]'
  - '[[procedures/Search-GitHub-for-Leaked-Credentials]]'
  - '[[procedures/Access-GitLab-Using-Leaked-Credentials]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:44.346Z'
description: >-
  An attack chain exploiting accidentally exposed admin credentials for a
  private DoD GitLab Enterprise Edition instance, discovered through public
  GitHub searches, leading to full administrative access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Gather Victim Host Information]]'
---
# DoD GitLab Admin Access via Leaked Credentials in Public GitHub Commit

Multi-stage attack chain demonstrating how exposed admin credentials in a public GitHub commit enable unauthorized access to a private DoD GitLab Enterprise Edition instance, potentially exposing sensitive source code, secrets, and enabling further compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify IP and GitLab] --> B[Discovery: Verify Exposure]
    B --> C[Credential Access: Search GitHub for Leaks]
    C --> D[Initial Access: Login with Leaked Creds]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GitHub]]

### Target Environment

- Web platform with GitLab EE on ports 80/443
- Public GitHub repositories
- Network access to target IP and GitHub

### Initial Access Requirements

- No prior credentials needed
- Internet access for GitHub searches
- Knowledge of target hostname from TLS cert

## Detailed Attack Procedures

### Step 1: Identify Hosting IP and Confirm GitLab Instance
procedure: [[procedures/Identify-Hosting-IP-and-Confirm-GitLab-Instance]]

**Objective**: Locate the IP address hosting the target subdomain and confirm it redirects to a private GitLab EE instance.

**Instructions**: Use a web browser or curl to query the IP on port 80, observing the TLS certificate for the hostname and the 301 redirect to HTTPS on port 443 pointing to GitLab EE.

**Expected Output**: HTTP response showing redirect to GitLab login or dashboard, with TLS cert revealing internal hostname.

**Success Indicators**:
- IP resolved and port 80/443 active
- Redirect confirms GitLab EE presence

### Step 2: Verify No Public Content on GitLab
procedure: [[procedures/Verify-No-Public-Content-on-GitLab]]

**Objective**: Check the GitLab explore page to ensure no public projects, groups, or snippets are exposed, confirming the instance is intended to be private.

**Instructions**: Navigate to https://[target-hostname]/explore in a web browser and inspect for any visible content.

**Expected Output**: Empty explore page with no projects, groups, or snippets listed.

**Success Indicators**:
- No public repositories visible
- Instance appears private but accessible via potential creds

### Step 3: Search GitHub for Leaked Credentials
procedure: [[procedures/Search-GitHub-for-Leaked-Credentials]]

**Objective**: Use the hostname from the TLS certificate to search public GitHub repositories for exposed credentials applicable to the GitLab root admin account.

**Instructions**: In GitHub's search bar, query the exact hostname string to find commits containing credentials, such as those for JENKINS_OC_USER and JENKINS_OC_PASSWD, which reuse the default 'root' username for GitLab.

**Expected Output**: Repository commit revealing username 'root' and password in code snippet.

**Success Indicators**:
- Leaked credentials found in public commit
- Credentials match default GitLab admin format

### Step 4: Access GitLab Using Leaked Credentials
procedure: [[procedures/Access-GitLab-Using-Leaked-Credentials]]

**Objective**: Authenticate to the GitLab instance using the leaked default root credentials to gain full administrative access.

**Instructions**: Navigate to the GitLab login page at https://[target-hostname]/users/sign_in, enter username 'root' and the leaked password, and submit.

**Expected Output**: Successful login to admin dashboard with full privileges.

**Success Indicators**:
- Admin access granted
- Ability to view users, projects, and settings

## Attack Chain Summary

### Key Achievements

1. Discovered private GitLab instance via IP and TLS analysis
2. Identified leaked admin credentials through GitHub search
3. Gained unauthorized full admin access without further exploitation
4. Highlighted risks of credential reuse across services like Jenkins and GitLab

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Gather Victim Host Information]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
