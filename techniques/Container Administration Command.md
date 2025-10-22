---
id: eaef2e48-7c40-43d5-b64b-1b680fd2dde7
name: Container Administration Command
type: technique
mitre_id: T1609
mitre_url: null
created_at: '2023-04-06T00:31:26.404204+00:00'
updated_at: '2023-04-06T03:56:16.945589+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Docker Security Assessment]]'
- '[[Mounted Docker Socket Pentest]]'
---

# Container Administration Command

**MITRE ID**: T1609

## Description

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.(Citation: Docker Daemon CLI)(Citation: Kubernetes API)(Citation: Kubernetes Kubelet)

In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as <code>docker exec</code> to execute a command within a running container.(Citation: Docker Entrypoint)(Citation: Docker Exec) In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as <code>kubectl exec</code>.(Citation: Kubectl Exec Get Shell)

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (2)

- [[Docker Security Assessment]]
- [[Mounted Docker Socket Pentest]]
