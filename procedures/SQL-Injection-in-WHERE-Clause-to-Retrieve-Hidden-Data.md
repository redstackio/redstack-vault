---
id: 079e5b19-72af-4bed-af4f-d5320d83442b
name: SQL-Injection-in-WHERE-Clause-to-Retrieve-Hidden-Data
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T17:20:01.981196+00:00'
updated_at: '2023-05-26T18:41:10.186906+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - sql
  - web-applications
commands:
  - '[[commands/curl-sqli-bypass-filter]]'
platforms:
  - Web
tools: []
validated: true
---

# SQL-Injection-in-WHERE-Clause-to-Retrieve-Hidden-Data

## Summary

This procedure demonstrates how to exploit a SQL injection vulnerability in a WHERE clause of an e-commerce application's product filtering query to bypass restrictions and retrieve hidden categories or all products, allowing unauthorized access to data that is intentionally concealed from standard users.

## Description

In e-commerce web applications, product listings are often filtered by categories selected by the user, with certain categories hidden for business or security reasons. If the backend SQL query uses unsanitized user input in the WHERE clause (e.g., SELECT * FROM products WHERE category = 'user_input'), attackers can inject malicious SQL payloads to alter the query logic. A common payload like ' OR 1=1 -- comments out the rest of the query, making the condition always true and returning all records. This technique is particularly effective against applications using dynamic SQL without prepared statements or input validation. The target environment is typically a web application with a database backend like MySQL or PostgreSQL, accessible via HTTP/HTTPS. Success reveals sensitive or hidden data, potentially leading to further reconnaissance or data exfiltration.

## Requirements

1. Valid access to the e-commerce web application's homepage and product filtering functionality (no authentication required if the vulnerability is in a public-facing page).
2. A web browser or command-line tool like curl for sending HTTP requests.
3. Optional: A proxy tool like Burp Suite to intercept and modify requests for more precise testing.
4. Knowledge of the application's URL structure, particularly the parameter handling product filters (e.g., ?category=).

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block common SQLi payloads like ' OR 1=1.
- Validate and sanitize all user inputs, restricting category parameters to a whitelist of valid values.
- Enable database logging to monitor anomalous queries returning excessive results.
- Conduct regular input validation and output encoding in the application code.

## Objectives

1. Identify the vulnerable category parameter in the product's filtering URL.
2. Inject a SQL payload to bypass the filter and retrieve all or hidden products.
3. Verify the injection by observing the expanded response data.

## Instructions

### Step 1: Identify the Vulnerable Filtering Parameter

**Context**: Access the e-commerce homepage and interact with the product filtering feature to observe the URL structure and confirm the category parameter is used for dynamic queries.

Navigate to the application's homepage (e.g., http://target.com/products) and select a category filter, such as 'Electronics'. Inspect the resulting URL to identify the parameter, typically ?category=electronics.

This step establishes the normal query behavior and confirms the input point for injection.

### Step 2: Test Normal Filter Response

**Context**: Send a legitimate request to baseline the expected output and ensure the filter works as intended.

Use a browser or curl to request products for a specific category.

**Command** ([[commands/curl-sqli-bypass-filter]]):

```bash
curl -X GET "http://target.com/products?category=electronics" -o normal_response.html
```

> This command fetches the filtered products page. Expected output is an HTML response showing only products in the 'electronics' category, confirming the parameter influences the SQL WHERE clause.

### Step 3: Inject SQL Payload to Bypass Filter

**Context**: Modify the category parameter with a SQL injection payload to make the WHERE condition always true, retrieving all products including hidden ones.

Replace the category value with the payload ' + OR +1=1 -- (URL-encoded as %27%20OR%201%3D1%20-- to handle spaces and quotes). The single quote closes the string, OR 1=1 evaluates to true, and -- comments out the rest of the query.

**Command** ([[commands/curl-sqli-bypass-filter]]):

```bash
curl -X GET "http://target.com/products?category=%27+OR+1%3D1+--" -o injected_response.html
```

> This sends the malicious request. Expected output is an HTML response displaying all products, including those from hidden categories, indicating successful injection. Compare the response size or content with the normal filter to confirm data leakage.

### Step 4: Verify and Analyze Results

**Context**: Compare the injected response against the baseline to confirm the vulnerability and extract hidden data.

Open the injected_response.html file or view the browser output. Look for additional categories or products not visible in the normal response.

Success is indicated by an expanded product list. If using a proxy, inspect the backend SQL query logs if accessible, or note any error messages that might reveal database details.
