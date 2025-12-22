---
id: 5c4a122e-dccb-45ab-9ec8-4968664b983d
name: Find-Kerberoastable-Users-with-SPNs
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T17:49:32.623152+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[cme-smb-enable-rdp]]'
sub_techniques: []
tags:
  - kerberoasting
  - active-directory
  - credential-access
  - spn
commands:
  - '[[commands/getuser-spns-query-domain-and-request-hashes]]'
  - '[[commands/get-aduser-filter-spn-powershell]]'
  - '[[commands/get-netuser-spn-filter-domain-admins-powerview]]'
  - '[[commands/get-domainuser-spn-powerview]]'
  - '[[commands/rubeus-kerberoast-rc4-user]]'
platforms:
  - Windows
tools: []
validated: true
---

# Find-Kerberoastable-Users-with-SPNs

## Summary

This procedure identifies Active Directory user accounts configured with Service Principal Names (SPNs), which are potential targets for Kerberoasting attacks. Kerberoasting involves requesting Kerberos Ticket Granting Service (TGS) tickets for these service accounts from the Domain Controller and extracting their password hashes for offline cracking. It is typically used in credential access scenarios where an attacker has initial domain credentials to enumerate and exploit weakly protected service accounts.

## Description

In Active Directory environments, service accounts often have SPNs registered to allow Kerberos authentication for services they run. These accounts can be targeted via Kerberoasting because any authenticated domain user can request a TGS ticket for an SPN, which includes an encrypted hash of the service account's password. This procedure focuses on enumerating users with SPNs using PowerShell modules like Active Directory and PowerView, as well as Impacket's GetUserSPNs.py for requesting the hashes. It is applicable in domain-joined Windows environments and requires domain credentials with read access to AD objects. Success enables offline cracking of service account passwords, potentially leading to lateral movement or privilege escalation if the account has elevated permissions.

## Requirements

1. Valid domain credentials (username and password) with at least domain user privileges to query AD.
2. Network access to a Domain Controller (typically over LDAP port 389 or LDAPS 636).
3. Installed tools: PowerShell Active Directory module, PowerView (for advanced enumeration), Impacket suite (for GetUserSPNs.py), or Rubeus.exe on the attacker's system.
4. Target environment: Windows Active Directory domain with service accounts configured.

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous Kerberos TGS requests, especially for service accounts (Event ID 4769 in Windows Security logs with frequent requests from non-service principals).
- Enforce strong, complex passwords for service accounts and rotate them regularly; consider using Managed Service Accounts (MSAs) or group Managed Service Accounts (gMSAs) to automate rotation.
- Restrict SPN registration to privileged accounts and audit SPN attributes on user objects.
- Enable Advanced Audit Policy for Kerberos authentication events and use tools like Microsoft ATA or SIEM for anomaly detection in AD queries.

## Objectives

1. Enumerate all domain users with registered SPNs to identify potential Kerberoasting targets.
2. Prioritize high-value targets like domain admin accounts with SPNs.
3. Request TGS tickets (hashes) for selected SPN users from the Domain Controller for offline cracking.
4. Validate successful hash extraction to confirm the procedure's outcome.

## Instructions

### Step 1: Enumerate All Domain Users with SPNs Using PowerView

**Context**: This step uses PowerView to query the domain for users with SPNs, providing a comprehensive list without requiring the native AD module. It helps identify service accounts suitable for Kerberoasting by filtering on the servicePrincipalName attribute.

**Command** ([[commands/get-domainuser-spn-powerview]]):
```powershell
Get-DomainUser -SPN
```

> This command queries the domain controller for user objects where the servicePrincipalName attribute is populated. It returns details like samAccountName, distinguishedName, and the SPN value. If no users are found, it indicates no Kerberoastable accounts exist or access is insufficient.

### Step 2: Enumerate Domain Users with SPNs Using Native AD Module

**Context**: As an alternative to PowerView, use the built-in Active Directory PowerShell module for enumeration. This is useful if PowerView is not loaded or for environments with restricted scripting. It filters users where ServicePrincipalName is not null and retrieves the SPN properties.

**Command** ([[commands/get-aduser-filter-spn-powershell]]):
```powershell
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

> The command lists users with SPNs, showing their names and associated SPNs. Compare the output with Step 1 to ensure consistency. Success is indicated by a list of users; pipe to Select-Object for cleaner output if needed (e.g., | Select Name, ServicePrincipalName).

### Step 3: Identify Domain Admin Accounts with SPNs Using PowerView

**Context**: Focus on high-privilege targets by filtering the SPN users for membership in the Domain Admins group. This step helps prioritize cracking efforts on accounts that could yield domain dominance if compromised.

**Command** ([[commands/get-netuser-spn-filter-domain-admins-powerview]]):
```powershell
Get-NetUser -SPN | Where-Object {$_.memberof -match 'Domain Admins'}
```

> This pipes the SPN users through a filter checking group membership. If any results appear, note the usernames for immediate targeting. No output means no admin-level Kerberoastable accounts, reducing risk but still warranting checks on other service accounts.

### Step 4: Request TGS Hashes for SPN Users Using Impacket

**Context**: Once SPN users are identified, request their TGS tickets (containing RC4/NTLM hashes) from the Domain Controller. This uses domain credentials to authenticate and extract crackable hashes in a format suitable for tools like Hashcat.

**Command** ([[commands/getuser-spns-query-domain-and-request-hashes]]):
```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
```

> Replace placeholders with actual values (e.g., DOMAIN=corp.local, USERNAME=attacker, PASSWORD=pass123, DOMAIN_IP=10.0.0.10). The -request flag triggers TGS ticket requests. Output includes $krb5tgs$ hashes; save them to a file for cracking. If requests fail, verify credentials and DC connectivity.

### Step 5: Request RC4 Hash for Specific SPN User Using Rubeus (Optional)

**Context**: For targeted requests on a single user, use Rubeus to perform Kerberoasting with RC4 opsec considerations, minimizing detectable events. This is useful for stealthy operations or when Impacket is unavailable.

**Command** ([[commands/rubeus-kerberoast-rc4-user]]):
```cmd
Rubeus.exe kerberoast /user:$_USERNAME /simple /rc4opsec /outfile:C:\hashes.txt
```

> Specify the target username (e.g., svc-mssql). The /rc4opsec flag requests only RC4-encrypted tickets to reduce AES usage logs. Output is saved to the specified file in crackable format. Verify the file contains the hash; if not, check for execution policy restrictions on the endpoint.
