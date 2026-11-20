# API Rationale Study --- Pacing & Trajectory

> **File:** `api_rationale_study_pacing_trajectory.md`\
> **Status:** Living study-control document\
> **Baseline:** 2026-11-21\
> **Primary scope:** OpenAI API + OpenAI-compatible provider mechanisms\
> **Engineering focus:** Digital Engineering (DE) + GitCom (GC)\
> **Secondary boundary:** Reality Engineering (RE)\
> **Purpose:** Preserve the current teaching branch, learning priority,
> conceptual alignment, experiment order, and restart point so this file
> can be fed back into a future session to resume teaching.

------------------------------------------------------------------------

## 0. Role of This File

This is not a complete API tutorial and not a chronological transcript.
It is the **pacing / trajectory / checkpoint controller** for the
API-mechanism study branch.

Use it to answer:

1.  What have we already learned?
2.  What should be learned next?
3.  What should wait until a real experiment creates demand?
4.  Where should API study reconnect with GitCom, Minimal Agents, and
    Tools?

``` text
Official Docs
    ↓
Mechanism Study
    ↓
Minimal Experiment
    ↓
GitCom / DE Friction
    ↓
Observation
    ↓
Abstraction
    ↓
Return to Official Docs
```

The study line should pause for implementation whenever the knowledge
threshold is sufficient. Finishing the whole OpenAI documentation tree
is not a prerequisite for GitCom.

------------------------------------------------------------------------

# 1. Governing Scope

## 1.1 Primary target

The target is not memorizing SDK syntax. It is understanding reusable
mechanisms underneath it:

``` text
Readiness
    ↓
Request
    ↓
Transport
    ↓
Remote Execution
    ↓
Response
    ↓
Semantic Result / Action Request / State
    ↓
Validation
    ↓
Artifact / Action
```

OpenAI is the main specimen. OpenAI-compatible providers are used to
test which mechanisms are portable.

## 1.2 DE / RE boundary

``` text
                Engineering
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
         DE                    RE
Digital Engineering      Reality Engineering
          │                     │
       DEEP STUDY            MAP FIRST
       + BUILD              + JUST-IN-TIME
```

DE includes code, files, documents, structured data, software tools, Git
operations, retrieval, digital artifacts, local execution, validation,
and agent/tool orchestration.

RE includes payment, booking, messaging with external side effects,
IoT/device control, sensors, robotics, physical actuation, and
real-world transactions.

Always distinguish:

``` text
READ REALITY
sensor / telemetry / search / location / observation

vs.

CHANGE REALITY
payment / booking / device control / robot action / transaction
```

`CHANGE REALITY` generally requires stronger authorization, validation,
idempotency, auditability, recovery, and human/safety controls.

------------------------------------------------------------------------

# 2. GitCom as the Primary Experimental Workload

Current R1 shape:

``` text
               2023-02-08 Anchor
                    /       \
                   /         \
                  ↓           ↓
          infer backward   infer forward
                  ↓           ↓
             2023-02-07   2023-02-09
                  \           /
                   \         /
                    ↓       ↓
                    validate
                       ↓
                   artifacts
```

First implementation stays deliberately small:

``` text
read
  ↓
infer
  ↓
inspect response
  ↓
extract
  ↓
validate
  ↓
write
```

Do not require LangGraph, Google ADK, multi-agent orchestration, MCP,
vector stores, or Agent-Matrix for R1.

------------------------------------------------------------------------

# 3. Cross-Provider Baseline

Previously compared:

-   OpenAI
-   DeepSeek
-   Gemini
-   xAI / Grok
-   Doubao Ark
-   Kimi / Moonshot
-   Qwen / DashScope

DeepSeek has been successfully tested for GitCom R1 through the OpenAI
Python SDK with a provider-specific `base_url`.

``` text
Provider Identity ≠ SDK Identity
```

Also:

``` text
same call shape ≠ same semantics
```

Provider differences may remain in reasoning fields, tool behavior,
structured output, usage metadata, completion state, model naming,
endpoints, limits, and extensions.

A common `infer(...)` operation is plausible, but its final contract
must be derived from experiments rather than assumed from syntactic
compatibility.

------------------------------------------------------------------------

