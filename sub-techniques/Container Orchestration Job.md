---
id: 49e9c7de-8659-40d5-80f0-d469fb3895ec
name: Container Orchestration Job
type: sub-technique
mitre_id: T1053.007
mitre_url: null
created_at: '2023-04-06T00:31:25.567402+00:00'
updated_at: '2023-04-06T00:31:25.567402+00:00'
parent_technique: '[[Scheduled Task|T1053 - Scheduled Task]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Container Orchestration Job

**MITRE ID**: T1053.007

**Parent Technique**: [[Scheduled Task|T1053 - Scheduled Task]]

This is a sub-technique of T1053 - Scheduled Task.

## Summary

Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernetes to schedule deployment of containers configured to execute malicious code. Container orchestration jobs run these automated tasks at a specific date and time, similar to cron jobs on a Li

## Description

Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernetes to schedule deployment of containers configured to execute malicious code. Container orchestration jobs run these automated tasks at a specific date and time, similar to cron jobs on a Linux system. Deployments of this type can also be configured to maintain a quantity of containers over time, automating the process of maintaining persistence within a cluster.

In Kubernetes, a CronJob may be used to schedule a Job that runs one or more containers to perform specific tasks.(Citation: Kubernetes Jobs)(Citation: Kubernetes CronJob) An adversary therefore may utilize a CronJob to schedule deployment of a Job that executes malicious code in various nodes within a cluster.(Citation: Threat Matrix for Kubernetes)

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
