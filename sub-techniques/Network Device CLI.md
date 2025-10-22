---
id: a60c7c28-b9c7-49eb-9b94-cfb0176eb181
name: Network Device CLI
type: sub-technique
mitre_id: T1059.008
mitre_url: null
created_at: '2023-04-06T00:31:26.484926+00:00'
updated_at: '2023-04-06T00:31:26.484926+00:00'
parent_technique: '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Network Device CLI

**MITRE ID**: T1059.008

**Parent Technique**: [[Command-Line Interface|T1059 - Command-Line Interface]]

This is a sub-technique of T1059 - Command-Line Interface.

## Summary

Adversaries may abuse scripting or built-in command line interpreters (CLI) on network devices to execute malicious command and payloads. The CLI is the primary means through which users and administrators interact with the device in order to view system information, modify device operations, or per

## Description

Adversaries may abuse scripting or built-in command line interpreters (CLI) on network devices to execute malicious command and payloads. The CLI is the primary means through which users and administrators interact with the device in order to view system information, modify device operations, or perform diagnostic and administrative functions. CLIs typically contain various permission levels required for different commands. 

Scripting interpreters automate tasks and extend functionality beyond the command set included in the network OS. The CLI and scripting interpreter are accessible through a direct console connection, or through remote means, such as telnet or [SSH](https://attack.mitre.org/techniques/T1021/004).

Adversaries can use the network CLI to change how network devices behave and operate. The CLI may be used to manipulate traffic flows to intercept or manipulate data, modify startup configuration parameters to load malicious system software, or to disable security features or logging to avoid detection.(Citation: Cisco Synful Knock Evolution)

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]
