from django.shortcuts import render, redirect


words = [
    {
        'Original': 'original',
        'Translated': 'translated'
    }
]


def home(request):
    return render(request, 'home.html', {'page': 'home'})


def words_list(request):
    return render(request, 'word_list.html', {'words': words})


def add_word(request):
    if request.method == 'GET':
        return render(request, "add_word.html", {"page": "add_word"})
    else:
        print(request.POST)
        with open("/home/kryukova/Dictionary_study/dictionary/my_app/words_list.txt", "a") as file:
            file.writelines(f"word1: {request.POST['word1']}, word2: {request.POST['word2']}")
        return redirect(words_list)
