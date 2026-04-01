# Publishing pympesa to PyPI

This guide covers everything needed to publish a release to PyPI and TestPyPI using the automated GitHub Actions workflow.

The workflow uses **OIDC Trusted Publishing** — no API tokens are stored in GitHub secrets. PyPI and GitHub exchange short-lived credentials automatically when a release is published.

---

## Prerequisites

- Push access to `github.com/pythias-io/pympesa`
- A PyPI account at `pypi.org`
- A TestPyPI account at `test.pypi.org` (same login as PyPI)

---

## One-time setup

These steps only need to be done once, before the first release.

### 1. Claim the package name on PyPI

If `pympesa` has never been published before, PyPI requires at least one upload before you can configure Trusted Publishing. Do a first manual upload from your local machine (see [Manual publishing](#manual-publishing-fallback) below), then return here.

If the package already exists on PyPI under your account, skip to step 2.

### 2. Configure Trusted Publisher on PyPI

1. Go to **https://pypi.org/manage/account/publishing/**
2. Click **"Add a new pending publisher"** (or open your existing project and go to **Publishing**)
3. Fill in the form:

   | Field | Value |
   |---|---|
   | PyPI Project Name | `pympesa` |
   | Owner | `pythias-io` |
   | Repository name | `pympesa` |
   | Workflow name | `publish.yml` |
   | Environment name | `pypi` |

4. Click **Add**.

### 3. Configure Trusted Publisher on TestPyPI

1. Go to **https://test.pypi.org/manage/account/publishing/**
2. Click **"Add a new pending publisher"**
3. Fill in the form:

   | Field | Value |
   |---|---|
   | PyPI Project Name | `pympesa` |
   | Owner | `pythias-io` |
   | Repository name | `pympesa` |
   | Workflow name | `publish.yml` |
   | Environment name | `testpypi` |

4. Click **Add**.

### 4. Create GitHub Environments

The workflow references two environments (`pypi` and `testpypi`). GitHub environments let you add optional protection rules (e.g. require manual approval before publishing to production).

1. Open the repo on GitHub → **Settings** → **Environments**
2. Click **New environment**, name it `pypi`
   - Optional: enable **Required reviewers** and add yourself for extra safety
3. Repeat for `testpypi`

---

## Releasing a new version

### Step 1 — Bump the version

Version is declared in two places; both must match.

**`pyproject.toml`**
```toml
[project]
version = "2.1.0"
```

**`src/pympesa/__init__.py`**
```python
__version__ = "2.1.0"
```

Update `CHANGELOG.md` with the release notes for the new version.

Commit and push to `master`:
```bash
git add pyproject.toml src/pympesa/__init__.py CHANGELOG.md
git commit -m "Bump version to 2.1.0"
git push origin master
```

### Step 2 — Create a GitHub Release

1. Go to **https://github.com/pythias-io/pympesa/releases/new**
2. Click **"Choose a tag"** → type `v2.1.0` → click **"Create new tag: v2.1.0 on publish"**
3. Set **Release title** to `v2.1.0`
4. Paste the `CHANGELOG.md` section for this release into the description box
5. Click **Publish release**

> The tag must match the pattern `v<version>` (e.g. `v2.1.0`). The version number must match what is in `pyproject.toml`.

### Step 3 — Monitor the workflow

After publishing the release, GitHub Actions triggers `.github/workflows/publish.yml` automatically.

1. Go to **https://github.com/pythias-io/pympesa/actions**
2. Open the **"Publish to PyPI"** workflow run
3. Three jobs run in sequence:
   - **Build distribution** — builds `pympesa-2.1.0.tar.gz` and `pympesa-2.1.0-py3-none-any.whl`
   - **Publish to PyPI** — pushes to `pypi.org` (requires the `pypi` environment to approve if reviewers are configured)
   - **Publish to TestPyPI** — pushes to `test.pypi.org`

If any job fails, see [Troubleshooting](#troubleshooting) below.

### Step 4 — Verify the release

```bash
# Verify it is live on PyPI
pip index versions pympesa

# Install from PyPI and smoke-test
pip install pympesa==2.1.0
python -c "import pympesa; print(pympesa.__version__)"

# Or install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pympesa==2.1.0
```

---

## Manual publishing (fallback)

If GitHub Actions is unavailable or for the very first upload to claim the package name:

```bash
# Install tools
pip install build twine

# Build
python -m build

# Check the dist files are valid
twine check dist/*

# Upload to TestPyPI first (recommended)
twine upload --repository testpypi dist/*

# Verify install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pympesa

# Upload to PyPI
twine upload dist/*
```

`twine upload` will prompt for your PyPI username and password (or an API token — use `__token__` as the username and paste the token as the password).

To avoid re-entering credentials, create `~/.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-<your-token-here>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-<your-testpypi-token-here>
```

---

## Troubleshooting

**`403 Forbidden` during publish**
The Trusted Publisher configuration does not match. Double-check that the Owner, Repository name, Workflow name (`publish.yml`), and Environment name (`pypi` / `testpypi`) all match exactly what is set on PyPI/TestPyPI.

**`400 File already exists`**
A release for this version was already uploaded. PyPI does not allow re-uploading the same filename. You must bump the version number — you cannot overwrite an existing release.

**`Invalid distribution` / twine check fails**
Run `twine check dist/*` locally. Common causes: malformed `README.md` (PyPI requires valid reStructuredText or Markdown), missing `description`, or a bad classifier string.

**Workflow does not trigger**
The workflow triggers only on `release` events of type `published`. Draft releases and pre-releases do not trigger it unless you explicitly click "Publish release".

**`Environment not found` error in Actions**
Create the `pypi` and `testpypi` environments in **Settings → Environments** on GitHub (see [step 4](#4-create-github-environments) above).
