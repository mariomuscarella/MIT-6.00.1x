class NewsStory(object):
    def __init__(self, guid, the_title, the_subject, the_summary, link):
        self.guid = guid
        self.the_title = the_title
        self.the_subject = the_subject
        self.the_summary = the_summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.the_title

    def getSubject(self):
        return self.the_subject

    def getSummary(self):
        return self.the_summary

    def getLink(self):
        return self.link
