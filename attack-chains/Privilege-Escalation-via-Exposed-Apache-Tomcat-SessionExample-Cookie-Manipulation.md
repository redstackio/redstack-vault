---
id: ac-77679-01
tags:
  - tomcat
  - privilege-escalation
  - cookie-manipulation
  - web-vuln
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Exposed-Tomcat-SessionExample-for-Cookie-Manipulation]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.834Z'
description: >-
  Attack chain exploiting publicly exposed Apache Tomcat Servlet Examples on
  wmf.ok.ru to manipulate cookies and achieve privilege escalation on the ok.ru
  platform.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Privilege Escalation via Exposed Apache Tomcat SessionExample Cookie Manipulation

Multi-stage attack chain demonstrating a complete attack workflow targeting the exposed Tomcat examples on wmf.ok.ru, leading to unauthorized session manipulation and privilege escalation on ok.ru.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Endpoint] --> B[Cookie Manipulation and Escalation]
    B --> C[Privilege Escalation Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser (e.g., Firefox or Chrome for manual interaction)
- [[tools/curl]]

### Target Environment

- Web platform with Apache Tomcat server
- Exposed servlet examples endpoint (e.g., /examples/jsp/snp/sessions/SessionExample)
- Network access to public subdomain (wmf.ok.ru)

### Initial Access Requirements

- No credentials required (public exposure)
- Direct internet access to the target subdomain
- No prior access needed

## Detailed Attack Procedures

### Step 1: Discovery and Exploitation of Exposed Tomcat Examples
procedure: [[procedures/Exploit-Exposed-Tomcat-SessionExample-for-Cookie-Manipulation]]

**Objective**: Identify the publicly accessible Tomcat Servlet Examples and exploit the SessionExample script to manipulate cookies, enabling privilege escalation on the associated ok.ru platform.

**Instructions**: Begin by accessing the exposed endpoint using a browser or [[commands/curl-access-endpoint]] to verify availability:

```bash
curl -v http://wmf.ok.ru/examples/jsp/snp/sessions/SessionExample
```

Navigate to the SessionExample interface, which allows setting and viewing session attributes via insecure forms. Use the form to inject or modify cookie values that correspond to ok.ru session tokens, simulating privilege escalation by altering user roles or IDs.

For manual testing, open the URL in a browser, interact with the session creation form, and submit manipulated cookie data (e.g., via developer tools) to override session parameters.

**Expected Output**: Successful access returns the SessionExample page with forms for session attribute manipulation; manipulated cookies result in altered session behavior, confirming escalation potential.

**Success Indicators**:
- HTTP 200 response on endpoint access
- Ability to set arbitrary session attributes without authentication
- Observed changes in ok.ru session privileges upon cookie injection
