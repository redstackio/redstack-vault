---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - rce
  - privilege-escalation
  - github-enterprise
  - ssh
  - git-hook
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-Pre-Receive-Hook-RCE-for-Root-Escalation]]'
step_count: 2
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:46.818Z'
description: >-
  An attacker with GitHub Enterprise Server Administrator privileges exploits an
  RCE vulnerability in the pre-receive hook environment to escalate to
  root-level SSH access, achieving full control over the instance.
skill_level: advanced
impact_level: critical
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Privilege Escalation to Root SSH Access via Pre-Receive Hook RCE in GitHub Enterprise Server
type: attack_chain
description: "An attacker with GitHub Enterprise Server Administrator privileges exploits an RCE vulnerability in the pre-receive hook environment to escalate to root-level SSH access, achieving full control over the instance."
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T12:00:00Z
updated_at: 2023-10-01T12:00:00Z
procedures: [[procedures/Exploit-Pre-Receive-Hook-RCE-for-Root-Escalation]]
techniques: [[Unix Shell]], [[Exploitation for Privilege Escalation]]
tactics: [[Execution]], [[Privilege Escalation]]
tags: rce, privilege-escalation, github-enterprise, ssh, git-hook
platforms: Linux
tools: []
complexity: medium
skill_level: advanced
impact_level: critical
---

# Privilege Escalation to Root SSH Access via Pre-Receive Hook RCE in GitHub Enterprise Server

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in GitHub Enterprise Server's pre-receive hook environment.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Administrator Access] --> B[RCE in Pre-Receive Hook]
    B --> C[Privilege Escalation to Root SSH]
    C --> D[Full Server Control]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Git client for repository interactions
- SSH client for post-exploitation access

### Target Environment

- GitHub Enterprise Server version 3.8.0 or higher
- Linux-based host (e.g., Ubuntu or RHEL)
- Services: Git (port 9418 or HTTP/HTTPS), SSH (port 22)

### Initial Access Requirements

- Administrator role in GitHub Enterprise Server
- Network access to the GitHub instance (e.g., via VPN or direct)
- No prior root access required, but admin privileges enable hook manipulation

## Detailed Attack Procedures

### Step 1: Trigger RCE in Pre-Receive Hook Environment
procedure: [[procedures/Exploit-Pre-Receive-Hook-RCE-for-Root-Escalation]]

**Objective**: Exploit the unspecified weakness in the pre-receive hook to execute arbitrary code in the hook's restricted environment, bypassing isolation.

**Instructions**: As an administrator, create or modify a repository to push commits that invoke the pre-receive hook. Craft a malicious payload (e.g., via specially formatted commit messages or hook scripts) that leverages the vulnerability to execute shell commands. Use Git to push the payload:

```bash
git push origin main
```

Monitor the hook execution logs for signs of code injection success, such as unexpected process spawns.

**Expected Output**: Successful push with evidence of code execution, like a reverse shell callback or file creation in the hook environment.

**Success Indicators**:
- Hook triggers without rejection
- Arbitrary code executes (e.g., confirmed via network callback or log artifacts)
- Access to restricted shell in the hook context

### Step 2: Escalate to Root SSH Access
procedure: [[procedures/Exploit-Pre-Receive-Hook-RCE-for-Root-Escalation]]

**Objective**: From the RCE foothold, exploit insufficient isolation to escalate privileges to root and establish persistent SSH access.

**Instructions**: Once RCE is achieved, chain commands to exploit validation flaws, such as overwriting sudoers or kernel parameters. For example, from the injected shell:

```bash
# Example escalation payload (inferred from vuln context)
echo 'ALL ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/escalate
sudo -i
```

Generate and install an SSH key for root access:

```bash
mkdir -p /root/.ssh
echo 'ssh-rsa AAAAB3NzaC1yc2E... attacker_key' >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
```

Exit the hook environment and connect via SSH as root.

**Expected Output**: Root shell prompt via SSH, confirming full control.

**Success Indicators**:
- SSH login succeeds without password
- Root-level commands execute (e.g., `whoami` returns 'root')
- Persistence via backdoor key

## Attack Chain Summary

### Key Achievements

1. Achieved RCE in a supposedly isolated pre-receive hook environment from admin privileges.
2. Escalated to root access, bypassing GitHub Enterprise's security boundaries.
3. Gained persistent SSH control, enabling data exfiltration, further pivoting, or sabotage.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T12:00:00Z*
