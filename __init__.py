from mycroft import MycroftSkill, intent_file_handler


class Extract(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('extract.intent')
    def handle_extract(self, message):
        self.speak_dialog('extract')


def create_skill():
    return Extract()

