from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone

# Create your views here.


def profile_info_view(request):
    data = {
        "email": "chukwudidavid02@gmail.com",
        "current_datetime": datetime.now(timezone.utc),
        "github_url": "https://github.com/Donchuks02/HNG12-Stage0-Task"
    }
    return JsonResponse(data)


