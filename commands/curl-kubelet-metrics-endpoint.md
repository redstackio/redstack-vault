---
id: 1f928f60-7125-4a99-b5a8-42bafd42329b
name: curl-kubelet-metrics-endpoint
type: command
executor: bash
data: 'curl -k https://$_IP_ADDRESS:10250/metrics'
output: null
created_at: '2023-04-06T03:56:01.511004+00:00'
updated_at: '2023-04-10T20:34:01.313707+00:00'
platforms:
  - Linux
  - Kubernetes
tags:
  - discovery
  - kubernetes
  - kubelet
  - metrics
verified: true
validated: true
---

# curl-kubelet-metrics-endpoint

## Command

```bash
curl -k https://$_IP_ADDRESS:10250/metrics
```

## Description

This command fetches Prometheus metrics from the Kubelet API, providing insights into node and pod resource usage. Ideal for identifying resource-heavy workloads in a Kubernetes cluster.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IP_ADDRESS | IP address of the target Kubernetes worker node | Yes |
| -k | Ignore SSL certificate errors | Yes |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:10250/metrics
```

### Save to File

```bash
curl -k https://192.168.1.100:10250/metrics > kubelet_metrics.txt
```

## Expected Output

Text-based metrics in Prometheus format:
```
# HELP kubelet_running_pods Number of pods currently running on the node
# TYPE kubelet_running_pods gauge
kubelet_running_pods 5
# HELP kubelet_cpu_usage_total CPU usage
# TYPE kubelet_cpu_usage_total counter
kubelet_cpu_usage_total 123.45
```

## Related

- [[procedures/Kubelet-API-Enumeration-via-Curl]]
- [[commands/curl-kubelet-root-endpoint]]
