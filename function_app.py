import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="test-samples-trigger/{name}",
                               connection="b29d71_STORAGE") 
def myblob_trigger21(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
