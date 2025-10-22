---
id: 6f93c513-9af3-405c-a916-486fb6794e30
name: Network Device Configuration Dump
type: sub-technique
mitre_id: T1602.002
mitre_url: null
created_at: '2023-04-06T00:31:26.115157+00:00'
updated_at: '2023-04-06T00:31:26.115157+00:00'
parent_technique: '[[Data from Configuration Repository|T1602 - Data from Configuration
  Repository]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
---

# Network Device Configuration Dump

**MITRE ID**: T1602.002

**Parent Technique**: [[Data from Configuration Repository|T1602 - Data from Configuration Repository]]

This is a sub-technique of T1602 - Data from Configuration Repository.

## Summary

Adversaries may access network configuration files to collect sensitive data about the device and the network. The network configuration is a file containing parameters that determine the operation of the device. The device typically stores an in-memory copy of the configuration while operating, and

## Description

Adversaries may access network configuration files to collect sensitive data about the device and the network. The network configuration is a file containing parameters that determine the operation of the device. The device typically stores an in-memory copy of the configuration while operating, and a separate configuration on non-volatile storage to load after device reset. Adversaries can inspect the configuration files to reveal information about the target network and its layout, the network device and its software, or identifying legitimate accounts and credentials for later use.

Adversaries can use common management tools and protocols, such as Simple Network Management Protocol (SNMP) and Smart Install (SMI), to access network configuration files.(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)(Citation: Cisco Blog Legacy Device Attacks) These tools may be used to query specific data from a configuration repository or configure the device to export the configuration for later analysis. 

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
