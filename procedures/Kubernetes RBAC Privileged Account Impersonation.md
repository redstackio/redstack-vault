---
id: 1bf13c14-d37d-4908-a03f-f936597c5f0a
name: Kubernetes RBAC Privileged Account Impersonation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.339458+00:00'
updated_at: '2023-04-10T20:34:06.521270+00:00'
tags:
- '[[Impersonating a Privileged Account]]'
- '[[Kubernetes]]'
- '[[RBAC Configuration]]'
commands:
- '[[Get secrets from kube-system namespace]]'
---

# Kubernetes RBAC Privileged Account Impersonation

## Summary

This procedure involves using Kubernetes Role-Based Access Control (RBAC) configuration to impersonate a privileged account in order to gain access to sensitive resources. By using a JSON Web Token (JWT) of an impersonator and the Impersonate-Group header, an attacker can bypass RBAC restrictions a

## Description

# Description

This procedure involves using Kubernetes Role-Based Access Control (RBAC) configuration to impersonate a privileged account in order to gain access to sensitive resources. By using a JSON Web Token (JWT) of an impersonator and the Impersonate-Group header, an attacker can bypass RBAC restrictions and gain access to resources that are restricted to the privileged account. This technique can be used to elevate privileges and move laterally within a Kubernetes cluster. From a technical perspective, this procedure involves crafting a specific HTTP request with the necessary headers to impersonate a privileged account. The business value of this procedure lies in its ability to bypass RBAC restrictions and gain access to sensitive resources, which can lead to data theft, tampering, or destruction.

 

## Requirements

1. Valid JWT token of an impersonator

1. Access to Kubernetes API server

1. Knowledge of the target Kubernetes cluster's RBAC configuration

 

## Defense

1. Ensure that RBAC configurations are properly defined and enforced

1. Monitor for unusual API requests and unauthorized access attempts

1. Implement network segmentation and access controls to limit access to Kubernetes API server

 

## Objectives

1. Impersonate a privileged account to gain access to sensitive resources

1. Elevate privileges within a Kubernetes cluster

1. Move laterally within a Kubernetes cluster

 

# Instructions

1. Replace <JWT TOKEN (of the impersonator)> with the valid JWT token of the impersonator and <master_ip> and <port> with the IP address and port of the Kubernetes API server.

 



**Code**: [[curl -k -v -XGET -H "Authorization: Bearer <JWT TO]]



> This command uses the curl utility to make an HTTP GET request to the Kubernetes API server. The -k option is used to allow insecure connections, while the -v option enables verbose output. The -H option is used to set the necessary headers for impersonating a privileged account. The Impersonate-Group header is set to system:masters, which is a privileged group in Kubernetes. The Impersonate-User header is set to null, which means that the impersonator's username is used. The Accept header is set to application/json to receive the response in JSON format. The last argument is the URL of the resource to be accessed.



**Command** ([[Get secrets from kube-system namespace]]):

```bash
curl -k -v -XGET -H "Authorization: Bearer <JWT TOKEN (of the impersonator)>" -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/
```



## Commands Used

- [[Get secrets from kube-system namespace]]

## Tags

- [[Impersonating a Privileged Account]]
- [[Kubernetes]]
- [[RBAC Configuration]]


