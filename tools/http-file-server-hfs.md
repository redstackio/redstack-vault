---
id: 0f2c63d2-95c6-4574-867a-7e623f4da486
type: tool
verified: true
created_at: '2020-03-22T21:32:12.087682+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - file-transfer
url: 'https://www.rejetto.com/hfs/'
validated: true
---

# HTTP File Server (HFS)

**Status**: ✓ Verified

## Overview

HTTP File Server (HFS) is a lightweight HTTP server designed specifically for Windows to easily host and share files over the network. It features a simple GUI with a log window and file manager, allowing users to add files via drag-and-drop, copy-paste, or folder integration. Ideal for red team operations requiring quick file hosting, such as serving payloads, scripts, or data exfiltration endpoints without the overhead of full-featured web servers.

## Description

HFS focuses on file serving capabilities, omitting unnecessary web server features to maintain a small footprint (under 1MB). It supports HTTP and HTTPS, customizable access controls, bandwidth limiting, and template-based web interfaces for file listings. In security testing, it's commonly used for lateral movement by hosting malicious files for download by compromised hosts or for simple C2 infrastructure setup.

## Features

- Feature 1: Drag-and-drop file management via intuitive GUI
- Feature 2: Real-time log monitoring for access and errors
- Feature 3: Customizable HTTP responses and file templates
- Feature 4: Support for virtual hosts and URL masking
- Feature 5: Bandwidth throttling and IP filtering for controlled sharing
- Feature 6: Portable executable—no installation required

## Installation

### Requirements

- Windows OS (XP or later)
- Administrator privileges for firewall exceptions on default ports

### Install Commands

HFS is a portable application and does not require traditional installation.

```cmd
# Download and run directly
# No command needed; execute the EXE
```

1. Download HFS from the official site: [https://www.rejetto.com/hfs/?f=dl](https://www.rejetto.com/hfs/?f=dl)
2. Extract the ZIP if needed (single EXE file)
3. Run `HFS.exe` and allow through Windows Firewall

For Kali/Ubuntu (via Wine): Not natively supported, but can run under Wine:

```bash
# Install Wine
sudo apt update && sudo apt install wine

# Download and run
wget https://www.rejetto.com/hfs/hfs_setup.exe
wine hfs_setup.exe
```

## Basic Usage

```cmd
HFS.exe
```

Launches the GUI. Add files/folders through the interface, configure port and options, then start the server. Files become accessible via http://localhost:PORT/ or IP-based URLs.

### Common Options

HFS supports limited CLI options; most configuration is GUI-based.

| Option | Description |
|--------|-------------|
| /port:PORT | Start server on specified port (e.g., /port:8080) |
| /minimized | Launch minimized to system tray |
| /? | Show help for CLI options |

## Examples

### Example 1: Basic Usage

```cmd
HFS.exe
```

Open GUI, add a folder with payloads, start server. Access files at http://192.168.1.100:80/

### Example 2: Advanced Usage

```cmd
HFS.exe /port:8443
```

Starts on port 8443 for HTTPS-like sharing (configure SSL in GUI if needed).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer (hosting files for download to targets)
- [[Encrypted Channel]] Encrypted Channel (if configured with HTTPS for file transfer)

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP servers on non-standard ports (e.g., process monitoring for HFS.exe)
- Detection method 2: Network traffic to internal IPs serving files (SIEM rules for unexpected HTTP responses)
- Detection method 3: File system artifacts like HFS.exe in temp directories
- Detection method 4: Log analysis for drag-and-drop file additions or bandwidth spikes

## Related Procedures

No specific procedures linked yet. Commonly used in file transfer procedures like [[procedures/Host-Payload-for-Download]].

## Related Tools

- [[tools/python-http-server]] (cross-platform alternative)
- [[tools/apache-http-server]] (full-featured web server)

## References

- Official website: [https://www.rejetto.com/hfs/](https://www.rejetto.com/hfs/)
- Download: [https://www.rejetto.com/hfs/?f=dl](https://www.rejetto.com/hfs/?f=dl)
- Forum/Support: Rejetto forums for advanced configuration
