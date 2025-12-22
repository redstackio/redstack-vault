---
id: bb9bf9ec-dfdc-4ebf-9d0e-b463679db0da
name: Enumerate-Domain-GPOs-Containing-LAPS
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T19:13:43.796117+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Permission Groups Discovery]]'
sub_techniques: []
tags:
  - enumeration
  - discovery
  - laps
commands:
  - '[[commands/Get-DomainGPO-LAPS-Filter]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
validated: true
---

# Enumerate-Domain-GPOs-Containing-LAPS

## Summary

This procedure uses PowerView to query Active Directory for Group Policy Objects (GPOs) whose display names contain 'LAPS', allowing attackers to identify policies related to Local Administrator Password Solution (LAPS) configurations. LAPS automates the management of local admin passwords in a domain, and enumerating these GPOs can reveal sensitive credential management details or lead to further discovery of administrative accounts.

## Description

In a Windows domain environment, LAPS is often implemented via GPOs to enforce password rotation and storage of local admin credentials in AD attributes. Attackers with domain access can enumerate GPOs to find those configured for LAPS, potentially extracting policy details or linked credentials. This technique falls under permission groups discovery as it helps map administrative policy structures. It requires domain-joined access or valid credentials for AD querying and is typically used during reconnaissance to understand credential management practices.

## Requirements

1. Valid domain user credentials with read access to AD objects (e.g., domain user or higher).
2. PowerShell execution policy allowing script execution (Bypass or Unrestricted).
3. PowerView module loaded in the current PowerShell session.
4. Network connectivity to a domain controller for AD queries.

## Defense

Defensive measures and detection strategies:

- Monitor PowerShell execution logs for imports of PowerView or similar modules (Event ID 4104 in PowerShell logs).
- Implement LAPS with restricted read access to ms-Mcs-AdmPwd attributes using ACLs.
- Use tools like BloodHound or AD auditing to detect anomalous GPO queries.
- Enable Advanced Audit Policy for directory service access (Event ID 4662) to log AD enumeration attempts.

## Objectives

1. Identify GPOs associated with LAPS to understand local admin password management.
2. Extract GPO names, display names, and file system paths for further analysis.
3. Map domain policy structures that may contain embedded credentials or configurations.
4. Validate success by confirming LAPS-related policies are present and accessible.

## Instructions

### Step 1: Load PowerView and Query GPOs

**Context**: First, ensure PowerView is imported into your PowerShell session. Then, execute a filtered query on all domain GPOs to find those with 'LAPS' in the display name. This step reveals policy details without alerting basic logging, as it's a standard AD query.

**Command** ([[commands/Get-DomainGPO-LAPS-Filter]]):
```powershell
Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name, GPCFileSysPath | fl
```

> This command retrieves all GPOs, filters by display name containing 'laps' (case-insensitive wildcard), and selects key attributes: DisplayName (user-friendly name), Name (GUID-based internal name), and GPCFileSysPath (file system path for policy files). If successful, it outputs formatted details for each matching GPO. If no matches, it returns empty output, indicating no LAPS policies or insufficient permissions.

### Step 2: Analyze Output for Further Actions

**Context**: Review the output to identify the GPO paths. If LAPS is configured, the GPCFileSysPath can be accessed (with appropriate permissions) to inspect policy XML files for credential-related settings. Decision point: If paths are accessible, proceed to manual inspection; otherwise, escalate privileges.

No specific command here; use file explorer or PowerShell to navigate to GPCFileSysPath (e.g., `\domain.com\SYSVOL\domain.com\Policies\{GUID}\`).

> Expected: Access to policy files revealing LAPS settings like password age or storage attributes. If access denied, this indicates restricted permissions on SYSVOL.
