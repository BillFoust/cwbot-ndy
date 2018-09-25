from kol.request.GenericRequest import GenericRequest

class ClanConsultRequest(GenericRequest):
    def __init__(self, session, playerId):
        super(ClanConsultRequest, self).__init__(session)
        self.url = session.serverURL + 'clan_viplounge.php'
        self.requestData['pwd'] = session.pwd
        self.requestData['preaction'] = 'dotestlove'
        # self.requestData['whichfloor'] = '1'
        self.requestData['testlove'] = playerId
        self.requestData['q1'] = 'pepper'
        self.requestData['q2'] = 'robin'
        self.requestData['q3'] = 'thin'
        #def setWho(self, who):
        #self.requestData['testlove'] = who;
    def parseResponse(self):
        self.responseData['result'] = 'success'