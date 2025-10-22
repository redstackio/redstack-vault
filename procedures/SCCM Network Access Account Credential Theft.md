---
id: e3fd9f63-6f7d-4916-92dc-48d3a40f2936
name: SCCM Network Access Account Credential Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.245825+00:00'
updated_at: '2023-04-10T20:26:02.182056+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[SCCM Network Access Accounts]]'
commands:
- '[[Get SCCM Data]]'
- '[[Retrieve Network Access Account Configuration]]'
- '[[Retrieve SCCM Credentials]]'
---

# SCCM Network Access Account Credential Theft

## Summary

This procedure involves the theft of SCCM network access account credentials. By using SCCM Blob Finder and SCCM Credential Retrieval, an attacker can retrieve the credentials of SCCM network access accounts stored in the SCCM database. These credentials can then be used to gain access to other sys

## Description

# Description

This procedure involves the theft of SCCM network access account credentials. By using SCCM Blob Finder and SCCM Credential Retrieval, an attacker can retrieve the credentials of SCCM network access accounts stored in the SCCM database. These credentials can then be used to gain access to other systems and data within the network. This attack can be particularly damaging as SCCM network access accounts often have elevated privileges within the network. 

From a technical perspective, SCCM Blob Finder and SCCM Credential Retrieval are used to query the SCCM database for network access account credentials. Check CIM Repository ACL is used to ensure that the attacker has the necessary permissions to perform these queries. 

The business value of this attack lies in the ability of the attacker to gain access to sensitive data and systems within the network. This can lead to data theft, system compromise, and reputational damage.

## Requirements

1. Access to the SCCM database

1. Permissions to perform queries using SCCM Blob Finder and SCCM Credential Retrieval

1. Permissions to check CIM Repository ACL

## Defense

1. Limit access to the SCCM database to only authorized personnel

1. Implement multi-factor authentication for SCCM network access accounts

1. Regularly review and update permissions for SCCM network access accounts

## Objectives

1. Retrieve SCCM network access account credentials

1. Gain access to other systems and data within the network

# Instructions

1. This command is used to find SCCM blob.

**Code**: [[Get-Wmiobject -namespace "root\ccm\policy\Machine\]]

> The SCCM blob contains important data related to SCCM policies and configurations. This command retrieves the SCCM blob by querying the WMI object 'CCM_NetworkAccessAccount' in the namespace 'root\ccm\policy\Machine\ActualConfig'. The NetworkAccessPassword and NetworkAccessUsername fields in the output contain the encrypted SCCM blob data.

**Command** ([[Retrieve Network Access Account Configuration]]):

```bash
Get-Wmiobject -namespace \"root\ccm\policy\Machine\ActualConfig\" -class \"CCM_NetworkAccessAccount\"\nNetworkAccessPassword : <![CDATA[E600000001...8C6B5]]>\nNetworkAccessUsername : <![CDATA[E600000001...00F92]]>
```

2. To use this command, run the following command in PowerShell: .\SharpDPAPI.exe SCCM
.\SharpSCCM.exe get naa -u USERNAME -p PASSWORD

**Code**: [[.\SharpDPAPI.exe SCCM
.\SharpSCCM.exe get naa -u U]]

> This command can be used to retrieve and decrypt SCCM credentials. The command uses two tools, SharpDPAPI and SharpSCCM, to perform the retrieval and decryption. The 'naa' argument specifies the type of SCCM credential to retrieve. The 'USERNAME' and 'PASSWORD' arguments should be replaced with the actual SCCM username and password. Once the command is run, the decrypted credentials will be displayed in the output.

**Command** ([[Retrieve SCCM Credentials]]):

```bash
.\SharpDPAPI.exe SCCM
```

**Command** ([[Get SCCM Data]]):

```bash
.\SharpSCCM.exe get naa -u USERNAME -p PASSWORD
```

3. Run the following command in PowerShell:

**Code**: [[Get-Acl C:\Windows\System32\wbem\Repository\OBJECT]]

> This command retrieves the Access Control List (ACL) for the CIM repository file located at the specified path. The ACL determines which users and groups have access to the file and what level of access they have. The `Format-List` cmdlet is used to display the results in a list format, including the path to the file and the Security Descriptor Definition Language (SDDL) string that represents the ACL. The `ConvertFrom-SddlString` cmdlet can be used to convert the SDDL string into a more readable format.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Get SCCM Data]]
- [[Retrieve Network Access Account Configuration]]
- [[Retrieve SCCM Credentials]]

## Tags

- [[Active Directory Attacks]]
- [[SCCM Network Access Accounts]]
