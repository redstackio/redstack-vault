---
id: ac-1078002
tags:
  - rce
  - uri-scheme
  - nextcloud
  - qt
  - webview
  - winscp
type: attack_chain
tools:
  - '[[tools/WinSCP]]'
  - '[[tools/xmessage]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Windows
  - Linux
  - Desktop
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Nextcloud-Add-Account-Flow]]'
  - '[[procedures/Serve-Malicious-Login-Page-with-URI-Links]]'
  - '[[procedures/Trigger-Malicious-URI-in-WebView]]'
  - '[[procedures/Exploit-OS-Handler-for-Arbitrary-Code-Execution]]'
step_count: 4
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:54.907Z'
description: >-
  Multi-stage attack exploiting the Nextcloud Desktop Client's lack of URI
  scheme validation in the Add Account WebView, allowing a malicious server to
  trigger OS handlers for arbitrary code execution on Windows and Linux.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
---
# Nextcloud-Desktop-Client-RCE-via-Malicious-URI-Schemes

Multi-stage attack chain demonstrating exploitation of the Nextcloud Desktop Client vulnerability (HackerOne #1078002), where a malicious server uses unvalidated URI schemes in the Add Account login flow to achieve remote code execution via OS default handlers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Add Account] --> B[Serve Malicious Page]
    B --> C[User Clicks URI Link]
    C --> D[OS Handler Executes Code]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/WinSCP]] (for Windows exploitation)
- Server to host malicious content (e.g., Apache/Nginx)

### Target Environment

- Nextcloud Desktop Client (vulnerable versions)
- Windows with WinSCP installed or Linux (e.g., Xubuntu) with SFTP auto-mount support
- QT-based WebView in client

### Initial Access Requirements

- User with Nextcloud Desktop Client attempting to add a malicious server account
- No prior credentials needed; relies on user interaction

## Detailed Attack Procedures

### Step 1: Initiate Add Account Flow
procedure: [[procedures/Initiate-Nextcloud-Add-Account-Flow]]

**Objective**: Start the account addition process to open the vulnerable WebView.

**Instructions**: Launch the Nextcloud Desktop Client and trigger the Add Account wizard. This opens a native WebView window loading the attacker's server login page.

**Expected Output**: WebView displays the login page from the malicious server.

**Success Indicators**:
- WebView window opens without errors
- Server receives the initial request from the client

### Step 2: Serve Malicious Login Page with URI Links
procedure: [[procedures/Serve-Malicious-Login-Page-with-URI-Links]]

**Objective**: Deliver HTML content with embedded malicious URI hyperlinks to the WebView.

**Instructions**: Configure the server to respond to the login request with HTML containing hyperlinks using schemes like `sftp://`. For example, embed a link disguised as a login button: `<a href="sftp://youtube:com;watch=sn96aVA2;x-proxymethod=5;x-proxytelnetcommand=calc.exe@foo.bar/">Login</a>`.

**Expected Output**: Page loads in WebView with clickable malicious links.

**Success Indicators**:
- Client WebView renders the page
- Links are present and clickable without visible warnings

### Step 3: Trigger Malicious URI in WebView
procedure: [[procedures/Trigger-Malicious-URI-in-WebView]]

**Objective**: Induce the user to click the link, invoking the unvalidated URI handler.

**Instructions**: Socially engineer the user to click the link (e.g., label it as "Continue Login"). The click calls `QDesktopServices::openUrl()` in `src/gui/wizard/webview.cpp` (L226-L232), passing the URI directly to the OS handler without scheme validation.

**Expected Output**: OS default handler launches for the URI scheme (e.g., SFTP client opens).

**Success Indicators**:
- No client-side blocking occurs
- OS handler (e.g., WinSCP or file manager) activates

### Step 4: Exploit OS Handler for Arbitrary Code Execution
procedure: [[procedures/Exploit-OS-Handler-for-Arbitrary-Code-Execution]]

**Objective**: Leverage the OS handler to execute arbitrary commands, achieving RCE.

**Instructions**: On Windows, use the SFTP URI to exploit WinSCP's proxy parsing: execute [[commands/sftp-uri-winscp-rce]] via the link. On Linux, use [[commands/sftp-uri-linux-desktop-execution]] to mount a share and run [[commands/desktop-file-rce]]. For NTLM leaks, use `file://` or `dav://` schemes.

```bash
# Example server-side .desktop file content (for Linux)
[Desktop Entry]
Exec=xmessage "Arbitrary RCE :)"
Type=Application
```

**Expected Output**: Command execution (e.g., calc.exe on Windows, xmessage on Linux) or hash leak.

**Success Indicators**:
- Calculator launches on Windows
- Message dialog appears on Linux
- Network traffic shows NTLM authentication attempts

## Attack Chain Summary

### Key Achievements

1. Bypassed URI validation in QT WebView for arbitrary scheme invocation
2. Achieved RCE on Windows via WinSCP proxy command injection
3. Enabled RCE on Linux via auto-mounted SFTP shares and .desktop execution
4. Potential for NTLM hash exfiltration using file/dav schemes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2024-01-01T00:00:00Z*
