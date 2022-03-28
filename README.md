# The takeaways

The most common methods used for REST APIs are GET, POST, PUT, and DELETE

## On the server side

In a Flask application, these correspond to their respective decorators (if using a Flask version > 2.0)

The usage is:

```py
@app.get("/")
def method_for_getting_data_on_path_slash()
    pass

@app.post("/")
def method_for_adding_new_data_on_path_slash()
    pass

@app.put("/")
def method_for_updating_existing_data_on_path_slash()
    pass

@app.delete("/")
def method_for_removing_data_on_path_slash()
    pass
```

If the method is PUT or POST, the data may come from either a form, or as JSON.

To get this data, use either `request.form.get('name_of_input_field')` (if form) or `request.json.get('key_of_submitted_object')` (if JSON).

* * *

## On the client side

HTML forms only support the GET and POST methods.

These are added as the `method` property in the form itself.

If you need to use either PUT or DELETE, you must use JavaScript.

The simplest way to do a request using JavaScript is to use the included `api`  object, which contains all 4 functions.

**PLEASE NOTE:** all 4 functions are asynchronous, which means that they **must** be called in a function that has the `async` keyword, and the results must have the `await` keyword.

E.G.

```js
async function read_from_the_server() {
    const result = await api.get("/some_url");
    return result;
}
```

Please see the code included for more details.
