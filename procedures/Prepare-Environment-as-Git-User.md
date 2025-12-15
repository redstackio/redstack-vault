---
id: proc-001
tags:
  - gitlab
  - setup
  - linux
type: procedure
tools:
  - '[[tools/sudo]]'
  - '[[tools/apt-get]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/apt-get-install-packages]]'
  - '[[commands/sudo-switch-to-git]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.005Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-Environment-as-Git-User

## Summary

This procedure sets up the attack environment by installing necessary packages and switching to the 'git' system user, which has write access to GitLab's log directories, enabling subsequent exploitation of the logrotate vulnerability.

## Description

In GitLab installations, the 'git' user owns log directories like /var/log/gitlab/, allowing local users to interact with them. This step simulates local access by installing tools like git and build-essential for compilation, then impersonating the 'git' user. It requires initial non-root access with sudo privileges to the 'git' user. The outcome is a shell as 'git', ready for exploit preparation in a Linux environment with GitLab Omnibus.

## Requirements

1. Non-root shell with sudo access to switch to 'git' user
2. Internet access for package installation
3. Linux system with apt package manager (Debian/Ubuntu-based GitLab)

## Defense

Defensive measures and detection strategies:

- Restrict sudo access to 'git' user (audit /etc/sudoers)
- Monitor package installations via auditd or falco for unusual apt-get usage
- Use AppArmor/SELinux to confine 'git' user actions

## Objectives

1. Install dependencies for exploit compilation and cloning
2. Gain shell as 'git' user for log directory manipulation
3. Prepare for race condition exploitation

## Instructions

### Step 1: Install Packages

**Context**: Ensure sudo, git, and build-essential are available for user switching, cloning, and compilation.

**Command** ([[commands/apt-get-install-packages]]):
```bash
apt-get install sudo git build-essential
```

> This command fetches and installs the packages. Expected output: 'Reading package lists... Done' followed by 'packages installed successfully'.

### Step 2: Switch to Git User

**Context**: Impersonate the 'git' user to access writable log directories.

**Command** ([[commands/sudo-switch-to-git]]):
```bash
sudo -u git /bin/bash
```

> Launches bash as 'git'. Expected output: Bash prompt changing to git@hostname:~$.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/apt-get-install-packages]]
- [[commands/sudo-switch-to-git]]

## Tools Used

- [[tools/sudo]]
- [[tools/apt-get]]

## Tags

- [[gitlab]]
- [[setup]]
- [[linux]]
