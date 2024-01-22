from user import User
from post import Post

app_user_one = User("njd@cc.cc", "Guy Dvorkin", "pwd1", "Not Just DevOps")
app_user_one.get_user_info()

app_user_two = User("ccc@cc.cc", "Gi Artem", "pwd1", "Just DevOps")
app_user_two.get_user_info()

new_post = Post("On duty today.", app_user_two.name)
new_post.get_post_info()