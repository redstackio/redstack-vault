---
id: 58bc12fb-c849-478e-9673-3188afdec321
name: Queue Requests
type: command
executor: bash
data: "def queueRequests(target, wordlists):\n    engine = RequestEngine(endpoint=target.endpoint,\n\
  \                        concurrentConnections=30,\n                        requestsPerConnection=30,\n\
  \                        pipeline=False\n                        )\n\n    # Queue\
  \ multiple requests with different parameters\n    for i in range(30):\n       \
  \ engine.queue(target.req, i)\n        engine.queue(target.req, target.baseInput,\
  \ gate='race1')\n\n    # Start the engine and open gate for race condition\n   \
  \ engine.start(timeout=5)\n    engine.openGate('race1')\n    engine.complete(timeout=60)\n\
  \n"
output: null
created_at: '2023-04-06T03:56:31.880462+00:00'
updated_at: '2023-04-06T03:56:31.891322+00:00'
---

# Queue Requests

```bash
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                        concurrentConnections=30,
                        requestsPerConnection=30,
                        pipeline=False
                        )

    # Queue multiple requests with different parameters
    for i in range(30):
        engine.queue(target.req, i)
        engine.queue(target.req, target.baseInput, gate='race1')

    # Start the engine and open gate for race condition
    engine.start(timeout=5)
    engine.openGate('race1')
    engine.complete(timeout=60)

```
