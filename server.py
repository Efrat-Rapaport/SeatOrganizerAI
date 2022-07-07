import os
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import time
from urllib.parse import urlparse, parse_qs
import json
from flask import Flask
import pyodbc
import ast
import faceRecognitionModel

hostName = "127.0.0.1"
hostPort = 9007


class MyServer(BaseHTTPRequestHandler):
    app = Flask(__name__)

    def sentiment(self):
        print("in senitment")
        pass

    #     do something
    # to use the model you need firefly

    def do_GET(self):
        # getparams
        #         print("in do_GET")
        query_components = parse_qs(urlparse(self.path).query)
        train_path = list(query_components.values())[0]
        test_path = list(query_components.values())[1]
        print("train:", train_path)
        print(f'test: {test_path}')

        self.send_response(200)
        self.send_header("Content-type", 'application/json')
        self.end_headers()
        if "sentiment" in self.path:
            guest_id=faceRecognitionModel.my_face_recognition(train_path[0], test_path[0])
            print(guest_id)
        self.send_response(200)
        self.end_headers()

        # Dictionary = {1: 'Welcome', 2: 'to',
        #               3: 'server', 4: 'for',}
        #
        # # Converts input dictionary into
        # # string and stores it in json_string
        # json_content = json.dumps(Dictionary)
        #
        # # json_content = json.dumps("the function/ model response", ensure_ascii=False)  # json.dumps(res)
        # print(json_content)
        self.wfile.write(bytes(str(guest_id), "utf-8"))
        return


# generate the server
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

# stop the server
myServer.server_close()
print(time.asctime(), "Server Closed - %s:%s" % (hostName, hostPort))



