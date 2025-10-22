---
id: 4d392951-8c47-4f9a-8a22-e0c8de221b25
name: Keylogging
type: sub-technique
mitre_id: T1056.001
mitre_url: null
created_at: '2023-04-06T00:31:25.473380+00:00'
updated_at: '2023-04-06T00:31:25.473380+00:00'
parent_technique: '[[Input Capture|T1056 - Input Capture]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Keylogging

**MITRE ID**: T1056.001

**Parent Technique**: [[Input Capture|T1056 - Input Capture]]

This is a sub-technique of T1056 - Input Capture.

## Summary

Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) efforts are not effective, and may require an adversary to 

## Description

Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of time before credentials can be successfully captured.

Keylogging is the most prevalent type of input capture, with many different ways of intercepting keystrokes.(Citation: Adventures of a Keystroke) Some methods include:

* Hooking API callbacks used for processing keystrokes. Unlike [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004), this focuses solely on API functions intended for processing keystroke data.
* Reading raw keystroke data from the hardware buffer.
* Windows Registry modifications.
* Custom drivers.
* [Modify System Image](https://attack.mitre.org/techniques/T1601) may provide adversaries with hooks into the operating system of network devices to read raw keystrokes for login sessions.(Citation: Cisco Blog Legacy Device Attacks) 

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
