---
id: 97f92a38-5c30-4899-b2e9-d1b94ae3328d
type: tool
verified: true
created_at: '2019-08-28T21:17:33.126811+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - pass-the-hash
url: 'https://github.com/byt3bl33d3r/CrackMapExec'
validated: true
---

# CrackMapExec

**Status**: Unverified

## Overview

CrackMapExec (CME) is a post-exploitation tool designed for assessing the security of Active Directory networks. It automates credential brute forcing across multiple protocols such as SMB/CIFS, HTTP, WinRM, SSH, and MSSQL. CME also supports advanced techniques like Pass-the-Hash (PtH) attacks, allowing operators to use NTLM hashes instead of plaintext passwords for authentication and lateral movement.

## Description

CME acts as a modular framework for network pentesting, enabling rapid enumeration of valid credentials, execution of commands on remote systems, and identification of misconfigurations in Windows environments. It is particularly useful in red team engagements for spraying credentials across a domain, verifying hash validity, and chaining into further exploitation. The tool supports Kerberos authentication, ticket passing, and can output results in various formats for integration with other tools.

## Features

- Multi-protocol brute forcing: Supports SMB, WinRM, SSH, HTTP/HTTPS, MSSQL, and RDP.
- Pass-the-Hash and Pass-the-Ticket: Authenticate using hashes or Kerberos tickets without cracking.
- Command execution: Run commands or scripts remotely over supported protocols.
- Target spraying: Test credentials against IP ranges or host lists efficiently.
- Output formatting: JSON, CSV, or human-readable for logging and analysis.
- Kerberos delegation: Handle complex AD scenarios with delegation and constrained accounts.

## Installation

### Requirements

- Python 3.7+ (for source install)
- Dependencies: Various Python libraries like ldap3, pyasn1 (handled by pip)
- For binary: No additional requirements beyond the executable

### Install Commands

#### Pre-built Binary (Recommended for Simplicity)

1. Navigate to the GitHub Actions page: https://github.com/byt3bl33d3r/CrackMapExec/actions
2. Select the latest successful workflow build.
3. Download the appropriate binary for your platform (e.g., crackmapexec_linux.zip for Linux).
4. Extract and make executable:
   ```bash
   unzip crackmapexec_linux.zip
   chmod +x crackmapexec
   sudo mv crackmapexec /usr/local/bin/
   ```

#### From Source (Kali/Ubuntu)

```bash
sudo apt update
sudo apt install crackmapexec  # On Kali Linux, pre-packaged
# Or via pip:
pip3 install crackmapexec
```

#### Windows

Use the Windows binary from GitHub Actions or install via pip in a Python environment.

## Basic Usage

```bash
crackmapexec --help
```

This displays all available modules, options, and usage syntax.

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --users` | Username or file containing usernames |
| `-p, --pass` | Password or file containing passwords |
| `-d, --domain` | Domain for authentication |
| `-x, --exec-method` | Method to execute commands (e.g., powershell) |
| `--no-bruteforce` | Disable brute forcing |
| `-o, --output-file` | Save output to file |

## Examples

### Example 1: Basic Usage - SMB Brute Force

```bash
crackmapexec smb 192.168.1.0/24 -u users.txt -p passwords.txt
```

This sprays credentials from wordlists against an IP range over SMB.

### Example 2: Advanced Usage - WinRM Command Execution with PtH

```bash
crackmapexec winrm 192.168.1.10 -u administrator -H aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 -x "whoami"
```

Executes 'whoami' on the target using a provided NTLM hash.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Remote Services]] Remote Services

### Tactics

- [[Credential Access]] Credential Access
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SMB/WinRM connections from a single source IP to multiple hosts.
- Failed authentication logs (Event ID 4625) followed by successes.
- Network traffic patterns matching CME's protocol probes (e.g., high volume of type 3 SMB negotations).
- Process creation on endpoints from WinRM (Event ID 4688) with command-line arguments indicating remote execution.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[tools/BloodHound]]
- [[tools/PowerSploit]]

## References

- Official GitHub: https://github.com/byt3bl33d3r/CrackMapExec
- Documentation: https://github.com/byt3bl33d3r/CrackMapExec/wiki
- Related resources: Black Hills Information Security blog posts on AD pentesting
