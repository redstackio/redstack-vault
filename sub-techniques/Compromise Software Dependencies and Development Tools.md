---
id: 7ef42a81-d53f-4f1e-9f93-7db74d3e838c
name: Compromise Software Dependencies and Development Tools
type: sub-technique
mitre_id: T1195.001
mitre_url: null
created_at: '2023-04-06T00:31:25.625587+00:00'
updated_at: '2023-04-06T00:31:25.625587+00:00'
parent_technique: '[[Supply Chain Compromise|T1195 - Supply Chain Compromise]]'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
---

# Compromise Software Dependencies and Development Tools

**MITRE ID**: T1195.001

**Parent Technique**: [[Supply Chain Compromise|T1195 - Supply Chain Compromise]]

This is a sub-technique of T1195 - Supply Chain Compromise.

## Summary

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applicatio

## Description

Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications may be targeted as a means to add malicious code to users of the dependency.(Citation: Trendmicro NPM Compromise)  

Targeting may be specific to a desired victim set or may be distributed to a broad set of consumers but only move on to additional tactics on specific victims. 

## Tactics

This sub-technique is used in the following tactics:

- [[Initial Access|TA0001 - Initial Access]]
