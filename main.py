# create server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to localhost and port 80
s.bind(('', 80))
print('Server listening on port 80')
# define maximum number of connections
s.listen(5)

while True:
    # accept connection
    conn, addr = s.accept()
    
    # get request
    request = conn.recv(1024)

    # get request method
    method = request.decode('utf-8').split(' ')[0]

    try:
        # get request path and query string
        [endpoint, parametersString] = request.decode('utf-8').split(' ')[1].split('?')
        # query string to dictionary
        parametersList = parametersString.split('&')
        parameters = {}
        for parameter in parametersList:
            [key, value] = parameter.split('=')
            parameters[key] = value
    except:
        # get request path when no query string
        endpoint = request.decode('utf-8').split(' ')[1]
        parameters = {}

    # ENDPONTS #

    # GET /led
    if (method == 'GET' and endpoint == '/led'):
        try:
            status = parameters['status']

            if (status == 'on'):
                led.on()
                conn.send('{"status": "ok", "message": "LED on"}'.encode('utf-8'))
            elif (status == 'off'):
                led.off()
                conn.send('{"status": "ok", "message": "LED off"}'.encode('utf-8'))
        except:
            conn.send('{"status": "error", "message": "Bad request"}'.encode('utf-8'))
    
    # END ENDPONTS #


    # close connection        
    conn.close()