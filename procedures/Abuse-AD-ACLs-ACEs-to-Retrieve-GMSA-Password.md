---
id: 238c2626-b828-4d71-b733-43f010f64af7
name: Abuse-AD-ACLs-ACEs-to-Retrieve-GMSA-Password
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.966448+00:00'
updated_at: '2023-04-10T20:26:00.803442+00:00'
tactics:
  - '[[Credential Access]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - '[[tags/Abusing Active Directory ACLs/ACEs]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/ReadGMSAPassword]]'
  - active-directory
  - gmsa
  - acl-abuse
  - credential-access
commands:
  - '[[commands/Get-GMSA-Object-Attributes-with-BloodyAD]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/DSInternals]]'
  - '[[tools/BloodyAD]]'
validated: true
---

# Abuse-AD-ACLs-ACEs-to-Retrieve-GMSA-Password

## Summary

This procedure details how to retrieve the managed password of a Group Managed Service Account (GMSA) in an Active Directory environment by leveraging misconfigured Access Control Lists (ACLs) and Access Control Entries (ACEs) that grant read permissions to the msDS-ManagedPassword attribute. Attackers with domain user credentials and appropriate read access can use PowerShell with the DSInternals module or the BloodyAD Python tool to extract and decode the password, enabling privilege escalation or lateral movement.

## Description

In Active Directory, GMSAs are used for service authentication with automatically managed passwords stored in the msDS-ManagedPassword attribute. By default, this attribute is protected, but misconfigured ACLs on the GMSA object may allow unauthorized users to read it. This procedure assumes the attacker has identified such a misconfiguration through prior enumeration (e.g., via BloodHound) and possesses credentials with at least GenericRead or specific property read permissions on the GMSA object. The technique involves querying the attribute directly and decoding the blob to reveal the plaintext password. Once obtained, the password can be used to authenticate as the GMSA, which often has elevated privileges on servers or services. This is particularly effective in environments where GMSAs are over-privileged, allowing attackers to impersonate high-value service accounts for persistence or data exfiltration. The target environment is a Windows domain with Active Directory Domain Services (AD DS) and PowerShell remoting or Python execution capabilities.

## Requirements

1. Domain user credentials with read access to the msDS-ManagedPassword attribute on the target GMSA object (via ACL/ACE misconfiguration).
2. Access to a domain-joined Windows host or a machine with network access to a Domain Controller (DC).
3. DSInternals PowerShell module installed for the native method, or BloodyAD Python tool for the alternative approach.
4. PowerShell execution policy allowing script execution, or Python 3.x environment.
5. Knowledge of the target GMSA account name (e.g., from prior enumeration).

## Defense

- Strictly limit ACLs on sensitive AD objects like GMSAs to only necessary principals; use the principle of least privilege and audit custom ACEs regularly.
- Monitor AD for unauthorized attribute reads using tools like Microsoft Advanced Threat Analytics (ATA) or custom auditing on msDS-ManagedPassword.
- Rotate GMSA passwords frequently and use just-in-time (JIT) access where possible; implement Protected Users group to restrict credential exposure.
- Enable DSInternals detection via PowerShell logging (ModuleLogging, ScriptBlockLogging) and monitor for BloodyAD-like LDAP queries.

## Objectives

1. Extract the msDS-ManagedPassword blob from the target GMSA account.
2. Decode the blob to obtain the plaintext GMSA password.
3. Use the retrieved credentials for privilege escalation, lateral movement, or access to GMSA-protected resources.
4. Validate successful retrieval without alerting defensive monitoring.

## Instructions

### Step 1: Retrieve GMSA Password Using DSInternals PowerShell Module

**Context**: This step uses native Active Directory PowerShell cmdlets combined with the DSInternals module to query and decode the managed password blob. It requires the ActiveDirectory module and DSInternals installed on a domain-joined host. The why: Direct AD querying is stealthy if permissions allow, avoiding external tools that might trigger network monitoring.

**Code** ([[codes/Retrieve-GMSA-Password-Using-DSInternals]]):

```powershell
# Save the blob to a variable
$gmsa = Get-ADServiceAccount -Identity 'SQL_HQ_Primary' -Properties 'msDS-ManagedPassword'
$mp = $gmsa.'msDS-ManagedPassword'

# Decode the data structure using the DSInternals module
ConvertFrom-ADManagedPasswordBlob $mp
```

> The Get-ADServiceAccount cmdlet retrieves the GMSA object and its properties from the DC. If successful, it outputs the account details including the blob. The ConvertFrom-ADManagedPasswordBlob function then parses the encrypted blob to reveal the current password, iteration count, and other metadata. Replace 'SQL_HQ_Primary' with the target GMSA name. Expected output includes the plaintext password if decoding succeeds; errors indicate insufficient permissions or module issues.

### Step 2: Retrieve GMSA Object Attributes Using BloodyAD

**Context**: If PowerShell is restricted or for remote execution, use the BloodyAD Python tool to query LDAP attributes over the network. This step targets the msDS-ManagedPassword specifically. The why: Python tools allow operation from non-domain systems and can be more flexible for scripted attacks, bypassing local PowerShell restrictions.

**Command** ([[commands/Get-GMSA-Object-Attributes-with-BloodyAD]]):

```bash
python bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes gmsaAccount$ msDS-ManagedPassword
```

> Authenticate to the DC using provided credentials and retrieve the specified attributes for the GMSA. The output will include the raw msDS-ManagedPassword blob, which can then be decoded offline using tools like DSInternals or custom scripts. Replace placeholders with actual values: username, domain, password, DC host, GMSA name (e.g., gmsaAccount$), and attribute. Success is indicated by the blob being returned without LDAP errors; further decoding is needed for the plaintext password.
