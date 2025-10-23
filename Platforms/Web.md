---
title: Web Applications Platform
type: platform
platform: Web
created: 2025-01-22
---

# 🌍 Web Applications

> **Web application vulnerabilities and exploitation techniques**  
> ~260 documented procedures covering OWASP Top 10 and beyond

---

## 📊 Overview

Web applications represent the largest attack surface in modern infrastructure, with extensive coverage of:
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Server-Side Request Forgery (SSRF)
- XML External Entity (XXE)
- Authentication & Authorization flaws
- CORS misconfigurations
- Deserialization attacks

```dataview
TABLE WITHOUT ID
  choice(verified = true, "✅", "⚠️") as "✓",
  file.link as "Procedure",
  tactics as "Tactics"
FROM "procedures"
WHERE contains(platforms, "Web")
SORT verified DESC, file.name ASC
LIMIT 50
```

---

## 🎯 By Vulnerability Type

### SQL Injection
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "SQL") OR
  contains(tags, "sql-injection") OR
  contains(tags, "sqli")
)
SORT file.name ASC
```

### Cross-Site Scripting (XSS)
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "XSS") OR
  contains(tags, "xss") OR
  contains(tags, "cross-site-scripting")
)
SORT file.name ASC
```

### Server-Side Request Forgery (SSRF)
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "SSRF") OR
  contains(tags, "ssrf")
)
SORT file.name ASC
```

### XML External Entity (XXE)
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "XXE") OR
  contains(tags, "xxe")
)
SORT file.name ASC
```

### Authentication & Authorization
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "Authentication") OR
  contains(file.name, "Authorization") OR
  contains(file.name, "2FA") OR
  contains(file.name, "JWT") OR
  contains(file.name, "Session") OR
  contains(tags, "authentication")
)
SORT file.name ASC
```

### CORS Misconfiguration
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "CORS") OR
  contains(tags, "cors")
)
SORT file.name ASC
```

### Deserialization
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "Deserialization") OR
  contains(tags, "deserialization")
)
SORT file.name ASC
```

### File Upload
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "Upload") OR
  contains(tags, "file-upload")
)
SORT file.name ASC
```

### Directory Traversal / Path Traversal
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "Traversal") OR
  contains(tags, "path-traversal")
)
SORT file.name ASC
```

### Command Injection
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status"
FROM "procedures"
WHERE contains(platforms, "Web")
AND (
  contains(file.name, "Command Injection") OR
  contains(tags, "command-injection")
)
SORT file.name ASC
```

---

## 🎯 By MITRE Tactic

### Initial Access
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Web")
AND contains(tactics, "[[Initial Access")
SORT file.name ASC
```

### Execution
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Web")
AND contains(tactics, "[[Execution")
SORT file.name ASC
```

### Persistence
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Web")
AND contains(tactics, "[[Persistence")
SORT file.name ASC
```

### Credential Access
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Web")
AND contains(tactics, "[[Credential Access")
SORT file.name ASC
```

### Collection
```dataview
TABLE WITHOUT ID
  file.link as "Procedure",
  choice(verified = true, "✅", "⚠️") as "✓"
FROM "procedures"
WHERE contains(platforms, "Web")
AND contains(tactics, "[[Collection")
SORT file.name ASC
```

---

## 🛠️ Web Testing Tools

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  category as "Category",
  description as "Description"
FROM "tools"
WHERE contains(platforms, "Web") OR contains(tags, "web")
SORT file.name ASC
```

---

## 📈 Statistics

### Verification Status
```dataview
TABLE WITHOUT ID
  choice(verified = true, "✅ Verified", "⚠️ Unverified") as "Status",
  length(rows) as "Count"
FROM "procedures"
WHERE contains(platforms, "Web")
GROUP BY verified
```

### Top Vulnerability Types (by tag)
```dataview
TABLE WITHOUT ID
  tags as "Vulnerability",
  length(rows) as "Procedures"
FROM "procedures"
WHERE contains(platforms, "Web") AND tags != null
FLATTEN tags
GROUP BY tags
SORT length(rows) DESC
LIMIT 15
```

---

## 🎯 Common Attack Paths

### OWASP Top 10 Testing Flow
1. **Reconnaissance** → Enumerate technologies, endpoints
2. **Authentication Testing** → Bypass, brute force, session hijacking
3. **Injection Testing** → SQL, XSS, XXE, SSRF, Command
4. **Access Control** → IDOR, privilege escalation, path traversal
5. **Configuration** → CORS, CSP, security headers
6. **Business Logic** → Race conditions, parameter tampering
7. **Data Exposure** → Sensitive data in responses, XXE OOB

### SQL Injection to RCE
1. **Identify Injection Point** → Error-based, blind, time-based
2. **Enumerate Database** → Version, tables, columns
3. **Extract Data** → Credentials, sensitive information
4. **File Operations** → Read files, write web shell
5. **Command Execution** → xp_cmdshell (MSSQL), UDF (MySQL)

### XSS to Account Takeover
1. **Find XSS** → Reflected, stored, DOM-based
2. **Bypass Filters** → Encoding, obfuscation, polyglots
3. **Craft Payload** → Session stealing, keylogging
4. **Deliver** → Social engineering, stored XSS
5. **Capture Credentials** → Cookie theft, form hijacking

---

## 🔗 Related Resources

### Internal Links
- [[Platforms/README|← All Platforms]]
- [[MITRE-Framework|Browse by Tactic]]
- [[Tools-Index|Web Testing Tools]]
- [[Queries/web-specific|Web Query Library]]

### Cross-References
- [[Cross-References/SQL-Injection|All SQL Injection Techniques]]
- [[Cross-References/XSS-Attacks|All XSS Attack Vectors]]
- [[Cross-References/SSRF-Techniques|SSRF Exploitation]]

### External Resources
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackTricks - Web Pentesting](https://book.hacktricks.xyz/pentesting/pentesting-web)
- [PayloadsAllTheThings - Web](https://github.com/swisskyrepo/PayloadsAllTheThings)

---

*Last updated: 2025-01-22*  
*Web Procedures: ~260 | Most documented platform*
