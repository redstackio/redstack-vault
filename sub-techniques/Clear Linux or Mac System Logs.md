---
id: 12b670d1-aad1-4d82-b708-9a023849d5b1
name: Clear Linux or Mac System Logs
type: sub-technique
mitre_id: T1070.002
mitre_url: null
created_at: '2023-04-06T00:31:25.799232+00:00'
updated_at: '2023-04-06T00:31:25.799232+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Windows - Clear Event Logs for Anti-Virus Evasion]]'
---

# Clear Linux or Mac System Logs

**MITRE ID**: T1070.002

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their r

## Description

Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system or user-initiated actions via system logs. The majority of native system logging is stored under the <code>/var/log/</code> directory. Subfolders in this directory categorize logs by their related functions, such as:(Citation: Linux Logs)

* <code>/var/log/messages:</code>: General and system-related messages
* <code>/var/log/secure</code> or <code>/var/log/auth.log</code>: Authentication logs
* <code>/var/log/utmp</code> or <code>/var/log/wtmp</code>: Login records
* <code>/var/log/kern.log</code>: Kernel logs
* <code>/var/log/cron.log</code>: Crond logs
* <code>/var/log/maillog</code>: Mail server logs
* <code>/var/log/httpd/</code>: Web server access and error logs

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Windows - Clear Event Logs for Anti-Virus Evasion]]
