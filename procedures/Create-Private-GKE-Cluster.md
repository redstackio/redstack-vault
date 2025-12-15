---
id: proc-create-gke-001
tags:
  - gke
  - provisioning
  - kubernetes
type: procedure
tools:
  - '[[tools/gcloud]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/gcloud-create-private-gke-cluster]]'
verified: false
platforms:
  - GCP
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:01.451Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Create-Private-GKE-Cluster

## Summary

This procedure provisions a private Google Kubernetes Engine (GKE) cluster configured for testing DoS vulnerabilities, using specific settings for private nodes, network policies, and scopes to mimic a production-like isolated environment.

## Description

In the context of exploiting Kubernetes Validating Webhooks for DoS, a private GKE cluster is created to ensure the attack targets an isolated control plane without affecting production resources. The cluster uses Kubernetes version 1.17.14-gke.1600, a single preemptible node of type e2-medium, and enables features like private endpoint, IP aliasing, and network policies. This setup allows kubectl access from a bastion VM in the same VPC while keeping the control plane private. The procedure requires GCP permissions for container clusters and uses the gcloud CLI.

## Requirements

1. GCP project with Container Engine Admin role
2. gcloud CLI installed and authenticated
3. Existing VPC network and subnetwork in us-central1
4. Bastion VM for post-creation access

## Defense

Defensive measures and detection strategies:

- Monitor GCP audit logs for cluster creation events
- Use IAM policies to restrict cluster provisioning to approved users
- Enable VPC Service Controls to limit network access

## Objectives

1. Establish a testable Kubernetes environment
2. Ensure private connectivity for secure attack simulation
3. Prepare for webhook configuration

## Instructions

### Step 1: Authenticate and Set Project

**Context**: Ensure gcloud is set up for the target project.

**Command** ([[commands/gcloud-set-project]]):
```bash
gcloud config set project gkek8s-178117
```

> Sets the active project; expected output: Updated property [core/project].

### Step 2: Create the Private GKE Cluster

**Context**: Execute the cluster creation with all specified flags for private setup.

**Command** ([[commands/gcloud-create-private-gke-cluster]]):
```bash
gcloud beta container --project "gkek8s-178117" clusters create "sieve-clone-1" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.17.14-gke.1600" --release-channel "regular" --machine-type "e2-medium" --image-type "COS_CONTAINERD" --disk-type "pd-standard" --disk-size "60" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --max-pods-per-node "64" --preemptible --num-nodes "1" --no-enable-stackdriver-kubernetes --enable-private-nodes --enable-private-endpoint --enable-ip-alias --network "projects/gkek8s-178117/global/networks/external" --subnetwork "projects/gkek8s-178117/regions/us-central1/subnetworks/external" --default-max-pods-per-node "64" --enable-network-policy --enable-master-authorized-networks --addons HorizontalPodAutoscaling,NodeLocalDNS --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --workload-pool "gkek8s-178117.svc.id.goog" --enable-shielded-nodes --security-group "gke-security-groups@lonimbus.com"
```

> Provisions the cluster; expected output: Cluster 'sieve-clone-1' created, ready after ~5 minutes.

### Step 3: Verify Cluster Access

**Context**: Get kubeconfig and test connectivity from bastion.

**Command** ([[commands/gcloud-get-credentials]]):
```bash
gcloud container clusters get-credentials sieve-clone-1 --zone us-central1-c --project gkek8s-178117
```

> Updates kubeconfig; expected output: Fetching cluster endpoint and auth data.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/gcloud-create-private-gke-cluster]]
- [[commands/gcloud-set-project]]
- [[commands/gcloud-get-credentials]]

## Tools Used

- [[tools/gcloud]]

## Tags

- gke
- provisioning
- kubernetes
