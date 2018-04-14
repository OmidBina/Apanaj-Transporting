from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError)
import os.path
import json
import codecs
import datetime
import base64
from PIL import Image

class PostInstagram:
    def __init__(self):

        self.login()

    def to_json(self, python_object):
        if isinstance(python_object, bytes):
            return {'__class__': 'bytes',
                    '__value__': codecs.encode(python_object, 'base64').decode()}
        raise TypeError(repr(python_object) + ' is not JSON serializable')

    def from_json(self, json_object):
        if '__class__' in json_object and json_object['__class__'] == 'bytes':
            return codecs.decode(json_object['__value__'].encode(), 'base64')
        return json_object

    def onlogin_callback(self, api, new_settings_file):
        cache_settings = api.settings
        with open(new_settings_file, 'w') as outfile:
            json.dump(cache_settings, outfile, default=self.to_json)
            print('SAVED: {0!s}'.format(new_settings_file))

    def login(self):
        device_id = None
        try:
            settings_file = "credentials.json"
            if not os.path.isfile(settings_file):
                # settings file does not exist
                print('Unable to find file: {0!s}'.format(settings_file))
                # login new
                self.api = Client("iustfuckers", "WihvxHPFraosazXactvkPckutxCouHrGiX7CpgLqQsTwcWquLvEwayDJRohZToio", on_login=lambda x: self.onlogin_callback(x, settings_file))
            else:
                with open(settings_file) as file_data:
                    cached_settings = json.load(file_data, object_hook=self.from_json)
                print('Reusing settings: {0!s}'.format(settings_file))
                device_id = cached_settings.get('device_id')
                self.api = Client("iustfuckers", "WihvxHPFraosazXactvkPckutxCouHrGiX7CpgLqQsTwcWquLvEwayDJRohZToio", settings=cached_settings)

        except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
            print('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))

            # Login expired
            # Do relogin but use default ua, keys and such
            self.api = Client(args.username, args.password, device_id=device_id, on_login=lambda x: self.onlogin_callback(x, settings_file))

        except ClientLoginError as e:
            print('ClientLoginError {0!s}'.format(e))
            exit(9)
        except ClientError as e:
            print('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response))
            exit(9)
        except Exception as e:
            print('Unexpected Exception: {0!s}'.format(e))
            exit(99)

            # Show when login expires
        cookie_expiry = self.api.cookie_jar.expires_earliest
        print('Cookie Expiry: {0!s}'.format(datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')))

    def check(self):
        print(self.api.current_user())



    def post_image(self):
        with open("./image.jpg", "rb") as imageFile:
            photo_data = imageFile.read()
            im = Image.open('./image.jpg')

            results = self.api.post_photo(photo_data, size=im.size, caption='HI')


a = PostInstagram()
a.post_image()
