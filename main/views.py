from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'nama aplikasi' : 'Panda Sportswear',
        'nama': 'Ryan Gibran Purwacakra Sihaloho',
        'kelas': 'PBP C'
    }

    return render(request, "main.html", context)
