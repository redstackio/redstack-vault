---
id: proc-001
tags:
  - installation
  - vulnerable-package
  - nordvpn
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/wget-download-nordvpn-release]]'
  - '[[commands/dpkg-install-release]]'
  - '[[commands/apt-get-update]]'
  - '[[commands/apt-get-install-nordvpn]]'
  - '[[commands/dpkg-list-package-contents]]'
  - '[[commands/sha256sum-verify-package]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
updated_at: '2025-12-14T17:30:07.242Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
---
# Install-NordVPN-Client-with-Vulnerable-Permissions

## Summary

This procedure installs the NordVPN Linux client package, which deploys service files like /usr/lib/systemd/system/nordvpnd.service with unsafe world-writable permissions (777), enabling subsequent local privilege escalation by unprivileged users.

## Description

The NordVPN client is installed via the Debian package manager on Linux systems using systemd. The package includes init scripts and unit files that are packaged with excessive permissions, allowing any local user to modify them post-installation. This sets up the environment for exploitation where an unprivileged user can alter the service configuration to run arbitrary root commands. Prerequisites include root access for installation and a Debian-based system.

## Requirements

1. Root or sudo access on a Debian-based Linux system (e.g., Ubuntu)
2. Internet connectivity for downloading packages
3. apt and dpkg package managers available

## Defense

Defensive measures and detection strategies:

- Verify package file permissions before installation using dpkg-deb --info
- Set strict umask and use immutable attributes on /usr/lib/systemd/system/ post-install
- Monitor file modifications in critical directories with auditd or inotify
- Regularly scan for world-writable files in service directories using find /usr/lib/systemd -perm -777

## Objectives

1. Deploy NordVPN client with vulnerable service files
2. Confirm unsafe permissions on key files
3. Prepare system for privilege escalation exploitation

## Instructions

### Step 1: Verify Package Integrity

**Context**: Download and check the SHA256 hash of the NordVPN release package to ensure it's unmodified before installation.

**Command** ([[commands/sha256sum-verify-package]]):
```bash
sha256sum nordvpn-release_1.0.0_all.deb
```

> Computes the checksum; expected output matches 204d0089e326542c629c5f50a235de82bf3fa9fa829065be0490a0902e6770b63 for the official package.

### Step 2: Download Repository Release

**Context**: Fetch the deb file to add the NordVPN repository to apt sources.

**Command** ([[commands/wget-download-nordvpn-release]]):
```bash
wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
```

> Downloads the file; success indicated by file presence in current directory.

### Step 3: Install Repository Release

**Context**: Install the release package to configure the apt repository.

**Command** ([[commands/dpkg-install-release]]):
```bash
sudo dpkg -i nordvpn-release_1.0.0_all.deb
```

> Adds the repo; no errors on successful install.

### Step 4: Update Package List

**Context**: Refresh apt cache to include the new NordVPN repository.

**Command** ([[commands/apt-get-update]]):
```bash
sudo apt-get update
```

> Updates lists; look for NordVPN entries in output.

### Step 5: Install NordVPN Client

**Context**: Install the main client package, deploying vulnerable files.

**Command** ([[commands/apt-get-install-nordvpn]]):
```bash
sudo apt-get install nordvpn
```

> Installs package; vulnerable files placed.

### Step 6: Inspect Package Contents

**Context**: Verify unsafe permissions in the installed package.

**Command** ([[commands/dpkg-list-package-contents]]):
```bash
dpkg -c /var/cache/apt/archives/nordvpn_3.10.0-1_amd64.deb
```

> Lists files; expect -rwxrwxrwx for /usr/lib/systemd/system/nordvpnd.service.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Sub-Techniques

-

## Commands Used

- [[commands/sha256sum-verify-package]]
- [[commands/wget-download-nordvpn-release]]
- [[commands/dpkg-install-release]]
- [[commands/apt-get-update]]
- [[commands/apt-get-install-nordvpn]]
- [[commands/dpkg-list-package-contents]]

## Tools Used

-

## Tags

- [[installation]]
- [[vulnerable-package]]
- [[nordvpn]]
