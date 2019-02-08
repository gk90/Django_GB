from social_core.exceptions import AuthForbidden


def save_user_profile(backend, user, response, *args, **kwargs):

    print('*' * 100)
    print('response', response)
    print('*' * 100)

    if backend.name == "vk-oauth2":
        if 'user_id' in response.keys():
            user.shopuserprofile.url = 'https://vk.com/' + str(response['user_id'])

    if backend.name == "google-oauth2":
        if 'gender' in response.keys():
            if response['gender'] == 'male':
                user.shopuserprofile.gender = 'M'
            else:
                user.shopuserprofile.gender = 'W'

        if 'tagline' in response.keys():
            user.shopuserprofile.tagline = response['tagline']

        if 'aboutMe' in response.keys():
            user.shopuserprofile.aboutMe = response['aboutMe']

        if 'locale' in response.keys():
            user.shopuserprofile.language = response['locale']

        if 'profile' in response.keys():
            user.shopuserprofile.url = response['profile']

        if 'ageRange' in response.keys():
            minAge = response['ageRange']['min']
            # print(f'{user} minAge: {minAge}')
            if int(minAge) < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.google.GoogleOAuth2')

    user.save()
    return
