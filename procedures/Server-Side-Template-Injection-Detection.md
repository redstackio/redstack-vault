---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.877004+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Detection]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - web
  - detection
commands:
  - '[[commands/curl-ssti-test-jinja]]'
  - '[[commands/curl-ssti-test-freemarker]]'
  - '[[commands/curl-ssti-test-velocity]]'
platforms:
  - Web
tools:
  - '[[tools/tplmap]]'
validated: true
---

# Server-Side-Template-Injection-Detection

## Summary

Server Side Template Injection (SSTI) detection is a procedure to identify vulnerabilities in web applications where user-supplied input is unsafely embedded into server-side templates, allowing execution of arbitrary code. This procedure outlines manual testing techniques using crafted payloads for common templating engines like Jinja2, Freemarker, and Velocity, combined with optional automated scanning to confirm if inputs are interpreted and executed on the server, preventing potential attacks such as remote code execution.

## Description

Server Side Template Injection (SSTI) occurs when a web application incorporates untrusted user input into a server-side template, which is then processed and rendered by the server. If the input is not properly sanitized, attackers can inject malicious template syntax that gets executed, leading to severe consequences like data exfiltration, privilege escalation, or full server compromise. Detection focuses on identifying vulnerable input points (e.g., search fields, URL parameters, or form inputs) by injecting test payloads that attempt to execute simple expressions, such as mathematical operations. Success is indicated by the server reflecting the evaluated result (e.g., injecting '{{7*7}}' and receiving '49' instead of the literal string). This procedure is applicable in penetration testing or vulnerability assessments on web applications using templating engines. Manual detection requires intercepting requests via a proxy, while automated tools can accelerate the process. Early detection allows for mitigation through input validation and template sandboxing, preserving application integrity and user trust.

## Requirements

1. Network access to the target web application (e.g., via browser, API endpoint, or direct HTTP requests).
2. A proxy tool like Burp Suite for intercepting and modifying requests (recommended for precise control).
3. Basic knowledge of common templating engines (Jinja2 for Python/Flask, Freemarker for Java, Velocity for Apache).
4. Command-line tools like curl for sending test requests (or integrated into a proxy workflow).
5. Optional: Automated scanner like tplmap for batch testing multiple endpoints.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, whitelisting allowed characters and rejecting template syntax like '{{', '${', or '#{'.
- Use template engines with built-in sandboxing features (e.g., Jinja2's safe mode or Freemarker’s secure configuration) to restrict access to sensitive functions.
- Employ web application firewalls (WAFs) with rules tuned for SSTI patterns, such as blocking common payloads.
- Regularly scan applications with automated tools and monitor server logs for anomalous template evaluations or error messages indicating injection attempts.
- Conduct code reviews focusing on template rendering functions to ensure user input is escaped or marked as safe only when necessary.

## Objectives

1. Identify vulnerable input points in the web application that allow SSTI exploitation.
2. Confirm the specific templating engine in use through payload response analysis.
3. Mitigate risks by documenting findings and recommending fixes to prevent data breaches and server compromise.
4. Expected outcome: A report of confirmed SSTI vulnerabilities with evidence from test responses.

## Instructions

### Step 1: Identify Potential Input Points

**Context**: Begin by mapping the application to find user-controllable inputs that could be processed by server-side templates, such as search boxes, profile fields, or URL parameters. Use reconnaissance to enumerate endpoints.

No specific command required here; manually explore the application or use a spidering tool in Burp Suite to crawl forms and parameters.

> Focus on inputs reflected in the response without HTML/JS escaping, as these are prime candidates for SSTI.

### Step 2: Test for Generic SSTI with Basic Payloads

**Context**: Inject simple, non-destructive payloads to check if the server evaluates template expressions. Start with engine-agnostic tests like '|' (pipe) for Ruby ERB or basic math to probe for execution.

**Command** ([[commands/curl-ssti-test-jinja]]):
```bash
curl -X POST "http://target.com/search" -d "q={{7*7}}" -v
```

> This sends a Jinja2-style payload to a search endpoint. If the response contains '49' instead of '{{7*7}}', it indicates SSTI. Observe HTTP responses for evaluation or errors revealing the engine (e.g., 'TemplateSyntaxError' from Django).

If no response, try other engines with subsequent steps.

### Step 3: Test for Freemarker Engine

**Context**: If the generic test fails, target specific engines. Freemarker uses '${}' syntax; inject a payload to execute and confirm via output like '49' or file access indicators.

**Command** ([[commands/curl-ssti-test-freemarker]]):
```bash
curl -X GET "http://target.com/page?param=${7*7}" -v
```

> Expected: Response body shows '49' or similar evaluated result. If successful, note for further exploitation testing in a controlled environment. Check for differences in error handling that might leak server details.

### Step 4: Test for Velocity Engine

**Context**: Velocity uses '#{}' for directives. This step verifies if the application uses Apache Velocity by attempting a simple set operation or math.

**Command** ([[commands/curl-ssti-test-velocity]]):
```bash
curl -X POST "http://target.com/form" -d "input=#set($x=7*7)$x" -v
```

> Success if '$x' evaluates to '49' in the output. If not, try variations or move to automated scanning.

### Step 5: Automate Detection with Tplmap (Optional)

**Context**: For comprehensive scanning, use an automated tool to test multiple payloads across endpoints. This reduces manual effort and covers more engines.

Use [[tools/tplmap]] by running it against the target URL with identified parameters.

> Example: `python tplmap.py -u http://target.com/search?q=`. Analyze output for detected engines and vulnerability levels. Verify positives manually to avoid false alarms.

### Step 6: Verify and Document Findings

**Context**: Confirm detections by re-testing in a non-production environment if possible. Document the vulnerable endpoint, payload used, engine identified, and potential impact.

No command; review logs or responses for indicators like unexpected computations or access to system info (e.g., injecting to read /etc/passwd if RCE confirmed).
