# MDSCollabSpecs

This site showcases the plan and demos of a redesign review process.

## Core problem

Software Development part of MDS curriculum is one of the most disrupted right now – development experience is rapidly changing, and we don't have full picture how. We need to make two radical shifts:

- The course should start providing situational decision making skills about software projects and infrastructures (with MDS flavour), with clear accent on how they apply what they learn not only for us, but outside of classroom
- The learning experience itself should evolve, giving students an opportunity to experience, interact and evaluate with key new components of software project infrastructure

## Summary of the proposal

Lecture part splits into:
- active learning "strategy" part, focusing on infrastructure and collaboration decisions and interactions
- procedural "how to do something" part, majorly asynchronous
- in 26-27 lecture activities are piloted and graded on quality completion, a year after become part of the grade, maybe with CBTF part testing strategy (see UBC-O experience on exams for project courses)

The main lab-milestone part transforms focusing on experiential learning:

- we expose students to navigate our requirements as software and course specifications, they need to tackle
- we adapt meaningful industry-inspired formats (JTBD, definitions of done, ATDD) to lay out the requirements in a way, making clear WHY they are meaningful, HOW to achieve them, and provide them with some choices
- we introduce shift to specification grading – evidence-informed tool, reducing focus on grading and increasing focus on mastery formation
- we expose them to partially automated TA-in-the-loop feedback from day 1
- we use this simulation to "unbox" modern approaches to dev infrastructure and collaboration in parallel with providing experience

The role of the TA changes. Instead of spending sync time on status collection, they come in with a compact evidence summary per spec already in front of them — mentoring time goes to root causes. When a spec fails across multiple dimensions, failure signals are ranked so feedback doesn't get skewed by one strong metric. Instructors get comparable pass/fail patterns across groups and milestones, so they can adjust teaching focus quickly rather than waiting until the course ends.

This redesign challenges students to exercise higher-order cognitive skills by navigating the trade-offs between project criticality, resource allocation, and technical debt. By engaging them in a professional simulation, we nudge them to take technical leadership thinking hat, encouraging to justify their architectural choices in real-world contexts.

We shift Week 1 to Software Development Management and introduce them to the ways to formulate and prioritise needs, requirements, precise Definitions of Done (DoD) using structured Gherkin syntax. This is a useful thinking device to nudge them thinking clearly and also a thinking device to structure interaction both with human collaborators and generative (AI) agents. We also expose them to prioritization approaches (Must/Should/Could lens used in specs, (R)ICE).

The technical core is CollabSpecsEval, a system allowing to formulate multi-level projects specs, navigate them, gather evidence, and generate feedback. We use GitHub API and repository analysis evidence gatherers, and engage binary structural requirements and LLM-Assisted Feedback to extract quality signals and provide feedback.

Students learn to manage their Debt Ledger model, where unresolved "Must-level" gaps from early milestones carry over as interest, making feedback is not an autopsy of past mistakes but a roadmap for future development.

> **Note: Habit formation psychology** — To be expanded.

Finally, we (as it is already done in 524) use "System as Syllabus" approach: in Week 3 instead of learning ci/cd from scratch, we deconstruct the infrastructure they already experienced and discuss the technical architecture and implications for future projects in evolving development landscape.
