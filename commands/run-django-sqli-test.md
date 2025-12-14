---
data: python runtests.py model_fields.test_jsonfield.TestQuerying.test_sqli
tags:
  - testing
  - sqli
  - django
type: command
output: null
executor: bash
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.747Z'
id: 74a42c76-a6f0-463a-aa43-d2c3823d7091
verified: false
validated: true
submitted: true
---
# run-django-sqli-test

## Command

```bash
python runtests.py model_fields.test_jsonfield.TestQuerying.test_sqli
```

## Description

This command runs a specific Django test case that demonstrates SQL injection in JSONField KeyTransform by executing a vulnerable query with injected input, reproducing the syntax error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| runtests.py | Django's test runner script | Yes |
| model_fields.test_jsonfield.TestQuerying.test_sqli | Path to the test class and method for SQLi POC | Yes |

## Examples

### Basic Usage

```bash
python runtests.py model_fields.test_jsonfield.TestQuerying.test_sqli
```

### Advanced Usage

```bash
python runtests.py --verbosity=2 model_fields.test_jsonfield.TestQuerying.test_sqli
```

## Expected Output

SQL syntax error when user_input includes special characters like '"', e.g., "OperationalError: (1064, \"You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"value_custom__beeeee\"' at line 1\")"

## Related

- [[Related Procedure]]
