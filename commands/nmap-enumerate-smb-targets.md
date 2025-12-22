---
id: b9c5adf0-b3fb-4212-a41b-db382a225d06
name: nmap-enumerate-smb-targets
type: command
executor: bash
data: >-
  nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args
  smbuser='Guest',smbpass='' -oN smb-targets.txt $_TARGET_NETWORK
output: null
created_at: '2023-04-06T03:56:05.363468+00:00'
updated_at: '2023-04-10T20:26:21.879066+00:00'
platforms:
  - Linux
  - Windows
tags:
  - recon
  - smb
verified: true
validated: true
---

# nmap-enumerate-smb-targets

## Command

```bash
nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args smbuser='Guest',smbpass='' -oN smb-targets.txt $_TARGET_NETWORK
```

## Description

This Nmap command scans for open SMB ports (139/445) and enumerates shares and users anonymously using Guest/null credentials. Ideal for identifying targets vulnerable to SMB relay attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p 139,445 | Ports to scan (NetBIOS and SMB) | Yes |
| --script smb-enum-shares.nse,smb-enum-users.nse | NSE scripts for enumeration | Yes |
| --script-args smbuser='Guest',smbpass='' | Anonymous auth args | Yes |
| -oN smb-targets.txt | Output file | Yes |
| $_TARGET_NETWORK | Network range (e.g., 192.168.0.0/24) | Yes |

## Examples

### Basic Usage

```bash
nmap -p 445 --script smb-enum-shares.nse --script-args smbuser='Guest',smbpass='' 192.168.1.100
```

### Full Network Scan

```bash
nmap -p 139,445 --script smb-enum-shares.nse,smb-enum-users.nse --script-args smbuser='Guest',smbpass='' -oN targets.txt 10.0.0.0/24
```

## Expected Output

Nmap scan report for 192.168.1.10
PORT    STATE SERVICE
445/tcp open  microsoft-ds
| smb-enum-shares: 
  account_used: Guest
  \IPC$ (IPC Service (Responder))
  \ADMIN$ (ADMIN$)
| smb-enum-users: 
  Guest (RID: 501)
  Administrator (RID: 500)

Hosts with open SMB ports and accessible shares indicate potential relay targets.

## Related

- [[procedures/SMB-Relay-Attack-via-Disabled-SMB-Signing]]
