---
id: 1a0538d4-a182-4782-aab1-09a3d6fbec11
name: oracle-sqli-query-database-type-and-version
type: procedure
verified: true
submitted: true
created_at: '2020-08-28T15:26:14.195419+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp-top-10
  - sql
  - sqli
  - sql-injection
  - web-applications
commands:
  - '[[commands/curl-oracle-sqli-union-select-version]]'
platforms:
  - Web
tools: []
validated: true
---

# oracle-sqli-query-database-type-and-version

## Summary

This procedure demonstrates a union-based SQL injection attack on an Oracle database to extract the database type and version information. It involves identifying the number of columns in the vulnerable query through trial-and-error payloads and then crafting a UNION SELECT statement to query the v$version view, retrieving the BANNER field which contains the Oracle version details. This technique is useful for reconnaissance during web application penetration testing to understand the backend database and plan further exploitation.

## Description

Union-based SQL injection exploits vulnerabilities in web applications where user input is not properly sanitized, allowing attackers to append SQL queries that union results with the original query. For Oracle databases, the v$version view provides system information including the database banner, which reveals the exact version (e.g., "Oracle Database 19c Enterprise Edition Release 19.0.0.0.0"). The attack requires determining the number of columns in the original SELECT statement by injecting payloads with increasing numbers of NULL values until no error occurs or data aligns properly. Once matched, the payload replaces NULLs with actual queries like SELECT BANNER FROM v$version. This procedure assumes a GET parameter vulnerability (e.g., ?category=) and is typically performed manually via browser or automated with tools like curl or Burp Suite. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactics Initial Access (TA0001) and Collection (TA0009), as it enables unauthorized data retrieval from public-facing web apps.

## Requirements

1. Valid access to a web application vulnerable to SQL injection in a GET parameter (e.g., search or category filter).
2. Basic knowledge of SQL syntax and Oracle-specific views like v$version.
3. Network connectivity to the target application (no authentication required for the vulnerable endpoint).
4. Optional: Intercepting proxy like Burp Suite for payload crafting and response analysis.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries to prevent injection.
- Implement a Web Application Firewall (WAF) to detect and block UNION SELECT patterns or anomalous SQL keywords.
- Enable database logging to monitor queries against system views like v$version.
- Input validation: Whitelist allowed characters and escape special SQL characters in user inputs.
- Regular vulnerability scanning with tools like SQLMap to identify injection points.

## Objectives

1. Confirm SQL injection vulnerability in the target parameter.
2. Determine the number of columns in the backend query to craft a valid UNION payload.
3. Extract Oracle database version information for further reconnaissance or exploitation planning.
4. Validate success by observing the banner data in the application response.

## Instructions

### Step 1: Identify Injectable Parameter and Determine Column Count

**Context**: Begin by confirming the SQL injection vulnerability in the target parameter (e.g., 'category') and iteratively test payloads to find the exact number of columns in the original query. Start with a basic injection like ' OR 1=1 -- to check for boolean-based injection, then escalate to UNION with NULL values. Increase the number of NULLs (e.g., UNION SELECT NULL, NULL --) until the payload executes without errors and aligns data properly, indicating a match (e.g., two columns in this case).

**Instructions**: Access the application URL and append a single quote to the parameter to trigger a syntax error, confirming injectability. Then, test UNION payloads starting with one NULL and incrementing until no error or misalignment occurs. For example, for a two-column query:

- Test: http://target.com/app?category=' UNION SELECT NULL --
- If error, try: http://target.com/app?category=' UNION SELECT NULL, NULL --

Observe the response for errors or blank fields indicating column match.

**Expected Output**: No SQL syntax errors and potential blank or aligned fields in the application output, confirming the column count (e.g., two columns).

### Step 2: Craft and Execute Union Payload to Query Database Version

**Context**: With the column count known (two in this example), replace the NULL values in the UNION SELECT with Oracle-specific queries. Use SELECT BANNER, NULL FROM v$version to retrieve the database banner while padding the second column with NULL to match the query structure. Comment out the rest of the query with -- to prevent errors.

**Command** ([[commands/curl-oracle-sqli-union-select-version]]):
```bash
curl "http://target.com/app?category=*'+UNION+SELECT+BANNER,+NULL+FROM+v\$version--*" -v
```

> This command sends the crafted payload via curl to the vulnerable endpoint. The \$ escapes the $ in v$version for shell compatibility. Replace the URL with the actual target. The -v flag provides verbose output for debugging. Success is indicated by the banner appearing in the response body, such as "Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - 64bit Production" injected into the application's result set.

**Expected Output**: The application page displays the Oracle version banner in place of the original data, e.g., a product listing replaced or appended with the database version string. No SQL errors in the response.

### Step 3: Verify and Document Results

**Context**: Confirm the extracted information is accurate and note any additional details like the exact version for targeted exploits (e.g., known CVEs in that Oracle version). If the banner doesn't appear, adjust the payload for encoding or try alternative views like v$instance.

**Instructions**: Review the response for the BANNER field. If partial data appears, refine the payload (e.g., use CAST(BANNER AS VARCHAR(4000)) if truncation occurs). Document the version for chaining with other procedures like privilege escalation via known vulnerabilities.

**Expected Output**: Clear extraction of database type (Oracle) and version details, enabling further attack planning.
