---
tags:
  - sqli
  - django
  - orm
  - injection
  - rce
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Python
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Define-Malicious-Alias-for-Django-FilteredRelation]]'
  - '[[procedures/Annotate-Queryset-with-Malicious-FilteredRelation]]'
  - '[[procedures/Apply-Select-Related-with-Malicious-Alias]]'
  - '[[procedures/Execute-Injected-Query-in-Django-ORM]]'
  - '[[procedures/Demonstrate-Django-FilteredRelation-SQLi-with-Test-Runner]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
updated_at: '2025-12-14T03:15:05.079Z'
description: >-
  Multi-stage attack exploiting SQL injection in Django's ORM through
  unsanitized aliases in FilteredRelation, annotate, and select_related, leading
  to arbitrary SQL execution and potential RCE.
skill_level: advanced
impact_level: high
id: f51dd21b-8f1e-408c-bc60-9325f436821b
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
---
# SQL Injection via Unsanitized FilteredRelation Aliases in Django ORM

Multi-stage attack chain demonstrating a complete attack workflow exploiting a SQL injection vulnerability in Django's ORM when using FilteredRelation with user-controlled, unsanitized column aliases. The attack injects a payload into dynamic alias variables used in annotate() and select_related(), breaking out of SQL string contexts to execute arbitrary SQL, potentially leading to data exfiltration, modification, or remote code execution on PostgreSQL via commands like COPY TO PROGRAM.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious Payload] --> B[Inject into Annotate]
    B --> C[Chain with Select Related]
    C --> D[Execute Query]
    D --> E[Demonstrate via Test]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Django development environment
- Python 3

### Target Environment

- Django web application using ORM with FilteredRelation
- Databases: SQLite or PostgreSQL
- Access to modify or control query aliases (e.g., via user input in a vulnerable app)

### Initial Access Requirements

- Code access or ability to influence dynamic alias variables in Django views/models
- No network access beyond local development; assumes attacker can inject via app logic

## Detailed Attack Procedures

### Step 1: Prepare Malicious Payload
procedure: [[procedures/Define-Malicious-Alias-for-Django-FilteredRelation]]

**Objective**: Create a malicious alias string that injects a closing quote to break out of the SQL string context in the JOIN clause.

**Instructions**: Define a user-controlled variable with the payload to escape the alias quoting.

```python
user_data = 'author_join2"'
```

**Expected Output**: The variable holds the injection payload ready for use in ORM methods.

**Success Indicators**:
- Payload variable defined without syntax errors
- Payload includes quote to close SQL string

### Step 2: Inject into Annotate
procedure: [[procedures/Annotate-Queryset-with-Malicious-FilteredRelation]]

**Objective**: Use the malicious alias in FilteredRelation within annotate() to insert the payload into the SQL JOIN alias.

**Instructions**: Annotate a queryset like Book.objects with the dynamic malicious alias.

```python
from django.db.models import FilteredRelation
qs = Book.objects.annotate(**{user_data: FilteredRelation('author')})
```

**Expected Output**: Queryset annotated, but SQL generation includes unescaped quotes from the payload.

**Success Indicators**:
- No immediate Python errors
- Inspect generated SQL to confirm injection point in JOIN

### Step 3: Chain with Select Related
procedure: [[procedures/Apply-Select-Related-with-Malicious-Alias]]

**Objective**: Reference the injected alias in select_related() to trigger the malformed SQL in the query execution.

**Instructions**: Chain select_related using the same malicious alias variable.

```python
qs = qs.select_related(user_data)
```

**Expected Output**: Queryset chained, preparing for execution with injected SQL.

**Success Indicators**:
- Chaining succeeds without ORM errors
- Payload alias referenced in the query build

### Step 4: Execute the Query
procedure: [[procedures/Execute-Injected-Query-in-Django-ORM]]

**Objective**: Fetch the results to run the malformed SQL and execute the injection.

**Instructions**: Call the fetch method to trigger SQL execution.

```python
qs._fetch_all()
```

**Expected Output**: SQL query executes with injection, potentially causing errors or arbitrary SQL effects like data dump.

**Success Indicators**:
- Query runs, showing SQL errors or unexpected data/behavior
- In PostgreSQL, possible RCE if payload includes COPY TO PROGRAM

### Step 5: Demonstrate with Test Runner
procedure: [[procedures/Demonstrate-Django-FilteredRelation-SQLi-with-Test-Runner]]

**Objective**: Reproduce the vulnerability using Django's test suite to validate the exploit.

**Instructions**: Run the specific test case that implements the POC.

Use [[commands/run-django-filteredrelation-sqli-test]]:

```bash
python3 django/tests/runtests.py filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli
```

**Expected Output**: Test execution shows generated SQL with injection, errors, or successful malformed JOIN.

**Success Indicators**:
- Test runs and highlights the SQLi in output
- Confirms vulnerability in the ORM

## Attack Chain Summary

### Key Achievements

1. Successful injection of quotes via alias to break SQL context
2. Arbitrary SQL execution through chained ORM methods
3. Demonstration of impact including potential RCE on PostgreSQL

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Server Software Component]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
