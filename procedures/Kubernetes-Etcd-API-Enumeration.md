---
id: 8889cf25-f63e-4dc3-87f4-15f5df18a723
name: Kubernetes-Etcd-API-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.488408+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network-Service-Discovery|T1046 - Network Service Discovery]]'
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/API addresses that you should know]]'
  - '[[tags/etcd API]]'
  - '[[tags/Kubernetes]]'
commands:
  - '[[commands/curl-etcd-endpoint-check]]'
  - '[[commands/curl-etcd-version]]'
  - '[[commands/etcdctl-get-keys]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes-Etcd-API-Enumeration

## Summary

This procedure enumerates the etcd API endpoints in a Kubernetes cluster to discover configuration data stored in the distributed key-value store. It involves checking endpoint accessibility, retrieving the etcd version, and extracting keys from the database, enabling attackers to gather sensitive cluster information such as secrets and configurations for further exploitation.

## Description

etcd serves as the primary data store for Kubernetes, holding all cluster state including pods, services, secrets, and configurations. Enumerating the etcd API allows discovery of these endpoints, typically exposed on port 2379, to read keys and values that may contain sensitive data. This technique is useful in post-compromise scenarios where an attacker has network access to the control plane or master nodes. The process uses HTTP/HTTPS requests via curl for basic probing and etcdctl for deeper interaction, assuming no or weak authentication on the etcd server. Success reveals the cluster's architecture and data, aiding in lateral movement or persistence. Prerequisites include network reachability to the etcd port and, for etcdctl, the tool installed on the attacker's system.

## Requirements

1. Network access to the Kubernetes master node or etcd endpoints (typically port 2379/TCP).
2. etcdctl tool installed (for key enumeration; can be installed via package manager or binary download).
3. Basic authentication credentials if etcd is secured (procedure assumes unauthenticated access for simplicity; adjust with --user flag if needed).
4. Target IP address of the master node or etcd cluster member.

## Defense

- Restrict etcd API exposure: Bind etcd to localhost or internal networks only, avoiding public internet access.
- Implement RBAC and authentication: Use client certificates, TLS, and API keys to protect etcd endpoints.
- Encrypt data at rest and in transit: Enable etcd encryption to protect sensitive keys like secrets.
- Monitor access: Log etcd API calls and alert on unauthorized queries using tools like Prometheus or audit logs.
- Network segmentation: Place etcd behind firewalls, allowing only kube-apiserver access.

## Objectives

1. Verify accessibility of etcd API endpoints on the target Kubernetes cluster.
2. Retrieve the etcd server version to assess compatibility and potential vulnerabilities.
3. Enumerate keys stored in etcd to identify configuration data and sensitive information.

## Instructions

### Step 1: Check etcd Endpoint Accessibility

**Context**: Probe the etcd endpoint to confirm it is reachable and responding, which indicates potential exposure. This step uses a simple HTTPS request to the default port, ignoring certificate validation for testing.

**Command** ([[commands/curl-etcd-endpoint-check]]):
```bash
curl -k https://$_TARGET_IP:2379
```

> This command sends a GET request to the root etcd path. If successful, it returns a JSON response indicating the endpoint is active; otherwise, it shows connection errors or refusals.

### Step 2: Retrieve etcd Version

**Context**: Query the version endpoint to gather information about the etcd server, which can reveal the build details and help identify exploitable versions (e.g., older versions with known CVEs).

**Command** ([[commands/curl-etcd-version]]):
```bash
curl -k https://$_TARGET_IP:2379/version
```

> Expect a JSON response with fields like 'etcdserver', 'etcdcluster', and build details. This confirms the API version and aids in tailoring further interactions.

### Step 3: Enumerate etcd Keys

**Context**: Use etcdctl to list all keys in the database with a prefix search from the root, providing an overview of stored data without retrieving values (to avoid large outputs). This reveals paths to sensitive configurations like /registry/secrets.

**Command** ([[commands/etcdctl-get-keys]]):
```bash
etcdctl --endpoints=https://$_TARGET_IP:2379 get / --prefix --keys-only
```

> The output lists keys in a hierarchical format, such as /registry/configmaps/default/myapp. Success is indicated by a list of keys; empty output may mean authentication is required or no data at root.
