---
id: bf89f1ce-c7d1-4d67-bfcb-c357616d641e
name: Password-of-Pre-Created-Computer-Account-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.471172+00:00'
updated_at: '2023-04-10T20:26:27.409776+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account-Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Password-of-Pre-Created-Computer-Account]]'
commands:
  - '[[commands/set-adcomputer-modify-samaccountname]]'
  - '[[commands/netdom-join-domain-with-prew2k]]'
  - '[[commands/djoin-provision-with-default-password]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Password-of-Pre-Created-Computer-Account-Attack

## Summary

The Password of Pre-Created Computer Account Attack involves modifying or provisioning Active Directory computer accounts to use weak or default passwords, allowing attackers to authenticate as those accounts for persistence, privilege escalation, or lateral movement. This technique targets pre-created computer objects in AD, exploiting insecure configurations to gain domain controller access and dump credentials.

## Description

In Active Directory environments, pre-created computer accounts can be manipulated to assign pre-Windows 2000 compatible names or provisioned with default passwords, making them vulnerable to compromise. Attackers with domain admin privileges or equivalent can alter the SAM account name to a format like DOMAIN\ComputerName$, enabling unauthorized joins or usage of the account's password. Alternatively, the djoin tool can provision new machines with a default password that is easily guessable or known. Once compromised, these accounts provide valid credentials for accessing domain controllers, escalating privileges, and moving laterally. This is particularly effective in legacy or misconfigured AD setups where strong password policies are not enforced on computer accounts. The attack assumes the attacker has initial foothold with sufficient privileges to modify AD objects.

## Requirements

1. Domain-joined Windows machine with administrative privileges (e.g., Domain Admin) to modify AD objects.
2. Knowledge of the target pre-created computer account name or desired machine name.
3. Active Directory PowerShell module installed for Set-ADComputer (or RSAT tools).
4. Network access to a domain controller for AD modifications and provisioning.
5. Tools like Password Cracking software (e.g., Hashcat) if the default password needs offline cracking, though defaults are often known.

## Defense

- Implement least privilege access: Restrict AD modifications to approved admins only and monitor changes to computer objects.
- Enforce strong, unique, and frequently rotated passwords for computer accounts using Group Policy.
- Enable auditing for account creation/modification events (Event ID 4720, 4738) and alert on suspicious changes like pre-W2K name assignments.
- Use tools like Microsoft Defender for Identity to detect anomalous AD activities, such as provisioning with default passwords.
- Regularly review and disable unused pre-created computer accounts.

## Objectives

1. Modify or create a computer account with a weak/default password to establish persistence.
2. Authenticate as the compromised computer account to access domain controllers.
3. Escalate privileges and perform lateral movement using the account's credentials.
4. Dump credentials from the domain controller for further compromise.
5. Access sensitive data across the network.

## Instructions

### Step 1: Modify Existing Computer Account SAM Account Name for Pre-Windows 2000 Compatibility

**Context**: This step alters a pre-created computer account's SAM account name to a pre-Windows 2000 format (e.g., DOMAIN\ComputerName$), which can facilitate unauthorized domain joins or exploitation of legacy authentication. This is performed using PowerShell's Active Directory module to directly modify the object in AD. The change allows the account to be used with potentially weak passwords in legacy contexts.

**Command** ([[commands/set-adcomputer-modify-samaccountname]]):
```powershell
Set-ADComputer -Identity $_COMPUTERNAME -SamAccountName $_SAMACCOUNTNAME
```

> This command updates the specified computer account. The -Identity parameter identifies the target computer by name, DN, GUID, or SID. The -SamAccountName sets the pre-W2K compatible name in the format NetBIOSDomainName\ComputerName$. Run this from a domain-joined machine with AD module loaded. If successful, the account is now modifiable for weak password assignment.

**Expected Output**: No output if successful; use Get-ADComputer to verify the change: "SAMAccountName : CONTOSO\Win10Comp$".

### Step 2: Join the Computer to the Domain Using the Pre-Windows 2000 Name

**Context**: After modifying the SAM account name, join the target machine to the domain specifying the pre-W2K name. This leverages the altered account to establish a session with potentially default or weak credentials, enabling further access. Netdom.exe is used for this legacy-compatible join operation.

**Command** ([[commands/netdom-join-domain-with-prew2k]]):
```cmd
netdom.exe join /domain:$_DOMAIN /ou:$_OU /preW2K:$_PREW2KNAME
```

> Execute this from the target machine or a management station. The /domain specifies the FQDN, /ou the target OU, and /preW2K the pre-Windows 2000 name (e.g., CONTOSO\Win10Comp$). This joins the computer using the modified account, potentially bypassing stricter checks if the password is known or default.

**Expected Output**: "The command completed successfully." The machine is now domain-joined under the pre-W2K account.

### Step 3: Provision a New Machine Account with Default Password

**Context**: For creating a new compromised account, use djoin to provision a machine offline or from a domain-joined device, setting a default password that is insecure and known (e.g., initial random but printable via /PRINTBLOB). This creates a backdoor account for later use in persistence or lateral movement. Run from a domain-joined device connected to the DC.

**Command** ([[commands/djoin-provision-with-default-password]]):
```cmd
djoin /PROVISION /DOMAIN $_DOMAIN /MACHINE $_MACHINENAME /SAVEFILE $_SAVEFILE /DEFPWD /PRINTBLOB /NETBIOS $_NETBIOS
```

> Replace placeholders: /DOMAIN with FQDN (e.g., contoso.com), /MACHINE with name (e.g., evilpc), /SAVEFILE with path (e.g., C:\temp\evilpc.txt), /NETBIOS with short name. The /DEFPWD sets a default password, /PRINTBLOB outputs the password blob for retrieval. This provisions the account in AD with the weak password.

**Expected Output**: Provisioning blob printed to console, including the machine password hash. The file contains the blob for offline join if needed. Verify with Get-ADComputer -Identity evilpc$.

**Success Indicators**:
- AD object modified or created successfully without errors.
- Password blob or default password retrievable for use.
- Account authenticates to domain services (test with kinit or similar).
