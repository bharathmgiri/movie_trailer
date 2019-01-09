import webbrowser
class cinemas():
    def __init__(self,cine_title,mov_storyline,
                        cine_poster_url,cine_youtube):
        self.title=cine_title
        self.storyline=mov_storyline
        self.poster_image_url=cine_poster_url
        self.trailer_youtube_url=cine_youtube
    def show_cinemas_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
