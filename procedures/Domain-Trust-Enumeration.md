---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Domain and Trust Discovery|T1482 - System Domain and
    Trust Discovery]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Enumerate trusts between domains]]'
  - '[[tags/Trust relationship between domains]]'
commands:
  - '[[commands/nltest-list-trusted-domains]]'
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# Domain-Trust-Enumeration

## Summary

Domain Trust Enumeration identifies trust relationships between domains in an Active Directory environment, enabling attackers to map potential paths for lateral movement across trusted domains. This procedure uses native Windows tools like nltest and PowerShell to query domain trusts without requiring additional software.

## Description

In Active Directory, trust relationships allow authentication and resource access between domains. Enumerating these trusts reveals interconnected domains, which attackers can exploit for privilege escalation or movement. This technique targets domain controllers or authenticated domain-joined systems and is commonly used during reconnaissance in multi-domain environments. It assumes the attacker has domain user credentials and network access to a domain controller. Outcomes include lists of trusted domains, trust types (e.g., bidirectional, one-way), and directions, aiding in planning attacks like pass-the-hash across trusts.

## Requirements

1. Authenticated access to an Active Directory domain (domain user credentials required).
2. Network connectivity to a domain controller or domain-joined Windows host.
3. Windows operating system (Server 2008 or later) with PowerShell enabled.
4. No elevated privileges needed, but domain admin access enhances results.

## Defense

Defensive measures and detection strategies:

- Monitor Active Directory queries via Event ID 4662 (object access) and 5136 (directory service changes) in Windows Security logs.
- Implement network segmentation to limit lateral movement between domains.
- Use tools like Microsoft Defender for Identity to detect anomalous trust enumerations.
- Regularly audit and minimize unnecessary trust relationships using Active Directory Domains and Trusts console.

## Objectives

1. Identify all trusted domains connected to the current domain.
2. Enumerate detailed trust relationships, including types and directions.
3. Map potential lateral movement targets for further exploitation.

## Instructions

### Step 1: List Trusted Domains Using nltest

**Context**: This step uses the native nltest utility to quickly list all domains trusted by the current domain, providing an initial overview of trust relationships. It queries the local system's secure channel to the domain controller and is useful for verifying basic trust connectivity.

**Command** ([[commands/nltest-list-trusted-domains]]):
```cmd
nltest /trusted_domains
```

> The nltest command tests trust relationships and lists trusted domains. Run this from an elevated Command Prompt on a domain-joined machine. If successful, it displays a list of trusted domain names. This step confirms if trusts exist and helps identify immediate neighbors for deeper enumeration.

### Step 2: Enumerate All Trust Relationships Using PowerShell

**Context**: For a more detailed view, this step leverages PowerShell's Active Directory .NET classes to retrieve comprehensive trust information, including source/target domains, trust types (e.g., TreeRoot, Forest), and directions (e.g., Bidirectional). This is essential for understanding the full topology and planning cross-domain attacks.

**Code** ([[codes/powershell-get-all-trust-relationships]]):
```powershell
([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()
```

> Execute this in PowerShell on a domain-joined system with domain authentication. The output includes columns for SourceName, TargetName, TrustType, and TrustDirection. Verify success by checking for listed relationships; empty output may indicate no external trusts or insufficient permissions. Use this data to identify exploitable one-way trusts.