# 4. API Mechanism Foundation --- Progress

Legend:

``` text
[DONE]   substantially taught and aligned
[INTRO]  introduced; deeper implementation remains
[NEXT]   current next teaching target
[EXP]    prefer experiment before more theory
[LATER]  useful but not blocking DE + GitCom
[AWARE]  awareness-level only
```

  --------------------------------------------------------------------------------
  Topic                   Status                  Checkpoint
  ----------------------- ----------------------- --------------------------------
  Client anatomy          DONE                    Local configured capability
                                                  object; not model/API/permanent
                                                  connection.

  API key / environment   DONE                    Credential/config concern,
                                                  separate from semantics.

  `base_url` / endpoint   DONE                    Destination config; omitted URL
                                                  may mean SDK default.

  Timeout / retry         DONE                    Transport policy, not model
                                                  thinking time.

  Request anatomy         DONE                    Python → serialization →
                                                  JSON/bytes → HTTP/TLS/network.

  Response anatomy        DONE                    HTTP response → SDK parsing →
                                                  Python object → semantic
                                                  extraction.

  SDK vs API              DONE                    SDK wraps the remote API
                                                  contract.

  Serialization           DONE                    `dict` is not JSON; network
                                                  eventually transfers bytes.

  Resource/object         DONE                    `client.responses.create(...)` =
  hierarchy                                       hierarchy + operation.

  Response species        DONE                    Semantic output, action request,
                                                  state, metadata, failure.

  Parameter lifetime      DONE                    Stable parameters move earlier;
                                                  variable ones stay runtime.

  Pre-binding             INTRO                   Provider/model/config can be
                                                  bound before inference.

  API Reading Card        DONE                    WHO / WHERE / WHAT IN / HOW /
                                                  WHAT OUT / WHO ACTS / STATE /
                                                  FAILURE.

  DE vs RE                DONE                    DE deep; RE map first.

  Idempotency             INTRO                   Retry must not duplicate side
                                                  effects accidentally.

  Human approval          INTRO                   Autonomy should be
                                                  capability-specific.
  --------------------------------------------------------------------------------

------------------------------------------------------------------------

# 5. OpenAI Official Core Concepts --- Priority Map

Current official Core Concepts:

``` text
Responses API
Decisions API
Conversation state
Background mode
Streaming
WebSocket mode
Mid-turn steering
Multi-agent
Webhooks
File inputs
Compaction
Counting tokens
```

Official order is not automatically our learning order.

  -----------------------------------------------------------------------------------------
  Core Concept            DE+GC Priority Status           Decision
  ---------------- --------------------- ---------------- ---------------------------------
  Responses API                       P0 DONE / EXP       Conceptual core learned; next
                                                          value is real GC use and response
                                                          inspection.

  Decisions API                    P0/P1 DONE             `predicate`, `choice`, `score`
                                         conceptually     learned; candidate for semantic
                                                          validation.

  Conversation                        P1 NEXT             Next official lesson; important
  state                                                   for Minimal Agents; GC R1 stays
                                                          mostly stateless.

  File inputs                         P1 INTRO            File/content/reference/artifact
                                                          distinction learned; revisit on
                                                          demand.

  Streaming                           P2 INTRO            SSE/event delivery understood;
                                                          not needed for R1.

  Background mode                     P2 INTRO            Background-job concept
                                                          understood; defer implementation.

  Compaction                          P2 LATER            Important for long-running
                                                          stateful agents.

  Counting tokens                     P2 LATER            Useful for context/cost
                                                          observability.

  Mid-turn                         P2/P3 LATER            Relevant to interactive
  steering                                                long-running agents.

  Webhooks                            P3 INTRO            Server-to-client notification
                                                          understood; no GC need yet.

  WebSocket mode                      P3 INTRO            Full-duplex persistent
                                                          interaction understood; no GC
                                                          need yet.

  Multi-agent            P1 concept / P3 LATER            Conceptually important;
                          implementation                  implementation waits for real
                                                          orchestration pressure.
  -----------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 6. Responses API --- Checkpoint

Conceptual shift:

``` text
Message-centric
      ↓
Item-centric / Response-centric
```

Minimal form:

