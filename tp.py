@views.route('/something', methods = ['GET', 'POST'] )

@login_required

def noteStuff():
    if request.method == 'GET':
        for (notes.userId==user.id)

