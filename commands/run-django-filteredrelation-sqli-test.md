---
data: >-
  python3 django/tests/runtests.py
  filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli
tags:
  - sqli
  - django
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.051Z'
id: e7b09f8e-6b54-47c0-9402-6f6d59b649b7
verified: false
validated: true
submitted: true
---
# run-django-filteredrelation-sqli-test

## Command

```bash
python3 django/tests/runtests.py filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli
```

## Description

Runs a specific Django test case to demonstrate the SQL injection vulnerability in FilteredRelation with select_related, outputting the generated SQL to show the injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli` | The test module, class, and method to execute | Yes |

## Examples

### Basic Usage

```bash
python3 django/tests/runtests.py filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli
```

### Advanced Usage

```bash
python3 django/tests/runtests.py --verbosity=2 filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli
```

## Expected Output

Test execution details, including the generated SQL query with the injection payload, potential syntax errors from the malformed JOIN, or confirmation of arbitrary SQL execution.

## Related

- [[procedures/Demonstrate-Django-FilteredRelation-SQLi-with-Test-Runner]]
