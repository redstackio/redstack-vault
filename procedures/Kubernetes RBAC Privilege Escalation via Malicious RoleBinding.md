---
id: d52fef61-dd7c-46b7-80ec-a89e43f791ea
name: Kubernetes RBAC Privilege Escalation via Malicious RoleBinding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.310218+00:00'
updated_at: '2023-04-10T20:34:00.632964+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Process Injection|T1055 - Process Injection]]'
tags:
- '[[Kubernetes]]'
- '[[Privilege to Get/Patch Rolebindings]]'
- '[[RBAC Configuration]]'
commands:
- '[[Create Secret in kube-system Namespace]]'
---

# Kubernetes RBAC Privilege Escalation via Malicious RoleBinding

## Summary

Kubernetes Role-Based Access Control (RBAC) is a security feature that allows cluster administrators to define fine-grained access policies for the resources within the Kubernetes API. Attackers can exploit RBAC misconfigurations to escalate privileges and gain unauthorized access to resources. Thi

## Description

# Description

Kubernetes Role-Based Access Control (RBAC) is a security feature that allows cluster administrators to define fine-grained access policies for the resources within the Kubernetes API. Attackers can exploit RBAC misconfigurations to escalate privileges and gain unauthorized access to resources. This procedure outlines the steps to create a malicious RoleBinding that binds the admin ClusterRole to a compromised service account. By doing so, an attacker can elevate the privileges of the compromised service account and gain access to sensitive resources. The attack can be carried out by an authenticated user with privileges to create RoleBindings.

 

## Requirements

1. Authenticated access to the Kubernetes API server.

1. Permissions to create RoleBindings.

 

## Defense

1. Ensure that Kubernetes RBAC is properly configured and that users have the least privilege necessary to perform their tasks.

1. Use network segmentation to isolate Kubernetes clusters from other critical infrastructure.

1. Monitor for unauthorized access to sensitive resources and unusual activity within the Kubernetes API server.

 

## Objectives

1. Create a malicious RoleBinding that binds the admin ClusterRole to a compromised service account.

1. Escalate privileges of the compromised service account to gain unauthorized access to resources.

 

# Instructions

1. Create a file named malicious-RoleBinding.json and copy the JSON data into it.

 



**Code**: [[{
    "apiVersion": "rbac.authorization.k8s.io/v1"]]



> This command creates a JSON file with the malicious RoleBinding data that will be used in the next command.

2. Replace <JWT TOKEN> with a valid JWT token and <master_ip> and <port> with the IP address and port of the Kubernetes API server. Run the following command:

 



**Code**: [[curl -k -v -X POST -H "Authorization: Bearer <JWT ]]



> This command creates a RoleBinding in the default namespace that binds the admin ClusterRole to the compromised service account.

3. Replace <COMPROMISED JWT TOKEN> with the JWT token of the compromised service account and <master_ip> and <port> with the IP address and port of the Kubernetes API server. Run the following command:

 



**Code**: [[curl -k -v -X POST -H "Authorization: Bearer <COMP]]



> This command accesses sensitive resources in the kube-system namespace using the compromised service account.



**Command** ([[Create Secret in kube-system Namespace]]):

```bash
curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED JWT TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secret
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Process Injection|T1055 - Process Injection]]

## Commands Used

- [[Create Secret in kube-system Namespace]]

## Tags

- [[Kubernetes]]
- [[Privilege to Get/Patch Rolebindings]]
- [[RBAC Configuration]]


