import nox
from laminci import move_built_docs_to_docs_slash_project_slug, upload_docs_dir
from laminci.nox import build_docs, login_testuser1, run_pre_commit

# from laminci.nox import run_pytest

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def build(session):
    login_testuser1(session)
    session.install(".[dev,test]")
    package_name = "pytorch_lamin_mnist"
    session.run(
        "pytest",
        "-s",
        f"--cov={package_name}",
        "--cov-append",
        "--cov-report=term-missing",
    )
    # session.run("coverage", "xml")
    build_docs(session)
    upload_docs_dir()
    move_built_docs_to_docs_slash_project_slug()
