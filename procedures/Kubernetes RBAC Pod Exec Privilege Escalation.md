---
id: e6df3056-1a91-4b03-8469-52a2d68c8272
name: Kubernetes RBAC Pod Exec Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.284651+00:00'
updated_at: '2023-04-10T20:34:05.488869+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]'
sub_techniques:
- '[[Create Cloud Instance|T1578.002 - Create Cloud Instance]]'
tags:
- '[[Kubernetes]]'
- '[[Privilege to Use Pods/Exec]]'
- '[[RBAC Configuration]]'
commands:
- '[[Execute shell in Kubernetes pod]]'
---

# Kubernetes RBAC Pod Exec Privilege Escalation

## Summary

This procedure details how an attacker with access to a Kubernetes pod can escalate their privileges to execute commands on other pods in the same namespace. By default, Kubernetes Role-Based Access Control (RBAC) configurations do not grant pods the ability to execute commands on other pods. Howev

## Description

# Description

This procedure details how an attacker with access to a Kubernetes pod can escalate their privileges to execute commands on other pods in the same namespace. By default, Kubernetes Role-Based Access Control (RBAC) configurations do not grant pods the ability to execute commands on other pods. However, if the attacker can gain access to a pod with the necessary privileges, they can use the 'kubectl exec' command to execute arbitrary commands on other pods in the same namespace. This can be used to move laterally within the cluster, exfiltrate data, or execute other malicious activities.

 

## Requirements

1. Access to a Kubernetes pod with the necessary RBAC privileges

1. Access to the 'kubectl' command-line tool

 

## Defense

1. Limit access to Kubernetes pods to only authorized personnel

1. Implement RBAC policies to restrict pod-to-pod communication

1. Monitor Kubernetes API server logs for suspicious activity, such as unauthorized use of the 'kubectl exec' command

 

## Objectives

1. Escalate privileges within the Kubernetes cluster

1. Execute arbitrary commands on other pods in the same namespace

 

# Instructions

1. 1. Open a terminal
2. Run the following command: 

kubectl exec -it <POD NAME> -n <PODS NAMESPACE> -- sh


 



**Code**: [[kubectl exec -it <POD NAME> -n <PODS NAMESPACE> --]]



> This command will open an interactive shell session with the target pod, allowing the attacker to execute arbitrary commands within the pod's environment.



**Command** ([[Execute shell in Kubernetes pod]]):

```bash
kubectl exec -it <POD NAME> -n <PODS NAMESPACE> -- sh
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

### Sub-Techniques

- [[Create Cloud Instance|T1578.002 - Create Cloud Instance]]

## Commands Used

- [[Execute shell in Kubernetes pod]]

## Tags

- [[Kubernetes]]
- [[Privilege to Use Pods/Exec]]
- [[RBAC Configuration]]


