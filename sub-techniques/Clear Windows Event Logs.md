---
id: 7fda8a6b-3ee4-4c95-a16f-74659bc44d73
name: Clear Windows Event Logs
type: sub-technique
mitre_id: T1070.001
mitre_url: null
created_at: '2023-04-06T00:31:26.245889+00:00'
updated_at: '2023-04-06T00:31:26.245889+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Linux Command History Evasion]]'
---

# Clear Windows Event Logs

**MITRE ID**: T1070.001

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record of a computer's alerts and notifications. There are three system-defined sources of events: System, Application, and Security, with five event types: Error, Warning, Information, Success Au

## Description

Adversaries may clear Windows Event Logs to hide the activity of an intrusion. Windows Event Logs are a record of a computer's alerts and notifications. There are three system-defined sources of events: System, Application, and Security, with five event types: Error, Warning, Information, Success Audit, and Failure Audit.

The event logs can be cleared with the following utility commands:

* <code>wevtutil cl system</code>
* <code>wevtutil cl application</code>
* <code>wevtutil cl security</code>

These logs may also be cleared through other mechanisms, such as the event viewer GUI or [PowerShell](https://attack.mitre.org/techniques/T1059/001).

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Linux Command History Evasion]]
