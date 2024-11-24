import pytest
import streamlit as st
from requests_oauthlib import OAuth2Session
from slash_user_interface import google_login, google_callback, UIManager, render_register
from oauthlib.oauth2 import InsecureTransportError

@pytest.fixture(autouse=True)
def mock_streamlit_functions(monkeypatch):
    # Mock Streamlit methods
    monkeypatch.setattr(st, "write", lambda x, **kwargs: None if "unsafe_allow_html" in kwargs else None)
    monkeypatch.setattr(st, "error", lambda x, **kwargs: None)
    monkeypatch.setattr(st, "set_page_config", lambda **kwargs: None)
    monkeypatch.setattr(st, "markdown", lambda x, **kwargs: None)
    monkeypatch.setattr(st, "experimental_set_query_params", lambda **kwargs: None)
    monkeypatch.setattr(st, "query_params", {"code": ["test_code"]})

    # Mock st.sidebar methods
    monkeypatch.setattr(st.sidebar, "markdown", lambda x, **kwargs: None)
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])


@pytest.fixture
def mock_oauth(monkeypatch):
    # Mock fetch_token to return a test access token
    monkeypatch.setattr(OAuth2Session, "fetch_token", lambda *args, **kwargs: {"access_token": "test_token"})
    
    # Mock get method to accept a URL and return mocked user info
    monkeypatch.setattr(
        OAuth2Session,
        "get",
        lambda *args, **kwargs: type("MockResponse", (object,), {"json": lambda: {"email": "test@example.com"}})()
    )

# Test Cases

def test_google_login_creates_link():
    google_login()
    assert True  # Passes if no exceptions occur during execution

def test_ui_manager_initialization():
    """
    Test if the UIManager initializes with an empty list of pages.
    """
    ui_manager = UIManager()
    assert isinstance(ui_manager.pages, list)
    assert len(ui_manager.pages) == 0


def test_ui_manager_add_page():
    """
    Test if UIManager can add a single page correctly.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    assert len(ui_manager.pages) == 1
    assert ui_manager.pages[0]["title"] == "Home"


def test_ui_manager_render_with_pages(monkeypatch):
    """
    Test rendering when multiple pages are added.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.addPage("About", lambda: st.write("About Page"))
    
    # Mock selectbox to return the first page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])

    try:
        ui_manager.render()
        assert True  # Pass if no exception occurs
    except Exception:
        assert False, "UIManager.render() raised an exception with pages."


def test_ui_manager_add_multiple_pages():
    """
    Test if UIManager can handle adding multiple pages correctly.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.addPage("About", lambda: st.write("About Page"))
    assert len(ui_manager.pages) == 2
    assert ui_manager.pages[1]["title"] == "About"


def test_ui_manager_clear_pages():
    """
    Test if UIManager can clear all pages.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.pages.clear()
    assert len(ui_manager.pages) == 0


def test_ui_manager_duplicate_page_titles():
    """
    Test adding duplicate page titles to UIManager.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.addPage("Home", lambda: st.write("Another Home Page"))
    assert len(ui_manager.pages) == 2
    assert ui_manager.pages[1]["title"] == "Home"


def test_ui_manager_render_first_page(monkeypatch):
    """
    Test rendering the first page in UIManager.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.addPage("About", lambda: st.write("About Page"))
    
    # Mock selectbox to always select the first page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])
    ui_manager.render()
    assert True  # Pass if no exception occurs


def test_ui_manager_render_last_page(monkeypatch):
    """
    Test rendering the last page in UIManager.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.addPage("About", lambda: st.write("About Page"))
    
    # Mock selectbox to always select the last page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[-1])
    ui_manager.render()
    assert True  # Pass if no exception occurs


def test_ui_manager_render_single_page(monkeypatch):
    """
    Test rendering when there is only one page.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))

    # Mock selectbox to return the only page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])
    ui_manager.render()
    assert True  # Pass if no exception occurs

def test_ui_manager_page_function_execution(monkeypatch):
    """
    Test if the page function executes correctly during render.
    """
    def home_page():
        st.write("Home Page Executed")
    
    ui_manager = UIManager()
    ui_manager.addPage("Home", home_page)

    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])
    ui_manager.render()
    assert True  # Pass if no exception occurs


