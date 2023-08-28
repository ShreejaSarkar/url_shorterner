import tkinter as tk
import pyshorteners

class ShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("480x480")  # Set the window size to 480x480
        self.root.configure(bg="black")  # Set the background color to black

        self.label = tk.Label(root, text="Enter the URL to shorten:", font=("Helvetica", 20), fg="white", bg="black")
        self.label.pack(pady=20)

        self.url_entry = tk.Entry(root, width=40, font=("Helvetica", 20))
        self.url_entry.pack()

        self.shorten_button = tk.Button(root, text="Shorten", command=self.shorten_url, font=("Helvetica", 20))
        self.shorten_button.pack(pady=10)

        self.shortened_label = tk.Label(root, text="", font=("Helvetica", 20), fg="white", bg="black")
        self.shortened_label.pack(pady=20)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Helvetica", 20))
        self.copy_button.pack()

    def shorten_url(self):
        original_url = self.url_entry.get()

        if original_url:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(original_url)
            self.shortened_label.config(text=shortened_url)  # Display only the shortened URL
        else:
            self.shortened_label.config(text="Please enter a URL.")

    def copy_to_clipboard(self):
        shortened_url = self.shortened_label.cget("text")
        if shortened_url:
            self.root.clipboard_clear()
            self.root.clipboard_append(shortened_url)
            self.root.update()  # Manually update clipboard contents
            self.print_copied_message()

    def print_copied_message(self):
        print("Shortened URL copied to clipboard!")

def main():
    print("\033[32mRunning Program ...\033[0m")
    root = tk.Tk()
    app = ShortenerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

