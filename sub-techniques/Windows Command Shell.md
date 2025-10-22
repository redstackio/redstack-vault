---
id: 33b7c8cf-fc43-4dc2-a7e7-989a16b2aa42
name: Windows Command Shell
type: sub-technique
mitre_id: T1059.003
mitre_url: null
created_at: '2023-04-06T00:31:26.981327+00:00'
updated_at: '2023-04-06T00:31:26.981327+00:00'
parent_technique: '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[ASP Razor Server Side Template Injection with C# Command Execution]]'
- '[[Automatic Sanitization Bypass in Angular and AngularJS]]'
- '[[Basic Command Injection Exploitation]]'
- '[[Basic LFI Filter Bypass]]'
- '[[Basic LFI via UTF-8 encoding]]'
- '[[Basic RFI with Double Encoding]]'
- '[[Cloudflare XSS Bypass via Common WAF and HTML Injection]]'
- '[[Command Injection Filter Bypass with $() and variable expansion]]'
- '[[Command Injection Filter Bypass with Backslash and Slash]]'
- '[[Command Injection - Filter Bypass with Backslash Newline]]'
- '[[Command Injection with $@]]'
- '[[Command Injection with $() Filter Bypass]]'
- '[[Command Injection with Double Quote Bypass]]'
- '[[Command Injection with Filter Bypass using Single Quote]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CVE-2021-44228 Log4Shell Remote Command Execution]]'
- '[[CVE-2021-44228 Log4Shell Remote Command Execution]]'
- '[[CVE-2021-44228 Log4Shell Remote Command Execution]]'
- '[[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]'
- '[[Filter Bypass using UTF-7 Encoding for XSS Injection]]'
- '[[Hidden Input XSS Attack]]'
- '[[Jinjava Command Execution]]'
- '[[LFI/RFI using php://filter wrapper]]'
- '[[LFI to RCE via /proc/self/environ]]'
- '[[Linux Bash Command Injection with Filter Bypass]]'
- '[[Malicious Macro-enabled Excel Documents with Macrome]]'
- '[[Metasploit Scripting with Meterpreter Reverse HTTPS Payload]]'
- '[[MultiBrowser RPO Attack and XSS Injection Prevention]]'
- '[[MYSQL Injection - Write Shell using Outfile Method]]'
- '[[Polyglot Command Injection for DNS Data Exfiltration]]'
- '[[Python Reverse Shell Cheat Sheet]]'
- '[[Reflective Assembly Loading with Powershell]]'
- '[[Server-Side Request Forgery to Cross-Site Scripting (SSRF to XSS) via Out-of-Band
  Output]]'
- '[[Server Side Template Injection - Django Templates - Leaking app''s Secret Key
  - Retrieve Signer Key]]'
- '[[Server Side Template Injection - Ruby - Retrieve /etc/passwd]]'
- '[[Twig Debugging Injection]]'
- '[[WAF Bypass using Chrome Auditor XSS Attack Vector]]'
- '[[XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert]]'
---

# Windows Command Shell

**MITRE ID**: T1059.003

**Parent Technique**: [[Command-Line Interface|T1059 - Command-Line Interface]]

This is a sub-technique of T1059 - Command-Line Interface.

## Summary

Adversaries may abuse the Windows command shell for execution. The Windows command shell ([cmd](https://attack.mitre.org/software/S0106)) is the primary command prompt on Windows systems. The Windows command prompt can be used to control almost any aspect of a system, with various permission levels 

## Description

Adversaries may abuse the Windows command shell for execution. The Windows command shell ([cmd](https://attack.mitre.org/software/S0106)) is the primary command prompt on Windows systems. The Windows command prompt can be used to control almost any aspect of a system, with various permission levels required for different subsets of commands. The command prompt can be invoked remotely via [Remote Services](https://attack.mitre.org/techniques/T1021) such as [SSH](https://attack.mitre.org/techniques/T1021/004).(Citation: SSH in Windows)

Batch files (ex: .bat or .cmd) also provide the shell with a list of sequential commands to run, as well as normal scripting operations such as conditionals and loops. Common uses of batch files include long or repetitive tasks, or the need to run the same set of commands on multiple systems.

Adversaries may leverage [cmd](https://attack.mitre.org/software/S0106) to execute various commands and payloads. Common uses include [cmd](https://attack.mitre.org/software/S0106) to execute a single command, or abusing [cmd](https://attack.mitre.org/software/S0106) interactively with input and output forwarded over a command and control channel.

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 41 procedures using this sub-technique:

- [[ASP Razor Server Side Template Injection with C# Command Execution]]
- [[Automatic Sanitization Bypass in Angular and AngularJS]]
- [[Basic Command Injection Exploitation]]
- [[Basic LFI Filter Bypass]]
- [[Basic LFI via UTF-8 encoding]]
- [[Basic RFI with Double Encoding]]
- [[Cloudflare XSS Bypass via Common WAF and HTML Injection]]
- [[Command Injection Filter Bypass with $() and variable expansion]]
- [[Command Injection Filter Bypass with Backslash and Slash]]
- [[Command Injection - Filter Bypass with Backslash Newline]]
- [[Command Injection with $@]]
- [[Command Injection with $() Filter Bypass]]
- [[Command Injection with Double Quote Bypass]]
- [[Command Injection with Filter Bypass using Single Quote]]
- [[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]
- [[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]
- [[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]
- [[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]
- [[CVE-2021-44228 Log4Shell Remote Command Execution]]
- [[CVE-2021-44228 Log4Shell Remote Command Execution]]

*...and 21 more*
