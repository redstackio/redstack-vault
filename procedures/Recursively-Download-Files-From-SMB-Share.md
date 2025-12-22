---
id: e3055560-9e5b-4666-bff4-ff647d10b1cd
name: Recursively-Download-Files-From-SMB-Share
type: procedure
verified: true
submitted: true
created_at: '2019-09-19T22:36:11.177562+00:00'
updated_at: '2023-05-25T19:46:23.343180+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Network Shared Drive]]'
sub_techniques: []
tags:
  - data-exposure
  - network
commands:
  - '[[commands/smbclient-connect-to-smb-share-with-ntlm]]'
  - '[[commands/smbclient-download-files-recursively]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/smbclient]]'
validated: true
---

# Recursively-Download-Files-From-SMB-Share

## Summary

This procedure demonstrates how to authenticate to a Windows SMB share using NTLM authentication and recursively download all accessible files from the share. It is useful in post-exploitation scenarios where an attacker has obtained valid credentials or hashes and needs to collect data from network-shared drives without alerting the target system.

## Description

Server Message Block (SMB) is a protocol commonly used for file sharing on Windows networks. Once an attacker has valid credentials (username and NTLM hash or password), they can mount and access SMB shares to exfiltrate sensitive data. This procedure uses the smbclient tool to connect to the share, enable recursive traversal, disable interactive prompts, and download all files. It targets scenarios where the attacker is operating from a Linux-based system like Kali Linux and has network access to the target Windows host. The technique aligns with collecting data from network shared drives, potentially exposing documents, configurations, or other valuable information.

## Requirements

1. Valid SMB credentials: Username and NTLM hash (or password) for a user with read access to the target share.
2. Network connectivity: Attacker machine must reach the target IP on SMB ports (typically 445/TCP).
3. Tools: smbclient installed on the attacker machine.
4. Target environment: Windows host with SMB shares enabled and accessible.

## Defense

Defensive measures and detection strategies:

- Monitor SMB traffic for unusual connections from external or unauthorized IPs using network intrusion detection systems (NIDS) like Snort or Suricata.
- Enable SMB signing and auditing on Windows shares to log access attempts and require authentication integrity.
- Implement least privilege access: Restrict share permissions to only necessary users and monitor for anomalous file access patterns via Windows Event Logs (Event ID 5145 for share access).
- Use endpoint detection and response (EDR) tools to alert on large-scale file downloads or connections to sensitive shares.

## Objectives

1. Authenticate to the SMB share using NTLM credentials to gain read access.
2. Traverse the share directory structure recursively to identify all files.
3. Download all accessible files to the local attacker machine for offline analysis or exfiltration.
4. Verify successful download without errors like sharing violations on locked files.

## Instructions

### Step 1: Connect to the SMB Share

**Context**: Establish an authenticated connection to the target SMB share using the provided username and NTLM hash. This step opens an interactive smbclient session, allowing subsequent commands to be executed within the share. If using a password instead of a hash, omit the --pw-nt-hash flag and provide the password in the -U parameter.

**Command** ([[commands/smbclient-connect-to-smb-share-with-ntlm]]):

```bash
smbclient -U $_USERNAME%$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```

> This command initiates the SMB connection. Upon success, you will enter an interactive smb: prompt where directory listings and file operations can be performed. Verify access by running 'ls' to list share contents.

### Step 2: Enable Recursion and Download Files

**Context**: Within the smbclient session, configure recursive downloading by enabling recursion and disabling prompts for each file. Then, use the mget command to retrieve all files (*) from the current directory and subdirectories. This step handles bulk data collection efficiently but may skip locked files (e.g., NTUSER.DAT) due to sharing violations.

**Command** ([[commands/smbclient-download-files-recursively]]):

```bash
smb: \$_SHARE_NAME\> RECURSE ON
smb: \$_SHARE_NAME\> PROMPT OFF
smb: \$_SHARE_NAME\> mget *
```

> Execute these commands sequentially in the smbclient prompt. RECURSE ON allows traversal into subfolders, PROMPT OFF bypasses confirmation for each file, and mget * downloads everything. Files will be saved to the current local directory. Monitor for errors like NT_STATUS_SHARING_VIOLATION on system files and timeouts on large transfers.
