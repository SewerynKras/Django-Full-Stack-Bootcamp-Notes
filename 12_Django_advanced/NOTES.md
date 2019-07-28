# Notes on different parts of the Django Advanced section

## DetailView, ListView

Detail and list views are common OOP alternatives to function-based views. To connect them to a template simply add `template_name = 'path_to_template.html'`. To pass external variables in a context you need to add

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

to the class (`context` is a dictionary). ListViews make displaying lists of all items easy. After you set a context name using `context_object_name = 'some_name'` you  can use it in templates by simply calling `{% for item in some_name %}`. DetailViews work similarly, except they're used to display information for a single item given it's primary key.


## CreateView, UpdateView, DeleteView

You can use these views to create/update/delete objects from the database. In CreateView you need to add the following function to the view class:

    def get_absolute_url(self):
        return reverse("url_to_something", kwargs={"pk": self.pk})

This way after creating the object users will be redirected to the given site. "pk" stands for "primary key" and can be used to point to a specific object in the database (using DetailView)
