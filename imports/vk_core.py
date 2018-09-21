import vk_api
from configs import passwords



class vk_parser:
    def __init__(self):
        login, password = passwords.login, passwords.password
        self.vk_session = vk_api.VkApi(login, password)

        try:
            self.vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)

    def get_info(self, id):
        tools = vk_api.VkTools(self.vk_session)
        wall = tools.get_all('wall.get', 100, {'owner_id': -id})
        return wall['items']
