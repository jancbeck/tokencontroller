# Token Controller

Cost accounting and management control for AI agents: token entries from agents are matched to provider bills, placed on the work that caused them, and compared with token budgets.

## Language

### The two sides

**Token entry**:
One agent session's account of what it spent and on what work: tokens, cost, model, time range and a one-line summary. It is to a token sheet what a time entry is to a timesheet.
_Avoid_: Receipt, report item, line item, usage record, voucher

**Bill**:
A provider's figure for one period: gross, discount, credit and net. It is the total the token entries must add up to.
_Avoid_: Statement, invoice

**Token sheet**:
One person's token entries for a stretch of time, sent in together, the way a timesheet holds hours.
_Avoid_: Report, submission

**Cost sheet**:
The locked account of one closed period for the whole organization: cost per project and ticket, adding up to the bill. With approval on, it holds approved cost only.
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
The part of a bill that no token entry explains. Always shown as its own line.
_Avoid_: Leftover, difference

### Where cost sits

**Posting**:
The placement of a token entry, or a share of it, on one cost object with one cost kind.
_Avoid_: Allocation, assignment

**Cost center**:
A node of the team tree that collects cost: a person, a team, a department or the organization. Every posting lands on exactly one person, the agent manager of the agent that spent it, and rolls up from there.
_Avoid_: Who, person side

**Cost object**:
The work a cost paid for: a ticket, a project or the organization. Ticket cost rolls up to its parent ticket and its project.
_Avoid_: What, work side

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
_Avoid_: Account, tenant, workspace, company, client

**Project**:
A body of work made of tickets.

**Client**:
A label on a project that names who the work is for. Projects with the same client can be totalled.
_Avoid_: Customer, account

**Ticket**:
Any unit of work: a feature, a story, an epic or a bug. Tickets can sit inside other tickets.
_Avoid_: Issue, task, story, work item

### People

**Person**:
A human in the organization. A person belongs to one team at a time.
_Avoid_: User, developer

**Team**:
A node in the team tree: a team, a department or the whole organization.
_Avoid_: Group

**Team tree**:
The organization's people arranged as person, team, department, organization.
_Avoid_: Org chart, hierarchy

**Member**:
Anyone in the organization, whatever their role.
_Avoid_: User, seat

**Agent manager**:
The role that manages agents: sends token sheets and sees its own cost. Every agent has exactly one agent manager, who answers for its cost.
_Avoid_: Member, supervisor, owner, orchestrator, prompter, developer

**People manager**:
The role that manages people and projects: reads reports, sets token budgets and cadence, and approves or rejects token entries, for the teams or projects it is assigned. A people manager is also an agent manager.
_Avoid_: Manager

**Controller**:
The role that sees everything, runs the close and posts adjustments.
_Avoid_: Owner, admin

**Assignee**:
The person a ticket is assigned to.
_Avoid_: Ticket owner

### Agents

**Agent**:
An identity that spends tokens and sends token entries: a developer's local agent, a CI automation or a remote agent. It has exactly one agent manager.
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
The one line an agent writes about what a session did. It is the only text in a token entry.

**Telemetry event**:
One model call as reported live by the agent: tokens, cost and IDs, no text.

**Door**:
A way token entries or telemetry reach Token Controller: session files, telemetry push, the GitHub Action or the token entries endpoint.
_Avoid_: Integration, connector

### Placing token entries

**Signal**:
A fact about a session that hints at its cost object: branch, working directory, repository, pull request, or a ticket key in a prompt.

**Rule**:
An instruction that turns signals into postings. Organization rules run before personal ones.
_Avoid_: Filter, mapping

**Classifier**:
An optional program on the developer's machine that picks among candidate tickets when rules cannot.

**Report**:
A view people managers read, such as token budget versus actual per project.
_Avoid_: Dashboard

**Review**:
A person checking their own draft token entries before pushing them.

**Push**:
Sending token entries from a machine to the organization.
_Avoid_: Sync, upload, submit

**Approval**:
A people manager accepting pushed token entries. An organization can switch approval off. With approval on, a period cannot be closed while a token entry in it is unapproved.
_Avoid_: Sign-off, posted

**Status**:
Where a token entry stands: draft (still on the machine), pushed (counts in reports), approved, rejected (does not count until fixed) or locked (its period is closed).

**Reject**:
A people manager sending a token entry back to its agent manager with a reason.
_Avoid_: Decline, return

**Cadence**:
How often a people manager requires token sheets: weekly, every two weeks, monthly or custom.
_Avoid_: Reporting cadence, schedule

### Money

**List value**:
A token entry's cost at the provider's published prices.
_Avoid_: Estimated cost

**Billed value**:
A token entry's cost as the provider actually charged it, where a bill or billed telemetry says so.
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
Locking a period so its token entries and postings can no longer change. It produces the cost sheet.
_Avoid_: Month-end, lock

**Adjustment**:
A signed correction a controller posts to a closed period.

### Management control

**Token budget**:
Money a human has planned for a person, a ticket, a project or a period. It is compared with actual cost and never stops spending.
_Avoid_: Budget, limit, cap, allowance

**Token forecast**:
Money Token Controller predicts for a ticket, a project or a period from past cost. It becomes a token budget only when a person accepts it.
_Avoid_: Forecast, estimate, prediction

**Actual**:
What was spent against a token budget.

**Overrun**:
Actual above token budget.

**Underrun**:
Actual below token budget.

**Outlier**:
A cost far from the organization's own baseline for similar work.
_Avoid_: Anomaly

## Words with two meanings

- **Team** and **Enterprise** are also plan names, here and at Anthropic. A plan is always written with the word: Team plan, Enterprise plan.
