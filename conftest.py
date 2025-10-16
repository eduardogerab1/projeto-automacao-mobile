import pytest
import os
import base64
from appium import webdriver
from appium.options.common.base import AppiumOptions

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        setattr(item, "rep_call", rep)

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_name = f"screenshot_{item.name}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)
            driver.get_screenshot_as_file(screenshot_path)
            print(f"Screenshot salvo em: {screenshot_path}")

@pytest.fixture(scope="function")
def driver(request):
    # --- SETUP PHASE ---
    options = AppiumOptions()
    options.load_capabilities({ 	"platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.saucelabs.mydemoapp.android",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
    "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
	"appWaitDuration": 30000})

    try:
        _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        _driver.start_recording_screen(videoType='h264') # Start recording
    except Exception as e:
        pytest.skip(f"Failed to create Appium driver: {e}")

    # The 'yield' keyword passes control to the test function
    yield _driver

    # --- TEARDOWN PHASE ---
    # This code runs AFTER the test function completes (or fails)
    if _driver:
        # Verifica se o teste falhou
        rep_call = getattr(request.node, "rep_call", None)
        if rep_call and rep_call.failed:
            print("Teste falhou! — salvando vídeo da execução...")
            video_data = _driver.stop_recording_screen()

            if video_data:
                videos_dir = os.path.join(os.getcwd(), "videos")
                os.makedirs(videos_dir, exist_ok=True)

                video_filename = f"video_{request.node.name}.mp4"
                video_path = os.path.join(videos_dir, video_filename)

                with open(video_path, "wb") as f:
                    f.write(base64.b64decode(video_data))
                print(f"Vídeo salvo em: {video_path}")
        else:
            # Se passou, apenas para e descarta o vídeo
            _driver.stop_recording_screen()

        print("\nQuitting driver...")
        _driver.quit()