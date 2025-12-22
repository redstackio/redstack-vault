---
id: 5b3f1e8a-e664-455c-9753-7adf2c7956d0
name: Egress-Assess
type: tool
verified: true
created_at: '2019-08-28T21:17:33.162846+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - egress-testing
  - network-security
  - red-team
  - detection-bypass
url: 'https://github.com/mdsecresearch/Egress-Assess'
validated: true
---

# Egress-Assess

**Status**: Unverified

## Overview

Egress-Assess is a PowerShell-based tool designed to test an organization's egress data detection and filtering capabilities. It simulates various outbound communication methods, such as HTTP, DNS, ICMP, and more, to identify allowed channels that could be used for data exfiltration during security assessments or red team operations.

## Description

Developed by MDSec, Egress-Assess helps security professionals evaluate network security controls by attempting to establish outbound connections using common protocols and payloads. It's particularly useful in controlled environments to map egress rules without causing real harm, providing insights into potential exfiltration paths. The tool supports both basic and advanced testing modes, including tunneling simulations, and logs results for analysis.

## Features

- Feature 1: Tests multiple protocols (HTTP/S, DNS, ICMP, SMTP, FTP) for outbound allowance.
- Feature 2: Simulates data exfiltration with customizable payloads and targets.
- Feature 3: Supports tunneling techniques like DNS tunneling to bypass strict filters.
- Feature 4: Verbose logging and result export for reporting.
- Feature 5: Modular design allowing extension for custom protocols.

## Installation

### Requirements

- PowerShell 5.0 or later (Windows environments).
- Internet access for initial download (ironic for egress testing, but required for setup).
- Administrative privileges may be needed for certain network tests.

### Install Commands

```powershell
# Clone the repository
Invoke-WebRequest -Uri https://github.com/mdsecresearch/Egress-Assess/archive/master.zip -OutFile Egress-Assess.zip
Expand-Archive Egress-Assess.zip -DestinationPath C:\Tools\

# Import the module
Import-Module C:\Tools\Egress-Assess-master\EgressAssess.psm1
```

For Kali Linux or cross-platform use, run via PowerShell Core:

```bash
# Install PowerShell Core
sudo apt install powershell

# Then follow Windows steps in pwsh
pwsh -Command "Invoke-WebRequest ..." # etc.
```

## Basic Usage

```powershell
Get-Help Invoke-EgressAssess -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| `-ScanType` | Specifies the scan mode (Basic, Full, Custom) |
| `-Protocol` | Limits test to a specific protocol (e.g., HTTP, DNS) |
| `-Target` | Custom target for outbound attempts |
| `-Data` | Payload to send during tests |
| `-Verbose` | Detailed output for troubleshooting |

## Examples

### Example 1: Basic Usage

```powershell
Invoke-EgressAssess -ScanType Basic
```

This runs a quick test on default protocols and reports allowances.

### Example 2: Advanced Usage

```powershell
Invoke-EgressAssess -Protocol HTTP -Target http://httpbin.org/post -Data "Egress test payload" -Verbose
```

Sends a POST request to test HTTP egress with a sample payload.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol
- [[Protocol Tunneling]] Protocol Tunneling
- [[Automated Exfiltration]] Automated Exfiltration

### Tactics

- [[Exfiltration]] Exfiltration
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell execution logs showing Invoke-EgressAssess module loads.
- Detection method 2: Unusual outbound connections to test domains (e.g., httpbin.org) from internal hosts.
- Detection method 3: Network monitoring for protocol-specific patterns like encoded DNS queries.
- Detection method 4: File system artifacts from downloaded ZIP or module imports.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/PowerSploit]]

## References

- Official GitHub Repository: https://github.com/mdsecresearch/Egress-Assess
- MDSec Blog Post: https://www.mdsec.co.uk/2019/08/egress-assess/
- Related Resource: PowerShell Empire Documentation for Egress Modules
