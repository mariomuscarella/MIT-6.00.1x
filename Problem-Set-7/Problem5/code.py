class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        text = self.replacePunc(text)
        return self.word in text.lower().split()

    def replacePunc(self, text):
        for p in string.punctuation:
            text = text.replace(p, ' ')

        return text

class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return self.phrase in story.getSubject() or \
            self.phrase in story.getTitle() or \
            self.phrase in story.getSummary()
            
def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist 
    fires.
    """
    result = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                result.append(story)
                break
        
    return result
