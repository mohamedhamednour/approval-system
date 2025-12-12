# utils/response.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class GenericResponse(Response):
    def __init__(self, data=None, approval=None, message=None,
                 status_code=status.HTTP_200_OK, **kwargs):
        
        if data is None :
            raise ValidationError("No data found.")

        payload = {
            "data": data,
            "approval": approval
        }

        if message:
            payload["message"] = message

        super().__init__(data=payload, status=status_code, **kwargs)
