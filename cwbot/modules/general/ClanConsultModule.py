from cwbot.modules.BaseChatModule import BaseChatModule
from cwbot.kolextra.request.ClanConsultRequest import ClanConsultRequest

class ClanConsultModule(BaseChatModule):
    """ 
    Module to handle consultations in the Clan VIP lounge.
    
    No configuration options
    """

    requiredCapabilities = ['chat']
    _name = "clan_consult"
    
    def __init__(self, manager, identity, config):
        super(ClanConsultModule, self).__init__(manager, identity, config)


    def _processCommand(self, message, cmd, args):
        if cmd == "consult":
            uid = message['userId']
            r = ClanConsultRequest(self.session, uid)
            d = self.tryRequest(r)
            replyStr = ("{}, I've replied to a consultation request for you.".format(message["userName"]))
            self.chat(replyStr) 
        return None


    def _availableCommands(self):
        return {'consult': "!consult: Reply to a consultation request."}

