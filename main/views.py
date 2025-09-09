from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'namaaplikasi' : 'Panda Sportswear',
        'nama': 'Ryan Gibran Purwacakra Sihaloho',
        'kelas': 'PBP C'
    }

    return render(request, "main.html", context)
