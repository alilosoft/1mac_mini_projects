import webbrowser

class Movie:
    def __init__(self, title, story_line, poster_img_url, trailer_url):
        print "init Movie: " + str(self)
        self.title = title
        self.story_line = story_line
        self.poster_img_url = poster_img_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
