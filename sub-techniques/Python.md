---
id: a637c6ba-af7b-4745-bc97-7a1889ba7171
name: Python
type: sub-technique
mitre_id: T1059.006
mitre_url: null
created_at: '2023-04-06T00:31:26.939800+00:00'
updated_at: '2023-04-06T00:31:26.939800+00:00'
parent_technique: '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]'
---

# Python

**MITRE ID**: T1059.006

**Parent Technique**: [[Command-Line Interface|T1059 - Command-Line Interface]]

This is a sub-technique of T1059 - Command-Line Interface.

## Summary

Adversaries may abuse Python commands and scripts for execution. Python is a very popular scripting/programming language, with capabilities to perform many functions. Python can be executed interactively from the command-line (via the <code>python.exe</code> interpreter) or via scripts (.py) that ca

## Description

Adversaries may abuse Python commands and scripts for execution. Python is a very popular scripting/programming language, with capabilities to perform many functions. Python can be executed interactively from the command-line (via the <code>python.exe</code> interpreter) or via scripts (.py) that can be written and distributed to different systems. Python code can also be compiled into binary executables.

Python comes with many built-in packages to interact with the underlying system, such as file operations and device I/O. Adversaries can use these libraries to download and execute commands or other scripts as well as perform various malicious behaviors.

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks]]
