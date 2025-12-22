---
id: db892aee-e4c4-47c6-b80f-c41963c124ea
name: adidnsdump-enumerate-zones
type: command
executor: bash
data: adidnsdump -u DOMAIN\\user --print-zones dc.domain.corp --dns-tcp
output: null
created_at: '2023-04-06T03:56:06.634632Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
  - Linux
tags:
  - dns-enumeration
  - active-directory
verified: true
validated: true
---

# adidnsdump-enumerate-zones

## Command

```bash
adidnsdump -u $_DOMAIN\\$_USERNAME --print-zones $_DC_HOSTNAME --dns-tcp
```

## Description

This command uses the adidnsdump tool to enumerate and print all DNS zones stored in Active Directory on a specified domain controller. It authenticates via NTLM and forces TCP for DNS queries to handle larger responses reliably.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_DOMAIN\\$_USERNAME | Domain credentials in DOMAIN\\user format for authentication | Yes |
| --print-zones | Flag to list zone names without full dump | Yes |
| $_DC_HOSTNAME | Hostname or IP of the domain controller (e.g., dc.domain.corp) | Yes |
| --dns-tcp | Force TCP protocol for DNS queries instead of UDP | Yes |

## Examples

### Basic Usage

```bash
adidnsdump -u CORP\\attacker --print-zones dc.corp.local --dns-tcp
```

### Advanced Usage

```bash
adidnsdump -u CORP\\attacker --print-zones 192.168.1.10 --dns-tcp -v
```

## Expected Output

```
[+] Enumerating zones on dc.domain.corp
Zone: _msdcs.domain.corp
Zone: domain.corp
Zone: 0.in-addr.arpa
[+] Enumeration complete
```

A list of DNS zones is displayed, showing AD-integrated zones like forest and domain partitions.

## Related

- [[procedures/Active-Directory-Integrated-DNS-Enumeration]]
- [[tools/adidnsdump]]
