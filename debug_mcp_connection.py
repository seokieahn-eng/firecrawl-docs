# Diagnostic Script for MCP Connection

# This script checks the connection to the MCP service.

import datetime
import requests

def check_connection():
    url = 'http://mcp.service.endpoint'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Connection successful: {datetime.datetime.utcnow()}')
        else:
            print(f'Connection failed with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Connection error: {e}')

if __name__ == '__main__':
    check_connection()