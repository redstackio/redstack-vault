---
id: ac-sql-injection-xml-dynamics-ax
tags:
  - sqli
  - blind-sqli
  - time-based
  - xml
  - microsoft-dynamics-ax
  - mssql
type: attack_chain
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Endpoint-via-Subdomain-Enumeration]]'
  - '[[procedures/Test-Unrestricted-File-Uploads]]'
  - '[[procedures/Craft-XML-Payloads-for-Backend-Identification]]'
  - '[[procedures/Attempt-XXE-Exploitation]]'
  - '[[procedures/Test-SQL-Injection-in-XML-Nodes]]'
  - '[[procedures/Trigger-SQL-Error-with-Escaped-Apostrophe]]'
  - '[[procedures/Develop-Time-Based-Blind-SQLi-Payload]]'
  - '[[procedures/Automate-SQLi-Exploitation-with-sqlmap]]'
  - '[[procedures/Dump-Database-Contents-with-sqlmap]]'
step_count: 9
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.328Z'
description: >-
  Multi-stage attack exploiting SQL injection in an XML-processed web service
  endpoint for Microsoft Dynamics AX, leading to extraction of sensitive
  financial and payroll data from Microsoft SQL Server 2012.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based Blind SQL Injection via XML Endpoint to Extract Starbucks Accounting Database

Multi-stage attack chain demonstrating discovery and exploitation of a SQL injection vulnerability in a web service endpoint processing XML requests for Microsoft Dynamics AX, resulting in the extraction of nearly a million sensitive financial, accounting, and payroll records from a Microsoft SQL Server 2012 backend.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 9 |
| Execution Time | ~120 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Subdomain Enumeration] --> B[File Upload Testing]
    B --> C[XML Payload Crafting]
    C --> D[XXE Attempt]
    D --> E[SQLi Testing]
    E --> F[Apostrophe Escape]
    F --> G[Time-Based Payload]
    G --> H[sqlmap Automation]
    H --> I[Data Dumping]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#3498db
    style H fill:#27ae60
    style I fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlmap]]

### Target Environment

- Web platform with XML-processing endpoint
- Microsoft Dynamics AX integration
- Microsoft SQL Server 2012 backend
- Open HTTP/HTTPS ports (80/443)

### Initial Access Requirements

- No credentials required
- Public network access to target subdomains
- No prior access needed

## Detailed Attack Procedures

### Step 1: Discover Endpoint via Subdomain Enumeration
procedure: [[procedures/Discover-Endpoint-via-Subdomain-Enumeration]]

**Objective**: Identify hidden web service endpoints through subdomain discovery to expand the attack surface.

**Instructions**: Use tools like subfinder or Amass to enumerate subdomains of the target domain.

**Expected Output**: List of subdomains, including the vulnerable one mistaken for a file upload form.

**Success Indicators**:
- Subdomain with HTML file upload form identified
- Endpoint confirmed as processing XML

### Step 2: Test for Unrestricted File Uploads
procedure: [[procedures/Test-Unrestricted-File-Uploads]]

**Objective**: Probe the endpoint for file upload vulnerabilities to understand processing behavior.

**Instructions**: Attempt uploading malicious files like PHP shells and observe server responses for XML parsing clues.

**Expected Output**: Verbose error messages indicating XML processing without file persistence.

**Success Indicators**:
- Errors reveal XML handling
- No file saved, confirming non-standard upload

### Step 3: Craft XML Payloads for Backend Identification
procedure: [[procedures/Craft-XML-Payloads-for-Backend-Identification]]

**Objective**: Create valid XML structures to trigger backend processing and identify the application stack.

**Instructions**: Construct XML with nodes like <MainAccount>, <Credit>, <Debit>, <Invoice> and submit via HTTP POST.

**Expected Output**: Errors referencing Microsoft Dynamics AX, confirming enterprise accounting platform.

**Success Indicators**:
- Backend identified as Dynamics AX
- XML nodes processed in SQL context

### Step 4: Attempt XXE Exploitation
procedure: [[procedures/Attempt-XXE-Exploitation]]

**Objective**: Test for XML External Entity vulnerabilities to achieve code execution or DoS.

**Instructions**: Inject external entities in XML payload; attempt Billion Laughs for DoS validation.

**Expected Output**: DoS achieved but external entities blocked; no file read or SSRF.

**Success Indicators**:
- Billion Laughs triggers resource exhaustion
- XXE partially confirmed but limited

### Step 5: Test for SQL Injection in XML Nodes
procedure: [[procedures/Test-SQL-Injection-in-XML-Nodes]]

**Objective**: Identify injectable parameters in XML nodes likely used in SQL queries.

**Instructions**: Target numerical IDs in <MainAccount> node, suspecting WHERE clause usage; test basic injections.

**Expected Output**: Initial failures due to XML restrictions, but potential SQLi path identified.

**Success Indicators**:
- Node confirmed as SQL parameter
- Injection attempts reveal database interaction

### Step 6: Trigger SQL Error with Escaped Apostrophe
procedure: [[procedures/Trigger-SQL-Error-with-Escaped-Apostrophe]]

**Objective**: Bypass XML entity restrictions to inject SQL syntax and confirm vulnerability.

**Instructions**: Use &apos; entity in <MainAccount>123456&apos;</MainAccount> to inject apostrophe.

**Expected Output**: Database error triggered, confirming SQL injection.

**Success Indicators**:
- SQL syntax error in response
- Vulnerability type validated as SQLi

### Step 7: Develop Time-Based Blind SQLi Payload
procedure: [[procedures/Develop-Time-Based-Blind-SQLi-Payload]]

**Objective**: Craft manual payloads for blind extraction where no direct output is visible.

**Instructions**: Build time-delay payloads using WAITFOR DELAY for Microsoft SQL Server.

**Expected Output**: Response delays confirming true/false conditions.

**Success Indicators**:
- Consistent delays on true conditions
- Blind SQLi viable for data exfil

### Step 8: Automate SQLi Exploitation with sqlmap
procedure: [[procedures/Automate-SQLi-Exploitation-with-sqlmap]]

**Objective**: Use automation to confirm backend and prepare for data extraction.

**Instructions**: Run sqlmap with --tamper=htmlencode to handle XML entities; target the endpoint URL.

```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml>payload</xml>" --tamper=htmlencode --dbms=mssql --technique=T
```

**Expected Output**: Backend confirmed as Microsoft SQL Server 2012; injection points validated.

**Success Indicators**:
- DBMS fingerprint successful
- Time-based technique confirmed

### Step 9: Dump Database Contents with sqlmap
procedure: [[procedures/Dump-Database-Contents-with-sqlmap]]

**Objective**: Extract sensitive data from the main accounting table.

**Instructions**: Research Dynamics AX schema for main table (e.g., LedgerJournalTrans); dump using --dump.

```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml>payload</xml>" --tamper=htmlencode --dbms=mssql --tables -D dynamics_ax_db --dump -T LedgerJournalTrans
```

**Expected Output**: Nearly 1 million rows of financial, accounting, and payroll data up to previous year.

**Success Indicators**:
- Data dumped successfully
- Sensitive info like accounts and payroll exposed

## Attack Chain Summary

### Key Achievements

1. Discovered hidden XML endpoint via enumeration
2. Confirmed SQLi through entity escaping and time-based blind techniques
3. Extracted enterprise database with critical financial data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
