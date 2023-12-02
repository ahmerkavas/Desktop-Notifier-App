from plyer import notification

icon_path = "alert.ico"
# Make sure it is an image with ico extension.

notification.notify(title="Alert", message="Get Back To Work!", app_icon=icon_path, timeout=5)
