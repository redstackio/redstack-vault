---
id: c123cbca-d16e-4abd-9fbb-c1fa4edd696b
name: certipy-relay-setup
type: command
executor: bash
data: certipy relay -ca $_CA_IP
output: null
created_at: '2023-04-06T03:56:05.989740+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - certipy
  - relay
verified: true
validated: true
---

# certipy-relay-setup

## Command

```bash
certipy relay -ca $_CA_IP
```

## Description

Configures Certipy relay mode targeting the specified CA IP for certificate operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ca $_CA_IP | Certificate Authority IP | Yes |

## Examples

### Basic

```bash
certipy relay -ca 172.16.19.100
```

## Expected Output

Relay configured for CA 172.16.19.100
Listening for relay requests...

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/Certipy]]
