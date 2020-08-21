from django.shortcuts import render


def index(request):
    return render(request, "index.html")


# def verify(request):
#     return render(request, "verify.html")

def verify(request):
    # Get the text

    djtext = request.GET.get('text', 'default')

    # Analyze the text

    lowcase = djtext.lower()
    x = list(map(str, lowcase.split(" ")))
    fmsg = ["send", "account", "hack", "cashless", "phone", "block", "money", "kyc", "office", "hold", "rewards",
            "cashback", "anydesk", "link", "teamviewer", "quicksupport"]

    a = 0
    b = 0
    f = ""
    t = ""
    for i in list(x):
        if i not in list(fmsg):
            a += 1
        else:
            b += 1
    if a >= 2:
        t = "True Message"
    else:
        f = "Fraud Message"

    params = {'purpose': t, 'f_msg': f, 'djtext': djtext}
    return render(request, "verify.html", params)
