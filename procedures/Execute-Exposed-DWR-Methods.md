---
tags:
  - information-disclosure
  - dwr
  - method-execution
  - exploitation
type: procedure
tools:
  - '[[tools/Firefox-Web-Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:52.000Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 223d86b0-5e68-4f1e-8fd5-ee0e4d93f063
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Exposed-DWR-Methods

## Summary

This procedure demonstrates interacting with the exposed DWR interface to view and execute available classes and methods, including hidden admin and test functions, to uncover additional vulnerabilities such as SQL injection or XSS in the underlying implementation.

## Description

Once the DWR default page is accessed, it provides an interactive interface where attackers can select classes (e.g., those handling database operations or user rendering) and invoke their methods directly via JavaScript-generated RPC calls. No authentication is enforced, allowing execution of sensitive operations like querying databases or rendering user inputs. This can reveal error messages exposing SQL syntax (indicating injection points) or reflected inputs (suggesting XSS). The procedure targets poorly secured DWR setups where debug features are not disabled, leading to information disclosure and potential escalation to full compromise. Expected outcomes include method outputs that confirm insecure functions, with prerequisites being successful access to the DWR page and basic understanding of the listed classes.

## Requirements

1. Successful access to the DWR default page from the prior procedure
2. Web browser with JavaScript enabled for method execution
3. Optional: Knowledge of expected method parameters from disclosed class details

## Defense

Defensive measures and detection strategies:

- Disable DWR's debug mode and controller exposure in configuration files (e.g., dwr.xml) to prevent method listing and execution.
- Use web application firewalls (WAFs) like ModSecurity to block requests to /dwr/* or detect anomalous RPC calls.
- Log and analyze DWR invocation attempts, flagging executions of admin/test methods and correlating with access logs for anomaly detection.

## Objectives

1. Execute unauthorized methods to gather detailed internal information.
2. Identify insecure functions vulnerable to injection or scripting attacks.
3. Chain discoveries into broader exploitation for data access or manipulation.

## Instructions

### Step 1: Browse Available Classes and Methods

**Context**: Use the DWR interface to enumerate and select targets for execution.

In the browser, scroll through the page to view the list of classes and their methods.

> Click on a class name to expand its methods. Note any with names suggesting sensitivity, like 'adminLogin' or 'testQuery'.
>
> Expected output: Detailed method signatures, including parameter types (e.g., String query for a database method).

### Step 2: Execute Sample Methods

**Context**: Invoke methods to test for outputs and vulnerabilities.

Select a method, enter test parameters if required, and submit the execution.

> For example, for a method like 'executeSQL(String sql)', input a benign query like 'SELECT 1' and execute. Observe the response for direct results or errors.
>
> Expected output: JSON or HTML response with execution results, potentially including database errors (e.g., SQL syntax hints) or rendered content (e.g., unescaped user input indicating XSS).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Firefox-Web-Browser]]

## Tags

- information-disclosure
- dwr
- exploitation
- method-execution
