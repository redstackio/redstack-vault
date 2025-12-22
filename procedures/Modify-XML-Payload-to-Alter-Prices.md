---
tags:
  - xml-tampering
  - parameter-modification
  - price-alteration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.459Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cad44a97-0f87-4ba7-aafe-a17e94e86922
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-XML-Payload-to-Alter-Prices

## Summary

This procedure involves editing the XML payload in an intercepted POST request to change product price values, exploiting the lack of server-side validation in e-commerce checkout workflows.

## Description

Targeted at systems like Adobe's e-commerce platform, this step modifies price parameters in XML (e.g., changing <price>100.00</price> to <price>0.00</price>) to enable purchases at arbitrary costs. The attack relies on client-side trust in the payload without integrity checks on the server. Prerequisites include an intercepted request from the prior step. Outcomes include a tampered payload ready for submission, potentially leading to financial loss.

## Requirements

1. Intercepted POST request with XML payload
2. Proxy tool capable of request editing (e.g., Burp Suite)
3. Knowledge of XML structure and price tag locations
4. Valid session cookie from the original request

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation and sanitization of all input parameters
- Use signed or hashed payloads to detect tampering
- Implement rate limiting on checkout requests and log anomalies in price values

## Objectives

1. Alter price parameters to unauthorized values
2. Maintain XML validity to bypass parsing errors
3. Prepare payload for seamless server processing

## Instructions

### Step 1: Locate Price Parameters

**Context**: Identify editable elements in the XML body of the intercepted request.

In the proxy tool, switch to the request editor and search for price-related tags in the XML (e.g., <price> or <amount>).

### Step 2: Edit Values

**Context**: Change the numerical values to desired amounts, ensuring the XML remains syntactically correct.

Modify the tag contents, e.g., replace "100.00" with "0.00" for all relevant items. Use the proxy's XML viewer if available to validate structure.

**Expected Output**: Updated XML with altered prices, e.g., <item><name>Product</name><price>0.00</price></item>.

### Step 3: Validate Modification

**Context**: Ensure changes do not introduce errors that would reject the request.

Preview the full request and check for well-formed XML using built-in tools or external validators.

**Expected Output**: No syntax errors in the modified payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xml-tampering]]
- [[parameter-modification]]
- [[price-alteration]]
