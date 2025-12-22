---
tags:
  - broken-access-control
  - request-tampering
  - airflow
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Apache Airflow
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:56.889Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3b6e0cb6-a514-4244-a1a7-b103a11a9b40
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Airflow-DAG-Run-Edit-Permissions-via-Request-Tampering

## Summary

This procedure exploits a Broken Access Control vulnerability in Apache Airflow (versions before 2.7.1) by using an authenticated user with only DAG-view permissions to tamper with HTTP requests, allowing unauthorized modifications to DAG run configurations such as the Conf parameter and start dates. This can lead to altered workflow executions and potential disruptions in automated data pipelines.

## Description

In Apache Airflow's web interface, users with view-only permissions see disabled fields like Conf in the DAG run edit view, enforced client-side. However, the server-side lacks proper validation, accepting tampered requests. An attacker navigates to DAG Runs, attempts an edit, intercepts the save request with a tool like Burp Suite, modifies restricted parameters, and submits, resulting in unauthorized updates. This affects Python-based Airflow deployments and requires web UI access.

## Requirements

1. Authenticated access to Apache Airflow web UI with DAG-view permissions (but not edit permissions)
2. Proxy tool like Burp Suite configured to intercept traffic from the browser
3. Target running Apache Airflow < 2.7.1 on a web-accessible platform
4. Basic knowledge of HTTP request manipulation

## Defense

Defensive measures and detection strategies:

- Upgrade to Apache Airflow 2.7.1 or later to enforce server-side permission checks
- Implement request validation on the backend to verify user permissions for DAG run modifications
- Monitor audit logs for unexpected DAG run updates from low-privilege users
- Use web application firewalls (WAF) to detect anomalous POST requests to DAG endpoints

## Objectives

1. Bypass client-side restrictions to modify restricted DAG run fields
2. Alter workflow configurations to potentially inject malicious parameters or change execution timing
3. Demonstrate impact on automated pipeline integrity

## Instructions

### Step 1: Navigate to DAG Runs

**Context**: Access the interface to list and select DAG runs for targeting.

No specific command; use the web UI: Browse > DAG Runs.

> This loads the list of DAG runs. Expected output: Table of runs with details like state and start time.

### Step 2: Select and Open Edit View

**Context**: Enter the edit mode to trigger the restricted form.

No specific command; click on a DAG run row.

> Edit interface opens. Expected output: Form with grayed-out Conf field.

### Step 3: Identify Restrictions

**Context**: Confirm client-side enforcement of permissions.

Inspect the form elements in browser dev tools.

> Conf textbox is disabled (readonly or hidden input). Expected output: Visual/JS confirmation of restrictions.

### Step 4: Intercept and Tamper Request

**Context**: Capture the save action and modify parameters.

Configure Burp Suite proxy, click Save, intercept POST to /dagrun/edit (or similar), change 'conf' to '1111111111111'.

> Request body altered. Expected output: Proxy shows modified JSON/form data with new conf value.

### Step 5: Submit and Validate

**Context**: Forward the request and check for successful update.

Forward in Burp, refresh the DAG run page.

> Server processes without error. Expected output: Conf field now shows '1111111111111'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- broken-access-control
- request-tampering
- airflow
- web-exploit