``` python
response = client.responses.create(
    model="...",
    input="..."
)
```

Interpretation:

``` text
CREATE RESPONSE
      │
      ├── model
      ├── input
      ├── instructions
      ├── tools
      └── other parameters
```

`input` is data supplied to the operation, not a separate execution
stage. `response.output_text` is a convenience projection, not the whole
response.

Richer mental model:

``` text
response
├── output[]
│   ├── message
│   ├── reasoning-related item
│   ├── function call
│   └── other typed items
├── status
├── usage
├── model
├── id
└── metadata
```

### API-design rationale

Human/pipeline intuition:

``` text
Input → Processing → Response
```

Provider API view:

``` text
Create Response
    ├── model
    ├── input
    └── tools
```

Key conclusion:

``` text
Pipeline View ≠ Resource / Operation View
```

For our narrower DE layer, an inference-centered interface may be more
natural:

``` python
result = infer(instrn)
```

Do not yet lock `infer(...) -> str`. Returning only text may discard
useful state, usage, tool calls, reasoning-related items, and completion
information.

------------------------------------------------------------------------

# 7. Decisions API --- Checkpoint

Core primitives:

``` text
predicate → Is X true? → probability
choice    → Which fixed option? → selected value + distribution/confidence
score     → Where on ordered rubric? → probability-weighted score
```

Conceptual split:

``` text
Responses → create/generate candidate outcomes
Decisions → evaluate evidence under constrained questions
```

Potential GitCom validation:

``` text
                    VALIDATION
                        │
             ┌──────────┴──────────┐
             ↓                     ↓
      Deterministic             Semantic
          Tools                 Judgment
             │                     │
     syntax / tests / diff      Decisions
                                  │
                    ┌─────────────┼─────────────┐
                    ↓             ↓             ↓
                predicate       choice         score
                    │             │             │
             function kept?  complexity?  plausibility?
```

Important:

``` text
LLM Judgment → Application Policy → Tool Execution
```

Do not call every LLM operation an Agent. A classification, predicate,
or score can simply be a semantic decision primitive.

------------------------------------------------------------------------

# 8. Important Concepts Outside the Core Sidebar

## Structured Outputs --- INTRO / HIGH PRIORITY EXPERIMENT

``` text
valid JSON ≠ schema-valid data ≠ semantically correct data
```

Likely GC uses: validation records, experiment metadata, artifact
descriptors, extraction/classification results.

## Function / Tool Calling --- INTRO / HIGH PRIORITY EXPERIMENT

``` text
Model
  ↓
Tool Call
  ↓
Application Runtime
  ↓
Actual Function
  ↓
Tool Result
  ↓
Model
```

``` text
Tool Call ≠ Tool Execution
```

Candidate tools:

``` text
read_file()
write_file()
check_python_syntax()
run_python()
git_diff()
git_status()
git_commit()
inspect_artifact()
```

## Files / Retrieval / Artifacts --- INTRO

``` text
File ≠ File Content ≠ File Reference/ID ≠ Artifact
```

``` text
File Input ≠ File Search / Retrieval
```

For R1, local file I/O is enough.

## Built-in Tools --- INTRO

Execution ownership differs:

``` text
Custom Function Tool → our runtime
Provider Built-in    → provider infrastructure
Remote Tool / MCP    → remote capability server
```

Always ask: `WHO ACTS?`

## MCP --- INTRO / LATER

``` text
Agent / Model
    ↓
standardized capability/context protocol
    ↓
MCP Server
    ↓
external tools / data / systems
```

MCP is not itself an Agent, Workflow, or LLM.

## Computer Use --- INTRO / LATER

``` text
Observe → Decide → Act → Observe
```

Prefer a reliable structured API when one exists.

------------------------------------------------------------------------

# 9. Interaction Topology

Conceptually introduced:

``` text
Synchronous Request / Response
Polling
Streaming / SSE
Webhook
WebSocket
Async / Background Job
Batch
```

GitCom R1 needs only synchronous request/response.

------------------------------------------------------------------------

# 10. Next Teaching Queue

Immediate next official lesson:

``` text
Core Concepts 03 — Conversation State
```

Questions:

