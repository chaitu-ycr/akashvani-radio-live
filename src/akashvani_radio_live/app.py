import webview


def main():
    url = "https://akashvani.gov.in/radio/live.php"
    webview.create_window(title="Akashvani Radio Live", url=url, width=480, height=800, resizable=True)
    webview.start()


if __name__ == '__main__':
    main()
