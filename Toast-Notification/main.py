from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Notification", "Follow @jeceey for more...", icon_path="custom.ico", duration=20, threaded=True)