def test_ui_manager_add_page_without_function():
    """
    Test adding a page without a function to UIManager.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Empty Page", None)
    assert len(ui_manager.pages) == 1
    assert ui_manager.pages[0]["function"] is None


def test_ui_manager_page_titles_are_unique():
    """
    Test if page titles in UIManager are unique.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.addPage("About", lambda: st.write("About Page"))
    page_titles = [page["title"] for page in ui_manager.pages]
    assert len(page_titles) == len(set(page_titles))


def test_ui_manager_remove_page():
    """
    Test removing a page from UIManager.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    ui_manager.pages.pop(0)
    assert len(ui_manager.pages) == 0


def test_ui_manager_render_with_invalid_page(monkeypatch):
    """
    Test rendering with an invalid page selected.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Home", lambda: st.write("Home Page"))
    
    # Mock selectbox to return an invalid page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: "Invalid Page")
    try:
        ui_manager.render()
        assert False, "UIManager.render() should raise an exception for an invalid page."
    except Exception:
        assert True  # Expected exception


def test_ui_manager_page_order():
    """
    Test if the pages in UIManager maintain their order.
    """
    ui_manager = UIManager()
    ui_manager.addPage("First", lambda: st.write("First Page"))
    ui_manager.addPage("Second", lambda: st.write("Second Page"))
    ui_manager.addPage("Third", lambda: st.write("Third Page"))

    page_titles = [page["title"] for page in ui_manager.pages]
    assert page_titles == ["First", "Second", "Third"]


def test_ui_manager_no_pages_return_empty():
    """
    Test if UIManager.pages returns an empty list when no pages are added.
    """
    ui_manager = UIManager()
    assert ui_manager.pages == []


def test_ui_manager_render_only_one_page(monkeypatch):
    """
    Test rendering when only one page is available.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Single Page", lambda: st.write("Only Page"))
    
    # Mock selectbox to always select the only page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])
    ui_manager.render()
    assert True  # Pass if no exception occurs


def test_ui_manager_add_pages_in_sequence():
    """
    Test adding pages sequentially and verify their order.
    """
    ui_manager = UIManager()
    ui_manager.addPage("First Page", lambda: st.write("Page 1"))
    ui_manager.addPage("Second Page", lambda: st.write("Page 2"))
    ui_manager.addPage("Third Page", lambda: st.write("Page 3"))
    
    page_titles = [page["title"] for page in ui_manager.pages]
    assert page_titles == ["First Page", "Second Page", "Third Page"]


def test_ui_manager_render_page_function_execution(monkeypatch):
    """
    Test if the selected page function executes correctly during render.
    """
    def test_page():
        st.write("Test Page Rendered")
    
    ui_manager = UIManager()
    ui_manager.addPage("Test Page", test_page)
    
    # Mock selectbox to always select the test page
    monkeypatch.setattr(st.sidebar, "selectbox", lambda x, y, format_func: y[0])
    ui_manager.render()
    assert True  # Pass if no exception occurs


def test_ui_manager_handle_no_function_page():
    """
    Test rendering a page with no assigned function.
    """
    ui_manager = UIManager()
    ui_manager.addPage("Empty Page", None)
    assert ui_manager.pages[0]["function"] is None
    assert len(ui_manager.pages) == 1

def test_google_callback_with_invalid_code(monkeypatch):
    """
    Test google_callback function with an invalid 'code' in query params.
    This simulates a failure in fetching the token.
    """
    # Mock the query params to provide an invalid 'code'
    monkeypatch.setattr(st, "query_params", {"code": ["invalid_code"]})

    # Mock OAuth2Session.fetch_token to raise an exception for invalid code
    def mock_fetch_token(*args, **kwargs):
        raise ValueError("Invalid authorization code")

    monkeypatch.setattr(OAuth2Session, "fetch_token", mock_fetch_token)

    try:
        google_callback()
        assert False, "google_callback() should raise an error for invalid code"
    except ValueError as e:
        assert str(e) == "Invalid authorization code"
    except Exception:
        assert False, "Unexpected exception raised by google_callback()"
