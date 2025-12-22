---
type: command
executor: command_prompt
data: >-
  SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USERNAME --ldappassword
  $_PASSWORD
output: |-
  Initializing SharpHound...
  Resolved Collection Methods: All
  [+] Pre-populating Domain Controller SIDs
  Status: 500 objects finished
  Enumeration finished in 00:01:30
  Compressing data to BloodHound.zip
  SharpHound Enumeration Completed!
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - ad
  - enumeration
verified: true
validated: true
---

# SharpHound-Collect-AD-Data

## Command

```command_prompt
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USERNAME --ldappassword $_PASSWORD
```

## Description

Collects all AD data types using authenticated LDAP queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c All | Collect all methods | Yes |
| -d | Domain name | Yes |
| --ldapusername | LDAP user | Yes |
| --ldappassword | LDAP pass | Yes |

## Examples

### Basic Usage

```command_prompt
SharpHound.exe -c All -d example.com
```

Anonymous if possible.

## Expected Output

ZIP file with JSON data.

## Related

- [[procedures/Map-Active-Directory-with-SharpHound]]
- [[tools/SharpHound]]
