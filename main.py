from win10toast import ToastNotifier

testNoti = ToastNotifier()
testNoti.show_toast(
    "Notification Title",
    "Notification Body",
    duration=20,
    threaded=False
)
