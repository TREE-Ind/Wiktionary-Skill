from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *
from wiktionaryparser import WiktionaryParser
from mycroft.util.log import LOG


class WiktionarySkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_entity_file("word.entity")
        self.parser = WiktionaryParser()

    @intent_file_handler('fallback.wiktionary.definition.intent')
    def handle_wiktionary_definition(self, message):
        #Get word to define from utterance
        word = message.data.get('word')
        #Lookup the word using Wiktionary
        get_word_info = self.parser.fetch(word)

        #Speak definition for requested word back to user
        try:
            # Get first definition from wiktionary response
            response = get_word_info[0]['definitions'][0]['text'][1]
            # Log the definition
            LOG.info(response)
            self.speak_dialog('fallback.wiktionary', {'word': word, 'definition': response})
        except:
            self.speak_dialog('error.wiktionary')


def create_skill():
    return WiktionarySkill()