-   What is state?
-   Where can state live?
-   What does `previous_response_id` mean?
-   Conversation vs context vs state vs memory?
-   Provider-managed vs application-managed state?
-   When does state help an Agent?
-   When does state create hidden dependency or experimental
    contamination?
-   Why should GC backward/forward inference probably remain isolated in
    R1?

After that, do not rigidly follow the sidebar:

``` text
Conversation State
    ↓
GitCom R1 experiment
    ↓
Response inspection
    ↓
Structured Output experiment
    ↓
Semantic validation experiment
    ↓
Function / Tool Calling experiment
    ↓
Minimal Agent modules
    ↓
Extract repeated deterministic operations as Tools
```

------------------------------------------------------------------------

# 11. Experiment-First Queue

## E01 --- Raw Inference Anatomy

``` text
anchor code
  ↓
DeepSeek/OpenAI-compatible inference
  ↓
inspect full response
  ↓
extract code
  ↓
materialize artifact
```

Observe response shape, text extraction, reasoning-related fields,
usage, completion state, exceptions, latency, and artifact quality.

## E02 --- GitCom Bidirectional Evolution

``` text
           02-08
          /     \
         ↓       ↓
      02-07     02-09
```

Keep branches independently derived from the same anchor; avoid state
contamination; validate syntax, complexity direction, semantic
preservation, and plausibility.

## E03 --- Structured Validator

Compare free-form validator prose against schema-constrained output.

## E04 --- Decision Primitive

Where API availability permits, compare Responses + Structured Output
with predicate/choice/score style semantic validation.

## E05 --- First Tool Loop

``` text
Model
  ↓
requests syntax check
  ↓
check_python_syntax()
  ↓
tool result
  ↓
model/application
```

Understand the mechanism before introducing an Agent framework.

------------------------------------------------------------------------

# 12. Three Active Branches

## A --- API / Agent Mechanism

``` text
Docs → Mechanism → Prediction → Minimal Code → Inspect Reality → Update Mental Model
```

Focus on OpenAI first, compatible providers second, DE deep and RE
map-first.

## B --- Minimal Agents

Possible future specimens:

``` text
Code Evolver
Code Reviewer
Semantic Validator
Artifact Inspector
Git Operator
```

Begin from the smallest viable shape:

``` python
def agent(input):
    ...
    return result
```

Let structure grow from experiment friction.

## C --- Tools

Extract repeated deterministic stable actions from A/B experiments.

Heuristic:

``` text
Requires semantic judgment?
    ↓ yes
Inference / Agent / Decision primitive

Can execute deterministically?
    ↓ yes
Tool
```

This is a working heuristic, not a permanent ontology.

------------------------------------------------------------------------

# 13. Agent-Matrix --- Status

``` text
EMERGENT HYPOTHESIS
NOT AN IMPLEMENTATION TRACK
```

Potential future shape:

``` text
Intent
  ↓
Agent-Matrix
  ↓
Readiness + Cognition + Tools + Execution
  ↓
Digital State Change
  ↓
Validation
  ↓
Artifact
```

Even Readiness may eventually become orchestratable.

Do not build Agent-Matrix now. Let it emerge only after validated
Agents, Tools, State, Readiness, Validation, and Artifact flows create
repeated orchestration pressure.

------------------------------------------------------------------------

# 14. `infer(...)` --- Open Design Question

Original micro-vision remains valuable:

``` python
infer(deep_seek, instrn)
```

or:

``` python
infer(instrn)
```

Working parameter-lifetime rule:

``` text
stable → bind earlier
variable → keep at runtime
```

Do not yet lock whether the public result is `str` or a richer
normalized result. Let GitCom experiments decide.

------------------------------------------------------------------------

# 15. UCU --- Status

UCU remains conceptual, not a frozen schema.

``` text
Provider-specific Response
        ↓
semantic normalization
        ↓
UCU ?
        ↓
Translator / Materializer
        ↓
Code / JSON / Document / Action
```

Desired properties discussed: expandable, retrievable, constrainable,
explainable, referenceable.

Text remains attractive under the 朴素原则, but:

``` text
readable ≠ lossless
```

Do not decide representation before observing real response/tool/state
requirements.

------------------------------------------------------------------------

# 16. Current Abstraction Judgments

