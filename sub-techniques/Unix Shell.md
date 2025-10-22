---
id: 956018c1-2b58-4de6-91cf-a4492a16e69b
name: Unix Shell
type: sub-technique
mitre_id: T1059.004
mitre_url: null
created_at: '2023-04-06T00:31:26.700386+00:00'
updated_at: '2023-04-06T00:31:26.700386+00:00'
parent_technique: '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[CSV Injection - Exploit]]'
- '[[Mako Server Side Template Injection to Retrieve User ID]]'
- '[[MYSQL Injection - Write Shell using Outfile Method]]'
- '[[Reflective Assembly Loading with Powershell]]'
---

# Unix Shell

**MITRE ID**: T1059.004

**Parent Technique**: [[Command-Line Interface|T1059 - Command-Line Interface]]

This is a sub-technique of T1059 - Command-Line Interface.

## Summary

Adversaries may abuse Unix shell commands and scripts for execution. Unix shells are the primary command prompt on Linux and macOS systems, though many variations of the Unix shell exist (e.g. sh, bash, zsh, etc.) depending on the specific OS or distribution.(Citation: DieNet Bash)(Citation: Apple Z

## Description

Adversaries may abuse Unix shell commands and scripts for execution. Unix shells are the primary command prompt on Linux and macOS systems, though many variations of the Unix shell exist (e.g. sh, bash, zsh, etc.) depending on the specific OS or distribution.(Citation: DieNet Bash)(Citation: Apple ZShell) Unix shells can control every aspect of a system, with certain commands requiring elevated privileges.

Unix shells also support scripts that enable sequential execution of commands as well as other typical programming operations such as conditionals and loops. Common uses of shell scripts include long or repetitive tasks, or the need to run the same set of commands on multiple systems.

Adversaries may abuse Unix shells to execute various commands or payloads. Interactive shells may be accessed through command and control channels or during lateral movement such as with [SSH](https://attack.mitre.org/techniques/T1021/004). Adversaries may also leverage shell scripts to deliver and execute multiple commands on victims or as part of payloads used for persistence.

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 4 procedures using this sub-technique:

- [[CSV Injection - Exploit]]
- [[Mako Server Side Template Injection to Retrieve User ID]]
- [[MYSQL Injection - Write Shell using Outfile Method]]
- [[Reflective Assembly Loading with Powershell]]
