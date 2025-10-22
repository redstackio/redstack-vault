---
id: d7989835-7836-4a2a-a1d9-41ced32edd5e
name: Trap
type: sub-technique
mitre_id: T1546.005
mitre_url: null
created_at: '2023-04-06T00:31:26.233756+00:00'
updated_at: '2023-04-06T00:31:26.233756+00:00'
parent_technique: '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Trap

**MITRE ID**: T1546.005

**Parent Technique**: [[Event Triggered Execution|T1546 - Event Triggered Execution]]

This is a sub-technique of T1546 - Event Triggered Execution.

## Summary

Adversaries may establish persistence by executing malicious content triggered by an interrupt signal. The <code>trap</code> command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common situation is a script allowing for graceful termination

## Description

Adversaries may establish persistence by executing malicious content triggered by an interrupt signal. The <code>trap</code> command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common situation is a script allowing for graceful termination and handling of common keyboard interrupts like <code>ctrl+c</code> and <code>ctrl+d</code>.

Adversaries can use this to register code to be executed when the shell encounters specific interrupts as a persistence mechanism. Trap commands are of the following format <code>trap 'command list' signals</code> where "command list" will be executed when "signals" are received.(Citation: Trap Manual)(Citation: Cyberciti Trap Statements)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
