from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / "loan_dashboard.py")


def run_app():
    return AppTest.from_file(APP, default_timeout=60).run()


def test_dashboard_loads_without_errors():
    at = run_app()
    assert not at.exception
    assert at.title[0].value == "Loan Data Dashboard"


def test_area_filter_lists_all_areas():
    at = run_app()
    options = at.sidebar.multiselect[0].options
    assert sorted(options) == ["Rural", "Semiurban", "Urban"]


def test_single_area_filter_works():
    at = run_app()
    at.sidebar.multiselect[0].set_value(["Rural"]).run()
    assert not at.exception


def test_empty_selection_shows_warning():
    at = run_app()
    at.sidebar.multiselect[0].set_value([]).run()
    assert not at.exception
    assert "Select at least one area" in at.warning[0].value
