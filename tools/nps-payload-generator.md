---
type: tool
description: >-
  A Python script for generating payloads to evade intrusion detection,
  supporting MSBuild XML payloads for local execution and HTA payloads for
  web-based delivery, often used to bypass AppLocker restrictions on Windows.
url: ''
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - applocker
  - defense-evasion
  - payload-generation
  - msbuild
  - metasploit
validated: true
---

# nps-payload-generator

**Status**: Unverified

## Overview

nps-payload-generator is a Python-based tool designed to create payloads that help in basic intrusion detection avoidance. It generates two main types: XML payloads executable via MSBuild.exe on Windows systems, which can bypass AppLocker rules requiring signed binaries, and HTA (HTML Application) payloads that can be hosted on a web server for execution in a victim's browser. The tool integrates with Metasploit for handling callbacks, making it useful for red team operations involving defense evasion and initial payload delivery.

Common use cases include generating reverse shells or Meterpreter payloads for Windows environments during penetration testing or red team exercises.

## Description

The tool supports generating payloads in formats compatible with MSBuild for local or remote execution and HTA for browser-based attacks. MSBuild payloads are particularly effective against environments with AppLocker policies, as they leverage the trusted MSBuild.exe to execute arbitrary code without requiring signed executables. HTA payloads allow for remote code execution via web delivery, often evading basic web application firewalls. The script prompts for payload selection (e.g., reverse_tcp, reverse_http), listener IP/port, and outputs an XML file for MSBuild and a .rc file for Metasploit resource loading.

## Features

- Generate MSBuild-compatible XML payloads for local execution on Windows.
- Create HTA payloads for web server hosting and browser execution.
- Integration with Metasploit for automated listener setup via resource scripts.
- Support for common Meterpreter payloads (reverse_tcp, reverse_http, reverse_https) and custom PowerShell payloads.
- Interactive menu for easy payload customization.

## Installation

### Requirements

- Python 2.7 (primary support; Python 3 may require minor adjustments).
- Metasploit Framework installed for handling generated resource scripts.
- Access to a Windows target with MSBuild.exe (part of .NET Framework v4.0+).

### Install Commands

Download the script from its source repository (e.g., GitHub if available) and place it in a working directory.

```bash
# On Kali/Debian/Ubuntu (Python 2 pre-installed on Kali)
git clone <repository-url> nps-payload
cd nps-payload
# No additional installation needed; script is standalone
```

For Python 3 compatibility on Ubuntu:

```bash
sudo apt update
sudo apt install python3
# Test with python3 nps_payload.py (may need syntax fixes for print statements)
```

## Basic Usage

```bash
python2 nps_payload.py
```

This launches an interactive menu for selecting payload type and options.

### Common Options

The tool is menu-driven with no CLI flags; selections are made via numbered choices:

| Option | Description |
|--------|-------------|
| 1 | Generate MSBuild/NPS/MSF payload (XML for local/remote execution) |
| 2 | Generate MSBuild/NPS/MSF HTA payload (for web delivery) |
| 99 | Quit |

Payload types include:

| Payload | Description |
|---------|-------------|
| 1 | windows/meterpreter/reverse_tcp |
| 2 | windows/meterpreter/reverse_http |
| 3 | windows/meterpreter/reverse_https |
| 4 | Custom PS1 Payload |

## Examples

### Example 1: Basic MSBuild Payload Generation

```bash
python2 nps_payload.py
```

Interactive session:
- Select task: 1 (MSBuild payload)
- Select payload: 1 (reverse_tcp)
- Enter LHOST: 10.10.10.100
- Enter LPORT: 443

This generates `msbuild_nps.xml` and `msbuild_nps.rc`.

### Example 2: HTA Payload for Web Delivery

```bash
python2 nps_payload.py
```

- Select task: 2 (HTA payload)
- Follow prompts for IP/port and payload type.

Host the generated HTA file on a web server and trick the victim into opening it via browser.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] System Binary Proxy Execution (MSBuild.exe usage)
- [[Remote File Copy]] Ingress Tool Transfer (HTA web delivery)
- [[PowerShell]] PowerShell (custom PS1 payloads)

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation
- [[Command and Control]] Command and Control

## Detection

- Monitor for MSBuild.exe spawning unusual child processes or network connections.
- Log PowerShell execution and script block logging for custom payloads.
- Web server logs for HTA file requests; browser logs for unexpected HTA executions.
- EDR alerts on unsigned XML files executed via MSBuild or anomalous Meterpreter callbacks.

## Related Procedures

- [[procedures/Windows-AppLocker-Bypass-Using-MSBuild]]
- [[procedures/Generate-and-Deploy-HTA-Payloads]]

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/MSBuild]]

## References

- Original script documentation (README.md in source)
- MITRE ATT&CK for technique details
