from django.shortcuts import render


def search(request):
    """Başlangıçta yalnızca yer tutucu sayfayı gösterir."""
    return render(request, "students/search.html")
