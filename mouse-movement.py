import pyautogui
import time

def move_mouse():
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2

    # Print screen dimensions
    print(f"Screen dimensions: {screen_width}x{screen_height}")

    # Print current mouse position
    current_mouse_x, current_mouse_y = pyautogui.position()
    print(f"Current mouse position: ({current_mouse_x}, {current_mouse_y})")

    # Move mouse to the center of the screen
    pyautogui.moveTo(center_x, center_y)
    time.sleep(1)
    print(f"Mouse moved to center: ({center_x}, {center_y})")

    # Move mouse to the right
    pyautogui.moveTo(center_x + 100, center_y)
    time.sleep(1)
    print(f"Mouse moved to right: ({center_x + 100}, {center_y})")

    # Move mouse to the left
    pyautogui.moveTo(center_x - 100, center_y)
    time.sleep(1)
    print(f"Mouse moved to left: ({center_x - 100}, {center_y})")

    # Move mouse up
    pyautogui.moveTo(1, 1)
    time.sleep(1)
    print(f"Mouse moved up: ({1}, {1})")

    # Move mouse down
    pyautogui.moveTo(center_x, center_y + 100)
    time.sleep(1)
    print(f"Mouse moved down: ({center_x}, {center_y + 100})")

if __name__ == "__main__":
    move_mouse()
