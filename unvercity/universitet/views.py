from django.http import HttpResponse
from .models import Student
from .inner import saaloom


def index(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            
        }

        ul {
            position: absolute;
            color: #484848;
            font-family: sans-serif;
            top: 50%;
            left: 50%;
            display: flex;
            transform: translate(-50%, -50%)
        }

        ul li {
            position: relative;
            letter-spacing: 15px;
            font-size: 15vh;
            margin: 0;
            padding: 0;
            list-style: none;
        }


    </style>
</head>

<body>
    <ul>
        <li>S</li>
        <li>A</li>
        <li>L</li>
        <li>O</li>
        <li>M</li>
    </ul>
</body>

</html>""")


def salom(request):
    return HttpResponse(saaloom())
def bazaa(requests):
    student = Student()
    student.name = "Xudoyberdi"
    student.group = "148-19 LTO"
    student.age = 20
    student.save()
    return HttpResponse("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            
        }

        ul {
            position: absolute;
            color: #484848;
            font-family: sans-serif;
            top: 50%;
            left: 50%;
            display: flex;
            transform: translate(-50%, -50%)
        }

        ul li {
            position: relative;
            letter-spacing: 15px;
            font-size: 15vh;
            margin: 0;
            padding: 0;
            list-style: none;
        }


    </style>
</head>

<body>
    <ul>
        <li>S</li>
        <li>T</li>
        <li>U</li>
        <li>D</li>
        <li>E</li>
        <li>N</li>
        <li>T</li>
        <li>A</li>
        <li>D</li>
        <li>D</li>
    </ul>
</body>

</html>
        
""")


def see(requests):
    student = Student.objects.all()
    string = ""
    for i in student:
        if i == list(student)[-1]:
            string += f"""<h2 style = "margin: 0; padding: 0; ">{i}</h2>"""
        else:
            string += f"""<h2 style = "margin: 0; padding: 0; ">{i}</h2><br>"""
    return HttpResponse(string)


