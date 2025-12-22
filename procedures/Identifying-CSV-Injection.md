---
id: a0b2a32f-bd84-4bc6-8829-691595fab328
name: Identifying-CSV-Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T18:08:48.242789+00:00'
updated_at: '2023-05-26T01:08:37.345596+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - '[[tags/CSV Injection]]'
  - '[[tags/injection]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Identifying-CSV-Injection

## Summary

This procedure demonstrates how to test for CSV injection vulnerabilities in web applications that allow user input to be exported into CSV files. By injecting formulas or malicious expressions into input fields that appear in exported CSVs, attackers can potentially execute code when the file is opened in spreadsheet software like Microsoft Excel, leading to client-side execution.

## Description

CSV injection occurs when an application fails to sanitize user-supplied input before including it in a CSV export. This allows attackers to embed formulas (e.g., starting with '=') that execute automatically upon opening the file in Excel. Common scenarios involve comment fields, user profiles, or any data exported via CSV. This procedure tests the vulnerability by injecting a simple formula like '=1+2' and verifying if it executes in the exported file. It targets web applications with user authentication and CSV download features, such as e-commerce or inventory management systems. Successful identification confirms lack of input validation, enabling further exploitation like data exfiltration or command execution via DDE or macros.

## Requirements

1. Access to a web application with user input fields (e.g., comment or remarks box) and a CSV export functionality.
2. Valid user account for submitting input; administrative or privileged account for viewing and exporting the data.
3. Spreadsheet software like Microsoft Excel to open and verify the exported CSV.
4. No special tools required beyond a web browser for interaction.

## Defense

Defensive measures and detection strategies:

- Sanitize all user input by prefixing with a single quote (') or using CSV-aware escaping libraries like Apache Commons CSV.
- Disable automatic formula calculation in Excel or use protected view for downloaded files.
- Implement content security policies (CSP) and validate input to block formula characters (=, +, -, @).
- Monitor for anomalous CSV downloads or input patterns containing formula syntax.

## Objectives

1. Inject a test formula into a user-controlled input field that is included in CSV exports.
2. Verify that the formula is preserved without sanitization in the exported CSV.
3. Confirm execution of the formula when the CSV is opened in a spreadsheet application.
4. Identify the vulnerability for remediation or further exploitation assessment.

## Instructions

### Step 1: Identify and Access the Input Field

**Context**: Locate a feature in the web application where user input is collected and later exported to CSV, such as a product return comment box. This step ensures you target a field that influences the export content.

Navigate to the relevant form (e.g., 'Return Product' function) using your standard user account. Enter a test formula in the input field, such as '=1+2', which should evaluate to 3 if vulnerable.

Submit the form to save the input.

### Step 2: Verify Input Persistence as Privileged User

**Context**: Switch to an administrative view to confirm the injected input is stored and displayed without alteration, setting up the export test.

Log in as an admin user and navigate to the section displaying the submitted data (e.g., 'Return Products List' under 'User Comments').

Observe if the formula '=1+2' appears unchanged in the list.

### Step 3: Export Data to CSV

**Context**: Trigger the CSV export to include the vulnerable input, allowing verification of sanitization failures.

From the admin view, select the 'Download CSV' option for the list containing the injected input.

Save the generated CSV file to your local system.

### Step 4: Validate Formula Execution

**Context**: Open the CSV in spreadsheet software to check if the formula executes, confirming the injection vulnerability.

Open the CSV file in Microsoft Excel or compatible software.

Check the cell containing the injected input (e.g., 'remarks' column). If vulnerable, it should display the evaluated result '3' instead of the literal '=1+2'.

If the formula does not execute, test variations like '=cmd|/c calc'!A0 or more complex payloads to assess severity.
