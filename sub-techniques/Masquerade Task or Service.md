---
id: a7a1ac6d-c50d-43cc-ad41-821e3d6a0b79
name: Masquerade Task or Service
type: sub-technique
mitre_id: T1036.004
mitre_url: null
created_at: '2023-04-06T00:31:26.413291+00:00'
updated_at: '2023-04-06T00:31:26.413291+00:00'
parent_technique: '[[Masquerading|T1036 - Masquerading]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Masquerade Task or Service

**MITRE ID**: T1036.004

**Parent Technique**: [[Masquerading|T1036 - Masquerading]]

This is a sub-technique of T1036 - Masquerading.

## Summary

Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign. Tasks/services executed by the Task Scheduler or systemd will typically be given a name and/or description.(Citation: TechNet Schtasks)(Citation: Systemd Service Units) Windows services will h

## Description

Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign. Tasks/services executed by the Task Scheduler or systemd will typically be given a name and/or description.(Citation: TechNet Schtasks)(Citation: Systemd Service Units) Windows services will have a service name as well as a display name. Many benign tasks and services exist that have commonly associated names. Adversaries may give tasks or services names that are similar or identical to those of legitimate ones.

Tasks or services contain other fields, such as a description, that adversaries may attempt to make appear legitimate.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Fysbis Dr Web Analysis)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
