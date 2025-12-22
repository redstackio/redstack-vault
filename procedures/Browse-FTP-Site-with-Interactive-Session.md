---
id: 9ded0054-1fba-4262-aa6f-b634a87026f2
name: Browse-FTP-Site-with-Interactive-Session
type: procedure
verified: true
submitted: true
created_at: '2020-04-01T00:29:32.993790+00:00'
updated_at: '2023-05-25T20:21:00.177175+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote File Copy|T1105 - Remote File Copy]]'
sub_techniques: []
tags:
  - file-transfer
  - network
commands:
  - '[[commands/launch-interactive-ftp-session]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Browse-FTP-Site-with-Interactive-Session

## Summary

This procedure authenticates to an FTP server and establishes an interactive session for browsing directories, listing files, and transferring data. It is commonly used during lateral movement to exfiltrate or infiltrate files over a network, leveraging FTP for remote file operations in environments where the protocol is enabled.

## Description

FTP (File Transfer Protocol) allows for the interactive management of files on a remote server. This procedure covers connecting to an FTP server, authenticating (including anonymous access), and executing common commands to navigate the filesystem and perform transfers. It is applicable in scenarios where an attacker has network access to an FTP service, such as after initial access or during command and control operations. The technique aligns with remote file copy activities, enabling the upload of tools or download of sensitive data. Prerequisites include an FTP client and knowledge of the target IP; anonymous access may be available on misconfigured servers.

## Requirements

1. Network connectivity to the target FTP server on port 21 (or 990 for FTPS).
2. FTP client installed (built-in on most Linux distributions via the `ftp` package and on Windows via command prompt).
3. Target IP address or hostname.
4. Valid credentials if anonymous access is not permitted; for anonymous, use 'anonymous' as username and any email as password.

## Defense

- Disable unnecessary FTP services or restrict to FTPS/SFTP for encryption.
- Block anonymous logins and implement strong authentication (e.g., integrate with Active Directory).
- Monitor network traffic for FTP connections (port 21) using tools like Snort or firewall logs.
- Enable logging on FTP servers to detect unusual file transfers or access patterns.

## Objectives

1. Establish a secure interactive connection to the FTP server.
2. Authenticate successfully to gain filesystem access.
3. Browse, list, and transfer files to achieve data exfiltration or tool deployment.
4. Verify session success through command responses and file operations.

## Instructions

### Step 1: Launch the Interactive FTP Session

**Context**: Initiate a connection to the target FTP server to begin the interactive session. This step establishes the TCP connection and prompts for authentication, allowing anonymous or credentialed login.

**Command** ([[commands/launch-interactive-ftp-session]]):
```bash
ftp $_TARGET_IP
```

> This command opens the FTP client and connects to the specified IP. Upon connection, enter the username (e.g., 'anonymous' for public access) and password when prompted. If credentials are invalid, the server will reject the login; retry with valid creds if known. Successful authentication grants access to the remote filesystem.

### Step 2: Authenticate and Verify Connection

**Context**: Complete the login process and confirm the session is active. This ensures the attacker can interact with the server before proceeding to file operations.

**Instructions**: After running the command, respond to the prompts:
- Username: Enter 'anonymous' or valid username.
- Password: Enter any string for anonymous or the actual password.
If login succeeds, the prompt changes to 'ftp>', indicating an active session. Type 'pwd' to verify the current directory on the server.

**Expected Output**:
```
Connected to 10.10.10.10.
220 Microsoft FTP Service
Name (10.10.10.10:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> pwd
```

### Step 3: Browse and Interact with the FTP Filesystem

**Context**: Use built-in FTP commands to navigate directories, list contents, and perform transfers. This step enables reconnaissance of the server's file structure and execution of file operations.

**Instructions**: Within the 'ftp>' prompt, execute commands as needed. Common operations include:

- Change to a directory: `cd $_DIR` (e.g., `cd /pub`)
- List current directory contents: `dir` or `ls`
- Download a file: `get $_REMOTE_FILENAME` (saves to local current directory)
- Upload a local file: `put $_LOCAL_FILENAME`
- Download multiple files: `mget $_PATTERN` (e.g., `mget *.txt`)
- Set transfer mode for binary files: `binary` (prevents corruption of non-text files like executables)
- Display help: `help` for all available commands
- Exit session: `bye` or `quit`

Decision point: If transferring binary files (e.g., .exe, .pdf), always run `binary` first; otherwise, use default ASCII mode for text. Verify each operation by checking local files or server responses.

**Expected Output** (example for `dir`):
```
f_tp> dir
200 PORT command successful.
150 Opening ASCII mode data connection for file list.
... (file listing) ...
226 Transfer complete.
f_tp>
```

> These commands allow real-time interaction. For large transfers, monitor progress via server responses. If a command fails (e.g., permission denied), the server returns an error code like 550; adjust path or credentials accordingly.
