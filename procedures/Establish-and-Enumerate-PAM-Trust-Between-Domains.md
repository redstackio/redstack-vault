---
id: 3e174a7f-c32d-4fda-9589-e6ae6c8a5b76
name: Establish-and-Enumerate-PAM-Trust-Between-Domains
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.399531+00:00'
updated_at: '2023-04-10T20:26:01.490587+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Privileged Access Management (PAM) Trust]]'
commands:
  - '[[commands/netdom-trust-create-transitive]]'
  - '[[commands/netdom-trust-enable-pam-options]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Establish-and-Enumerate-PAM-Trust-Between-Domains

## Summary

This procedure outlines how to establish a Privileged Access Management (PAM) trust relationship between two Active Directory domains (e.g., lab.local and bastion.local) using netdom commands, enabling transitive trusts with SID history and PIM support for lateral movement and privileged access. It also covers enumeration of the trust, shadow security principals, and bastion forest management using PowerShell to verify the configuration and identify exploitable trust attributes.

## Description

In Active Directory environments, establishing a PAM trust allows controlled access to privileged accounts and resources across domains or forests, often used in hybrid setups like bastion forests for just-in-time administration. An attacker with domain admin privileges on one domain can create such a trust to facilitate lateral movement, pass-the-ticket attacks, and discovery of shadow principals that map privileged identities. The process involves creating a forest-transitive trust without quarantine (disabling SID filtering), enabling SID history for seamless access, and activating PIM trust for managed privileged access. Once established, enumeration reveals trust attributes like Trust_Attribute_PIM_Trust and Trust_Attribute_Treat_As_External, enabling further exploitation. This technique targets domain controllers and requires high privileges, making it suitable for post-compromise scenarios in enterprise networks. Expected outcomes include successful trust creation verifiable via AD queries, allowing access to resources in the trusted domain without additional authentication.

## Requirements

1. Domain Administrator credentials on both lab.local and bastion.local domain controllers.
2. Direct console or RDP access to the domain controllers to execute netdom commands.
3. Active Directory PowerShell module installed (Import-Module ActiveDirectory) for enumeration.
4. Network connectivity between the domains for trust establishment.

## Defense

- Monitor domain controller event logs for trust creation events (e.g., Event ID 4624 for logons, 5136 for directory service changes) and netdom.exe execution via Sysmon or EDR.
- Enforce SID filtering (quarantine) on all trusts and require explicit approval for trust changes through change management processes.
- Limit netdom and PowerShell AD module usage to bastion hosts with just-in-time privileges; audit AD object queries for shadow principals.
- Implement network segmentation to isolate domain controllers and use Privileged Access Workstations (PAWs) for admin tasks.

## Objectives

1. Create a bidirectional forest-transitive PAM trust between lab.local and bastion.local with SID history and PIM enabled.
2. Disable quarantine to allow unrestricted access across domains.
3. Enumerate trust attributes, shadow security principals, and bastion management flags to confirm exploitability.
4. Verify success through AD queries showing transitive trusts without SID filtering.

## Instructions

### Step 1: Establish Transitive Trust from lab.local to bastion.local

**Context**: On the lab.local domain controller, create the initial forest-transitive trust to bastion.local. This enables propagation across the forest and is a prerequisite for additional PAM options.

**Command** ([[commands/netdom-trust-create-transitive]]):
```cmd
netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes
```

> This command establishes a transitive trust, allowing authentication requests to flow across the entire forest. Run as domain admin. Expected output includes a success message confirming the trust creation. If the domains are in different forests, ensure DNS resolution is configured.

### Step 2: Enable PAM Options for lab.local Trust

**Context**: Still on the lab.local domain controller, apply SID history, PIM trust, and disable quarantine to fully enable PAM features, allowing legacy permissions and privileged management without isolation.

**Command** ([[commands/netdom-trust-enable-pam-options]]):
```cmd
netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes
netdom trust lab.local /domain:bastion.local /EnablePIMTrust:Yes
netdom trust lab.local /domain:bastion.local /Quarantine:No
```

> These sequential commands enhance the trust: /EnableSIDHistory preserves user SIDs for access to old resources; /EnablePIMTrust activates privileged identity management; /Quarantine:No disables SID filtering for full access. Each should output a success confirmation. Decision point: If errors occur (e.g., existing trust), use /verify or /reset first.

### Step 3: Establish Transitive Trust from bastion.local to lab.local

**Context**: On the bastion.local domain controller, create the reciprocal transitive trust to complete the bidirectional relationship.

**Command** ([[commands/netdom-trust-create-transitive]]):
```cmd
netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
```

> This mirrors Step 1 on the opposite side, ensuring mutual trust. Expected output is a success message. No additional PAM options are needed on this side for basic PAM setup.

### Step 4: Enumerate and Verify PAM Trust Configuration

**Context**: On any domain-joined machine in either forest with AD PowerShell, import the module and run queries to detect PAM trusts, list shadow principals, and check bastion attributes. This verifies success and identifies exploitable elements like non-quarantined transitive trusts.

**Code** ([[codes/PowerShell-Enumerate-AD-PAM-Trusts-and-Shadow-Principals]]):
```powershell
# Detect if current forest is PAM trust
Import-Module ActiveDirectory
Get-ADTrust -Filter {(ForestTransitive -eq $True) -and (SIDFilteringQuarantined -eq $False)}

# Enumerate shadow security principals 
Get-ADObject -SearchBase ("CN=Shadow Principal Configuration,CN=Services," + (Get-ADRootDSE).configurationNamingContext) -Filter * -Properties * | select Name,member,msDS-ShadowPrincipalSid | fl

# Enumerate if current forest is managed by a bastion forest
# Trust_Attribute_PIM_Trust + Trust_Attribute_Treat_As_External
Get-ADTrust -Filter {(ForestTransitive -eq $True)} 
```

> First, import the AD module if not loaded. The Get-ADTrust filter identifies transitive, non-quarantined trusts indicative of PAM. The Get-ADObject query lists shadow principals (e.g., names, members, SIDs) that map bastion admins to local groups. The final query shows all transitive trusts; inspect attributes for PIM_Trust (0x800) and Treat_As_External (0x2000) flags. Expected output: List of trusts with properties like Direction: Bidirectional, TrustType: Forest, and shadow objects if configured. Success if lab.local-bastion.local trust appears without quarantine.
