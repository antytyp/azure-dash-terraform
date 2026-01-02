import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HelloWorld")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        "Hello from Azure Functions deployed via GitHub Actions 🚀",
        status_code=200
    )
