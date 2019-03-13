from social_core.exceptions import AuthForbidden


def save_user_profile(backend, user, response, *args, **kwargs):

    if backend.name == "vk-oauth2":
        if 'user_id' in response.keys():
            user.shopuserprofile.url = 'https://vk.com/' + str(response['user_id'])

    user.save()
    return
