---
id: 45520002-40af-40f3-b85c-41abc9553f03
name: Update-Metasploit-Framework
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.183193+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics: []
techniques: []
sub_techniques: []
tags:
  - installation
  - metasploit
commands:
  - '[[commands/update-metasploit-omnibus-script]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Update-Metasploit-Framework

## Summary

This procedure updates the Metasploit Framework to the latest version using the official Omnibus installer script. It ensures access to the newest exploits, payloads, and modules for penetration testing, maintaining the tool's effectiveness against evolving vulnerabilities.

## Description

The Metasploit Framework is a widely used open-source platform for developing and executing exploit code against remote targets. Updating it regularly is essential to incorporate the latest security research, bug fixes, and new capabilities. This procedure uses Rapid7's Omnibus package, which handles dependencies and provides a streamlined update process on Unix-like systems. It is typically run after initial installation or periodically to keep the framework current. The process downloads an installer script from the official GitHub repository, makes it executable, and runs it to perform the update. This approach avoids manual compilation and ensures compatibility with the msfconsole interface.

## Requirements

1. Internet access to download the update script from GitHub.
2. Sufficient disk space (at least 2GB free) for downloading and installing updates.
3. Administrative or sudo privileges on the target system to execute the installer.
4. A Unix-like operating system (e.g., Kali Linux, Ubuntu) where Metasploit is already installed.

## Defense

Defensive measures and detection strategies:

- Verify the script source by checking the GitHub repository integrity before execution to prevent supply chain attacks.
- Run updates in an isolated environment or VM to avoid unintended system changes.
- Monitor for unexpected network traffic or file modifications during updates using tools like auditd or file integrity monitoring.

## Objectives

1. Download and execute the official update script for Metasploit Framework.
2. Verify the successful application of updates to access new modules.
3. Ensure the framework remains operational without disrupting existing configurations.

## Instructions

### Step 1: Download the Omnibus Update Script

**Context**: Retrieve the official msfupdate script from the Rapid7 GitHub repository. This script handles the update logic, including dependency resolution and framework refresh.

**Command** ([[commands/update-metasploit-omnibus-script]]):
```bash
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall
```

> This chained command uses curl to fetch the script and saves it as 'msfinstall', then sets executable permissions with chmod. Expected output includes download progress and confirmation of file creation with permissions set (e.g., -rwxr-xr-x).

### Step 2: Execute the Update Script

**Context**: Run the downloaded script to perform the actual update. This step pulls the latest Metasploit packages and integrates them into the system path.

**Command** ([[commands/update-metasploit-omnibus-script]]):
```bash
./msfinstall
```

> Execute the script directly. It will display progress messages, such as downloading packages, installing dependencies, and updating the database. The process may take several minutes depending on the update size. Expected output ends with a success message like "Metasploit Framework successfully updated."

### Step 3: Verify the Update

**Context**: Confirm the update by launching msfconsole and checking the version. This ensures all new modules are loaded and the framework is functional.

**Command**:
```bash
msfconsole -v
```

> Run msfconsole with the version flag to display the current build. Expected output shows the updated version number (e.g., "Framework Version: 6.3.0-dev"). If issues arise, check logs in ~/.msf6/logs for errors.
