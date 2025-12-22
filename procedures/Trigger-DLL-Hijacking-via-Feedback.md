---
id: trigger-dll-hijack-001
tags:
  - dll-hijacking
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:29:20.094Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Trigger-DLL-Hijacking-via-Feedback

## Summary

This procedure triggers the DLL hijacking by interacting with the Acronis True Image feedback feature, causing report_sender.exe to load the malicious DLL from the PATH and execute code as Administrator.

## Description

Opening the feedback form and submitting it launches report_sender.exe, which fails to find required DLLs and loads from insecure PATH locations, executing the payload. This can occur automatically on crashes. Target environment is Windows with Acronis installed; no special credentials needed beyond local access.

## Requirements

1. Malicious DLL prepared and placed (from prior procedure)
2. Acronis True Image 2021 installed and accessible
3. Local user session

## Defense

Defensive measures and detection strategies:

- Disable automatic crash reporting
- Implement application whitelisting to restrict unsigned DLL loads
- Log and alert on unexpected process creations from backup software

## Objectives

1. Initiate the vulnerable feature
2. Load and execute the hijacked DLL
3. Gain Administrator shell

## Instructions

### Step 1: Launch Acronis and Access Feedback

**Context**: Open the application and navigate to the trigger point.

Manually launch via Start menu or executable.

Navigate to Help > Send feedback.

> Expected output: Feedback form dialog appears.

### Step 2: Submit Feedback to Execute

**Context**: Provide minimal input to trigger submission and DLL load.

Fill in any required fields (e.g., description) and click Send.

> This executes report_sender.exe, loads ubsec.dll, and spawns cmd.exe as Admin. Expected output: Elevated cmd.exe window opens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow: DLL Search Order Hijacking

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[dll-hijacking]]
- [[feedback-trigger]]
