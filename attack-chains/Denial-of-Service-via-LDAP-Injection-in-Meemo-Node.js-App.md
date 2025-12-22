---
tags:
  - ldap-injection
  - dos
  - node-js
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/MongoDB]]'
  - '[[tools/git]]'
  - '[[tools/npm]]'
  - '[[tools/gulp]]'
  - '[[tools/node]]'
  - '[[tools/ldapjstestserver]]'
  - '[[tools/Python]]'
  - '[[tools/requests]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Node.js
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Meemo-Environment-with-LDAP]]'
  - '[[procedures/Verify-Normal-Meemo-Functionality]]'
  - '[[procedures/Exploit-LDAP-Injection-for-DoS]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.292Z'
description: >-
  Multi-stage attack chain exploiting LDAP Injection in the meemo-app Node.js
  module to cause memory exhaustion and server crash via crafted login requests.
skill_level: intermediate
impact_level: high
id: 8d8a4b83-70a7-42dd-8de3-c0737e96f768
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Denial of Service via LDAP Injection in Meemo Node.js App

Multi-stage attack chain demonstrating exploitation of an LDAP Injection vulnerability in the meemo-app Node.js module. The attack involves setting up a local environment to reproduce the vulnerable application, verifying normal operation, and then sending a crafted payload via the /api/login endpoint to inject malicious LDAP filter syntax, resulting in massive filter expansion that exhausts Node.js memory and crashes the server, causing Denial of Service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Environment Setup] --> B[Verify Functionality]
    B --> C[Exploit LDAP Injection]
    C --> D[Server Crash - DoS Achieved]

    style A fill:#3498db
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[tools/MongoDB]]
- [[tools/git]]
- [[tools/npm]]
- [[tools/gulp]]
- [[tools/node]]
- [[tools/ldapjstestserver]]
- [[tools/Python]]
- [[tools/requests]]

### Target Environment

- Linux (Ubuntu recommended)
- Node.js v14.2.0 or compatible
- Ports 3000 (app), 3002 (LDAP server), MongoDB default port
- GitHub access for cloning repository
- Local network access to localhost

### Initial Access Requirements

- No remote credentials needed; local setup for reproduction
- Administrative privileges for MongoDB service start
- Python environment with requests library

## Detailed Attack Procedures

### Step 1: Environment Setup
procedure: [[procedures/Setup-Meemo-Environment-with-LDAP]]

**Objective**: Prepare a local vulnerable instance of the meemo app with MongoDB and simulated LDAP backend to enable testing of the LDAP Injection vulnerability.

**Instructions**: Follow the procedure to install dependencies, clone the repo, build the app, and start services. Use [[commands/start-mongodb-service]] to initialize the database:

```bash
sudo systemctl start mongod
```

Create testing directory with [[commands/create-poc-directory]]:

```bash
mkdir poc
cd poc/
```

Clone and setup with [[commands/clone-meemo-repo]] and [[commands/install-npm-dependencies]]:

```bash
git clone https://github.com/nebulade/meemo.git
cd meemo
npm i
```

Build with [[commands/build-meemo-app]]:

```bash
./node_modules/.bin/gulp
```

Start LDAP server using [[commands/start-ldap-test-server]]:

```bash
node ldapjstestserver.js
```

Launch app with [[commands/start-meemo-app-with-ldap]]:

```bash
CLOUDRON_LDAP_BIND_DN="cn=admin,ou=users,dc=example" CLOUDRON_LDAP_BIND_PASSWORD="password" CLOUDRON_LDAP_USERS_BASE_DN="ou=users,dc=example" CLOUDRON_LDAP_URL="ldap://localhost:3002" node app.js
```

**Expected Output**: MongoDB running, app accessible at http://localhost:3000, LDAP server on port 3002.

**Success Indicators**:
- No errors in service starts
- App logs show successful initialization with LDAP enabled

### Step 2: Verify Normal Functionality
procedure: [[procedures/Verify-Normal-Meemo-Functionality]]

**Objective**: Confirm the application operates correctly under normal conditions before exploitation to establish a baseline.

**Instructions**: Access the app via web browser and perform a standard login. Visit http://localhost:3000/, enter username 'normal' and password 'test', then logout.

**Expected Output**: Successful login and logout without errors; user profile loads via LDAP lookup.

**Success Indicators**:
- App UI responsive
- LDAP authentication succeeds for valid credentials
- No crashes or memory issues

### Step 3: Exploit LDAP Injection
procedure: [[procedures/Exploit-LDAP-Injection-for-DoS]]

**Objective**: Inject malicious LDAP filter syntax via the login endpoint to create an exponentially large query, exhausting Node.js heap memory and crashing the server.

**Instructions**: Use a Python script with [[tools/requests]] to POST a crafted payload to /api/login. The payload username is ")" + "(cn=*)" * 700000 + "(cn=*", which alters the filter in src/users.js to generate a massive OR expression.

**Expected Output**: Node.js process throws 'JavaScript heap out of memory' error and crashes; service becomes unavailable.

**Success Indicators**:
- Server logs show memory exhaustion
- App unresponsive on subsequent requests
- Process termination observed

## Attack Chain Summary

### Key Achievements

1. Successful local reproduction of the vulnerable meemo app with LDAP integration
2. Baseline verification of normal LDAP user lookup functionality
3. Exploitation causing DoS through unsanitized input leading to filter bloat and crash

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
