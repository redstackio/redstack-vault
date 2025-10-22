---
id: 825a4ea2-bbc5-4363-bbd7-8a275701c810
name: Web Portal Capture
type: sub-technique
mitre_id: T1056.003
mitre_url: null
created_at: '2023-04-06T00:31:26.294323+00:00'
updated_at: '2023-04-06T00:31:26.294323+00:00'
parent_technique: '[[Input Capture|T1056 - Input Capture]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Web Portal Capture

**MITRE ID**: T1056.003

**Parent Technique**: [[Input Capture|T1056 - Input Capture]]

This is a sub-technique of T1056 - Input Capture.

## Summary

Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials before logging the user in to the service.

This variation on

## Description

Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials before logging the user in to the service.

This variation on input capture may be conducted post-compromise using legitimate administrative access as a backup measure to maintain network access through [External Remote Services](https://attack.mitre.org/techniques/T1133) and [Valid Accounts](https://attack.mitre.org/techniques/T1078) or as part of the initial compromise by exploitation of the externally facing web service.(Citation: Volexity Virtual Private Keylogging)

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
