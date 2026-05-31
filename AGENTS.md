# Project Context for Codex

## User Profile

The user is an engineering graduate student on Windows. Their research direction is polarization imaging combined with super-resolution and HDR reconstruction. They are interested in AI products, model systems, agents, programming tools, and research productivity. They can handle moderately dense technical explanations, but prefer compact Chinese answers with fewer unnecessary lists and line breaks.

## Current Project

Workspace:

```text
current project root
```

GitHub repository:

```text
MingyiJiang/Polarization-HDR-SR-Baseline
```

Purpose:

```text
Git/GitHub learning context and practice record for Codex.
```

Current repository structure:

```text
AGENTS.md
```

This repository is now mainly used to preserve Git/GitHub learning context across Codex conversations. Do not treat it as a frontend project, Python package, or active research baseline unless the user explicitly repurposes it. Do not provide localhost preview links unless a real dev server has been started for a frontend app.

Only `AGENTS.md` is intended to remain as a content file in this repository. The `.git` directory must remain because it stores Git history and the remote connection.

## Git/GitHub Learning Progress

The user has already practiced GitHub Star/Watch, Fork, Pull Request, Issue, personal repository creation, local clone, Git identity configuration, add/commit/push, pull/fetch/clone/init, branch/merge/delete, restore/revert, HEAD, and basic Trae source-control operations.

The user prefers Trae for Git operations, but can run PowerShell commands when needed. Explain both only when useful.

At the start of a new conversation, first align state with:

```powershell
git status --short --branch
git remote -v
```

Then explain the result before suggesting any Git operation.

This conversation previously connected to the user's remote GitHub repository through the local Git remote:

```text
origin = https://github.com/MingyiJiang/Polarization-HDR-SR-Baseline.git
```

The user successfully pushed to GitHub after configuring a temporary proxy in PowerShell. Remote branch cleanup and feature branch merge practice were also completed.

## GitHub Practice History

- Forked `ChenyangLEI/awesome-polarization-in-vision`.
- Opened PR `Add PIDSR CVPR 2025 paper` to add a PIDSR CVPR 2025 paper entry.
- Opened an Issue in `elerac/polanalyser` about HDR and high-bit-depth polarization image workflows.
- Created the personal repository `MingyiJiang/Polarization-HDR-SR-Baseline`.
- Practiced local branch creation, push, merge into `main`, and remote branch deletion.

## Important Git Notes

Common mental model:

```text
edit files -> stage/add -> commit locally -> push to GitHub
```

Branch mental model:

```text
main = stable line
feature/... or experiment/... = temporary work line
merge = bring accepted work back into main
```

For undo:

```text
restore = discard uncommitted changes
revert = create a new commit that reverses a committed change
```

Avoid `reset --hard` unless the user explicitly requests it and understands the consequence.

## Network and Proxy

GitHub access from Git may fail with:

```text
Failed to connect to github.com port 443
```

This was caused by Git not using the proxy. A temporary PowerShell proxy that worked was:

```powershell
$env:HTTPS_PROXY="http://127.0.0.1:7890"
$env:HTTP_PROXY="http://127.0.0.1:7890"
```

This only applies to the current terminal session.

## PowerShell Note

PowerShell may print an execution policy warning for:

```text
C:\Users\MingyiJiang\Documents\WindowsPowerShell\profile.ps1
```

This is related to profile script execution policy and Conda initialization. The user chose not to change it for now. It does not usually block Git commands.

## Response Preferences

- Use Chinese by default.
- Keep answers compact but technically clear.
- For Git operations, first explain what the operation changes.
- When the user asks to inspect or clean the repo, check status first and avoid destructive operations without a clear reason.
- Do not manually modify `.git`.
- Do not suggest opening localhost unless a real local server is running.
- If the user asks to continue GitHub learning, prefer practical task-based guidance over abstract command memorization.
