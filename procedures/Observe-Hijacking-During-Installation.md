---
id: proc-acronis-observe-hijack
tags:
  - file-access
  - vulnerability-discovery
  - windows
type: procedure
tools:
  - '[[tools/Procmon]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:51.492Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Observe-Hijacking-During-Installation

## Summary

This procedure runs the Acronis installer under monitoring to capture and analyze file access attempts, specifically identifying the hijackable 'C:\program.exe' path via Procmon logs.

## Description

During the installation of Acronis True Image 2021, the subprocess 'atih_installer_shell_standard.exe' performs a CreateFile operation on 'C:\program.exe', resulting in 'NAME NOT FOUND' if absent. This reveals a path hijacking opportunity. The procedure assumes Procmon is already configured and focuses on execution and log review in a controlled environment.

## Requirements

1. Downloaded AcronisTrueImage2021.exe ready.
2. Procmon running with appropriate filters.
3. Elevated privileges for installer execution.

## Defense

Defensive measures and detection strategies:

- Implement path validation in installers to avoid root directory searches.
- Use behavioral analytics in EDR to flag installer processes accessing unusual paths.
- Regularly audit installer behaviors with tools like Procmon in secure environments.

## Objectives

1. Trigger the vulnerable file access during installation.
2. Log and verify the exact path and operation.
3. Confirm exploitability without placing a payload.

## Instructions

### Step 1: Start the Installation

**Context**: Launch the installer to initiate the subprocess and trigger file operations.

Run the executable:

Right-click AcronisTrueImage2021.exe > Run as administrator

> Expected output: Installation wizard opens; Procmon begins logging events.

### Step 2: Review Procmon Logs

**Context**: Stop capture after key events and filter logs for the target path.

In Procmon: Ctrl+E to stop, then search for 'program.exe' or filter on Path contains 'C:\program.exe'

> Expected output: Event details showing CreateFile on 'C:\Program.exe' with Result 'NAME NOT FOUND' and Process 'atih_installer_shell_standard.exe'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Procmon]]

## Tags

- [[file-access]]
- [[vulnerability-discovery]]
