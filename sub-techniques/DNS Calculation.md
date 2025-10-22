---
id: 6c6d0f2e-a3f2-473e-9132-4b872e3fb1f2
name: DNS Calculation
type: sub-technique
mitre_id: T1568.003
mitre_url: null
created_at: '2023-04-06T00:31:26.500165+00:00'
updated_at: '2023-04-06T00:31:26.500165+00:00'
parent_technique: '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# DNS Calculation

**MITRE ID**: T1568.003

**Parent Technique**: [[Dynamic Resolution|T1568 - Dynamic Resolution]]

This is a sub-technique of T1568 - Dynamic Resolution.

## Summary

Adversaries may perform calculations on addresses returned in DNS results to determine which port and IP address to use for command and control, rather than relying on a predetermined port number or the actual returned IP address. A IP and/or port number calculation can be used to bypass egress filt

## Description

Adversaries may perform calculations on addresses returned in DNS results to determine which port and IP address to use for command and control, rather than relying on a predetermined port number or the actual returned IP address. A IP and/or port number calculation can be used to bypass egress filtering on a C2 channel.(Citation: Meyers Numbered Panda)

One implementation of [DNS Calculation](https://attack.mitre.org/techniques/T1568/003) is to take the first three octets of an IP address in a DNS response and use those values to calculate the port for command and control traffic.(Citation: Meyers Numbered Panda)(Citation: Moran 2014)(Citation: Rapid7G20Espionage)

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
