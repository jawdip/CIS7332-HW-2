import argparse
import requests
from bs4 import BeautifulSoup
import os


def download(link, destination=os.getcwd(), print_only=False):
    filename = "index.html"
    destination = os.path.abspath(destination)

    if not os.path.exists(destination):
        os.mkdir(destination)
        os.chdir(destination)

    des = os.path.join(destination, os.path.basename(link))

    if not os.path.exists(des):
        os.mkdir(des)
    os.chdir(des)

    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    pretty_soup = soup.prettify()

    if not print_only:
        with open(f"{filename}", "w+") as file:
            file.write(pretty_soup)
            file.close()
        print(f"File Saved as: {filename} in: {des}")

    elif print_only:
        print(pretty_soup)


parser = argparse.ArgumentParser(prog="wget", description="This is a WGET alternative program written in Python which "
                                                          "helps you download files from the internet.")

parser.add_argument("URL", metavar="URLs", nargs="+", help="Enter the URL (or URLs) you want to download.")

parser.add_argument("-d", dest="destination", help="Specify the Downloads folder [DEFAULT = Current "
                                                   "Folder]", default=".")
parser.add_argument("-p", "--print-only", help="Don't download the file, just print it's content.", dest="print",
                    default=False, action="store_const", const=True)
args = parser.parse_args()

for url in args.URL:
    download(url, destination=args.destination, print_only=args.print)
