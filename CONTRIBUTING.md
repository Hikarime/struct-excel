# Contributing Guide

## Requirements

- `python` >= `3.13`
- [`black`](https://github.com/psf/black)

## Setup Development Environment

1. Fork this repository
2. Clone the forked repository and enter the directory

   ```bash
   git clone git@github.com:<username>/struct-excel.git
   cd struct-excel
   ```

   > Replace `<username>` with your username.

3. Set up the virtual environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Set and update the upstream

   ```bash
   git remote add upstream https://github.com/Fovir-GitHub/struct-excel.git
   git fetch upstream
   ```

6. Create and switch to a new branch based on `upstream/main`

   ```bash
   git switch --create <branch-name> upstream/main
   ```

   > Replace the `<branch-name>` with a new branch name.
   >
   > The branch name should follow [Branch Style](#branch-style)

7. Format code with `black`

   ```bash
   black .
   ```

8. Run tests (see [Testing](#testing))

9. Commit changes

   The commit style should follow [Conventional Commits](https://www.conventionalcommits.org/).

10. Push changes to forked repository

    ```bash
    git push -u origin <branch-name>
    ```

    > `<branch-name>` is the branch where your changes exist.

11. Create a pull request and wait for review and approval.

12. Delete the merged branch (optional)

## Branch Style

- `feature/*`: For submitting a new feature. For example, `feature/normalization`.
- `fix/*`: For fixing bugs. For example, `fix/fix-error-type`.
- `docs`: Document-related changes such as modifying `README`.
- `refactor/*`: For refactoring code. For example, `refactor/normalize-phone-number`.

## Testing

All testing files are under the `tests/` folder.

Run full testing:

```bash
pytest
```

Run specific testing:

```bash
pytest /path/to/test/file
```

E.g.

```bash
pytest ./tests/test_to_student.py
pytest ./tests/test_to_supervisor.py
```
