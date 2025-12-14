---
tags:
  - brave-browser
  - webtorrent
  - rce
  - file-download
  - header-manipulation
  - client-side
type: attack_chain
tools:
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
created_at: '2024-10-04T00:00:00Z'
procedures:
  - '[[procedures/Configure-Malicious-PHP-Server-for-Header-Manipulation]]'
  - '[[procedures/Initiate-Download-Prompt-in-Brave-Browser]]'
  - '[[procedures/Execute-Downloaded-Malicious-Batch-File]]'
step_count: 6
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Malicious File]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:46:32.007Z'
description: >-
  Exploits Brave browser's WebTorrent feature by manipulating
  Content-Disposition and Content-Type headers on a malicious PHP server to
  disguise a batch file as a torrent, tricking the user into downloading and
  executing it for remote code execution on Windows.
skill_level: intermediate
impact_level: high
id: d31fc388-f6f7-4411-84c1-657d2d2a314f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Malicious File]]'
  - '[[Windows Command Shell]]'
---
# Arbitrary File Download via WebTorrent Header Manipulation Leading to Client-Side RCE in Brave Browser

Multi-stage attack chain demonstrating exploitation of Brave browser's WebTorrent validation flaw, allowing attackers to serve malicious executable content disguised as a torrent file via header manipulation, resulting in user-executed remote code execution on Windows.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Malicious Server] --> B[Visit Malicious Page in Brave]
    B --> C[Trigger Download Prompt]
    C --> D[Save as Torrent File]
    D --> E[Execute Downloaded File]
    E --> F[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PHP]]

### Target Environment

- Brave browser on Windows
- Web access to malicious server
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Attacker controls a PHP-enabled web server
- Victim uses Brave browser with WebTorrent enabled (default)
- No credentials needed; relies on user interaction

## Detailed Attack Procedures

### Step 1: Set up a Malicious PHP Server
procedure: [[procedures/Configure-Malicious-PHP-Server-for-Header-Manipulation]]

**Objective**: Create a server that detects Brave's Referer header and serves torrent-like headers with malicious batch content.

**Instructions**: Deploy a PHP script on a web server that checks the HTTP_REFERER. If present (from Brave), set headers to mimic a torrent file and output batch payload.

Use the following PHP code in a file like test-driver.php:

```php
<?php
if (isset($_SERVER['HTTP_REFERER']) && strpos($_SERVER['HTTP_REFERER'], 'brave') !== false) {
    header('Content-Disposition: attachment; filename="PoC.torrent"');
    header('Content-Type: application/octet-stream');
} else {
    header('Content-Disposition: attachment; filename="malicious.bat"');
    header('Content-Type: application/x-msdownload');
}

// Malicious batch content
echo "@echo off\nSTART C:\\Windows\\NOTEPAD.EXE";
?>
```

Host this at a URL like https://your-server.com/test-driver.php.

**Expected Output**: Server responds with appropriate headers based on Referer.

**Success Indicators**:
- PHP script deploys without errors
- Headers set correctly when tested with curl from Brave context

### Step 2: Visit the Malicious Page in Brave Browser on Windows
procedure: [[procedures/Initiate-Download-Prompt-in-Brave-Browser]]

**Objective**: Access the malicious endpoint from Brave to trigger Referer detection.

**Instructions**: Open Brave browser on a Windows machine and navigate to the malicious page, e.g., https://your-server.com/test-driver.php. The server detects the Brave Referer and prepares torrent headers.

No specific command needed; this is browser navigation.

**Expected Output**: Page loads, but download may not trigger yet.

**Success Indicators**:
- Referer header sent successfully (verify server logs)
- No immediate errors in browser console

### Step 3: Click the 'Click Me' Link on the Page
procedure: [[procedures/Initiate-Download-Prompt-in-Brave-Browser]]

**Objective**: Initiate the download via a link that integrates with WebTorrent.

**Instructions**: On the malicious page, include a simple HTML link like <a href="download.php">Click me</a> that points to the PHP script. Clicking it triggers the download prompt due to WebTorrent integration.

**Expected Output**: Browser prompts for download with 'Save .torrent file' option.

**Success Indicators**:
- Download dialog appears
- File suggested as PoC.torrent

### Step 4: Select 'Save .torrent File' Option in the Browser
procedure: [[procedures/Initiate-Download-Prompt-in-Brave-Browser]]

**Objective**: Trick WebTorrent into downloading the file without content validation.

**Instructions**: In the Brave download prompt, choose 'Save .torrent file'. The browser saves the file as PoC.torrent, but the content is the malicious .bat payload due to header manipulation.

**Expected Output**: File downloads to default location with .torrent extension.

**Success Indicators**:
- File saved with torrent extension
- Content inspection shows batch script (e.g., via text editor)

### Step 5: Save and Open the Downloaded File
procedure: [[procedures/Execute-Downloaded-Malicious-Batch-File]]

**Objective**: User executes the disguised batch file.

**Instructions**: Locate the downloaded PoC.torrent file and double-click to open it. Windows interprets the batch content despite the extension, executing the payload.

Use [[commands/Launch-Notepad-via-Batch-Script]] embedded in the file.

**Expected Output**: Batch file runs silently.

**Success Indicators**:
- File executes without extension warning
- Payload initiates

### Step 6: Observe Execution of Payload
procedure: [[procedures/Execute-Downloaded-Malicious-Batch-File]]

**Objective**: Confirm RCE by observing application launch.

**Instructions**: After execution, monitor for the payload effect, such as Notepad opening.

**Expected Output**: Notepad launches, demonstrating arbitrary code execution.

**Success Indicators**:
- External application (Notepad) opens
- Potential for further exploitation like malware install

## Attack Chain Summary

### Key Achievements

1. Bypassed WebTorrent validation using Referer-based header manipulation
2. Forced download of executable as harmless torrent file
3. Achieved client-side RCE via user execution of disguised batch script

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Malicious File]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2024-10-04T00:00:00Z*
