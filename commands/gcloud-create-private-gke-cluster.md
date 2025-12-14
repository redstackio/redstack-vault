---
id: cmd-gcloud-cluster-001
data: >-
  gcloud beta container --project "gkek8s-178117" clusters create
  "sieve-clone-1" --zone "us-central1-c" --no-enable-basic-auth
  --cluster-version "1.17.14-gke.1600" --release-channel "regular"
  --machine-type "e2-medium" --image-type "COS_CONTAINERD" --disk-type
  "pd-standard" --disk-size "60" --metadata disable-legacy-endpoints=true
  --scopes
  "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append"
  --max-pods-per-node "64" --preemptible --num-nodes "1"
  --no-enable-stackdriver-kubernetes --enable-private-nodes
  --enable-private-endpoint --enable-ip-alias --network
  "projects/gkek8s-178117/global/networks/external" --subnetwork
  "projects/gkek8s-178117/regions/us-central1/subnetworks/external"
  --default-max-pods-per-node "64" --enable-network-policy
  --enable-master-authorized-networks --addons
  HorizontalPodAutoscaling,NodeLocalDNS --enable-autoupgrade --enable-autorepair
  --max-surge-upgrade 1 --max-unavailable-upgrade 0 --workload-pool
  "gkek8s-178117.svc.id.goog" --enable-shielded-nodes --security-group
  "gke-security-groups@lonimbus.com"
tags:
  - gke
  - provisioning
type: command
output: Cluster 'sieve-clone-1' created. kubeconfig entry generated for sieve-clone-1.
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.400Z'
verified: false
validated: true
submitted: true
---
# gcloud-create-private-gke-cluster

## Command

```bash
gcloud beta container --project "gkek8s-178117" clusters create "sieve-clone-1" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.17.14-gke.1600" --release-channel "regular" --machine-type "e2-medium" --image-type "COS_CONTAINERD" --disk-type "pd-standard" --disk-size "60" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --max-pods-per-node "64" --preemptible --num-nodes "1" --no-enable-stackdriver-kubernetes --enable-private-nodes --enable-private-endpoint --enable-ip-alias --network "projects/gkek8s-178117/global/networks/external" --subnetwork "projects/gkek8s-178117/regions/us-central1/subnetworks/external" --default-max-pods-per-node "64" --enable-network-policy --enable-master-authorized-networks --addons HorizontalPodAutoscaling,NodeLocalDNS --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --workload-pool "gkek8s-178117.svc.id.goog" --enable-shielded-nodes --security-group "gke-security-groups@lonimbus.com"
```

## Description

Creates a private GKE cluster with specific configurations for testing, including private nodes and endpoint to isolate the environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--project` | GCP project ID | Yes |
| `--zone` | Compute zone | Yes |
| `--cluster-version` | Kubernetes version | Yes |
| `--machine-type` | Node machine type | Yes |
| `--num-nodes` | Number of nodes | Yes |
| `--enable-private-nodes` | Enable private nodes | Yes |
| `--enable-private-endpoint` | Enable private API endpoint | Yes |

## Examples

### Basic Usage

```bash
gcloud beta container clusters create my-cluster --zone us-central1 --num-nodes 1
```

### Advanced Usage

Use the full command above for private setup.

## Expected Output

Cluster creation progress, ending with "Created [CLUSTER_URI]" and kubeconfig update.

## Related

- [[Related Procedure: Create-Private-GKE-Cluster]]
