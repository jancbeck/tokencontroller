# Token Controller

Cost accounting and management control for AI agents: receipts from agents are matched to provider bills, placed on the work that caused them, and compared with budgets.

## Language

### The two sides

**Receipt**:
One agent session's account of what it spent and on what work: tokens, cost, model, time range and a one-line summary.
_Avoid_: Report item, line item, usage record

**Bill**:
A provider's figure for one period: gross, discount, credit and net. It is the total the receipts must add up to.
_Avoid_: Statement, invoice

**Token sheet**:
One person's receipts for a stretch of time, sent in together, the way a timesheet holds hours.
_Avoid_: Report, submission

**Cost sheet**:
The locked account of one closed period for the whole organization: cost per client, project and ticket, adding up to the bill.
_Avoid_: Statement, close sheet, monthly report

**Provider**:
A company that charges for model usage, such as Anthropic, OpenAI or a cloud marketplace.
_Avoid_: Vendor

**Cost source**:
One way a provider charges an organization: subscription, seat, usage at API rates, API key, cloud marketplace or reseller.

**Reconciliation**:
Checking, per period, that postings plus unattributed plus residual equal the bill.
_Avoid_: Matching

**Residual**:
The part of a bill that no receipt explains. Always shown as its own line.
_Avoid_: Leftover, difference

### Where cost sits

**Posting**:
The placement of a receipt, or a share of it, on one cost object with one cost kind.
_Avoid_: Allocation, assignment

**Cost center**:
The person who answers for a cost. Every posting has exactly one.

**Cost object**:
The work a cost paid for: a ticket, a project or the organization.

**Cost kind**:
The label on a posting that says how it relates to work: direct, project overhead, organization overhead, personal or unattributed.
_Avoid_: Category, cost type

**Direct**:
Cost placed on a ticket.

**Project overhead**:
Project cost that belongs to no single ticket, such as research or setup.

**Organization overhead**:
Cost that belongs to no project, such as internal tooling.

**Personal**:
A person's own learning and experiments.

**Unattributed**:
Spend that no rule or person has placed yet. Always shown as its own line.
_Avoid_: Unassigned, unallocated, other

**Attribution**:
The share of spend placed on tickets and projects, as a percentage of the total.
_Avoid_: Coverage, allocation rate

**Attribution target**:
The attribution an organization aims for.

### Work

**Organization**:
One customer of Token Controller: its people, teams, projects and periods.
_Avoid_: Account, tenant, workspace, company

**Project**:
A body of work for one client or one product, made of tickets.

**Ticket**:
Any unit of work: a feature, a story, an epic or a bug. Tickets can sit inside other tickets.
_Avoid_: Issue, task, story, work item

### People

**Person**:
A human in the organization. A person belongs to one team at a time.
_Avoid_: User, seat, developer

**Team**:
A node in the team tree: a team, a department or the whole organization.
_Avoid_: Group

**Team tree**:
The organization's people arranged as person, team, department, organization.
_Avoid_: Org chart, hierarchy

**Member**:
The role that sends in receipts and sees its own.

**Manager**:
The role that reads reports, sets budgets and cadence, and rejects receipts, for the teams, projects or clients it is assigned.

**Owner**:
The role that sees everything, runs the close and posts adjustments.
_Avoid_: Admin

### Agents

**Agent**:
An identity that spends tokens and sends receipts: a developer's local agent, a CI automation or a remote agent. It has exactly one person who answers for it.
_Avoid_: Bot, tool

**Agent type**:
The product an agent runs on, such as Claude Code or Codex.

**Subagent**:
An agent started by another agent inside the same session.

**Session**:
One continuous run of an agent, from start to end.
_Avoid_: Conversation, chat

**Segment**:
A stretch of a session on one branch and one working directory.

**Transcript**:
The full text of a session. It never leaves the machine.

**Summary**:
The one line an agent writes about what a session did. It is the only text in a receipt.

**Telemetry event**:
One model call as reported live by the agent: tokens, cost and IDs, no text.

**Door**:
A way receipts or telemetry reach Token Controller: session files, telemetry push, the GitHub Action or the receipts endpoint.
_Avoid_: Integration, connector

### Placing receipts

**Signal**:
A fact about a session that hints at its cost object: branch, working directory, repository, pull request, or a ticket key in a prompt.

**Rule**:
An instruction that turns signals into postings. Organization rules run before personal ones.
_Avoid_: Filter, mapping

**Classifier**:
An optional program on the developer's machine that picks among candidate tickets when rules cannot.

**Report**:
A view managers read, such as budget versus actual per project.
_Avoid_: Dashboard

**Review**:
A person checking their own draft receipts before pushing them.

**Push**:
Sending receipts from a machine to the organization.
_Avoid_: Sync, upload, submit

**Reject**:
A manager sending a receipt back to its person with a reason.
_Avoid_: Decline, return

**Cadence**:
How often a manager requires token sheets: weekly, every two weeks, monthly or custom.
_Avoid_: Reporting cadence, schedule

### Money

**List value**:
A receipt's cost at the provider's published prices.
_Avoid_: Estimated cost

**Billed value**:
A receipt's cost as the provider actually charged it, where a bill or billed telemetry says so.
_Avoid_: Actual cost

**Price table**:
The published prices per model used to compute list value. Each period keeps the table it was closed with.

**Unknown model**:
A model missing from the price table. Its cost is labelled, never shown as zero.

### Time

**Period**:
One calendar month, open or closed.
_Avoid_: Billing cycle

**Close**:
Locking a period so its receipts and postings can no longer change. It produces the cost sheet.
_Avoid_: Month-end, lock

**Adjustment**:
A signed correction an owner posts to a closed period.

### Management control

**Budget**:
A planned figure for a person, a ticket, a project or a period.
_Avoid_: Limit, cap, allowance

**Estimate**:
The size of a ticket as recorded in the ticket system.

**Actual**:
What was spent against a budget.

**Overrun**:
Actual above budget.

**Underrun**:
Actual below budget.

**Outlier**:
A cost far from the organization's own baseline for similar work.
_Avoid_: Anomaly

## Words with two meanings

- **Owner** also names the person who answers for an agent, and the person a ticket is assigned to.
- **Client** appears as a level above project and as a kind of project.
- **Member** names both a role and anyone counted towards the plan's 150.
- **Team** and **Enterprise** are also plan names, here and at Anthropic.
- **Forecast** is used next to budget without its own meaning.
