import pyshorteners

def main():
    s = pyshorteners.Shortener()

    original_url = input("Enter the URL to shorten: ")

    shortened_url = s.tinyurl.short(original_url)

    print("Shortened URL:", shortened_url)

if __name__ == "__main__":
    main()
