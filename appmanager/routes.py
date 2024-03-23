from flask import render_template, session
from appmanager import app
from appmanager.server.articles import get_articles_from_api, get_data_from_demo
from appmanager.server.constants import jokes, happy_emojis


@app.route("/")
@app.route("/<int:page_index>")
def home(page_index=1):
    if 'articles' in session:
        data = session['articles']
    else:
        data = get_articles_from_api(page_index)
        # stores all articles in session
        session['articles'] = data
    # data = get_data_from_demo()
    # Define pagination parameters
    items_per_page = 8
    num_pages = int(len(data) / items_per_page)

    # Calculate start and end indices for pagination
    start_index = (page_index - 1) * items_per_page
    end_index = start_index + items_per_page

    # Extract articles for the current page
    articles_for_page = data[start_index:end_index]
    # print(f"print ${start_index} and end ${end_index} and len ${len(articles_for_page)}")

    return render_template("home.html", result=articles_for_page, total_pages=num_pages, page=page_index)

@app.route("/game")
def game():
    return render_template("game-page.html")

@app.route ("/tic_tac_toe")
def tic_tac_toe():
    return render_template("tic-tac-toe.html")

@app.route ("/memory_game")
def memory_game():
    return render_template("memory-game.html")

@app.route ("/emoji_catcher")
def emoji_catcher():
    return render_template("emoji-catcher.html")

@app.route("/contributors")
def contributors():
    return render_template("contributors-page.html")


@app.route("/article/<int:article_id>")
def article_details(article_id):
    # gets especific article from session with index from article clicked
    article = session.get("articles", {})[article_id]
    return render_template("article-details.html", article=article)


@app.route("/gallery")
def gallery():
    jokes_with_emojis = list(zip(jokes, happy_emojis))
    return render_template("gallery.html", data = jokes_with_emojis)
