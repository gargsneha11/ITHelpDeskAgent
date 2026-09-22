from azure.identity import AzureCliCredential

credential = AzureCliCredential()

token = credential.get_token("https://cognitiveservices.azure.com/.default")

print("Azure authentication successful!")
print("Token received:", token.token[:20] + "...")