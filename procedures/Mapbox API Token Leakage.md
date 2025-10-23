---
id: 1abce01d-4ec3-4653-bfff-4e791a66a14f
name: Mapbox API Token Leakage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:51.914089+00:00'
updated_at: '2023-04-10T20:21:11.909711+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[API Key Leaks]]'
- '[[Exploit]]'
- '[[Mapbox API Token]]'
commands:
- '[[Calculate primary key value for table_name and id 123]]'
- '[[Check token validity]]'
- '[[Create a pod from a YAML file]]'
- '[[Delete a pod]]'
- '[[Execute a command in a container]]'
- '[[Follow logs of a container]]'
- '[[Get list of all tokens associated with an account]]'
- '[[List all configmaps]]'
- '[[List all deployments]]'
- '[[List all events]]'
- '[[List all namespaces]]'
- '[[List all nodes]]'
- '[[List all pods]]'
- '[[List all secrets]]'
- '[[List all services]]'
- '[[Open a shell in a container]]'
- '[[Port-forward to a pod]]'
- '[[View logs of a container]]'
---

# Mapbox API Token Leakage

## Summary

Mapbox API tokens are used to authenticate and authorize access to Mapbox services. These tokens can be leaked through various means such as hard-coded in source code, stored in configuration files or even accidentally committed to public repositories. Attackers can exploit these leaked tokens to g

## Description

# Description

Mapbox API tokens are used to authenticate and authorize access to Mapbox services. These tokens can be leaked through various means such as hard-coded in source code, stored in configuration files or even accidentally committed to public repositories. Attackers can exploit these leaked tokens to gain unauthorized access to Mapbox services and data.

An attacker can use a leaked Mapbox API token to access Mapbox services and data, which can include sensitive information such as geolocation data, map data, and user information. This information can be used for further attacks or sold on the black market. Additionally, the attacker can use the Mapbox API token to launch attacks on other systems that use the token for authentication and authorization.

 

## Requirements

1. Access to the internet

1. Mapbox API token

 

## Defense

1. Avoid hard-coding API tokens in source code or configuration files.

1. Use environment variables to store API tokens instead of hard-coding them.

1. Regularly rotate API tokens to limit the impact of a potential token leak.

1. Monitor source code and repositories for leaked API tokens.

1. Limit the scope of API tokens to only the necessary APIs and actions.

 

## Objectives

1. To identify and exploit leaked Mapbox API tokens to gain unauthorized access to Mapbox services and data.

 

# Instructions

1. To identify a Mapbox API token, search for the string 'pk.' or 'sk.' followed by a JWT in the target system's source code or configuration files.

 



**Code**: [[sk]]



> The attacker can use various methods to search for the Mapbox API tokens on the target system, such as searching for specific strings in the source code or configuration files. Once a token is identified, the attacker can use it to access Mapbox services and data.



**Command** ([[List all pods]]):

```bash
sk get pod
```





**Command** ([[List all services]]):

```bash
sk get svc
```





**Command** ([[List all deployments]]):

```bash
sk get deploy
```





**Command** ([[List all configmaps]]):

```bash
sk get cm
```





**Command** ([[List all secrets]]):

```bash
sk get secret
```





**Command** ([[List all nodes]]):

```bash
sk get node
```





**Command** ([[List all namespaces]]):

```bash
sk get ns
```





**Command** ([[List all events]]):

```bash
sk get event
```





**Command** ([[Create a pod from a YAML file]]):

```bash
sk create -f path/to/pod.yaml
```





**Command** ([[Delete a pod]]):

```bash
sk delete pod <pod-name>
```





**Command** ([[Port-forward to a pod]]):

```bash
sk port-forward <pod-name> <local-port>:<pod-port>
```





**Command** ([[Execute a command in a container]]):

```bash
sk exec <pod-name> -c <container-name> -- <command>
```





**Command** ([[View logs of a container]]):

```bash
sk logs <pod-name> -c <container-name>
```





**Command** ([[Follow logs of a container]]):

```bash
sk logs -f <pod-name> -c <container-name>
```





**Command** ([[Open a shell in a container]]):

```bash
sk exec -it <pod-name> -c <container-name> -- /bin/sh
```



2. To exploit a leaked Mapbox API token, the attacker can use the token to access Mapbox services and data.

 



**Code**: [[pk]]



> The attacker can use the Mapbox API token to access Mapbox services and data. Depending on the scope of the token, the attacker can access specific Mapbox APIs. The attacker can use this access to gather sensitive information or launch further attacks.



**Command** ([[Calculate primary key value for table_name and id 123]]):

```bash
Set `id` to 123.
Concatenate `table_name` and `id` to create the primary key value.
```



3. To check the validity of a Mapbox API token and list all tokens associated with an account, the attacker can use the following commands in the terminal:

 



**Code**: [[#Check token validity
curl "https://api.mapbox.com]]



> These commands can be used to check the validity of a Mapbox API token and list all tokens associated with an account. This information can be used by the attacker to identify valid tokens and launch further attacks.



**Command** ([[Check token validity]]):

```bash
curl "https://api.mapbox.com/tokens/v2?access_token=YOUR_MAPBOX_ACCESS_TOKEN"
```





**Command** ([[Get list of all tokens associated with an account]]):

```bash
curl "https://api.mapbox.com/tokens/v2/MAPBOX_USERNAME_HERE?access_token=YOUR_MAPBOX_ACCESS_TOKEN"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Calculate primary key value for table_name and id 123]]
- [[Check token validity]]
- [[Create a pod from a YAML file]]
- [[Delete a pod]]
- [[Execute a command in a container]]
- [[Follow logs of a container]]
- [[Get list of all tokens associated with an account]]
- [[List all configmaps]]
- [[List all deployments]]
- [[List all events]]
- [[List all namespaces]]
- [[List all nodes]]
- [[List all pods]]
- [[List all secrets]]
- [[List all services]]
- [[Open a shell in a container]]
- [[Port-forward to a pod]]
- [[View logs of a container]]

## Tags

- [[API Key Leaks]]
- [[Exploit]]
- [[Mapbox API Token]]


