---
id: bed6cfcd-858e-4b27-a7fb-73bf227d84ae
name: Container and Resource Discovery
type: technique
mitre_id: T1613
mitre_url: null
created_at: '2023-04-06T00:31:25.437685+00:00'
updated_at: '2023-04-06T00:31:27.780688+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Container and Resource Discovery

**MITRE ID**: T1613

## Description

Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs.(Citation: Docker API)(Citation: Kubernetes API) In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution. 

## Tactics

- [[Discovery|TA0007 - Discovery]]
