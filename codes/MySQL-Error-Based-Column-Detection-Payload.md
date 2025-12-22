---
id: 2c45a9c8-951e-4d74-8d05-21112f3c4d74
name: MySQL-Error-Based-Column-Detection-Payload
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.306179+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - MySQL
tags:
  - sqli
  - union-based
  - error-based
  - column-detection
validated: true
---

# MySQL-Error-Based-Column-Detection-Payload

## Code

```sql
1' UNION SELECT @--+        #The used SELECT statements have a different number of columns
1' UNION SELECT @,@--+      #The used SELECT statements have a different number of columns
1' UNION SELECT @,@,@--+    #No error means query uses 3 column
                            #-1' UNION SELECT 1,2,3--+    True
```

## Description

This SQL code snippet demonstrates error-based detection for determining the number of columns in a vulnerable MySQL query during a UNION-based SQL injection attack. By injecting incremental user variables (@) into a UNION SELECT, MySQL generates errors for column mismatches, allowing the attacker to count columns without prior knowledge of the query structure.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The payloads use generic placeholders (@ for variables, numbers for literals); customize based on injection point (e.g., append to id=1). No runtime variables needed. | N/A |

## Usage

Inject these payloads sequentially into a confirmed SQLi parameter (e.g., via GET/POST or tools like Burp). Start with one @ and add until no error: the successful count matches the original query. Then replace with actual SELECT (e.g., UNION SELECT 1,2,3) for data exfiltration. Used in web apps with dynamic SQL, such as search forms.

## Detection

- Web server logs showing SQL syntax errors with UNION SELECT or user variables (@).
- Application error pages exposing MySQL details (version, syntax).
- WAF alerts for keywords like UNION, SELECT, or repeated error patterns.
- Database audit logs recording failed queries with mismatched columns.

## Related

- [[procedures/MySQL-Union-Based-Injection-with-Error-Based-Detection]]
