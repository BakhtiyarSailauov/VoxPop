from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from repository import CommentsRepository

app = FastAPI()

templates = Jinja2Templates(directory="../templates")
repository = CommentsRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/comments")
def get_main_page(request: Request):
    return templates.TemplateResponse(
        "comments/index.html",
        {"request": request},
    )

@app.get("/comments/add_comment")
def get_add_comments(request: Request):
    return templates.TemplateResponse(
        "comments/add_comment.html",
        {
           "request": request
        }
    )

@app.post("/comments/add_comment")
def post_add_comment(comment: str = Form(), category: str = Form()):
    repository.save({"text": comment, "category": category})
    return RedirectResponse("/comments", status_code=303)

@app.get("/comments/show_comment")
def get_comments(request: Request, page: int = 1, category: str = ""):
    limit = 10
    filtered_comments = []
    comments = repository.get_all()
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit

    next_page = page + 1 if len(comments) > end_idx else None
    previous_page = page - 1 if start_idx > 0 else None

    for comment in comments:
        if category.lower() in comment["category"].lower():
            filtered_comments.append(comment)

    paginated_comments = list(reversed(filtered_comments))[start_idx:end_idx]

    return templates.TemplateResponse(
        "comments/get_comments.html",
        {
            "request": request,
            "comments": paginated_comments,
            "next_page": next_page,
            "previous_page": previous_page,
            "category_name": category,
        },
    )