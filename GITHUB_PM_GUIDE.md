# GitHub Project Management Guide

This document explains how to use GitHub's project management tools effectively for the 524-pmdemo project.

## Table of Contents
1. [GitHub Issues](#github-issues)
2. [Labels](#labels)
3. [Milestones](#milestones)
4. [Projects (Boards)](#projects-boards)
5. [Pull Requests](#pull-requests)
6. [Workflows](#workflows)

## GitHub Issues

### Creating Issues

All work should start with an issue. Issues are used to track:
- Bugs
- Feature requests
- Documentation improvements
- Questions and discussions

### Using Issue Templates

We have three issue templates:
1. **Bug Report** (`.github/ISSUE_TEMPLATE/bug_report.md`)
2. **Feature Request** (`.github/ISSUE_TEMPLATE/feature_request.md`)
3. **Documentation Update** (`.github/ISSUE_TEMPLATE/documentation.md`)

To create an issue:
1. Go to the Issues tab
2. Click "New Issue"
3. Select the appropriate template
4. Fill in all required fields
5. Add labels and assignees
6. Link to related issues or PRs

### Issue Lifecycle

```
Open → In Progress → In Review → Closed
```

### Best Practices for Issues

- **One issue per topic**: Keep issues focused on a single task or bug
- **Clear titles**: Use descriptive titles that summarize the issue
- **Detailed descriptions**: Provide enough context for anyone to understand
- **Regular updates**: Comment with progress or blockers
- **Link related items**: Reference related issues and PRs using #number
- **Close when done**: Close issues promptly when resolved

## Labels

### Standard Labels

We use the following label categories:

#### Type Labels
- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Documentation improvements
- `question`: Further information is requested

#### Priority Labels
- `priority: critical`: Must be addressed immediately
- `priority: high`: Should be addressed soon
- `priority: medium`: Normal priority
- `priority: low`: Nice to have

#### Status Labels
- `status: in-progress`: Work is ongoing
- `status: blocked`: Work is blocked by something
- `status: needs-review`: Ready for review
- `status: wontfix`: This will not be worked on

#### Area Labels
- `area: processor`: Related to data processing
- `area: analyzer`: Related to data analysis
- `area: visualizer`: Related to visualization
- `area: tests`: Related to testing
- `area: ci-cd`: Related to CI/CD pipeline

#### Difficulty Labels
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `difficulty: easy`: Easy to fix
- `difficulty: medium`: Moderate complexity
- `difficulty: hard`: Requires significant effort

### Applying Labels

1. When creating an issue, add relevant labels
2. Update labels as the issue progresses
3. Use multiple labels to provide complete context

## Milestones

Milestones group related issues and track progress toward goals.

### Creating Milestones

Example milestones:
- **v0.1.0 - Initial Release**
- **v0.2.0 - Enhanced Analysis Features**
- **Sprint 1 (Jan 8-22)**
- **Documentation Sprint**

### Using Milestones

1. Go to Issues → Milestones
2. Click "New milestone"
3. Set title, description, and due date
4. Assign issues to the milestone
5. Track progress on the milestone page

### Best Practices

- Set realistic due dates
- Don't overload milestones
- Close completed milestones
- Review milestone progress in team meetings

## Projects (Boards)

GitHub Projects provide a Kanban-style board for visualizing work.

### Setting Up a Project Board

1. Go to the Projects tab
2. Click "New project"
3. Choose "Board" template
4. Create columns:
   - 📋 Backlog
   - 🎯 To Do
   - 🚧 In Progress
   - 👀 In Review
   - ✅ Done

### Using the Board

1. **Add issues to the board**
   - Drag issues from Backlog to columns
   - Or add from the issue page

2. **Move cards through workflow**
   - Drag cards between columns as work progresses
   - Update issue status accordingly

3. **Team workflow**
   ```
   Backlog → To Do → In Progress → In Review → Done
   ```

4. **Weekly process**
   - Monday: Team reviews Backlog, moves items to To Do
   - Daily: Team members update their cards
   - Friday: Review completed work, close issues

### Automation

Set up automation rules:
- Auto-move to "In Progress" when issue is assigned
- Auto-move to "In Review" when PR is opened
- Auto-move to "Done" when issue is closed

## Pull Requests

### Creating Pull Requests

1. Create a feature branch
2. Make your changes
3. Push to your fork
4. Open a PR to the main repository
5. Fill in the PR template:
   - Clear title
   - Description of changes
   - Link to related issues (e.g., "Closes #123")
   - Screenshots if applicable

### PR Review Process

1. **Request reviewers**
   - Assign at least one team member
   - Use the "Reviewers" sidebar

2. **Code review**
   - Reviewers examine code
   - Leave comments and suggestions
   - Approve or request changes

3. **Addressing feedback**
   - Make requested changes
   - Push new commits to the branch
   - Respond to comments
   - Re-request review

4. **Merging**
   - All checks must pass
   - At least one approval required
   - No merge conflicts
   - Merge using "Squash and merge" or "Rebase and merge"

### PR Labels

Apply relevant labels to PRs:
- `status: needs-review`
- `status: changes-requested`
- `priority: high`
- `area: processor`

### Linking PRs to Issues

In the PR description:
```markdown
Closes #123
Fixes #456
Related to #789
```

## Workflows

### Issue → Development → PR → Review → Merge

```
1. Create Issue
   ↓
2. Assign to team member
   ↓
3. Create feature branch
   ↓
4. Develop & commit
   ↓
5. Push & open PR
   ↓
6. Code review
   ↓
7. Address feedback
   ↓
8. Approval & merge
   ↓
9. Close issue
```

### Sprint Workflow

**Week 1:**
- Monday: Sprint planning
  - Review backlog
  - Create/update milestone
  - Assign issues
  - Move to "To Do" column

- Tuesday-Thursday: Development
  - Work on assigned issues
  - Update issue status
  - Move cards on board
  - Daily standups (optional)

- Friday: Sprint review
  - Demo completed work
  - Close finished issues
  - Update milestone progress

**Week 2:**
- Continue work on remaining items
- Friday: Retrospective
  - What went well?
  - What can improve?
  - Action items for next sprint

### Release Workflow

1. Create release milestone
2. Assign issues to milestone
3. Complete all issues
4. Run full test suite
5. Update CHANGELOG
6. Create release tag
7. Publish release on GitHub
8. Close milestone

## Team Collaboration

### Communication

- **Issues**: Use for discussions about specific topics
- **PR Reviews**: Use for code-related discussions
- **Project Discussions**: Use GitHub Discussions for general topics

### Notifications

Configure notifications:
1. Watch the repository
2. Set custom notification preferences
3. Enable email or web notifications

### Team Conventions

1. **Tag team members** with @username when needed
2. **Use references** (#123) to link related items
3. **Update status** regularly on issues and PRs
4. **Be responsive** to review requests
5. **Celebrate wins** 🎉 when closing major issues

## GitHub Actions Integration

Our CI/CD pipeline (`.github/workflows/ci.yml`) automatically:
- Runs linting on all PRs
- Runs tests on all PRs
- Builds the package
- Reports status to PR

### Checks

Before merging, ensure:
- ✅ All CI checks pass
- ✅ Code coverage maintained
- ✅ No linting errors
- ✅ Tests pass on all Python versions

## Metrics and Insights

### Using Insights Tab

Track project health:
1. **Pulse**: Recent activity summary
2. **Contributors**: Contribution statistics
3. **Traffic**: Repository visits and clones
4. **Commits**: Commit frequency
5. **Code frequency**: Lines added/removed

### Issue Metrics

Monitor:
- Open vs. closed issues
- Average time to close
- Issue velocity
- Label distribution

### Example Report

```
Sprint 1 Metrics:
- Issues opened: 15
- Issues closed: 12
- PRs merged: 10
- Code coverage: 85%
- Average time to merge: 2 days
```

## Recommended Tools

### GitHub CLI

Install `gh` for command-line operations:
```bash
# Create issue
gh issue create --title "Bug fix" --body "Description"

# List issues
gh issue list --label bug

# Create PR
gh pr create --title "Add feature" --body "Description"

# Check PR status
gh pr status
```

### Browser Extensions

- **Refined GitHub**: Enhances GitHub interface
- **OctoTree**: File tree navigation
- **GitHub PR Helper**: Improved PR review

## Summary

Effective use of GitHub project management tools:
1. ✅ Use issues for all work tracking
2. ✅ Apply appropriate labels
3. ✅ Group work with milestones
4. ✅ Visualize workflow with project boards
5. ✅ Follow PR review process
6. ✅ Automate with GitHub Actions
7. ✅ Monitor metrics and insights
8. ✅ Communicate effectively

---

For more information, see:
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [TEAM_CONTRACT.md](TEAM_CONTRACT.md)
- [GitHub Docs](https://docs.github.com)
