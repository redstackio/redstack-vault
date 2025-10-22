---
id: f909d6f2-bcee-4cc4-a0f4-0037dce5b131
name: SNMP (MIB Dump)
type: sub-technique
mitre_id: T1602.001
mitre_url: null
created_at: '2023-04-06T00:31:27.155021+00:00'
updated_at: '2023-04-06T00:31:27.155021+00:00'
parent_technique: '[[Data from Configuration Repository|T1602 - Data from Configuration
  Repository]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# SNMP (MIB Dump)

**MITRE ID**: T1602.001

**Parent Technique**: [[Data from Configuration Repository|T1602 - Data from Configuration Repository]]

This is a sub-technique of T1602 - Data from Configuration Repository.

## Summary

Adversaries may target the Management Information Base (MIB) to collect and/or mine valuable information in a network managed using Simple Network Management Protocol (SNMP).

The MIB is a configuration repository that stores variable information accessible via SNMP in the form of object identifiers

## Description

Adversaries may target the Management Information Base (MIB) to collect and/or mine valuable information in a network managed using Simple Network Management Protocol (SNMP).

The MIB is a configuration repository that stores variable information accessible via SNMP in the form of object identifiers (OID). Each OID identifies a variable that can be read or set and permits active management tasks, such as configuration changes, through remote modification of these variables. SNMP can give administrators great insight in their systems, such as, system information, description of hardware, physical location, and software packages(Citation: SANS Information Security Reading Room Securing SNMP Securing SNMP). The MIB may also contain device operational information, including running configuration, routing table, and interface details.

Adversaries may use SNMP queries to collect MIB content directly from SNMP-managed devices in order to collect network information that allows the adversary to build network maps and facilitate future targeted exploitation.(Citation: US-CERT-TA18-106A)(Citation: Cisco Blog Legacy Device Attacks) 

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
