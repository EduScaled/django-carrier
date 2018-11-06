class MessageManagerHelperSingleton:
    instance = None

    class __MessageManagerHelperSingleton:
        def __init__(self):
            self._to_listen = []

    def __init__(self):
        if not MessageManagerHelperSingleton.instance:
            MessageManagerHelperSingleton.instance = MessageManagerHelperSingleton.__MessageManagerHelperSingleton()

    def set_manager_to_listen(self, manager):
        self.instance._to_listen.append(manager)   
        
    def get_message_managers_to_listen(self):
        return self.instance._to_listen 

MessageManagerHelper = MessageManagerHelperSingleton()