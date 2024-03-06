from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Главная</h1>")


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)


def contact(request):
    host = request.META["HTTP_HOST"]                # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные браузера
    path = request.path                             # получаем запрошенный путь

    return HttpResponse(f"""
            <p>Host: {host}</p>
            <p>Path: {path}</p>
            <p>User-agent: {user_agent}</p>
        """)


def products(request):
    return HttpResponse("Список товаров")


def new(request):
    return HttpResponse("Новые товары")


def top(request):
    return HttpResponse("Наиболее популярные товары")


def product(request, p_id):
    return HttpResponse(f"Товар {p_id}")


def comments(request, p_id):
    return HttpResponse(f"Комментарии о товаре {p_id}")


def questions(request, p_id):
    return HttpResponse(f"Вопросы о товаре {p_id}")
