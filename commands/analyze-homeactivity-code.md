---
id: cmd-analyze-homeactivity
data: >-
  protected void onResume() { // ... handleIntentExtras(getIntent()); //
  attacker can pass anything to getIntent() } private void
  handleIntentExtras(Intent intent) { // ... Intent deeplinkIntent = (Intent)
  intent.getParcelableExtra("extra_deep_link_intent"); // ... if
  (!(deeplinkIntent == null || this.consumedDeeplinkIntent)) { // ...
  startActivity(deeplinkIntent); // danger! starting an intent provided by an
  attacker // ... } // ... }
tags:
  - decompilation
  - analysis
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.599Z'
verified: false
validated: true
submitted: true
---
# analyze-homeactivity-code

## Command

```java
protected void onResume() { // ... handleIntentExtras(getIntent()); // attacker can pass anything to getIntent() } private void handleIntentExtras(Intent intent) { // ... Intent deeplinkIntent = (Intent) intent.getParcelableExtra("extra_deep_link_intent"); // ... if (!(deeplinkIntent == null || this.consumedDeeplinkIntent)) { // ... startActivity(deeplinkIntent); // danger! starting an intent provided by an attacker // ... } // ... }
```

## Description

Decompiled code snippet from Slack's HomeActivity showing vulnerable intent handling. Use in analysis tools to identify the flaw where attacker-provided deeplinkIntent is started without validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| getIntent() | Retrieves incoming intent | Yes |
| getParcelableExtra("extra_deep_link_intent") | Extracts embedded intent | Yes |
| startActivity(deeplinkIntent) | Launches the arbitrary intent | Yes |

## Examples

### Basic Usage

```java
// In decompiler output
protected void onResume() { handleIntentExtras(getIntent()); }
```

### Advanced Usage

```java
// Full method inspection
private void handleIntentExtras(Intent intent) { Intent deeplinkIntent = (Intent) intent.getParcelableExtra("extra_deep_link_intent"); if (!(deeplinkIntent == null || this.consumedDeeplinkIntent)) { startActivity(deeplinkIntent); } }
```

## Expected Output

Code revealing unvalidated startActivity call on attacker-controlled intent, confirming vulnerability.

## Related

- [[commands/create-webview-intent]]
- [[procedures/Analyze-Slack-HomeActivity-for-Intent-Vulnerabilities]]
