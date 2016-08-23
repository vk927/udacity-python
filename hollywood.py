import webbrowser
class Movie():
    def __init__(self,title,story,poster,trailor):
        self.title=title
        self.storyline=story
        self.poster=poster
        self.trailor=trailor

    def show_trailor(self):
        webbrowser.open(self.trailor)

