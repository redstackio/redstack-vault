---
id: 7920dfc7-ff45-43bb-aec0-c2b0adb28082
type: tool
verified: true
created_at: '2019-08-28T21:17:30.415879+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - spoofing
  - mitm
  - llmnr
  - nbt-ns
  - mdns
  - credential-access
url: 'https://github.com/Kevin-Robertson/Inveigh'
validated: true
---

# Inveigh

**Status**: Unverified

## Overview

Inveigh is a PowerShell-based tool for performing LLMNR (Link-Local Multicast Name Resolution), mDNS (Multicast DNS), and NBT-NS (NetBIOS Name Service) spoofing and man-in-the-middle attacks. It is commonly used in red team engagements to capture NTLM authentication hashes on Windows networks by responding to name resolution failures with spoofed responses, enabling credential theft or relay attacks.

## Description

Inveigh operates by listening for name resolution requests on the local network and injecting forged responses to redirect traffic through the attacker's machine. This allows interception of authentication attempts, particularly useful in environments where users mistype hostnames or access uncached resources. The tool supports console output, file logging, and integration with relay functions for further exploitation. It is lightweight, requiring only PowerShell, and runs without elevated privileges in many cases, though admin rights enhance capabilities.

## Features

- Feature 1: LLMNR, NBT-NS, and mDNS spoofing to capture Net-NTLMv1/v2 hashes
- Feature 2: Real-time console monitoring and file-based capture of hashes and requests
- Feature 3: Optional HTTP/HTTPS server for challenge-response handling
- Feature 4: Integration with relay tools for SMB, HTTP, and other protocol attacks
- Feature 5: Customizable IP and hostname spoofing responses
- Feature 6: Support for WPAD (Web Proxy Auto-Discovery) poisoning

## Installation

### Requirements

- PowerShell 2.0 or later (Windows 7+ recommended)
- .NET Framework 3.5 or higher
- Network interface with access to target subnet (admin privileges for promiscuous mode optional but beneficial)

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri "https://github.com/Kevin-Robertson/Inveigh/archive/master.zip" -OutFile "Inveigh.zip"
Expand-Archive -Path "Inveigh.zip" -DestinationPath ".\Inveigh"

# Or clone repository if Git is available
git clone https://github.com/Kevin-Robertson/Inveigh.git
```

For Windows environments without internet, transfer the Inveigh.ps1 file manually.

## Basic Usage

```powershell
tool-name --help
```

Load the module and start basic spoofing:

```powershell
Import-Module .\Inveigh\Inveigh.ps1
Invoke-Inveigh -LLMNR Y -NBTNS Y
```

### Common Options

| Option | Description |
|--------|-------------|
| `-LLMNR <Y/N>` | Enable/disable LLMNR spoofing |
| `-NBTNS <Y/N>` | Enable/disable NBT-NS spoofing |
| `-mDNS <Y/N>` | Enable/disable mDNS spoofing |
| `-ConsoleOutput <ConsoleOnly/FileOnly/Both>` | Control output destination |
| `-SpooferIP <IP>` | IP to spoof in responses |
| `-FileName <string>` | Prefix for log files |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module .\Inveigh.ps1; Invoke-Inveigh -ConsoleOutput ConsoleOnly -LLMNR Y -NBTNS Y -mDNS Y
```

This starts spoofing on all protocols with console output.

### Example 2: Advanced Usage

```powershell
Import-Module .\Inveigh.ps1; Invoke-Inveigh -LLMNR Y -HTTP Y -SpooferIP 192.168.1.100 -FileName mycaptures
```

Enables HTTP challenge-response and logs to files prefixed with 'mycaptures'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and Relay
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Web Protocols]] Application Layer Protocol: Web Protocols

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual multicast traffic (ports 5355 UDP for LLMNR/mDNS, 137 UDP for NBT-NS)
- Detection method 2: PowerShell script block logging showing Inveigh imports or Invoke-Inveigh calls
- Detection method 3: Network logs of spoofed responses or unexpected NTLM auth attempts to non-DC hosts
- Detection method 4: Enable SMB signing and LLMNR disabling via Group Policy
- Detection method 5: Sysmon events for process creation (powershell.exe) with network connections

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Responder]]
- [[Impacket-Suite]]

## References

- Official GitHub: https://github.com/Kevin-Robertson/Inveigh
- Blog post by author: https://github.com/Kevin-Robertson/Inveigh/wiki
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1557/001/
