---
id: 4c6b127f-d219-42d0-a505-71fb63e2960e
name: Deploy Container
type: technique
mitre_id: T1610
mitre_url: null
created_at: '2023-04-06T00:31:26.162332+00:00'
updated_at: '2023-04-06T03:56:38.776204+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Docker Security Assessment]]'
- '[[Server-Side Request Forgery for Docker Containers and Images Enumeration]]'
---

# Deploy Container

**MITRE ID**: T1610

## Description

Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases, adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user limitations, etc. to bypass existing defenses within the environment.

Containers can be deployed by various means, such as via Docker's <code>create</code> and <code>start</code> APIs or via a web application such as the Kubernetes dashboard or Kubeflow.(Citation: Docker Containers API)(Citation: Kubernetes Dashboard)(Citation: Kubeflow Pipelines) Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime.(Citation: Aqua Build Images on Hosts)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (2)

- [[Docker Security Assessment]]
- [[Server-Side Request Forgery for Docker Containers and Images Enumeration]]
