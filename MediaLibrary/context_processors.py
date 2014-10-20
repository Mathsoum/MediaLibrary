from datetime import datetime

def get_infos(request):
    return { 'date': datetime.now() }