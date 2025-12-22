---
id: f5151f6d-996f-4462-9f78-06b2e4e11015
type: tool
verified: true
created_at: '2019-08-28T21:17:25.517965+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - windows-sam
  - offline-editing
  - registry
url: 'https://www.chntpw.com/'
validated: true
---

# chntpw

**Status**: Unverified

## Overview

chntpw is a suite of tools for viewing, extracting, and modifying user account information in Windows NT/2000/XP/Vista/7/10 SAM files and registry hives. It enables offline password changes, account unlocking, and basic registry editing without requiring the original passwords. Commonly used in penetration testing for post-exploitation credential access and persistence on Windows systems.

## Description

The primary component, chntpw, reads and edits the SAM database to reset user passwords by overwriting hashes. It includes a simple registry editor for hive files (like SYSTEM or SOFTWARE) and a hex-editor for low-level modifications. This tool is particularly useful when physical or mounted access to a Windows drive is available, such as from a Linux live USB. It supports same-size writes to avoid corrupting files and is lightweight for inclusion in bootable recovery disks.

## Features

- Feature 1: List users and account details from SAM files without modification.
- Feature 2: Change, blank, or unlock user passwords interactively.
- Feature 3: Promote users to administrators or disable accounts.
- Feature 4: Edit registry hives with a built-in viewer and hex-editor.
- Feature 5: Support for NTLM hash extraction and basic auditing.

## Installation

### Requirements

- Linux environment (Kali Linux recommended).
- Access to mounted Windows filesystems (e.g., via ntfs-3g).
- No additional dependencies beyond standard libc.

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update
sudo apt install chntpw

# On Ubuntu
sudo apt update
sudo apt install chntpw

# From source (if needed)
# Download from https://www.chntpw.com/ and compile
make
sudo make install
```

## Basic Usage

```bash
chntpw --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v | Verbose output for debugging |
| -l | List users only (SAM files) |
| -u <user> | Edit specific user |
| -e | Edit registry hive |
| -N | Set empty password (no prompt) |
| -d | Disable user account |
| -E | Enable user account |
| -I | Unlock account |

## Examples

### Example 1: Basic Usage

List users in a mounted SAM file:

```bash
chntpw -l /mnt/windows/Windows/System32/config/SAM
```

### Example 2: Advanced Usage

Change password for a user interactively:

```bash
chntpw -u Administrator /mnt/windows/Windows/System32/config/SAM
```

(Select option [2] in the menu to set a new password.)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Security Account Manager]] SAM Dumping (for listing and editing credentials)
- [[Account Manipulation]] Account Manipulation (password resets and unlocks)
- [[Modify Registry]] Modify Registry (hive editing)

### Tactics

- [[Credential Access]] Credential Access
- [[Privilege Escalation]] Privilege Escalation
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: File system access logs showing reads/writes to SAM or registry hives (e.g., /Windows/System32/config/).
- Detection method 2: Unusual bootable media or live USB usage on Windows systems.
- Detection method 3: Modified password hashes or account states post-incident (compare with backups).
- Detection method 4: Process monitoring for chntpw execution in Linux environments accessing NTFS partitions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/samdump2]] (for dumping NTLM hashes)
- [[reged]] (advanced Windows registry editor)
- [[ntfs-3g]] (for mounting Windows filesystems on Linux)

## References

- Official website: https://www.chntpw.com/
- Kali Linux package: https://pkg.kali.org/package/chntpw
- Man page: man chntpw
