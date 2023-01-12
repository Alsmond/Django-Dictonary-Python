from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.
def index(request):
    data=""
    synonyms=""
    if request.method=="POST":
        name=request.POST.get("search")
        dicts=Dictionary(name)
        data=dicts.meanings()
        synonyms=dicts.synonyms()
    context={"data":data,"synonyms":synonyms}
    return render(request,"index.html",context)