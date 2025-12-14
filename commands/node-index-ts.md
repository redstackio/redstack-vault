---
data: node index.ts
tags:
  - execution
  - typeorm
type: command
output: >-
  Logs insertion messages and outputs the injected query result, e.g., 'User {
  id: 5, firstName: "Timber 3", lastName: "Saw", age: 28 }'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.118Z'
id: c34a2025-cf11-4460-b4c1-fdf4ce0ef52c
verified: false
validated: true
submitted: true
---
# node-index-ts

## Command

```bash
node index.ts
```

## Description

Executes the modified TypeScript/JavaScript index.ts file in a Node.js environment to connect to the database, insert test data, and run the vulnerable SQL injection query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `index.ts` | The script file path | Yes |

## Examples

### Basic Usage

```bash
node index.ts
```

### Advanced Usage

```bash
node --trace-warnings index.ts
```

## Expected Output

Series of console logs: Insertion confirmations for 10 users, followed by the exploited query result showing an unauthorized user object.

## Related

- [[Related Procedure: Execute-Injected-Query]]
