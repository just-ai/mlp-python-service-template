from mlp_sdk.abstract import Task
from mlp_sdk.hosting.host import host_mlp_cloud
from mlp_sdk.transport.MlpServiceSDK import MlpServiceSDK
from pydantic import BaseModel


class PredictRequest(BaseModel):
    name: str

    def __int__(self, name):
        self.name = name


class PredictResponse(BaseModel):
    response: str

    def __int__(self, response):
        self.response = response


class SimpleActionExample(Task):
    def __init__(self, config: BaseModel, service_sdk: MlpServiceSDK = None) -> None:
        super().__init__(config, service_sdk)

    def predict(self, data: PredictRequest, config: BaseModel) -> PredictResponse:
        return PredictResponse(response="Hello, " + data.name + "!")


if __name__ == "__main__":
    host_mlp_cloud(SimpleActionExample, BaseModel())
