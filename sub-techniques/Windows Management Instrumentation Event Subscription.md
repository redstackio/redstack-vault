---
id: b507b75b-0ad0-4f18-9a47-024ece73f464
name: Windows Management Instrumentation Event Subscription
type: sub-technique
mitre_id: T1546.003
mitre_url: null
created_at: '2023-04-06T00:31:26.565452+00:00'
updated_at: '2023-04-06T00:31:26.565452+00:00'
parent_technique: '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Windows Privilege Escalation using PowerUp, PrivescCheck, and WES-NG]]'
---

# Windows Management Instrumentation Event Subscription

**MITRE ID**: T1546.003

**Parent Technique**: [[Event Triggered Execution|T1546 - Event Triggered Execution]]

This is a sub-technique of T1546 - Event Triggered Execution.

## Summary

Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Windows Management Instrumentation (WMI) event subscription. WMI can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Examples

## Description

Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Windows Management Instrumentation (WMI) event subscription. WMI can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Examples of events that may be subscribed to are the wall clock time, user loging, or the computer's uptime.(Citation: Mandiant M-Trends 2015)

Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event occurs, providing persistence on a system.(Citation: FireEye WMI SANS 2015)(Citation: FireEye WMI 2015) Adversaries may also compile WMI scripts into Windows Management Object (MOF) files (.mof extension) that can be used to create a malicious subscription.(Citation: Dell WMI Persistence)(Citation: Microsoft MOF May 2018)

WMI subscription execution is proxied by the WMI Provider Host process (WmiPrvSe.exe) and thus may result in elevated SYSTEM privileges.

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Windows Privilege Escalation using PowerUp, PrivescCheck, and WES-NG]]
