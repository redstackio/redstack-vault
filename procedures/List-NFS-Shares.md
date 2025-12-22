---
id: 7e5b207c-edb4-458d-9075-506fa6498143
name: List-NFS-Shares
type: procedure
verified: true
submitted: false
created_at: '2019-09-11T21:53:20.976114+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Share Discovery]]'
sub_techniques: []
tags:
  - Network
commands:
  - '[[commands/showmount-list-mounted-nfs-directories]]'
  - '[[commands/showmount-list-nfs-exports]]'
platforms:
  - Linux
tools: []
validated: true
---

# List-NFS-Shares

## Summary

This procedure uses the showmount utility to enumerate NFS (Network File System) shares on a target Linux system, revealing exported directories and mounted paths that could expose sensitive files or directories over the network. It is useful during reconnaissance to identify potential file share access points for further exploitation or data discovery.

## Description

NFS is a protocol that allows file systems to be shared across a network, similar to SMB on Windows. When NFS is enabled on a target, attackers can query it remotely to list available exports (shared directories) and mounted directories without authentication in many configurations. This technique aids in discovering network-accessible resources, potentially leading to unauthorized file access if permissions are misconfigured. The procedure assumes the target has NFS services running (typically on ports 2049/TCP and UDP) and that the attacker has network connectivity to the target. It maps to the MITRE ATT&CK framework under Discovery, specifically Network Share Discovery, as it reveals shared resources that could be leveraged for lateral movement or data collection.

## Requirements

1. Network access to the target system (firewall must allow UDP/TCP to NFS ports, typically 111 for RPC and 2049 for NFS).
2. showmount tool installed on the attacker's Linux machine (standard on most distributions like Kali Linux).
3. Target IP address or hostname resolved.
4. No authentication required for basic enumeration, but root privileges may be needed for advanced mounts.

## Defense

Defensive measures include disabling unnecessary NFS exports, restricting NFS to trusted networks via firewall rules (e.g., iptables to block port 2049 from external IPs), and configuring NFS with authentication (e.g., using Kerberos). Monitor for anomalous showmount queries via network logs or tools like Snort/Zeek. Enable RPC logging and audit NFS access attempts.

- Restrict NFS exports in /etc/exports to specific hosts/subnets.
- Use tools like rpcinfo to verify exposed services and auditd for file access monitoring.

## Objectives

1. Identify NFS-exported directories on the target to map potential data access points.
2. Discover mounted NFS paths that indicate active shares and their scope.
3. Gather intelligence on the target's file system structure for targeted follow-on actions like mounting shares.

## Instructions

### Step 1: List Mounted NFS Directories

**Context**: This step queries the target for currently mounted NFS directories, providing insight into active mounts and their paths. It helps identify if the target is actively using NFS and what root-level directories are exposed.

**Command** ([[commands/showmount-list-mounted-nfs-directories]]):
```bash
showmount -d $_TARGET_IP
```

> The -d flag lists only the directories that are currently mounted by clients. Replace $_TARGET_IP with the target's IP address. This command contacts the target's mountd service via RPC to retrieve mount information. If successful, it reveals paths like '/' or specific subdirectories, indicating broad exposure.

### Step 2: List NFS Exports

**Context**: This step enumerates all NFS exports configured on the target, showing which directories are shared and to whom (e.g., world-readable with '*'). It reveals the full scope of available shares for potential mounting and access.

**Command** ([[commands/showmount-list-nfs-exports]]):
```bash
showmount -e $_TARGET_IP
```

> The -e flag retrieves the export list from the target's mountd daemon. This provides a comprehensive view of shared resources, such as '/' exported to all ('*'), which could allow anonymous read/write access depending on permissions. Use this to prioritize shares for further enumeration or exploitation.
