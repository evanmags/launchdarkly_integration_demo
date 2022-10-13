from functools import cache
import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

@cache
def init_secrets_manager() -> SecretCache:
    client = botocore.session.get_session().create_client("secretsmanager", "us-west-2")
    cache_config = SecretCacheConfig()
    cache = SecretCache(config=cache_config, client=client)
    return cache

def get_secret(secret: str):
    client = init_secrets_manager()
    return client.get_secret_string(secret)
