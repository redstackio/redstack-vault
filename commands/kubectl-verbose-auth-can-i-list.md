---
id: 01ec2dfa-f285-4f28-8cc4-39f4bb2c8933
name: kubectl-verbose-auth-can-i-list
type: command
executor: bash
data: kubectl -v=9 auth can-i --list
output: null
created_at: '2023-04-06T03:56:01.118710+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
  - Linux
tags:
  - kubernetes
  - discovery
verified: true
validated: true
---

# kubectl-verbose-auth-can-i-list

## Command

```bash
kubectl -v=9 auth can-i --list
```

## Description

This command uses kubectl to query the Kubernetes API for all authorization rules applicable to the current user or Service Account, outputting a detailed list of permissions. The -v=9 flag enables maximum verbosity, logging the internal HTTP request (including the curl equivalent) to the authorization API endpoint. Use this to understand and replicate the API call for manual simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v=9 | Verbosity level (9 is maximum, shows raw API requests) | Yes |
| auth | Subcommand for authorization checks | Built-in |
| can-i | Checks if the subject can perform actions | Built-in |
| --list | Outputs all applicable rules in a table format | Yes |

## Examples

### Basic Usage

```bash
kubectl -v=9 auth can-i --list
```

Runs the check and logs the API interaction.

### Advanced Usage

```bash
KUBECONFIG=/path/to/config kubectl -v=9 auth can-i --list -n specific-namespace
```

Limits to a namespace; adjust config for token-based auth.

## Expected Output

Permissions table:

```
Resources                                         Non-Resource URLs  Resource Names  Verbs
---------                                         -----------------  --------------  -----
selfsubjectrulesreviews []                       []                 []               [create]
[*]                                              []                 []               [get list watch]
```

Followed by verbose logs:

```
I1028 18:58:38.193912   76118 round_trippers.go:419] curl -k -v -XPOST  -H "Accept: application/json, */*" -H "Content-Type: application/json" ... 'https://api-server:6443/apis/authorization.k8s.io/v1/selfsubjectrulesreviews'
I1028 18:58:38.295722   76118 round_trippers.go:438] POST ... 201 Created
```

Success is a 201 response with rules populated.

## Related

- [[procedures/Simulate-Kubectl-API-for-Self-Subject-Rules-Review]]
- [[commands/curl-post-selfsubjectrulesreview]]
