---
id: 4607a28e-dc06-4fe6-b85f-79cfa8107786
name: Sync-Local-Clock-with-Remote-Domain-Controller
type: procedure
verified: true
submitted: false
created_at: '2020-06-25T00:16:01.552025+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Time Discovery]]'
sub_techniques: []
tags:
  - setup
  - windows
  - active-directory
  - time-sync
commands:
  - '[[commands/net-display-remote-server-time]]'
  - '[[commands/net-sync-local-time-with-remote-server]]'
platforms:
  - Windows
tools: []
validated: true
---

# Sync-Local-Clock-with-Remote-Domain-Controller

## Summary

This procedure synchronizes the local Windows system's clock with a remote domain controller using the SMB service, ensuring accurate time alignment necessary for Kerberos authentication and other time-sensitive operations in Active Directory environments.

## Description

In Active Directory domains, time synchronization is critical for validating Kerberos tickets and preventing authentication failures due to clock skew. This procedure uses the built-in Windows 'net time' command to query and set the local system time based on a remote domain controller's SMB service. It is typically used during red team setups to maintain domain compatibility or in post-exploitation to align timestamps for evasion. The process involves first displaying the remote time for verification and then syncing the local clock. This assumes network access to the domain controller over SMB (port 445) and appropriate permissions.

## Requirements

1. Network connectivity to the target domain controller over SMB (TCP/445).
2. Local administrator privileges on the target Windows system (for time synchronization).
3. Windows operating system (Server or Workstation editions in a domain environment).
4. Domain-joined system or valid credentials for SMB access.

## Defense

Defensive measures and detection strategies:

- Monitor SMB traffic for unusual 'net time' queries from non-domain controllers using network logs (e.g., Windows Event ID 5145 for share access).
- Enable Windows Time Service (W32Time) auditing to detect manual time adjustments (Event ID 29 in System log).
- Implement group policy to restrict time synchronization to trusted NTP sources only.
- Use endpoint detection tools to alert on 'net time' command executions outside of automated services.

## Objectives

1. Verify the current time on the remote domain controller.
2. Align the local system clock with the domain controller to within acceptable skew (typically 5 minutes for Kerberos).
3. Ensure seamless authentication in Active Directory without time-based errors.

## Instructions

### Step 1: Display Remote Server Time

**Context**: Query the remote domain controller to retrieve its current time via SMB, allowing verification before synchronization. This step confirms connectivity and displays the reference time.

**Command** ([[commands/net-display-remote-server-time]]):

```cmd
net time \\$_TARGET_IP /QUERY
```

> This command connects to the specified domain controller IP and queries its time. Replace $_TARGET_IP with the IP or hostname of the domain controller (e.g., 192.168.1.10). Expected output includes the current date and time from the remote server, confirming successful SMB access.

### Step 2: Sync Local Time with Remote Server

**Context**: Set the local system's clock to match the remote domain controller's time, resolving any discrepancies that could impact domain operations.

**Command** ([[commands/net-sync-local-time-with-remote-server]]):

```cmd
net time \\$_TARGET_IP /SET
```

> This command synchronizes the local clock using the remote server's time as the source. Replace $_TARGET_IP with the domain controller's IP or hostname. Expected output confirms the time has been set successfully, with the local clock now aligned.
