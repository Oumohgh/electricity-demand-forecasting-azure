from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="59b3f2eb-caba-469e-afca-cde678d49c24",
    resource_group_name="MohammedOUH",
    workspace_name="mlough"
)

workspace = ml_client.workspaces.get("mlough")

print("Connected successfully:", workspace.name)