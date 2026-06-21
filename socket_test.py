import socket 

host = "localhost"
port = 3000
timeout = 3

def server_connection(host, port, timeout):
    """Establishing a TCP Connection using Sockets"""
    try:
        with socket.create_connection((host, port),timeout):
            print(f"Connection to {host} on port {port} successful")
            
            return {
                "StatusCode": "HTTP/1.1 200 OK",
                "Server": "nginx/1.28.0",
                "Message": "Nginx connection successful"
            }
    
    except socket.timeout:
        print(f" Connection to {host} failed")
        return {
            "StatusCode": "HTTP/1.1 503",
            "Message": "Connection failure"
        }
    except TimeoutError:
        print(f"Connection to {host} timed out") 
        return {
            "StatusCode": "HTTP/1.1 504",
            "Message": "Connection timeout"
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "StatusCode": "HTTP/1.1 500",
            "Message": "internal server error"
        }
          
result = server_connection(host, port, timeout)
print(result)        
        
                      