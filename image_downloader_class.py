import requests

class ImgDwnld:

    IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg")
    DEFAULT_SIZE_LIMIT = 5242880 #this is 5 Mb in bytes
    
    def __init__(self, file_path, img_size=DEFAULT_SIZE_LIMIT):
        self.file_path = file_path
        self.img_size = img_size

    def url_list(self):
        with open(self.file_path) as f:
            # Making a list where each element is a URL-line from opened file.
            # Each element except the last one contains '\n' in the end.

            raw_list_of_urls = f.readlines()
            clear_list_of_urls = []

            # Getting rid of '\n'
            for i in raw_list_of_urls:
                clear_list_of_urls.append(i.replace('\n',''))

        return clear_list_of_urls

    def validate_format(self, r):
        if r.headers["Content-Type"] in self.IMAGE_FORMATS:
            return True
        else:
            print("improper file format: {}".format(r.headers["Content-Type"]))
            return False

    def validate_size(self, r):
        if int(r.headers["Content-Length"]) <= self.img_size:
            return True
        else:
            print("the size should be less or equal to {} (in bytes)".format(self.img_size))
            return False

    def img_download(self, r, img_name):
        # open in binary mode
        with open(img_name, "wb") as f:
            # write to file
            f.write(r.content)

    def list_download(self):
        for url in self.url_list():
            r = requests.get(url)
            if self.validate_size(r) and self.validate_format(r):
                self.img_download(r, input("file name: "))
            else:
                print("cannot download 1 or more files: {}".format(url))

test = ImgDwnld("URL_list.txt")

test.list_download()
