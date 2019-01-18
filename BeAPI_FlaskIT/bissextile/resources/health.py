from flaskit.proxy import app, g, request, flaskit, Resource
from flaskit.utils import abort


##################################################################################################
# Health resource
##################################################################################################
@flaskit
class Health(Resource):

    @flaskit
    def HealthGet(self):

        results = []
        results.append({
            "id": "0000",
            "message": "OK",
            "status": 0
        })

        metadatas = {
            "message": "all tests passed",
            "status": 0
        }
        response = {
            "_metadata": metadatas,
            "results": results,
        }

        return response