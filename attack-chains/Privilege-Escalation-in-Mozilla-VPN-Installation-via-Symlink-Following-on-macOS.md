---
tags:
  - privilege-escalation
  - symlink
  - macos
  - mozilla-vpn
  - local-attack
  - bypass
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - macOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Mozilla-VPN-Installer-for-Symlink-Flaws]]'
  - '[[procedures/Create-Symbolic-Links-to-Redirect-File-Operations]]'
  - '[[procedures/Achieve-Privilege-Escalation-via-Installer]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:26.873Z'
description: >-
  A multi-stage attack exploiting a logic flaw in the Mozilla VPN macOS
  installer, using symbolic links to bypass restrictions and achieve root
  privilege escalation from an unprivileged user.
skill_level: intermediate
impact_level: high
id: 5cbc2200-34f3-4667-a5f6-f3ffb05dc610
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Privilege Escalation in Mozilla VPN Installation via Symlink Following on macOS

Multi-stage attack chain demonstrating a complete privilege escalation workflow by exploiting improper symlink resolution in the Mozilla VPN installer on macOS. This bypasses a prior fix (report #2261577) and allows an unprivileged local attacker to gain root access during the installation process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze Installer] --> B[Create Symlinks]
    B --> C[Run Installation and Escalate]
    C --> D[Root Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Built-in macOS tools (e.g., ln for symlinks)

### Target Environment

- macOS (tested on recent versions)
- Mozilla VPN installer package (.pkg file) downloaded
- Local unprivileged user access

### Initial Access Requirements

- Local access to the target macOS system as an unprivileged user
- No network access required beyond downloading the installer
- No prior credentials needed beyond standard user login

## Detailed Attack Procedures

### Step 1: Analyze Mozilla VPN Installer for Symlink Flaws
procedure: [[procedures/Analyze-Mozilla-VPN-Installer-for-Symlink-Flaws]]

**Objective**: Identify the logic flaw in the installer's symlink handling to confirm exploitability as a bypass for the prior fix.

**Instructions**: Review the installation process by examining the Mozilla VPN .pkg file structure and testing file access patterns. Use built-in tools to inspect the package contents without executing it fully.

```bash
pkgutil --expand MozillaVPN.pkg /tmp/mozilla-vpn-expanded
ls -la /tmp/mozilla-vpn-expanded
```

Focus on scripts or components that perform file operations, looking for areas where symlinks could redirect root-privileged writes or reads.

**Expected Output**: Expanded package directory revealing installer scripts and potential symlink interaction points.

**Success Indicators**:
- Identification of file paths vulnerable to symlink manipulation
- Confirmation of bypass potential for report #2261577

### Step 2: Create Symbolic Links to Redirect File Operations
procedure: [[procedures/Create-Symbolic-Links-to-Redirect-File-Operations]]

**Objective**: Set up symbolic links in predictable locations that the installer will follow, redirecting operations to allow unprivileged manipulation of root-protected files.

**Instructions**: As an unprivileged user, create symlinks in a temporary directory that points to sensitive root-owned files or directories (e.g., /etc or /Library). Use the [[commands/ln-create-symlink]] command to establish the links before initiating installation.

```bash
mkdir -p /tmp/vpn-exploit
ln -s /etc/sudoers /tmp/vpn-exploit/target-file
ln -s /Library/Preferences /tmp/vpn-exploit/redirect-dir
```

Position these symlinks in paths the installer is known to access during its logic checks.

**Expected Output**: Symlinks created successfully, verifiable with `ls -l` showing the links point to root areas.

**Success Indicators**:
- Symlinks established without privilege errors
- Links resolve to root-protected resources

### Step 3: Achieve Privilege Escalation via Installer
procedure: [[procedures/Achieve-Privilege-Escalation-via-Installer]]

**Objective**: Trigger the installation process to follow the symlinks, exploiting the flaw to perform root-level actions and gain elevated privileges.

**Instructions**: Run the Mozilla VPN installer, which will resolve the symlinks improperly, allowing the unprivileged user to inject or modify root files. Monitor for escalation indicators post-installation.

```bash
sudo installer -pkg MozillaVPN.pkg -target / -dumplog /tmp/install.log
```

The sudo prompt may appear, but the symlink flaw bypasses proper checks, leading to root shell or persistent access.

**Expected Output**: Installation completes with unauthorized root file modifications; check logs for errors bypassed.

**Success Indicators**:
- Root privileges obtained (e.g., via modified sudoers allowing passwordless sudo)
- Persistence established through altered system files

## Attack Chain Summary

### Key Achievements

1. Bypassed prior symlink fix in Mozilla VPN installer
2. Redirected installer file operations using symlinks
3. Elevated from unprivileged user to root access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
