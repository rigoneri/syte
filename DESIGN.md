- All JS behavior is kicked off by the call to fetchBlogPosts() (syte/static/js/components/blog-posts.js)

    - This function is added with JQuery after page finishes loading.

- fetchBlogPosts() handles:

    - Setting up the handlebars template 'environment', etc.
    - Then calls setupLinks()

- setupLinks() is main entry point for the supported services

    - This attaches behavior to the click event of all 'a' tags.
    - Each click event will determine if it's a link for one of the supported
      services.
    - If the click is for a supported service:

        - All other service modal dialogs are hidden and the setup* function
            for the specified service is called.

    - The setup* function for the service is in charge of:

        - Querying server-side endpoint for the service and populating
            handlebar.js context with json returned.
        - Rendering template for service with handlebar.js
