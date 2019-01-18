from flaskit.proxy import app, g, request, flaskit, Resource
from flaskit.utils import abort


##################################################################################################
# Manage resource bissext
##################################################################################################
@flaskit
class Bissext(Resource):

    ####################################################################################
    # List resources
    ####################################################################################
    @flaskit
    def BissextList(self):
        # INSERT BUSINESS CODE HERE...
        record = {
            "_metadata": {},
            "items": []
        }
        return record

    ####################################################################################
    # Create a resource
    ####################################################################################
    @flaskit
    def BissextPost(self):
        # INSERT BUSINESS CODE HERE...
        year = g.args["Years"]
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            is_bissext = True
        else:
            is_bissext = False
        record = {
            "_metadata": {},
            "item": {
                "year": year,
                "isBissext": is_bissext,
            }
        }
        return record, 201


    ####################################################################################
    # Modify a resource
    ####################################################################################
    @flaskit
    def BissextPut(self, id):
        # INSERT BUSINESS CODE HERE...
        record = {
            "_metadata": {},
            "item": {}
        }
        return record

    ####################################################################################
    # Delete a resource
    ####################################################################################
    @flaskit
    def BissextDelete(self, id):
        # INSERT BUSINESS CODE HERE...
        record = {
            "_metadata": {},
            "item": {}
        }
        return record
