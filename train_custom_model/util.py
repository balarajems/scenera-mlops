from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

def get_resource_key():
    key_vault_name = os.getenv("KEY_VAULT_NAME")
    KVUri = f"https://{key_vault_name}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    return client.get_secret("resource-key")