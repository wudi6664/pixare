from django.shortcuts import render_to_response
#需要放在下面这些前面，否则在这些文件中将无法import error_404
def error_404(request):
    return render_to_response('404.html', {'request':request})

from . import home
from . import explore