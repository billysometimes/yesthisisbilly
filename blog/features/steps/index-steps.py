from behave import *
from blog.factories import UserFactory, PostFactory

@given('there is a list of posts')
def step_impl(context):
    posts = [PostFactory(title=row['title'], slug=row['slug'], author=UserFactory(username=row['author']), body=row['body']) for row in context.table]

@when('I visit the url "/blog"')
def step_impl(context):
    context.browser.visit(context.config.server_url+'/blog')

@then('I see a list of 5 posts')
def step_impl(context):
    posts = context.browser.find_by_css('.post-card')
    assert len(posts) == 5
