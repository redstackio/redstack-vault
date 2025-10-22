---
id: cce57635-0039-4d74-8378-ab79684b8e5c
name: Data from Configuration Repository
type: technique
mitre_id: T1602
mitre_url: null
created_at: '2023-04-06T00:31:25.491360+00:00'
updated_at: '2023-04-06T00:31:27.783320+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Data from Configuration Repository

**MITRE ID**: T1602

## Description

Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.

Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.(Citation: US-CERT-TA18-106A)(Citation: US-CERT TA17-156A SNMP Abuse 2017)

## Tactics

- [[Collection|TA0009 - Collection]]
