# Contributing to ZoPy

## Branching Strategy

### Main Branches:
- `main` → Stable, production-ready code.
- `develop` → Active development, integrates feature branches.

### Supporting Branches:
- `feature/*` → New features, branched from `develop`.
- `hotfix/*` → Critical fixes for `main`.
- `release/*` → Preparing new stable releases, branched from `develop`.

## Workflow
1. **Developing a Feature:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/feature-name
   ```
2. **Fixing a Bug:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/fix-bug-name
   ```
3. **Hotfix for Production:**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b hotfix/critical-fix-name
   ```
4. **Releasing a Version:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b release/version-number
   ```
5. **Merging to `main`:**
   - All merges to `main` require **peer review and CI checks**.
   - Tag releases (`git tag -a vX.Y.Z -m "Release vX.Y.Z"`).
   ```bash
   git checkout main
   git merge release/version-number
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push origin main --tags