# pylint: disable=missing-module-docstring
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    set static storage location
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    set media storage location
    """
    location = settings.MEDIAFILES_LOCATION