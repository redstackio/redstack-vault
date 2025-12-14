---
data: >-
  gcloud beta container --project "copper-frame-263204" clusters create
  "hostmitm" --zone "us-central1-c" --no-enable-basic-auth --cluster-version
  "1.14.10-gke.36" --machine-type "n1-standard-1" --image-type "COS" --disk-type
  "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true
  --scopes
  "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append"
  --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network
  "projects/copper-frame-263204/global/networks/default" --subnetwork
  "projects/copper-frame-263204/regions/us-central1/subnetworks/default"
  --default-max-pods-per-node "110" --no-enable-master-authorized-networks
  --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade
  --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0
tags:
  - gke
  - cluster
type: command
output: null
executor: bash
platforms:
  - Cloud (GCP)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.897Z'
id: b4a94ca6-90a7-48e8-b48c-a6ce13a3fe8a
verified: false
validated: true
submitted: true
---
# gcloud-create-gke-cluster

## Command

```bash
gcloud beta container --project "copper-frame-263204" clusters create "hostmitm" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.14.10-gke.36" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/copper-frame-263204/global/networks/default" --subnetwork "projects/copper-frame-263204/regions/us-central1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0
```

## Description

Creates a GKE cluster for testing Kubernetes vulnerabilities, using beta features, specific version, machine type, and scopes to mimic a vulnerable setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --project | GCP project ID | Yes |
| --zone | Compute zone | Yes |
| --cluster-version | Kubernetes version | Yes |
| --machine-type | Node machine type | Yes |
| --num-nodes | Number of nodes | Yes |
| --scopes | OAuth scopes for nodes | No |

## Examples

### Basic Usage

```bash
gcloud beta container clusters create my-cluster --zone us-central1-a
```

### Advanced Usage

```bash
gcloud beta container clusters create hostmitm --project copper-frame-263204 --zone us-central1-c --cluster-version 1.14.10-gke.36 --num-nodes 3 --machine-type n1-standard-1
```

## Expected Output

Cluster 'hostmitm' created. kubeconfig entry updated.

## Related

- [[procedures/Create-GKE-Cluster-for-Vulnerability-Testing]]
