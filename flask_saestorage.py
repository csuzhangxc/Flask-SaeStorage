# -*- coding: utf-8 -*-

from sae import storage


class SaeStorage(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        access_key = app.config.get('SAE_ACCESS_KEY', storage.ACCESS_KEY)
        secret_key = app.config.get('SAE_SECRET_KEY', storage.SECRET_KEY)
        app_name = app.config.get('SAE_APP_NAME', storage.APP_NAME)
        bucket_name = app.config.get('SAE_BUCKET_NAME', '')
        connection = storage.Connection(access_key, secret_key, app_name)
        self._bucket = connection.get_bucket(bucket_name)

    def save(self, data, filename):
        return self._bucket.put_object(filename, data)

    def delete(self, filename):
        return self._bucket.delete_object(filename)

    def url(self, filename):
        return self._bucket.generate_url(filename)