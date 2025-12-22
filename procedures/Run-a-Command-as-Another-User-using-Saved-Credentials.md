---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Defense Evasion]]'
  - '[[Initial Access]]'
  - '[[Persistence]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - access-control
  - authentication
commands:
  - '[[commands/runas-execute-command-with-saved-credentials]]'
platforms:
  - Windows
tools: []
validated: true
---

# Run-a-Command-as-Another-User-using-Saved-Credentials

## Summary

This procedure uses the built-in Windows runas.exe utility to execute a command or program as another user by leveraging previously saved credentials in the Windows Credential Manager. It bypasses the interactive password prompt, which is particularly useful in remote shell environments like netcat or PowerShell remoting where standard input prompts may not function correctly. This technique allows for privilege escalation or lateral movement using valid domain or local accounts without re-entering credentials each time.

## Description

The runas.exe command is a native Windows tool designed to run programs under alternate user credentials, supporting both local and domain accounts. In typical usage, it prompts for a password, but the /savedcred switch enables execution using credentials stored via the Credential Manager (accessible through runas /savecred initially or Windows UI). This is essential in non-interactive scenarios, such as remote access tools, where password input cannot be provided. Prior to using /savedcred, credentials must be saved once interactively. The procedure maps to MITRE ATT&CK technique T1078 (Valid Accounts), enabling defense evasion, initial access, persistence, and privilege escalation by impersonating legitimate users. It requires administrative rights to save credentials initially and works on Windows systems with Credential Manager enabled.

## Requirements

1. Windows operating system (tested on Windows 7+).
2. Previously saved credentials for the target user in Windows Credential Manager (use runas /savecred once interactively to store them).
3. Command prompt or PowerShell access on the target machine.
4. The target user account must have appropriate permissions to execute the desired command.
5. In remote scenarios, ensure the shell supports subprocess spawning (e.g., avoid pure netcat without enhancements).

## Defense

- Monitor process creation events for runas.exe executions via Sysmon or Windows Event Logs (Event ID 4688), filtering for /savedcred usage.
- Restrict Credential Manager access through Group Policy (Computer Configuration > Administrative Templates > System > Credentials Delegation) to prevent saving of sensitive credentials.
- Implement least privilege: Limit non-admin users from saving domain admin credentials.
- Enable Protected Users group for high-privilege accounts to block credential caching.
- Use application whitelisting (e.g., AppLocker) to restrict runas.exe invocation from unauthorized contexts.

## Objectives

1. Impersonate another user to execute commands without interactive password entry.
2. Facilitate lateral movement or privilege escalation in remote sessions.
3. Maintain access using valid accounts while evading detection from password prompts.

## Instructions

### Step 1: Verify Saved Credentials and Execute Command

**Context**: Before running the command, ensure credentials for the target user (e.g., DOMAIN\Administrator) are saved in Credential Manager. This step uses runas.exe with the /savedcred flag to launch the specified command as the alternate user. The /profile flag loads the user's environment variables and profile for accurate execution. If credentials are not saved, the command will fail with an error indicating no saved credentials.

**Command** ([[commands/runas-execute-command-with-saved-credentials]]):
```cmd
runas.exe /profile /user:$_DOMAIN\$_USERNAME /savedcred "$_COMMAND"
```

> This command spawns a new process running $_COMMAND under the context of the specified user. Replace $_DOMAIN with the domain name (or leave blank for local accounts), $_USERNAME with the target username, and $_COMMAND with the full command string (e.g., "powershell.exe -Command 'Get-Process'"). If successful, it executes without prompting for a password and may open a new window or return output directly in the current shell, depending on the command. Verify success by checking if the command's effects occur under the target user's context (e.g., files created with the user's SID). Common errors include "RUNAS ERROR: Unable to run - $_COMMAND" if the path is invalid or "LOGON FAILURE: The user has not been granted the requested logon type" if permissions are insufficient.
