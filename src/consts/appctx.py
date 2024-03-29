success_status = {
    200: 'Operation succeeded',
    201: 'Created',
    202: 'Accepted',
    204: 'Reply does not contain additional content',
    304: 'Not modified'
}

failure_status = {
    400: 'Internal error occurred - unexpected error caused by request data',
    401: 'Unauthorized operation',
    403: 'Forbidden operation',
    404: 'Specified object not found',
    405: 'Method Not Allowed, for example, resource doesn\'t support DELETE method',
    406: 'Method Not Acceptable',
    409: 'Conflict',
    423: 'Locked',
    426: 'Upgrade Required',
    500: 'Internal Server Error - unexpected server-side error',
    501: 'Not Implemented - functionality is not implemented on the server side',
    503: 'Service is unavailable'
}