import contextlib
import os
from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from pages.basic_cart_page import BasicCartPage
from pages.seven_char_val_page import SevenCharValPage
from pages.triangle_page import TrianglePage


def _headless() -> bool:
    # domyślnie headless, chyba że lokalnie ustawisz PW_HEADLESS=0
    return os.getenv("PW_HEADLESS", "1") not in {"0", "false", "False"}


def _get_artifact_dir() -> str:
    artifact_dir = Path("test-results")
    artifact_dir.mkdir(exist_ok=True)
    return str(artifact_dir)


def pytest_configure(config):
    """Konfiguracja Pytest."""
    _get_artifact_dir()
    config.addinivalue_line("markers", "on_failure: załaduj artefakty tylko przy porażce")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Track test results for artifact saving."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=_headless())
        yield browser
        browser.close()


@pytest.fixture
def context(
    browser: Browser, request: pytest.FixtureRequest
) -> Generator[BrowserContext, None, None]:
    artifact_dir = _get_artifact_dir()
    test_name = request.node.name

    # Nagrywanie wideo (będzie usunięte jeśli test przejdzie)
    video_dir = os.path.join(artifact_dir, "videos")
    Path(video_dir).mkdir(exist_ok=True)

    ctx = browser.new_context(
        record_video_dir=video_dir,
    )

    # Tracing - zawiera screenshots i snapshots
    ctx.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield ctx

    # Pobierz ścieżkę wideo
    video_path = None
    if ctx.pages:
        for page in ctx.pages:
            video = page.video
            if video:
                with contextlib.suppress(Exception):
                    video_path = video.path()
    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    if test_failed:
        # Zapisz trace
        trace_path = os.path.join(artifact_dir, f"{test_name}.zip")
        ctx.tracing.stop(path=trace_path)
        print(f"\n🔍 Trace zapisany: {trace_path}")

        # Trace zawiera wszystkie informacje
        print("   ✓ Screenshots")
        print("   ✓ DOM Snapshots")
        print("   ✓ Network Events")
    else:
        # Nie zapisuj trace jeśli test przeszedł
        ctx.tracing.stop()

        # Usuń wideo jeśli test przeszedł
        if video_path and os.path.exists(video_path):
            with contextlib.suppress(Exception):
                os.remove(video_path)


@pytest.fixture
def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    p = context.new_page()
    yield p

    # Screenshots on failure
    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    if test_failed:
        artifact_dir = _get_artifact_dir()
        screenshot_path = os.path.join(artifact_dir, f"{request.node.name}_failure.png")
        p.screenshot(path=screenshot_path, full_page=True)
        print(f"📸 Screenshot zapisany: {screenshot_path}")

    p.close()


@dataclass
class AppPages:
    triangle: TrianglePage
    seven_char_val: SevenCharValPage
    basic_cart: BasicCartPage


@pytest.fixture
def app_pages(page: Page) -> AppPages:
    return AppPages(
        triangle=TrianglePage(page),
        seven_char_val=SevenCharValPage(page),
        basic_cart=BasicCartPage(page),
    )
