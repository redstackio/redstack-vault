---
id: 2883aaeb-d8fe-4ea5-99d9-a3539bac3dc9
name: bloodhound-py-enumerate-active-directory
type: command
executor: bash
data: python bloodhound.py -c All -u $_USER -p $_PASSWORD -ns $_DCIP -d $_DOMAIN
output: >-
  root@kali:~# python bloodhound.py -c All -u bob -p s3cr3tpass  -ns 10.10.10.10
  -d megabank.local

  INFO: Found AD domain: megabank.local

  INFO: Connecting to LDAP server: DC01.megabank.local

  INFO: Found 1 domains

  INFO: Found 1 domains in the forest

  INFO: Found 2 computers

  INFO: Connecting to LDAP server: DC01.megabank.local

  WARNING: Could not resolve SID: S-1-5-21-3072663084-364016917-1341370565-1153

  INFO: Found 30 users

  INFO: Found 65 groups

  INFO: Found 1 trusts

  INFO: Starting computer enumeration with 10 workers

  INFO: Querying computer: DC01.megabank.local

  INFO: Querying computer: EXCH01.megabank.local

  INFO: Done in 00M 25S
created_at: '2020-03-23T21:16:03.287744+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
  - Linux
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# bloodhound-py-enumerate-active-directory

## Command

```bash
python bloodhound.py -c All -u $_USER -p $_PASSWORD -ns $_DCIP -d $_DOMAIN
```

## Description

This command uses BloodHound.py to enumerate an entire Active Directory environment, collecting data on domains, computers, users, groups, trusts, and session information. It authenticates remotely using provided credentials and outputs JSON files compatible with the BloodHound GUI for visualization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c All | Collection method: 'All' gathers comprehensive data including users, groups, computers, trusts, and sessions | Yes |
| -u $_USER | Username for authentication (domain user) | Yes |
| -p $_PASSWORD | Password for the specified user | Yes |
| -ns $_DCIP | IP address or hostname of the domain controller (NetBIOS name server) | Yes |
| -d $_DOMAIN | Fully qualified domain name (FQDN) | Yes |

## Examples

### Basic Usage

```bash
python bloodhound.py -c All -u bob -p s3cr3tpass -ns 10.10.10.10 -d megabank.local
```

### Advanced Usage

For local execution on a domain-joined system (no remote auth needed):

```bash
python bloodhound.py -c All -d megabank.local
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# python bloodhound.py -c All -u bob -p s3cr3tpass  -ns 10.10.10.10 -d megabank.local
INFO: Found AD domain: megabank.local
INFO: Connecting to LDAP server: DC01.megabank.local
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 2 computers
INFO: Connecting to LDAP server: DC01.megabank.local
WARNING: Could not resolve SID: S-1-5-21-3072663084-364016917-1341370565-1153
INFO: Found 30 users
INFO: Found 65 groups
INFO: Found 1 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC01.megabank.local
INFO: Querying computer: EXCH01.megabank.local
INFO: Done in 00M 25S
```

The command generates JSON files (e.g., users.json, computers.json) in the current directory for import into BloodHound.

## Related

- [[Related Procedure]]
- [[tools/bloodhound-py]]
