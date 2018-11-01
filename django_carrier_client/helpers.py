class MessageManagerHelperClass():

    def __init__(self):
        self._to_listen = []

    def set_manager_to_listen(self, manager):
        self._to_listen.append(manager)   
        
    def get_message_managers_to_listen(self):
        return self._to_listen 

# TODO singleton
MessageManagerHelper = MessageManagerHelperClass()