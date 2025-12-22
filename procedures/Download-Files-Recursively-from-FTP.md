---
type: procedure
tactics:
  - '[[Exfiltration]]'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
sub_techniques: []
tags:
  - data-exposure
  - file-transfer
  - network
commands:
  - '[[commands/wget-ftp-connectivity-test]]'
  - '[[commands/wget-recursive-ftp-download]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Wget]]'
skill_level: beginner
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Download-Files-Recursively-from-FTP

## Summary

This procedure enables the recursive download of files and folders from an FTP server using the wget utility, effectively mirroring the remote directory structure locally. It is particularly useful in post-exploitation scenarios where an attacker has identified an open FTP server containing sensitive data for exfiltration, but it generates substantial network traffic, making it unsuitable for stealthy operations.

## Description

In offensive security engagements, discovering an FTP server with anonymous access often reveals valuable data such as configuration files, backups, or internal documents. This procedure uses wget's recursive mirroring capabilities to download the entire contents without manual intervention, preserving the original directory hierarchy. The approach assumes anonymous login (no credentials required), which is common for misconfigured servers. Key considerations include assessing the size of the target directory beforehand to avoid overwhelming bandwidth or alerting defenders via traffic volume. This maps to exfiltration tactics where data is pulled over alternative protocols like FTP instead of standard channels.

## Requirements

1. Network connectivity to the target FTP server on port 21 (TCP).
2. wget utility installed on the attacker's system (pre-installed on most Linux distributions; available via package managers on Windows).
3. Anonymous FTP access enabled on the target server (no username/password needed; tested via connectivity check).
4. Sufficient local disk space to accommodate the mirrored content.

## Defense

Defensive measures and detection strategies:

- Implement network monitoring tools like Zeek or Suricata to flag large outbound FTP sessions or unusual RETR/LIST command volumes from internal hosts.
- Enable detailed logging on FTP servers (e.g., vsftpd or ProFTPD) to track anonymous downloads and alert on recursive patterns.
- Use firewalls to restrict FTP access to trusted IPs and disable anonymous logins where possible.
- Deploy endpoint detection agents to identify wget processes initiating FTP connections.

## Objectives

1. Verify accessibility of the FTP server to ensure anonymous login succeeds without errors.
2. Recursively download all files and folders, mirroring the server's structure for complete data exfiltration.
3. Confirm the integrity and completeness of the downloaded content for analysis or further exploitation.

## Instructions

### Step 1: Test FTP Connectivity

**Context**: Before initiating a full download, confirm that the FTP server is reachable and allows anonymous access. This step prevents wasted resources on inaccessible targets and provides an initial assessment of the server's response.

**Command** ([[commands/wget-ftp-connectivity-test]]):
```bash
wget --spider ftp://$_TARGET_IP/
```

> This command performs a spider crawl, connecting to the server and listing the root directory without retrieving files. It helps identify if the server is up and accessible. If the connection fails, check firewalls or credentials; success indicates readiness for download.

### Step 2: Download Files Recursively

**Context**: With connectivity confirmed, execute the recursive download to mirror the FTP server's contents. The --no-passive mode ensures active FTP for environments blocking passive connections, while -m enables mirroring to timestamp files and recurse infinitely.

**Command** ([[commands/wget-recursive-ftp-download]]):
```bash
wget -r --no-passive --no-parent -m ftp://$_TARGET_IP
```

> Run this from a directory where you want the files saved (wget creates a subdirectory named after the server IP). Monitor progress via console output showing directories and files being retrieved. This step accomplishes bulk exfiltration but may take time for large repositories; interrupt with Ctrl+C if needed.

### Step 3: Verify Downloaded Content

**Context**: After the download completes, inspect the local copy to ensure all files transferred correctly and the structure is intact. This validates the exfiltration success and allows for quick scanning of retrieved data.

**Instructions**: Navigate to the created subdirectory (e.g., cd 192.168.1.100) and use standard shell commands to list contents recursively:

```bash
ls -R | wc -l
```

> This counts files and directories. Compare against any pre-download assessment (from Step 1 output) for completeness. Look for sensitive files like .txt, .conf, or databases. If files are missing, retry the download or investigate server permissions.
