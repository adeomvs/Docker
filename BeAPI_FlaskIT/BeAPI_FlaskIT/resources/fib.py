from flaskit.proxy import app, g, request, flaskit, Resource
from flaskit.utils import abort


##################################################################################################
# Manage resource fib
##################################################################################################
@flaskit
class Fib(Resource):

    ####################################################################################
    # List resources
    ####################################################################################
    @flaskit
    def FibList(self):
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
    def FibPost(self):
        # INSERT BUSINESS CODE HERE...
        n = g.args["n"]
        def Fibonacci(n):
            if n < 0:
                fibN = 0
            elif n == 0:
                fibN = 0
            elif n == 1:
                fibN = 1
            else:
                fibN = Fibonacci(n - 2) + Fibonacci(n - 1)
            
            return fibN

        record = {
            "_metadata": {},
            "item": {
                "n": n,
                "fibN": Fibonacci(n),
            }
        }
        return record, 201

    ####################################################################################
    # Get a resource
    ####################################################################################
    @flaskit
    def FibGet(self, id):
        # INSERT BUSINESS CODE HERE...
        record = {
            "_metadata": {},
            "item": {}
        }
        return record

    ####################################################################################
    # Modify a resource
    ####################################################################################
    @flaskit
    def FibPut(self, id):
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
    def FibDelete(self, id):
        # INSERT BUSINESS CODE HERE...
        record = {
            "_metadata": {},
            "item": {}
        }
        return record
