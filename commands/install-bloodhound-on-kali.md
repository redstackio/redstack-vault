---
id: d6c975dc-27f7-4531-bae8-f5059327e3f3
name: install-bloodhound-on-kali
type: command
executor: bash
data: apt install bloodhound
output: null
created_at: '2023-04-06T03:56:02.119679+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - setup
  - ad
verified: true
validated: true
---

# install-bloodhound-on-kali

## Command

```bash
apt install bloodhound
```

## Description

Installs BloodHound package on Debian-based systems like Kali Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| apt | Package manager | Built-in |
| install | Install action | Built-in |
| bloodhound | Package name | Yes |

## Examples

### Basic Usage

```bash
apt update && apt install bloodhound
```

## Expected Output

Package installation progress, ending with "bloodhound is already the newest version" or similar.

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/BloodHound]]