These are working judgments, not a finalized doctrine.

### Conceptual separation does not require physical separation

``` text
conceptual component ≠ class/module/process
```

### Do not abstract before repeated friction

``` text
real workload → repetition → stable boundary → abstraction
```

### Hide mechanical complexity, not semantic necessity

Provider/network/serialization complexity can often stay below the DE
boundary. Correctness/state/tool/validation/observability information
may need to cross it.

### Simple upper layer does not imply simple lower layer

``` text
bottom: complex enough to be correct
top:    simple enough to be usable
```

### API ergonomics matter

Real-world API users care about writing flow, reading flow, parameter
locality, cognitive load, discoverability, and composition.

But:

``` text
ergonomic separation
must be weighed against
coordination complexity
```

especially when input/output are heterogeneous, polymorphic, optional,
or many-to-many.

------------------------------------------------------------------------

# 17. Restart Protocol

When this file is fed back into a future session:

``` text
1. Read this document.
2. Treat GitCom R1 as the active experimental workload.
3. Preserve DE-deep / RE-map-first.
4. Do not prematurely build Agent-Matrix, Router classes, multi-agent frameworks, MCP, or RAG.
5. Resume official Core Concepts at Conversation State,
   unless a current GC experiment creates a more urgent mechanism question.
6. Teach each mechanism as:
      Official Concept
          ↓
      Mechanism
          ↓
      DE Projection
          ↓
      GitCom Projection
          ↓
      Need now / later?
7. Update this file after meaningful teaching or experimental milestones.
```

------------------------------------------------------------------------

# 18. Current Position Snapshot

``` text
API FOUNDATION
████████████████████    substantially established

OpenAI Responses
████████████████░░░░    conceptual core learned; experiment next

OpenAI Decisions
██████████████░░░░░░    conceptual core learned; experiment later

Conversation State
██████░░░░░░░░░░░░░░    mechanism introduced; official deep-dive next

Structured Outputs
████████░░░░░░░░░░░░    introduced; implementation pending

Tool Calling
████████░░░░░░░░░░░░    mechanism introduced; implementation pending

Files / Artifacts
██████████░░░░░░░░░░    local GitCom path sufficient

Streaming / Async / Webhooks / WebSocket
██████░░░░░░░░░░░░░░    topology understood; no immediate need

MCP / Computer Use
██████░░░░░░░░░░░░░░    conceptual awareness; defer

Minimal Agents
███░░░░░░░░░░░░░░░░░    branch established; implementation pending

Tools
███░░░░░░░░░░░░░░░░░    candidates emerging; extract from experiments

Agent-Matrix
█░░░░░░░░░░░░░░░░░░░    hypothesis only; intentionally not built
```

------------------------------------------------------------------------

# 19. Immediate Handoff

Current recommendation:

``` text
PAUSE THEORY
    ↓
RUN GITCOM EXPERIMENT
    ↓
OBSERVE REAL FRICTION
    ↓
RETURN HERE
```

If teaching resumes first:

``` text
Core Concepts 03 — Conversation State
```

If implementation starts first, let GitCom determine which concept is
pulled forward.

------------------------------------------------------------------------

# 20. Official Reference Anchor

Primary current documentation anchor:

`https://developers.openai.com/api/docs/quickstart`

Current official Core Concepts:

-   Responses API
-   Decisions API
-   Conversation state
-   Background mode
-   Streaming
-   WebSocket mode
-   Mid-turn steering
-   Multi-agent
-   Webhooks
-   File inputs
-   Compaction
-   Counting tokens

Treat official docs as source of truth for current endpoint names, model
support, parameter names, limits, and feature availability.

Treat this file as source of truth for **our learning priority,
conceptual alignment, GitCom projection, and restart position**.

------------------------------------------------------------------------

## End State

The objective is not:

``` text
Learn every OpenAI API feature
```

It is:

``` text
Understand enough stable mechanism
        ↓
build small DE systems
        ↓
observe real friction
        ↓
derive useful Agents and Tools
        ↓
abstract only what earns abstraction
```

For GitCom, the next meaningful proof remains:

``` text
read → infer → inspect → validate → materialize
```

Everything larger must earn its place.
