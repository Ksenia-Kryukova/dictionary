from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html', {'page': 'home'})


def words_list(request):
    with open("/home/kryukova/Dictionary_study/dictionary/my_app/words_list.txt", 'r', encoding='utf-8') as file:
        content = file.read().splitlines()

    words1 = []
    words2 = []
    for line in content:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)

    return render(request, 'words_list.html', {'words1': words1, 'words2': words2})


def add_word(request):
    if request.method == 'GET':
        return render(request, "add_word.html", {"page": "add_word"})

    else:
        print(request.POST)
        with open("/home/kryukova/Dictionary_study/dictionary/my_app/words_list.txt", "a") as file:
            file.write(request.POST['word1'] + "-" + request.POST['word2'] + "\n")

        return redirect(home)