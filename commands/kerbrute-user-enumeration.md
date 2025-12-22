---
id: c8a256df-5e04-4d35-a938-d68948ccefa0
name: kerbrute-user-enumeration
type: command
executor: bash
data: kerbrute userenum --dc $_DC_HOST -d $_DOMAIN $_USERLIST_FILE
output: null
created_at: '2023-04-06T03:56:04.223718+00:00'
updated_at: '2023-04-10T20:26:23.736913+00:00'
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - active-directory
verified: true
validated: true
---

# kerbrute-user-enumeration

## Command

```bash
kerbrute userenum --dc $_DC_HOST -d $_DOMAIN $_USERLIST_FILE
```

## Description

This command uses Kerbrute to enumerate valid usernames in an Active Directory domain by attempting Kerberos pre-authentication requests for each entry in a username list. It identifies active accounts without triggering full authentication events.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --dc $_DC_HOST | IP address or hostname of the Domain Controller | Yes |
| -d $_DOMAIN | Target domain name (e.g., contoso.local) | Yes |
| $_USERLIST_FILE | Path to a text file containing one username per line | Yes |

## Examples

### Basic Usage

```bash
kerbrute userenum --dc 10.0.0.1 -d contoso.local /path/to/users.txt
```

### Advanced Usage

```bash
kerbrute userenum --dc dc.contoso.local -d contoso.local users.txt -v
```
(Adds verbose output with -v flag for detailed logging.)

## Expected Output

Valid usernames are marked with [+], invalid with [-]:

```
2023/10/01 12:00:00 [!] Invalid username: invaliduser@contoso.local
2023/10/01 12:00:00 [+] VALID USERNAME: administrator@contoso.local
2023/10/01 12:00:00 Finished user enumeration. Found 1 valid usernames.
```

## Related

- [[procedures/Kerberos-Pre-Auth-Bruteforcing-with-Kerbrute]]
- [[commands/kerbrute-password-bruteforce]]
