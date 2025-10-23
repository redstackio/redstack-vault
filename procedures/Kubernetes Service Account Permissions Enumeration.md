---
id: f7609fcc-b527-460c-bda9-b752d70cc3e1
name: Kubernetes Service Account Permissions Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.150511+00:00'
updated_at: '2023-04-10T20:33:58.582905+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Information Gathering]]'
- '[[Kubernetes]]'
- '[[Service Account Permissions]]'
commands:
- '[[Check kubectl access to kube-system namespace]]'
- '[[Check Kubernetes Authorization]]'
---

# Kubernetes Service Account Permissions Enumeration

## Summary

The Kubernetes Service Account Permissions Enumeration procedure is used to determine the permissions granted to the default service account. This procedure is useful for identifying potential paths for cluster compromise or lateral movement. By default, the Kubernetes API server grants all service

## Description

# Description

The Kubernetes Service Account Permissions Enumeration procedure is used to determine the permissions granted to the default service account. This procedure is useful for identifying potential paths for cluster compromise or lateral movement. By default, the Kubernetes API server grants all service accounts in a namespace read access to secrets and config maps. This may be further expanded by cluster administrators to include additional permissions. By enumerating these permissions, a potential attacker can identify privileged service accounts and use them to escalate privileges or move laterally within the cluster.

To enumerate service account permissions, this procedure uses kubectl and curl commands to query the Kubernetes API server for self-subject rules reviews. These reviews provide a detailed list of the permissions granted to the default service account, including both namespace-level and cluster-level permissions.

 

## Requirements

1. Authenticated access to the Kubernetes API server

 

## Defense

1. Restrict access to the Kubernetes API server to only authorized personnel

1. Implement least privilege access policies for service accounts

1. Monitor for suspicious activity, such as unusual service account activity or changes to service account permissions.

 

## Objectives

1. Identify potential paths for cluster compromise or lateral movement

 

# Instructions

1. 

 



**Code**: [[kubectl auth can-i --list]]



> This command uses kubectl to query the Kubernetes API server for a list of all actions that the default service account can perform in the specified namespace.



**Command** ([[Check Kubernetes Authorization]]):

```bash
kubectl auth can-i --list
```



2. 

 



**Code**: [[kubectl auth can-i --list --namespace=kube-system]]



> This command uses kubectl to query the Kubernetes API server for a list of all actions that the default service account can perform across all namespaces.



**Command** ([[Check kubectl access to kube-system namespace]]):

```bash
kubectl auth can-i --list --namespace=kube-system
```



3. 

 



**Code**: [[NAMESPACE=$(cat "/var/run/secrets/kubernetes.io/se]]



> This command uses curl to query the Kubernetes API server for a detailed list of the permissions granted to the default service account, including both namespace-level and cluster-level permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Check kubectl access to kube-system namespace]]
- [[Check Kubernetes Authorization]]

## Tags

- [[Information Gathering]]
- [[Kubernetes]]
- [[Service Account Permissions]]


