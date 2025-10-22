---
id: 238c2626-b828-4d71-b733-43f010f64af7
name: Abusing Active Directory ACLs/ACEs to Retrieve GMSA Password
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.966448+00:00'
updated_at: '2023-04-10T20:26:00.803442+00:00'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[ReadGMSAPassword]]'
commands:
- '[[Get Object Attributes for GMSA Account]]'
---

# Abusing Active Directory ACLs/ACEs to Retrieve GMSA Password

## Summary

Abusing Active Directory ACLs/ACEs to Retrieve GMSA Password is a technique used by attackers to obtain the password of a Group Managed Service Account (GMSA) in an Active Directory environment. This technique involves abusing the access control lists (ACLs) and access control entries (ACEs) of obj

## Description

# Description

Abusing Active Directory ACLs/ACEs to Retrieve GMSA Password is a technique used by attackers to obtain the password of a Group Managed Service Account (GMSA) in an Active Directory environment. This technique involves abusing the access control lists (ACLs) and access control entries (ACEs) of objects in Active Directory to gain access to sensitive information. By using the DSInternals tool, an attacker can retrieve the password of a GMSA account and use it to escalate privileges or move laterally within the network.

From a technical standpoint, this technique involves manipulating the access control lists and access control entries of objects in Active Directory to grant an attacker the necessary permissions to retrieve the password of a GMSA account. This can be achieved by modifying the permissions of the object that the GMSA is associated with or by creating a new object with the necessary permissions.

The business value of this technique for an attacker is that it allows them to obtain the password of a GMSA account, which can be used to escalate privileges or move laterally within the network. It can also be used to gain access to sensitive information that is stored using the GMSA account.

## Requirements

1. Access to an Active Directory environment

1. DSInternals tool

## Defense

1. Limit the permissions of objects in Active Directory to only those that are necessary

1. Monitor Active Directory for changes to ACLs/ACEs

1. Use strong passwords for GMSA accounts and rotate them regularly

## Objectives

1. Retrieve the password of a GMSA account

1. Escalate privileges or move laterally within the network

1. Gain access to sensitive information stored using the GMSA account

# Instructions

1. To read the GMSA password of an account, use the following PowerShell commands:

**Code**: [[# Save the blob to a variable
$gmsa = Get-ADServic]]

> 1. Get-ADServiceAccount -Identity 'SQL_HQ_Primary' -Properties 'msDS-ManagedPassword': This command retrieves the msDS-ManagedPassword property of the specified GMSA account.
2. $mp = $gmsa.'msDS-ManagedPassword': This command saves the msDS-ManagedPassword property to the $mp variable.
3. ConvertFrom-ADManagedPasswordBlob $mp: This command decodes the $mp variable using the DSInternals module, revealing the GMSA password.

2. To retrieve the managed password for a gMSA account, use the getObjectAttributes command with the gmsaAccount$ and msDS-ManagedPassword arguments.

**Code**: [[python bloodyAD.py -u john.doe -d bloody -p Passwo]]

> -u: The username used to authenticate to the domain. 
-d: The name of the domain. 
-p: The password for the user account. 
--host: The IP address or hostname of the domain controller. 
gmsaAccount$: The name of the gMSA account to retrieve the managed password for. 
msDS-ManagedPassword: The attribute used to store the managed password for the gMSA account.

**Command** ([[Get Object Attributes for GMSA Account]]):

```bash
python bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes gmsaAccount$ msDS-ManagedPassword
```

## Commands Used

- [[Get Object Attributes for GMSA Account]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[ReadGMSAPassword]]
