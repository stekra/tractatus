# tractatus txt -> html generator

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def decimals(value):
    count = value[::-1].find('.')

    if count == -1:
        return 0
    else:
        return count


with open('tractatus.txt', 'r') as txt, open('index.html', 'w') as html:
    html.write(r'''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tractatus logico-philosophicus</title>
    <style>
        body {
            width: 800px;
            line-height: 1.4;
            padding-bottom: 100px;
        }
        details summary {
            cursor: pointer;
            margin-top: 1em;
            margin-bottom: 1em
        }
        details > *:not(summary){
            margin-left: 2em;
        }
        div {
            text-indent: 1em;
            margin-top: 1em;
            margin-bottom: 1em
        }
    </style>
</head>
<body>
<h2>Ludwig Wittgenstein</h2>
<h1>Tractatus logico-philosophicus</h1>
<h3>Fassung 1922</h3>
<hr>
<details><summary>Vorwort</summary>
<p>Dieses Buch wird vielleicht nur der verstehen, der die Gedanken, die darin ausgedrückt sind—oder doch ähnliche Gedanken—schon selbst ein- mal gedacht hat.—Es ist also kein Lehrbuch.—Sein Zweck wäre erreicht, wenn es Einem, der es mit Verständnis liest Vergnügen bereitete.</p>
<p>Das Buch behandelt die philosophischen Probleme und zeigt—wie ich glaube—dass die Fragestellung dieser Probleme auf dem Missverständ- nis der Logik unserer Sprache beruht. Man könnte den ganzen Sinn des Buches etwa in die Worte fassen: Was sich überhaupt sagen lässt, lässt sich klar sagen; und wovon man nicht reden kann, darüber muss man schweigen.</p>
<p>Das Buch will also dem Denken eine Grenze ziehen, oder vielmehr— nicht dem Denken, sondern dem Ausdruck der Gedanken: Denn um dem Denken eine Grenze zu ziehen, müssten wir beide Seiten dieser Grenze denken können (wir müssten also denken können, was sich nicht denken lässt).</p>
<p>Die Grenze wird also nur in der Sprache gezogen werden können und was jenseits der Grenze liegt, wird einfach Unsinn sein.</p>
<p>Wieweit meine Bestrebungen mit denen anderer Philosophen zusam- menfallen, will ich nicht beurteilen. Ja, was ich hier geschrieben habe macht im Einzelnen überhaupt nicht den Anspruch auf Neuheit; und darum gebe ich auch keine Quellen an, weil es mir gleichgültig ist, ob das was ich gedacht habe, vor mir schon ein anderer gedacht hat.</p>
<p>Nur das will ich erwähnen, dass ich den grossartigen Werken Freges und den Arbeiten meines Freundes Herrn Bertrand Russell einen grossen Teil der Anregung zu meinen Gedanken schulde.</p>
<p>Wenn diese Arbeit einen Wert hat, so besteht er in Zweierlei. Erstens darin, dass in ihr Gedanken ausgedrückt sind, und dieser Wert wird umso grösser sein, je besser die Gedanken ausgedrückt sind. Je mehr der Nagel auf den Kopf getroffen ist.—Hier bin ich mir bewusst, weit hinter dem Möglichen zurückgeblieben zu sein. Einfach darum, weil meine Kraft zur Bewältigung der Aufgabe zu gering ist.—Mögen andere kommen und es besser machen.</p>
<p>Dagegen scheint mir die Wahrheit der hier mitgeteilten Gedanken unantastbar und definitiv. Ich bin also der Meinung, die Probleme im Wesentlichen endgültig gelöst zu haben. Und wenn ich mich hierin nicht irre, so besteht nun der Wert dieser Arbeit zweitens darin, dass sie zeigt, wie wenig damit getan ist, dass diese Probleme gelöst sind.</p>
<p>L. W.</p>
<p><i>Wien, 1918.</i></p>
</details>
<hr>
''')

    lines = list(txt)
    lines = [line.strip() for line in lines]
    lines = [line.replace('\\r', '<br>') for line in lines]

    for index, current_line in enumerate(lines):
        if index < (len(lines) - 1):
            next_line = lines[index+1]

            current_nr = current_line.split()[0]
            next_nr = next_line.split()[0]

            current_decimals = decimals(current_nr)
            next_decimals = decimals(next_nr)
            tabs = current_decimals * "\t"

            if next_decimals > current_decimals:
                html.write(tabs + "<details><summary>")
                html.write("<b>" + current_nr + "</b> ")
                split_line = current_line.split(' ', 1)
                if len(split_line) > 1:
                    html.write(split_line[1])
                html.write("</summary>\n")

            else:
                html.write(tabs + "<div>")
                html.write("<b>" + current_nr + "</b> ")
                html.write(current_line.split(' ', 1)[1])
                html.write("</div>\n")

                if next_decimals < current_decimals:
                    for x in range(current_decimals - next_decimals):
                        tabs = (current_decimals - (x + 1)) * "\t"
                        html.write(tabs + "</details>\n")

    # Last line
    html.write("<div>")
    html.write("<b>" + "7" + "</b> ")
    html.write(lines[-1].split(' ', 1)[1])
    html.write("</div>\n")

    html.write(r'''<hr>
<details><summary>*</summary>
<p>Die Decimalzahlen als Nummern der einzelnen Sätze deuten das logische Gewicht der Sätze an, den Nachdruck, der auf ihnen in meiner Darstellung liegt. Die Sätze n.1, n.2, n.3, etc., sind Bemerkungen zum Satze No. n; die Sätze n.m1, n.m2, etc. Bemerkungen zum Satze No. n.m; und so weiter.<p>
</details>
<hr><hr>
<details><summary>Seiteninformation</summary>
<p>Simpelstes einseitiges Hypertext Tractatus.</p>
</details>
</body>
</html>''')
