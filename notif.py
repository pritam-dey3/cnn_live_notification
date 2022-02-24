import time

from plyer import notification

from scrapper import get_headlines


max_noti = 3
timeout = 120

old_headlines = set()


def send_single_notif(headline):
    print("showing notification.")
    notification.notify(
        title="Russia and Ukraine",
        message=headline,
        app_name="RvU",
        timeout=20,
    )
    time.sleep(2)


def send_notification():
    print("checking for new news...")
    new_headlines = get_headlines()
    n = 0
    print(len(new_headlines))
    for hl in new_headlines:
        if hash(hl) not in old_headlines:
            send_single_notif(hl)
            old_headlines.add(hash(hl))
            n += 1
        if n > max_noti:
            break


def start():
    while True:
        send_notification()
        print(f"waiting for {timeout} seconds.")
        time.sleep(timeout)


if __name__ == "__main__":
    start()
